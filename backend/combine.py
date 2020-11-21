import pandas as pd
import ocr_functions as ocr
import os

def create_csv():
    df = pd.DataFrame(columns=['return.pdf','our data',''])


    #### T4 DATA ####
    '''
           t4 labels:
           - SIN
           - Employment Income
           - Employment Income Cents
           - Last Name
           - First Name
           - Street Address
           - City
           - Province
           - Postal Code
    '''
    result = ocr.predict("t4", "./images/t4/t4first.pdf")

    # SIN
    if (type(result.get("SIN")) is not None):
        df = df.append({'return.pdf': 23, 'our data': "SIN",
                        '': result.get("SIN")},
                       ignore_index=True)
    # Employment Income
    if(type(result.get("Employment Income Cents")) is not None):
        df = df.append({'return.pdf':52, 'our data':"Employment Income",
                        '':result.get("Employment Income")+"  "+result.get("Employment Income Cents")+"  "},
                       ignore_index=True)
    else:
        df = df.append({'return.pdf': 52, 'our data': "Employment Income",
                        '': result.get("Employment Income") + "     "},
                       ignore_index=True)

    # Last Name
    if (type(result.get("Last Name")) is not None):
        df = df.append({'return.pdf': 10, 'our data': "Last Name",
                        '': result.get("Last Name")},
                       ignore_index=True)
    # First Name
    if (type(result.get("First Name")) is not None):
        df = df.append({'return.pdf': 9, 'our data': "First Name",
                        '': result.get("First Name")},
                       ignore_index=True)

    # Street Address
    if (type(result.get("Street Address")) is not None):
        df = df.append({'return.pdf': 11, 'our data': "Street Address",
                        '': result.get("Street Address")},
                       ignore_index=True)
    # City
    if (type(result.get("City")) is not None):
        df = df.append({'return.pdf': 14, 'our data': "City",
                        '': result.get("City").replace(",","")},
                       ignore_index=True)
    # Province
    if (type(result.get("Province")) is not None):
        df = df.append({'return.pdf': 15, 'our data': "Province",
                        '': result.get("Province")},
                       ignore_index=True)

    # Postal Code

    if (type(result.get("Postal Code")) is not None):
        temp = result.get("Postal Code").replace(" ","")
        df = df.append({'return.pdf': 16, 'our data': "Postal Code",
                        '': temp},
                       ignore_index=True)

    #### T4A ####
    '''
    t4a labels:
       - RDSP
       - RDSP Cents
    '''
    result = ocr.predict("t4a","./images/t4a/t4afirst.pdf")
    # RDSP
    if (type(result.get("RDSP Cents")) is not None):
        df = df.append({'return.pdf': 70, 'our data': "RDSP",
                        '': result.get("RDSP") + "  " + result.get("RDSP Cents") + "  "},
                       ignore_index=True)
    else:
        df = df.append({'return.pdf': 70, 'our data': "RDSP",
                        '': result.get("RDSP") + "  " + "00" + "  "},
                       ignore_index=True)

    #### T4(OAS) ####
    '''
     t4a OAS labels:
       - Taxable Pension Paid
    '''
    result = ocr.predict("t4aoas", "./images/t4a(oas)/oasfirst.pdf")

    #Taxable Pension Paid
    if (type(result.get("Taxable Pension Paid")) is not None):
        if("." in result.get("Taxable Pension Paid")):
            temp = result.get("Taxable Pension Paid").split(".")
            df = df.append({'return.pdf': 57, 'our data': "Taxable Pension Paid",
                            '': temp[0] + "  " + temp[1]+ "  "},
                           ignore_index=True)
        else:
            df = df.append({'return.pdf': 57, 'our data': "Taxable Pension Paid",
                            '': result.get("Taxable Pension Paid") + "  " + "00" + "  "},
                           ignore_index=True)

    #### T4A P ####
    '''
       t4a p labels:
       - Taxable CPP Benefits
       - Disability Benefit
    '''
    result = ocr.predict("t4ap", "./images/t4ap/pfirst.pdf")

    if (type(result.get("Taxable CPP Benefits")) is not None):
        # Taxable CPP Benefits
        if ("." in result.get("Taxable CPP Benefits")):
            temp = result.get("Taxable CPP Benefits").split(".")
            df = df.append({'return.pdf': 58, 'our data': "Taxable CPP Benefits",
                            '': temp[0] + "  " + temp[1] + "  "},
                           ignore_index=True)
        else:
            df = df.append({'return.pdf': 58, 'our data': "Taxable CPP Benefits",
                            '': result.get("Taxable CPP Benefits") + "  " + "00" + "  "},
                           ignore_index=True)

    # Disability Benefits
    if(type(result.get("Disability Benefit")) is not None):
        if ("." in result.get("Disability Benefit")):
            temp = result.get("Disability Benefit").split(".")
            df = df.append({'return.pdf': 59, 'our data': "Disability Benefit",
                            '': temp[0] + "  " + temp[1] + "  "},
                           ignore_index=True)
        else:
            df = df.append({'return.pdf': 59, 'our data': "Disability Benefit",
                            '': result.get("Disability Benefit") + "  " + "00" + "  "},
                           ignore_index=True)

    #### T1032 ####
    '''
       t1032 labels:
       - Elected Split-Pension
       - Elected Split-Pension Cents
    '''
    result = ocr.predict("t1032", "./images/t1032/t1032first.pdf")
    # T1032
    if (type(result.get("Elected Split-Pension Cents")) is not None):
        df = df.append({'return.pdf': 61, 'our data': "Elected Split-Pension",
                        '': result.get("Elected Split-Pension") + "  " + result.get("Elected Split-Pension Cents") + "  "},
                       ignore_index=True)
    else:
        df = df.append({'return.pdf': 61, 'our data': "Elected Split-Pension",
                        '': result.get("Elected Split-Pension") + "  " + "00" + "  "},
                       ignore_index=True)

    #### T4E ####
    '''
       T4E labels:
       - Benefits
    '''
    result = ocr.predict("t4e", "./images/t4e/first.pdf")
    # T1032
    if (type(result.get("Benefits")) is not None):
        if ("." in result.get("Benefits")):
            temp = result.get("Benefits").split(".")
            df = df.append({'return.pdf': 64, 'our data': "Benefits",
                            '': temp[0] + "  " + temp[1] + "  "},
                           ignore_index=True)
        else:
            df = df.append({'return.pdf': 64, 'our data': "Benefits",
                            '': result.get("Benefits") + "  " + "00" + "  "},
                           ignore_index=True)



    df.to_csv("results.csv", index=False)
    os.system('pdfforms fill results.csv')
