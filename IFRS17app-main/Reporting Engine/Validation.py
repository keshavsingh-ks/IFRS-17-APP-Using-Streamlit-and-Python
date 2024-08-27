import pandas as pd
import numpy as np

assumptions = pd.read_csv("sample-Annual_v1.csv")
parameters = pd.read_csv("Parameters.csv")

class validation:
    def __init__(self, file, parameters):
        
        self.Parameters = parameters
        self.File1 = file.copy()
        self.File2 = file.copy()
        self.File3 = file.copy()
        date_check= []
        
        # date = pd.to_datetime(file['Cohort'],format = '%d/%m/%Y').dt.month
        # if self.Parameters.loc[2, "Selection"] == "Annually":
        #     for i in date:
        #         if date[i] == 12:

        #             print("Cohort Dates Correctly Specified")
        #         else:
        #             print("Cohort Dates In-Correctly Specified")

        self.checks = []
        self.status = []

        date = pd.to_datetime(file['Cohort'], format='%d/%m/%Y').dt.month
        if self.Parameters.loc[2, "Selection"] == "Annually":
            if any(date != 12):
                check = "Cohort Dates In-Correctly Specified"
                status = "Failed"
            else:
                check = "Cohort Dates Correctly Specified"
                status = "Passed"
            self.checks.append(check)
            self.status.append(status)
        

#Dealing with NA's 
        self.File1.drop(self.File1.columns[[3,4]], axis=1, inplace=True)
        count_missing = self.File1.isnull().sum().sum()
        if count_missing == 0:
            check = "No Missing Value"
            status = "Passed"
        else:
            check = str(count_missing) + " Missing Values"
            status = "Failed"
        
        self.checks.append(check)
        self.status.append(status)
        
#Signage Checks
        for i in self.File2.loc[self.File2['Key'] == 'MAP003',"Gross_BE"]:
            if i > 1:
                check = "Correct Sign for Expected Premiums (MAP003-Gross)"
                status = "Passed"
            else:
                check = "Incorrect Sign for Expected Premiums (MAP003-Gross)"
                status = "Failed"

            self.checks.append(check)
            self.status.append(status)
            
        for i in self.File2.loc[self.File2['Key'] == 'MAP002',"Gross_Actual_BE"]:
            if i > 1:
                check = "Correct Sign for Actual Premiums (MAP002-Gross)"
                status = "Passed"
            else:
                check = "Incorrect Sign for Actual Premiums (MAP002-Gross)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
        for i in self.File2.loc[self.File2['Key'] == 'MAP012',"Gross_Actual_BE"]:
            if i < 1:
                check ="Correct Sign for Actual BE Cash Outflows (MAP012-Gross)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Actual BE Cash Outflows (MAP012-Gross)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
        for i in self.File2.loc[self.File2['Key'] == 'MAP013',"Gross_BE"]:
            if i < 1:
                check ="Correct Sign for Expected BE Cash Outflows (MAP013-Gross)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Expected BE Cash Outflows (MAP013-Gross)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
        for i in self.File2.loc[self.File2['Key'] == 'MAP012',"Gross_Actual_RA"]:
            if i < 1:
                check ="Correct Sign for Actual RA Cash Outflows (MAP012-Gross)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Actual RA Cash Outflows (MAP012-Gross)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)   
            
        for i in self.File2.loc[self.File2['Key'] == 'MAP013',"Gross_RA"]:
            if i < 1:
                check ="Correct Sign for Expected RA Cash Outflows (MAP013-Gross)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Expected RA Cash Outflows (MAP013-Gross)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
        for i in self.File2.loc[self.File2['Key'] == 'MAP015',"Gross_Actual_BE"]:
            if i < 1:
                check ="Correct Sign for Actual Insurance Acquisistion CashFlows (MAP015-Gross)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Actual Insurance Acquisistion CashFlows (MAP015-Gross)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
        for i in self.File2.loc[self.File2['Key'] == 'MAP016',"Gross_BE"]:
            if i < 1:
                check ="Correct Sign for Expected Insurance Acquisistion CashFlows (MAP016-Gross)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Expected Insurance Acquisistion CashFlows (MAP016-Gross)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
##Reinsurance
        for i in self.File2.loc[self.File2['Key'] == 'MAP003',"Reins_BE"]:
            if i > 1:
                check = "Correct Sign for Expected Premiums (MAP003-Reinsurance)"
                status = "Passed"
            else:
                check = "Incorrect Sign for Expected Premiums (MAP003-Reinsurance)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
            
        for i in self.File2.loc[self.File2['Key'] == 'MAP002',"Reins_Actual_BE"]:
            if i > 1:
                check = "Correct Sign for Actual Premiums (MAP002-Reinsurance)"
                status = "Passed"
            else:
                check = "Incorrect Sign for Actual Premiums (MAP002-Reinsurance)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
        for i in self.File2.loc[self.File2['Key'] == 'MAP012',"Reins_Actual_BE"]:
            if i < 1:
                check ="Correct Sign for Actual BE Cash Outflows (MAP012-Reinsurance)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Actual BE Cash Outflows (MAP012-Reinsurance)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
        for i in self.File2.loc[self.File2['Key'] == 'MAP013',"Reins_BE"]:
            if i < 1:
                check ="Correct Sign for Expected BE Cash Outflows (MAP013-Reinsurance)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Expected BE Cash Outflows (MAP013-Reinsurance)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
        for i in self.File2.loc[self.File2['Key'] == 'MAP012',"Reins_Actual_RA"]:
            if i < 1:
                check ="Correct Sign for Actual RA Cash Outflows (MAP012-Reinsurance)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Actual RA Cash Outflows (MAP012-Reinsurance)"
                status = "Failed"
            self.checks.append(check)  
            self.status.append(status) 
            
        for i in self.File2.loc[self.File2['Key'] == 'MAP013',"Reins_RA"]:
            if i < 1:
                check ="Correct Sign for Expected RA Cash Outflows (MAP013-Reinsurance)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Expected RA Cash Outflows (MAP013-Reinsurance)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
        for i in self.File2.loc[self.File2['Key'] == 'MAP015',"Reins_Actual_BE"]:
            if i < 1:
                check ="Correct Sign for Actual Insurance Acquisistion CashFlows (MAP015-Reinsurance)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Actual Insurance Acquisistion CashFlows (MAP015-Reinsurance)"
                status = "Failed"
            self.checks.append(check)
            self.status.append(status)
        for i in self.File2.loc[self.File2['Key'] == 'MAP016',"Reins_BE"]:
            if i < 1:
                check ="Correct Sign for Expected Insurance Acquisistion CashFlows (MAP016-Reinsurance)"
                status = "Passed"
            else:
                check ="Incorrect Sign for Expected Insurance Acquisistion CashFlows (MAP016-Reinsurance)"
                status = "Failed"

            self.checks.append(check)
            self.status.append(status)
        
        filtered_gross = self.File2.loc[self.File2['Gross_BE'] * self.File2['Gross_RA'] != 0]
        filtered_Reins = self.File2.loc[self.File2['Reins_BE'] * self.File2['Reins_RA'] != 0]
        opposite_signs_gross =(np.sign(filtered_gross['Gross_BE']) != np.sign(filtered_gross['Gross_RA'])).sum()
        opposite_signs_Reins =(np.sign(filtered_Reins['Reins_BE']) != np.sign(filtered_Reins['Reins_RA'])).sum()
        if opposite_signs_gross == 0:
            check = "Correct BEL and RA signage (Gross)"
            status = "Passed"
        else:
            check = "The dataset has " + str(opposite_signs_gross)+" set of rows where the Gross BE values have opposite signs as compared to Gross RA (Gross)"
            status = "Failed"
        self.checks.append(check)
        self.status.append(status)
        if opposite_signs_Reins == 0:
            check = "Correct BEL and RA signage (Reinsurance)"
            status = "Passed"
        else:
            check = "The dataset has " + str(opposite_signs_Reins)+" set of rows where the Gross BE values have opposite signs as compared to Gross RA (Reinsurance)-- Re-check Inputs"
            status = "Failed"
        self.checks.append(check)
        self.status.append(status)
        
        data_dict = {
                'assumption_' + str(i): grp
                for i, grp in self.File3.groupby(['Product', 'Sub-Product'])
            }
        
        
        for group in data_dict:
            cohort = data_dict[group]
            for i in cohort:
                sum_gross = cohort.loc[cohort['Key'] == 'MAP002',"Gross_Actual_BE"]+cohort.loc[cohort['Key'] == 'MAP015',"Gross_Actual_BE"]+cohort.loc[cohort['Key'] == 'MAP004',"Gross_BE"]+cohort.loc[cohort['Key'] == 'MAP004',"Gross_RA"]+cohort.loc[cohort['Key'] == 'MAP004',"Gross_LossC_BE"]+cohort.loc[cohort['Key'] == 'MAP004',"Gross_LossC_RA"]+cohort.loc[cohort['Key'] == 'MAP004',"Gross_CSM"]
                sum_Reins = cohort.loc[cohort['Key'] == 'MAP002',"Reins_Actual_BE"]+cohort.loc[cohort['Key'] == 'MAP015',"Reins_Actual_BE"]+cohort.loc[cohort['Key'] == 'MAP004',"Reins_BE"]+cohort.loc[cohort['Key'] == 'MAP004',"Reins_RA"]+cohort.loc[cohort['Key'] == 'MAP004',"Reins_LossC_BE"]+cohort.loc[cohort['Key'] == 'MAP004',"Reins_LossC_RA"]+cohort.loc[cohort['Key'] == 'MAP004',"Reins_CSM"]
                if sum_gross.sum() == 0:
                    check = "New business CSM (Gross) is correct"
                    status = "Passed"
                else:
                    check = "New business CSM (Gross) is incorrect"
                    status = "Failed"
                self.checks.append(check)
                self.status.append(status)
                if sum_Reins.sum() == 0:
                    check = "New business CSM (Reinsurance) is correct"
                    status = "Passed"
                else:
                    check = "New business CSM (Reinsurance) is incorrect"
                    status = "Failed"
                self.checks.append(check)
                self.status.append(status)
        
        self.checks = pd.DataFrame(self.checks,columns = ["Validation Checks"])
        self.status = pd.DataFrame(self.status,columns = ["Status"])
        self.validation_table = pd.concat([self.checks,self.status], axis=1)
        self.count_status = pd.DataFrame(self.validation_table['Status'].value_counts()).reset_index()
        passed_count = self.count_status.loc[self.count_status['index'] == "Passed", "Status"].item()
        failed_count = self.count_status.loc[self.count_status['index'] == "Failed", "Status"].item()
        self.print_count_status = str(passed_count) + " Validation Checks Passed " + "\n" + str(failed_count) + " Validation Checks Failed"
                                      

validation(assumptions,parameters)