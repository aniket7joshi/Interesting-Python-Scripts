import csv
import re
out = open('valid_cards.csv','w')
with open('card_details.csv', 'r') as f:
	reader = csv.reader(f)
	re_in=re.compile('\+91[-\s][7-9][0-9]{3}[-\s][0-9]{6}')
	re_omn=re.compile('\+968[-\s]9[1-9][0-9]{2}[-\s]?[0-9]{4}')
	re_uae=re.compile('\+971[-\s]5[0256][-\s][0-9]{6}')
	re_visa=re.compile('4[0-9]{15}')
	re_mastercard=re.compile('(5[1-5][0-9]{14})|(222[1-9][0-9]{12})|(22[3-9][0-9][0-9]{12})|(2[3-6][0-9]{2}[0-9]{12})|(27[0-1][0-9][0-9]{12})|(2720[0-9]{12})')
	re_diners=re.compile('(30[0-5][0-9]{11})|(36[0-9]{12})|(38[0-9]{12})')
	for row in reader:
		flag=0
		if(row[3]=='IND'):
			if(re.match(re_in,row[1])):
				if(re.match(re_visa,row[2])):
					cardtype='VISA'
					flag=1
				elif(re.match(re_mastercard,row[2])):
					cardtype='MasterCard'
					flag=1
				elif(re.match(re_diners,row[2])):
					cardtype='Diners Club'
					flag=1
			if(flag==1):
				out.write(','.join(row)+','+cardtype+'\n')

		if(row[3]=='OMN'):
			if(re.match(re_omn,row[1])):
				if(re.match(re_visa,row[2])):
					cardtype='VISA'
					flag=1
				elif(re.match(re_mastercard,row[2])):
					cardtype='MasterCard'
					flag=1
				elif(re.match(re_diners,row[2])):
					cardtype='Diners Club'
					flag=1
			if(flag==1):
				out.write(','.join(row)+','+cardtype+'\n')
		if(row[3]=='ARE'):
			if(re.match(re_uae,row[1])):
				if(re.match(re_visa,row[2])):
					cardtype='VISA'
					flag=1
				elif(re.match(re_mastercard,row[2])):
					cardtype='MasterCard'
					flag=1
				elif(re.match(re_diners,row[2])):
					cardtype='Diners Club'
					flag=1
			if(flag==1):
				out.write(','.join(row)+','+cardtype+'\n')
f.close()
out.close()				
	