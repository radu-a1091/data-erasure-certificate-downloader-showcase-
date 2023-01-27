import pandas as pd
from tkinter import messagebox
import math

def get_link_list():
    imei_list_to_search = []
    results = pd.read_csv("imei.csv",delimiter=",")
    for i in range(len(results)):
        imei_list_to_search.append(results.iat[i,0])
    
    for i in range(len(imei_list_to_search)):
        try:
            imei_list_to_search[i] = str(imei_list_to_search[i])
        except ValueError:
            pass

    imei_list_from_export = []
    results_from_export = pd.read_csv("database_export.csv", usecols=["Serial","IMEI","Erasure Certificate Link"])

    summary = []
    added_imeis = []
    for i in imei_list_to_search:
        row_index = results_from_export.index[results_from_export["IMEI"]==str(i)].to_list()
        for j in row_index:
            value = results_from_export.iat[j,2]
            try:
                math.isnan(float(value))
            except:
                try:
                    imei_link_list = []
                    if str(i) in results_from_export["IMEI"].values:
                        for x in range(len(summary)):
                            if summary[x][0] not in added_imeis:
                                added_imeis.append(summary[x][0])
                        if i not in added_imeis:
                            imei_list_from_export.append(results_from_export.iat[j,2])
                            imei_link_list.append(i)
                            imei_link_list.append(results_from_export.iat[j,2])
                            summary.append(imei_link_list)
                except:
                    try:
                        imei_link_list = []
                        if str(i) in results_from_export["Serial"].values:
                            for x in range(len(summary)):
                                if summary[x][0] not in added_imeis:
                                    added_imeis.append(summary[x][0])
                            if i not in added_imeis:
                                imei_list_from_export.append(results_from_export.iat[j,2])
                                imei_link_list.append(i)
                                imei_link_list.append(results_from_export.iat[j,2])
                                summary.append(imei_link_list)
                    except:
                        print("IMEI or SN not in the database")
    with open("database_lookup_results.txt","w") as f:
        pass
    f.close()

    with open("database_lookup_results.txt","a") as f:
        with_link_count = 0
        missing_link_count = 0
        no_link_imei = ""
        imei_list = ""
        for i in imei_list_to_search:
            if i in added_imeis:
                with_link_count += 1
                imei_list += i+"\n"
            else:
                missing_link_count += 1
                
                if i != summary[-1]:
                    no_link_imei += i+"\n"
                else:
                    no_link_imei += i
        f.write(f"""Devices without data erasure certificates.
                
Count - {missing_link_count}:
{no_link_imei}""")
        display_message = f"""Downloading {with_link_count} certificates.
                
Database_lookup_results.txt updated with {missing_link_count} IMEI/SN without a certificate."""
    f.close()
    
    messagebox.showinfo("Summary",display_message)
    return imei_list_from_export


