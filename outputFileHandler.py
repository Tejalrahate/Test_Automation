import json
from datetime import datetime

import xlsxwriter as xls

from answer_similarity import SimilarityComparitor


# from testDriver import expected_result

#this class creates an output file, each row has following 4 columns
#test case no
#question
#Response
#response time
#Expected result

class OutputFileHandler:
#Constructer -
#output_file - The location of output file
    def __init__(self, output_file):
        self.output_file = output_file
        self.workbook = xls.Workbook(output_file,options={'nan_inf_to_errors': True})#create file based on output_location. # ability to handle null data for expected result
        self.worksheet=self.workbook.add_worksheet("test")#create sheet in the xls file
        #next steps will write header entry on row 0
        self.worksheet.write(0, 0, "#")           # -- firstrow first column (row,column,data)
        self.worksheet.write(0, 1, "Question")    #-- firstrow second column
        self.worksheet.write(0, 2, "Expected Result")
        self.worksheet.write(0, 3, "Answer")
        self.worksheet.write(0, 4, "Response Time in Sec")
        # self.worksheet.write(0, 5, "Similarity Percentage")
        # self.worksheet.write(0, 4, "Expected Result")

    def write_line(self,row_number, question, expected_result, answer, response_item):
#    def write_line(self,row_number, question, expected_result, answer, response_item,similarity_percentage):
        self.worksheet.write(row_number, 0, row_number)
        self.worksheet.write(row_number, 1,question)

        self.worksheet.write(row_number, 2, expected_result)
        self.worksheet.write(row_number, 3, answer)
        self.worksheet.write(row_number, 4, response_item)
        # self.worksheet.write(row_number, 5, similarity_percentage)

    def closeFile(self):
        self.workbook.close()



    def parse_response(self, response):
        # print('-------------------- Raw response start --------------------')
        # print(response.text)
        # print('-------------------- Raw response end --------------------')
        response_lines = response.text.splitlines()#list of strings of response
        for line in response_lines:
            if "chat_history" in line:
                # removes the 'data: ' from begging of response so that we get a valid json
                json_object = json.loads(line.replace("data: ", ""))
                #JSOS is loaded into dictionary by json library, access the 'answer' from dictionary
                answer = json_object["chat_history"][0].get("answer")
                print(answer)
                return answer
