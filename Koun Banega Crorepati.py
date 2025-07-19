import random
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
Questions = [
    ["The enzyme pepsin converts?","Carbohydrates to sugars","Proteins to amino acids", "Protein to peptones", "Fats to fatty acids and glycerol", 3],
    ["Which of these does not generate energy but are still essential for body?", "Fats", "Proteins", "Vitamins", "Carbohydrates", 3],
    ["Recently died sportsperson, Saksham Yadav belongs to which sport?", "Power lifter","Boxer", "Wrestler", "Cricketer", 1],
    ["Riyadh is the capital of which country?","Saudi Arabia", "Oman", "Bulgaria", "Nairobi", 1],
    ["Which state government has become the first to launch high risk pregnancy portal ?", "Gujarat", "Haryana", "Uttar Pradesh", "Kerala", 2],
    ["Sportsperson Shiv Kapur belongs to which game?", "Snooker", "Skiing", "Golf", "Basketball", 3],
    ["Who is the present CM of Goa?","Satyapal Malik","Manoharlal Parrikar","Jagdish Mukki","Banwarilal Purohit",2],
    ["The scheme 'Saral Rural Housing Loan' was launched by which of he following private sector bank?","Axis bank","HDFC bank","ICICI bank","Karur Vysya bank",3],
    ["Minority Affairs minister Shri Mukhtar Abbas Naqvi belongs to which of the following state constituency?","BiharMizoram", "Jammu and Kashmir", "Jharkhand", 4],
    ["Which of the following country is going to host ITTF Table Tennis World Cup 2018?","France","England","London","Germany",3],
    ["Which among the following International organisation doesn't have its head quarter in London?","Amnesty international","International atomic energy agency","International Maritime organisation","Commonwealth of Nations",4],
    ["Khajuraho Temple is located in which state in India?","Uttar Pradesh","Punjab","Madhya Pradesh","Jharkhand",3],
    ["MacMahon is the boundary line between which two countries?","India and Nepal","India and China","India and Pakistan","Nepal and China",2],
    ["Famous Paradip port is located in which state of India?","Odisha","Kerala","Goa","Gujarat",1],
    ["Koteshwar dam is built across which river and is located in which state of India?","Bhagirathi and Uttar Pradesh","Bhagirathi and Uttarakhand","Yamuna and Uttarakhand","Rihand and Uttar Pradesh",2],
    ["Religious Siddhivinayak Temple is located in which place?","Mumbai","Kolkata","Madurai","Delhi",1],
    ["Gair is a type of folk dance famous in which state of India?","Gujarat",'Rajasthan','Punjab',"Bihar",2],
    ['World food day is celebrated on?','October 16','October 15',"November 16","November 15",1],
    ["Garuda shakthi is the joint exercise between India and which of the following country","Sri Lanka","Indonesia","Japan","Singapore",2],
    ["which city in India is called as 'city of weavers'?","Prayag","Panipet","Jamshedpur","Varanasi",2],
    ["Newlands stadium is located in which country?","New-Zealand","Netherland","South Africa","Thailand",3],
    ["The book 'India 2017 Yearbook', compiled by Rajiv Mehrishi, was launched by the Chief minister of which state?","Gujarat","Uttar Pradesh","Bihar","Rajasthan",4],
    ["What is the rank of India in world bank's ease of doing business ranking?",'100','105','200',"205",1],
    ["Recently died Sukharanjan Sengupta belongs to which field?","Veteran actor","Eminent Hindi poet & Jnanpith awardee","Veteran journalist","Renowned Malayalam writer",3],
    ["Pawan Kumar Chamling is the Chief minister of which of the following indian state?",'Sikkim','Tripura','Uttarakhand',"D. Himachal Pradesh",1],
    ["Nameri National Park is in which state of India?","Chattisgarh","Assam","Nagaland","Himachal Pradesh",2],
    ["Sitamata Wild life sanctuary is in which state of India?","Gujarat","Rajesthan","Maharashtra","Bihar",2],
    ["Talcher Super Thermal Power Station is in which state of India?","Odisha","Uttar Pradesh","Haryana","Karnataka",1],
    ["Which is the first state in India to treat Hepatitis-C patients through oral medicine?","Punjab","Himachal Pradesh","Haryana","Telangana",3],
    ["Valletta is the capital city of which of the following country?","Bolivia","Belarus","Malta","Somalia",3],
    ["Which of the following is the currency of Peru?","Kwanza","Sol","dong","Kim",2],
    ["Walmart India launched its first Launched its first fulfilment centre in which city?","Mumbai","Ahmedabad","Chennai","Delhi",1],
    ["Which institution is called as the 'Think Tank' of Government of India?","RBI","NITI aayog","FICCI","SEBI",2],
    ["Who is the present director general of UNESCO?","Irina Bokova","Audrey Azoulay","Halimah Yacob","Jacinda Ardern",2],
    ["Who is the CEO of Flipkart?","Kalyan Krishnamurthy","Shashi Shanker","Shri Sanjiv Singh","B S Sahrawat",1],
    ["Chilika lake is located in which of the following cities?","Kerala","Maharashtra","west Bengal","Odisha",4],
    ["Who is the present President of Boxing Federation of India (BFI) ?","Ajay Singh","Sanjay Agarwal","Vijay Shekhar Sharma","Rana Kapoor",1],
    ["Warsaw is the capital of which of the following country?","Austria","Poland","Syria","Belarus",2],
    ["Which of the following bank is India’s largest private bank by market capitalization?","Axis bank","ICICI bank","HDFC bank","Kotek Mahindra bank",3],
    ["Who was the first Railway Minister of Independent India?","John Mathai.","Pawan Kumar Bajaj","Srivatsa Krishna","Mahesh Kumar Jain",1],
    ["Who has won Miss Supranational 2016?","Srinidhi Shetty","Peden ongmu nymgyal","Kevin Lilliana","Manushi chillar",1],
    ["Nizam gold cup is given in which of the following sports?","Cricket","Football","Basketball","Tennis",2],
    ["Guru Gobind Singh Gold Cup is given to which of the following games?","Hockey","Football","Tennis","Horse riding",1],
    ["Grey revolution implies growth in which of the following?","Jute production","Fertilizer Production","Poultry production","Cotton production",2],
    ["Ukai dam is located in which of the following state?","Odisha","Uttarakhand","Jharkhand","Gujarat",4],
    ["Which of the following is the world's first and largest stock market in the world?","NYSE","NASDAQ","LSE","SGX",1],
    ["International mango festival is celebrated in which of the following city in India?","Mumbai","Chennai","Cochin","New Delhi",4],
    ["Which of the following award is not given to Literature field?","Sahitya academy award","Man booker award","Dhanvantri award","Saraswati Samman award",3],
    ["Dodoma is the capital city of which of the following country?","Tunisia","Tanzania","Somalia","Nigeria",2],
    ["What is the tagline of Andhra Bank?","Where India Banks","Relationship Beyond Banking","A Friend you can bank upon","Your Perfect Banking Partner", 1],
    ["Which of the following is the autobiography of Indian Hockey Player Dhyan Chand?","Dreams","Sun shine","Hockey journey","Goal",3],
    ["Pravasi Bharatiya Diwas is celebrated annually on which of the following days?","January 25","January 19","January 9","January 5",3],
    ["Shora is the parliament of which of the following country?","Australia","Afghanistan","Algeria","Albania",2],
    ["Head quarter of (UNWTO) United Nation's World Tourism Organisation is located in?","Geneva, Switzerland","Rome, Italy","Madrid, Spain","London, UK",3],
    ["Manipuri girl, Laishram Saritha Devi belongs to which of the following games?","Wrestler","Boxer","Cricketer","Hockey player",2],
    ["In FICCI, first 'I' and Second 'C' represents which of the following?","Industry and Chambers","Indian and Chambers","Indian and Commerce","Industry and Commerce",3],
    ["Nathpa Jhagri Dam in Himachal Pradesh is built across which of the following rivers?","River Godavari","River Sutlej","River Indus","River Chenab",2],
    ["Mudiyettu is the traditional folk dance drama of which Indian state?","Karnataka","Kerala","Andhra Pradesh","Maharashtra",2],
    ['''The book " War and Diplomacy in Kashmir" was authed by?''',"C Dasgupta","Khushwant Singh","Anwar Singh","RK Narayanan",3],
    ["Kempegowda International Airport is located in which of the following city?","Mumbai","Hyderabad","Bangalore","Chennai",1],
    ["World's teachers day is celebrated on?","September 5","October 5","November 5","August 5",2],
    ["Prathama Grameen bank is a RRB sponsored by which of the following public sector bank?","Andhra bank","Oriental bank of commerce","Syndicate bank","Dena bank",3],
    ["Nichigin for short is the nickname of which of the following bank?","Bank of America","Bank of Japan","Bank of China","Bank of Canada",2],
    ["In SARFAESI act, what does the letter R stand for?","Reconstruction","Residential","Remuneration","Restructuring",1],
    ["Barak valley is situated in which state?","Assam","Bihar","Chandigarh","Haryana",1],
    ["Which of the following is the currency of the country Somalia?","Somali dollar","Somali pound","Somali Shilling","Somali rubble",3],
    ["Which city is called as city of Four junction?","Cochin","Madurai","Coimbatore","Hyderabad",2],
    ["Althing is the parliament of which of the following country?","Netherland","Switzerland","Lithuania","Iceland", 4],
    ["Khajuraho Temples were situated in which state of India?","Maharashtra","Mizoram","Madhya Pradesh","Arunachal Pradesh",3],
    ["The book ' Beyond the last blue mountain' is the biography of which of the following personality?","J.R.D. Tata","Mukesh Ambani","Amitabh Bachchan","Sundara Murthy",1],
    ["The Melghat Tiger reserve is in which of the following state?","Gujarat","Rajasthan","Maharashtra","Madhya Pradesh",3],
    ["Indian player Shubhankar Sharma is associated with which of the following games?","Golf","Football","Hockey","Snooker",1],
    ["Who is the author of the book ' Exam Warriors' ?","Manmohan Singh","Abdul Kalam","Narendra Modi","Raghuram Rajan",3],
    ["Recently Sri Lankan government has celebrated it's 70 th Independence day. What is the theme of the ceremony?","United Nation","One Nation","People's Nation","Nation of the warriors",2],
    ["Who is the present vice President of India?","Manoharlal Parrikar","Suresh Prabhu","Venkaiah Naidu","Ram naik",3],
    ["Every year world cancer day is celebrated on February 4th. Main goal of this day is to eradicate death related to cancer by which of the following year?","2020","2030","2040","2050",2],
    ["Which country tops the world democracy index 2017?","Denmark","Iceland","Norway","Switzerland",3],
    ["Bulletin is the app launched by which of the following?","Facebook","Google","Microsoft","Flipkart",1],
    ["Who has won the Yash Chopra memorial award for this year?","AR Rahman","Asha Bhosle","Amitabh Bachchan","Shahrukh Khan",3],
    ["VINBAX is the joint military exercise between India and which country?","Bangladesh","Vietnam","Bahrain","Pakistan",2],
    ["Dudhwa National Park is located in which of the following state?","Uttarakhand","Jharkhand","Uttar Pradesh","Himachal Pradesh",2],
    ["Which state government has launched the women safety app 'Shakti' recently?","Himachal Pradesh","Madhya Pradesh","Assam","Bihar",2],
    ["Which Bollywood actor has been Honoured with Crystal Award at World Economic Forum?","Amitabh Bachchan","Hrithik Roshan","Salman Khan","Shahrukh Khan",3],
    ["India's first Garbage Festival, 'Kachra Mahotsav 2018', was organised by which of the following state?","Chhattisgarh","Uttar Pradesh","Himachal Pradesh","Haryana",1],
    ["Who is the present governor of Madhya Pradesh?","Anandiben Patel","Om Prakash Kohli","Sathya pal Malik","Banwarilal Purohit",4],
    ["Where is the head quarter of small finance bank?","Jaipur","Ahmedabad","Bangalore","Hyderabad",1],
    ["Chandi Lahiri, who have been passed away recently belongs to which field?","Playback singer","Cartoonist","Director","Actor",1],
    ["Who is the MD and CEO of Yes Bank?","Rana Kapoor","Jai Kumar","Rajneesh Kumar","Himant Singh",1],
    ["First Chief Election Commissioner of India after Independence is?","Sukumar Sen","Achal Kumar Jyoti","Narayanan","Desh mukh",2],
    ["What is the currency of Israel?","Dollar","Riyal","New shekel","Dinar",1],
    ["Mukhyamantri Kalakar Sahayata Jojana was launched by the CM of which state?","Rajasthan","Gujarat","Odisha","Chattisgarh",1],
    ["under Bangladesh-Bhutan-India-Nepal (BBIN) Motor vehicles agreement between Bhutan, India, Bangladesh and Nepal is called as?","BIBN pact","BBIN pact","INBB pact","BBNI pact",2],
    ["Who is the present Minister of Petroleum and Natural Gas?","Manoharlal Parrikar","Suresh Prabhu","Dharmendra Pradhan","Prakash javadekar",1],
    ["The book ‘Imperfect’ is the autobiography of which of the following personality?","Harper Collins","Sanjay Manjrekar","Dilip Vengsarkar","Sinha",1],
    ["What is ' C' in CIPAM?","Center","Cement","Cell","Criminal",3],
    ["Iron Fist is the joint military exercise between Japan and which of the following country?","India","South Korea","USA","China",3],
    ["Introduce India’s First Battery-Powered Interactive Payment Card was launched by which of the following bank?","Kotek Mahindra bank","IndusInd Bank","Lakshmi Vilas bank","IDFC bank",2],
    ["Where is the head quarter of ISRO?","Ahmedabad","Mumbai","Bangalore","New Delhi",3],
    ["In SFOORTI application, second O stands for?","Optimization","Operation","Online","Organisation",2],
    ["who is the founder and CEO of Amazon?","Jeff Bezos","Bill gates","Mark Zuckerberg","Larry Page",3],
    ["Anchal Thakur is related to which of the following games?","Badminton","Skiing","Snooker","Cricket",3],
    ["Which state has topped the logistics performance index chart this year?","Rajasthan","Uttar Pradesh","Maharashtra","Gujarat",2],
    ["Recently died sportsperson, Saksham Yadav belongs to which sport?","Power lifter","Boxer","Wrestler","Cricketer",3],
    ["Riyadh is the capital of which country?","Saudi Arabia","Oman","Bulgaria","Nairobi",1]


]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,500000,1000000]
money = 0
random.shuffle(Questions)
for i in range(0, len(Questions)):
    question = (Questions[i])
    print(f'Question for Rs.{levels[i]}')
    print(question[0])
    speaker.Speak(question[0])
    options1 = f'1.{question[1]} \t\t 2.{question[2]}'
    options2 = f'3.{question[3]} \t\t\t4.{question[4]}'
    print(options1)
    print(options2)
    speaker.Speak(options1)
    speaker.Speak(options2)
    while True:
       reply = int(input("Enter Your Answer (1-4)\n"))
       while reply < 5:
           if reply == question[-1]:
               win = f'Correct Answer!! You won Rs.{levels[i]}'
               print(win)
               speaker.Speak(win)
               speaker.Speak('Next Question')
               if i==4:
                   money = 10000
               elif i==9:
                   money = 320000
               elif i==14:
                   money = 10000000
           else:
               lose = f'Incorrect Answer!!You are Eliminated! and take Rs.{money} home'
               print(lose)
               speaker.speak(lose)
               break
       else :
           invaild = 'Invalid Answer!! Enter option in (1-4)'
           print(invaild)
           speaker.Speak(invaild)















