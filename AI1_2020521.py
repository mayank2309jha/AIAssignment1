import pandas as pd
import numpy as np
from textblob import TextBlob
import random

# We take the data as input from the csv file in the directory.
data = pd.read_csv("knowledge_base.csv")
my_data = data.values
filtered_data = data.values
class Location:
    def __init__(self,row):
        self.row = row
    def __str__(self):
        print("---------------     Location Data     ---------------")
        print("Location = "+self.row[0])
        print("Region = "+self.row[1])
        print("Weather = "+self.row[2])
        print("Rating = "+str(self.row[3]))
        print("Connectivity= "+self.row[4])
        print("Feedback = "+self.row[5])
        print("The activities available are:- ")
        if type(self.row[6]) ==str:
            for item in self.row[6].strip('[]').split(","):
                print(item)
        else:
            for item in self.row[6]:
                print(item)
        
        return "---------------     End of Location Data     ---------------"

# Function to get sentiment polarity
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def filter_recommendations():
        global filtered_data
        filtering = True
        while filtering:
            print("----------------------------------------  AITRAVEL => Time to make a choice.----------------------------------------  ")
            print("-----1 => FILTER BY REGION")
            print("-----2 => FILTER BY WEATHER")
            print("-----3 => FILTER BY RATING")
            print("-----4 => FILTER BY FEEDBACKS")
            print("-----5 => FILTER BY ACTIVITIES")
            print("-----6 => FILTER BY CONNECTIVITY")
            print("-----7 => HIGHEST RATING FIRST")
            print("-----8 => LOWEST RATING FIRST")
            print("-----9 => SHOW NAMES OF FILTERED LOCATIONS")
            print("-----10 => SHOW DESCRIPTION OF SOME FILTERED LOCATIONS")
            print("-----11 => EXIT")
            user_input = input("TRAVELLER => ")
            if(user_input == "1"):
                unique_items = set()
                for item in filtered_data:
                    unique_items.add(item[1])
                print("AITRAVEL => Okay then. Here is a list of regions. Enter the full name as shown.")
                for item in unique_items:
                    print(item)
                user_input = input("TRAVELLER => ")
                print("AITRAVEL => Before filtering we had "+str(len(filtered_data))+" locations.")
                filtered_data = [item for item in filtered_data if item[1] == user_input]
                print("AITRAVEL => Now we have "+str(len(filtered_data))+" locations.")
            elif(user_input == "2"):
                print("AITRAVEL => Give me the weather experience you want.")
                print("AITRAVEL => Mild / Extreme {Pick one}")
                me = input("TRAVELLER => ")
                print("AITRAVEL => Summer / Winter {Pick one}")
                sw = input("TRAVELLER => ")
                print("AITRAVEL => Cloudy / Not Cloudy {Pick one}")
                cn = input("TRAVELLER => ")
                print("AITRAVEL => Rain / No Rain {Pick one}")
                rn = input("TRAVELLER => ")
                weather = me + ", " + sw + ", " + cn + ", " + rn
                print("AITRAVEL => Before filtering we had "+str(len(filtered_data))+" locations.")
                filtered_data = [item for item in filtered_data if item[2] == weather]
                print("AITRAVEL => Now we have "+str(len(filtered_data))+" locations.")
            elif(user_input == "3"):
                print("AITRAVEL => What is the minimum rating you want?")
                user_input = input("TRAVELLER => ")
                print("AITRAVEL => Before filtering we had "+str(len(filtered_data))+" locations.")
                filtered_data = [row for row in filtered_data if int(user_input) < row[3]]
                print("AITRAVEL => Now we have "+str(len(filtered_data))+" locations.")
            elif(user_input == "4"):
                # we will just perform a simple sentiment analysis on the column Feedback of the data.
                # Apply sentiment analysis function to the "Feedback" column in the array
                sentiments = np.array([get_sentiment(row[5]) for row in filtered_data])
                # Add the sentiment scores as a new column in the array
                arr_with_sentiments = np.column_stack((filtered_data, sentiments))
                # Sort the array based on the sentiment scores (positive to negative)
                sorted_arr = arr_with_sentiments[arr_with_sentiments[:, -1].argsort()[::-1]]
                for i in min(range(0,5),len(sorted_arr)):
                    item = sorted_arr[i]
                    print(Location(item))
            elif(user_input == "5"):
                doneChoosingActivities = False
                while doneChoosingActivities == False:
                    print("AITRAVEL => What kind of activities? Select one.")
                    print("----- 1 => ADVENTURE")
                    print("----- 2 => RELAXATION")
                    print("----- 3 => CULTURE")
                    print("----- 4 => I HAVE SOMETHING SPECIFIC IN MIND")
                    print("----- 5 => EXIT")
                    user_input = input("TRAVELLER => ")
                    adventure = ["Hiking","Adventure sports (e.g., zip-lining, paragliding)","Hot air balloon rides","Water sports (e.g., snorkeling, kayaking)"]
                    relaxation = ["Sightseeing", "Photography","Shopping", "Dining at local restaurants","Relaxing at beaches","Taking guided tours","Cruises or boat tours","Exploring local markets", "Visiting amusement parks","Wine or food tasting", "Taking scenic drives", "Relaxing in spas or wellness retreats","Cycling", "Attend workshops or classes","Camping", "Joining city walks or food tours","Taking cooking classes", "Golfing", "Engaging in community service or volunteer activities"]
                    culture = ["Visiting museums", "Attending cultural performances","Exploring historical sites","Wildlife watching", "Participating in local festivals","Visiting religious or spiritual sites","Learning about local history"]
                    if(user_input == "1"):
                        print("AITRAVEL => Great choice. You can choose one of the following activities:-")
                        for item in adventure:
                            print(item)
                        user_input = input("TRAVELLER => ")
                        filtered_data = [row for row in filtered_data if user_input in row[6] ]
                        if len(filtered_data) == 0:
                            print("AITRAVEL => There is a problem. Try again.")
                        else:
                            print("I have made some changes to the recommendations.")
                            print("AITRAVEL => Now we have "+str(len(filtered_data))+" locations.")
                            for item in filtered_data[:5] if len(filtered_data) >= 5 else filtered_data:
                                print(Location(item))
                    elif(user_input == "2"):
                        print("AITRAVEL => Great choice. You can choose one of the following activities:-")
                        for item in relaxation:
                            print(item)
                        user_input = input("TRAVELLER => ")
                        filtered_data = [row for row in filtered_data if user_input in row[6] ]
                        if len(filtered_data) == 0:
                            print("AITRAVEL => There is a problem. Try again.")
                        else:
                            print("I have made some changes to the recommendations.")
                            print("AITRAVEL => Now we have "+str(len(filtered_data))+" locations.")
                            for item in filtered_data[:5] if len(filtered_data) >= 5 else filtered_data:
                                print(Location(item))
                    elif(user_input == "3"):
                        print("AITRAVEL => Great choice. You can choose one of the following activities:-")
                        for item in culture:
                            print(item)
                        user_input = input("TRAVELLER => ")
                        filtered_data = [row for row in filtered_data if user_input in row[6] ]
                        if len(filtered_data) == 0:
                            print("AITRAVEL => There is a problem. Try again.")
                        else:
                            print("I have made some changes to the recommendations.")
                            print("AITRAVEL => Now we have "+str(len(filtered_data))+" locations.")
                            for item in filtered_data[:5] if len(filtered_data) >= 5 else filtered_data:
                                print(Location(item))
                    elif(user_input == "4"):
                        print("AITRAVEL => What activity do you want to do?")
                        user_input = input("TRAVELLER => ")
                        present = False
                        for item in adventure + relaxation + culture:
                            if item == user_input:
                                print("AITRAVEL => Okay, let me check.")
                                present = True
                        if present:
                            filtered_data = [row for row in filtered_data if user_input in row[6]]
                            print("Now we have "+str(len(filtered_data))+" locations. Let me show you some of them.")
                            for item in filtered_data[:5] if len(filtered_data) >= 5 else filtered_data:
                                print(Location(item))
                        else:
                            print("AITRAVEL => I do not think we have this activity.")

                    elif(user_input == "5"):
                        print("AITRAVEL => Okay, Glad I could be of help.")
                        doneChoosingActivities = True
            elif(user_input == "6"):
                print("AITRAVEL => Okay, first answer me this.")
                print("-----1 => Spots with best connectivity first.")
                print("-----2 => Sports with worst connectivity first.")
                user_input = input("TRAVELLER => ")
                if(user_input == "1"):
                    # we will just perform a simple sentiment analysis on the column Connectivity of the data.
                    # Apply sentiment analysis function to the "Connectivity" column in the array
                    sentiments = np.array([get_sentiment(row[4]) for row in filtered_data])
                    # Add the sentiment scores as a new column in the array
                    arr_with_sentiments = np.column_stack((filtered_data, sentiments))
                    # Sort the array based on the sentiment scores (positive to negative)
                    sorted_arr = arr_with_sentiments[arr_with_sentiments[:, -1].argsort()][::-1]
                    for i in range(min(5, len(sorted_arr))):
                        item = sorted_arr[i]
                        print(Location(item))
                elif(user_input == "2"):
                    # we will just perform a simple sentiment analysis on the column Connectivity of the data.
                    # Apply sentiment analysis function to the "Connectivity" column in the array
                    sentiments = np.array([get_sentiment(row[4]) for row in filtered_data])
                    # Add the sentiment scores as a new column in the array
                    arr_with_sentiments = np.column_stack((filtered_data, sentiments))
                    # Sort the array based on the sentiment scores (positive to negative)
                    sorted_arr = arr_with_sentiments[arr_with_sentiments[:, -1].argsort()]
                    for i in range(min(5, len(sorted_arr))):
                        item = sorted_arr[i]
                        print(Location(item))
                else:
                    return
            elif(user_input == "7"):
                filtered_data = sorted(filtered_data, key=lambda row: row[3], reverse=True)
                print("AITRAVEL => Great, I have sorted the data for you")
                for item in filtered_data[:5] if len(filtered_data) >= 5 else filtered_data:
                    print(Location(item))
            elif(user_input == "8"):
                filtered_data = sorted(filtered_data, key=lambda row: row[3])
                print("AITRAVEL => Great, I have sorted the data for you")
                for item in filtered_data[:5] if len(filtered_data) >= 5 else filtered_data:
                    print(Location(item))
            elif(user_input == "9"):
                print("AITRAVEL => Here, are the names of some filtered locations.")
                limit = min(20, len(filtered_data))
                random_numbers = random.sample(range(len(filtered_data)), limit)
                for i in random_numbers:
                    print(filtered_data[i][0])
            elif(user_input == "10"):
                print("AITRAVEL => Okay, let me show you some places in detail")
                limit = min(5, len(filtered_data))
                random_numbers = random.sample(range(len(filtered_data)), limit)
                for i in random_numbers:
                    print(Location(filtered_data[i]))
            elif(user_input == "11"):
                print("AITRAVEL => Okay, let me compose my final recommendation.")
                if len(filtered_data) == 0:
                    print("AITRAVEL => Sorry, I have no recommendations for you as no location matches your preference.")
                    return
                print("AITRAVEL => I have "+str(len(filtered_data))+" recommendations for you.")
                print("AITRAVEL => Let me summarise...")

                print("AITRAVEL = > If Feedbacks are more important to you. Then I will give you the location with the best feedbacks.")
                sentiments = np.array([get_sentiment(row[5]) for row in filtered_data])
                arr_with_sentiments = np.column_stack((filtered_data, sentiments))
                sorted_arr = arr_with_sentiments[arr_with_sentiments[:, -1].argsort()[::-1]]
                limit = min(1,len(sorted_arr))
                for i in range(0,limit):
                    item = sorted_arr[i]
                    print(Location(item))

                print("AITRAVEL = > If Connectivity is more important to you. Then I will give you the location with the best connectivity.")
                sentiments = np.array([get_sentiment(row[4]) for row in filtered_data])
                arr_with_sentiments = np.column_stack((filtered_data, sentiments))
                sorted_arr = arr_with_sentiments[arr_with_sentiments[:, -1].argsort()[::-1]]
                limit = min(1,len(sorted_arr))
                for i in range(0,limit):
                    item = sorted_arr[i]
                    print(Location(item))

                print("AITRAVEL = > If Ratings are more important to you. Then I will give you the highest rated location according to your preference.")
                sentiments = np.array([row for row in filtered_data])
                arr_with_sentiments = np.column_stack((filtered_data, sentiments))
                sorted_arr = arr_with_sentiments[arr_with_sentiments[:, 3].argsort()[::-1]]      
                limit = min(1,len(sorted_arr))
                for i in range(0,limit):
                    item = sorted_arr[i]
                    print(Location(item))   

                filtering = False
            else:
                print("AITRAVEL => There seems to be an error. Please try again.")

def recommend_destination(num, option):
    if(num == 1):
        noItem = True
        for item in my_data:
            if item[0] == option:
                spot = Location(item)
                noItem = False
                print(spot)
        if noItem:
            print(f"{option} is not present in the database.")
    elif(num == 2):
        # pick a random number from 0 to the length of my_data-1.
        # Give the location of htis index.
        index = random.randint(0, len(my_data))
        spot = Location(my_data[index])
        print(spot)
    elif(num == 3):
        print("AITRAVEL => Okay, this is the fun part. I love to give recommendations. Your wish is my command.")
        filter_recommendations()

def add_new_destination():
    print("AITRAVEL => Give me the location.")
    location = input("TRAVELLER => ")

    print("AITRAVEL => Give me the region it belongs to {India, China, Japan, Australia, Europe, North America,South America, Middle East, Africa}")
    region = input("TRAVELLER => ")

    print("AITRAVEL => Give me the weather you experienced")
    print("AITRAVEL => Was it Mild / Extreme?")
    me = input("TRAVELLER => ")
    print("AITRAVEL => Was it Summer / Winter?")
    sw = input("TRAVELLER => ")
    print("AITRAVEL => Was it Cloudy / Not Cloudy?")
    cn = input("TRAVELLER => ")
    print("AITRAVEL => Was there Rain / No Rain?")
    rn = input("TRAVELLER => ")

    weather = me + "," + sw + "," + cn + "," + rn

    print("AITRAVEL => Give me the rating.")
    rating = input("TRAVELLER => ")

    print("AITRAVEL => Give me the connectivity. {Give a 5 word decription of connectivity.}")
    connectivity = input("TRAVELLER => ")

    print("AITRAVEL => Give me the feedback. {About 20 words text feedback}")
    feedback = input("TRAVELLER => ")

    print("AITRAVEL => Give me the activities.")
    activities = []
    flag = True
    while(flag):
        print("AITRAVELLER => Enter an activity. To exit enter -1.")
        user_input = input("TRAVELLER => ")
        if(user_input == "-1"):
            flag = False
            print("Okay, that's all the activities.")
        else:
            activities.append(user_input)
        
    row = [location,region,weather,rating,connectivity,feedback,activities]
    spot = Location(row)
    print(spot)
    print("AITRAVEL => Do you really want to add this location to the database?")
    user_input = input("TRAVELLER (y/n)=> ")
    if(user_input == "y"):
        global data,my_data
        to_add_df = pd.DataFrame([row], columns=data.columns) 
        data = pd.concat([data, to_add_df], axis = 0,ignore_index=True)
        print("AITRAVEL => The location has been added successfully.")
        print("We had "+str(len(my_data))+" locations.")
        my_data = data.values
        data.to_csv('knowledge_base.csv', index=False)
        print("We now have "+str(len(my_data))+" locations.")
    return

def delete_destination_by_location(location_to_delete):
    global data, my_data
    row = []
    for item in my_data:
        if item[0] == location_to_delete:
            spot = Location(item)
            row = item
            print(spot)
    print("AITRAVEL => Do you really want to delete this item? (y/n)")
    user_input = input("TRAVELLER => ")
    if(user_input == "n"):
        print("AITRAVEL => Okay. I will not delete this location. FOR NOW :)")
        return
    else:
        data = data.loc[data['Location'] != location_to_delete].reset_index(drop=True)
        print("We had "+str(len(my_data))+" locations.")
        my_data = data.values
        data.to_csv('knowledge_base.csv', index=False)
        print("We now have "+str(len(my_data))+" locations.")

def add_feedback(location, feedback):
    global data,my_data
    row = []
    for item in my_data:
        if item[0] == location:
            spot = Location(item)
            row = item
            print(spot)
    print("AITRAVEL => Do you really want to add a feedback? (y/n)")
    user_input = input("TRAVELLER => ")
    if user_input == "y":
        if location in data['Location'].values:
            data.loc[data['Location'] == location, 'Feedback'] = feedback 
            my_data = data.values
            data.to_csv('knowledge_base.csv', index=False)
            print("The location has been updated.")
            for item in my_data:
                if item[0] == location:
                    spot = Location(item)
                    print(spot)
        else:
            print("Location not found: {location}")
    else:
        print("Okay, good to know.")
        return
    
def add_rating(location, rating):
    global data,my_data
    row = []
    for item in my_data:
        if item[0] == location:
            spot = Location(item)
            row = item
            print(spot)
    print("AITRAVEL => Do you really want to add a rating? (y/n)")
    user_input = input("TRAVELLER => ")
    if user_input == "y":
        if location in data['Location'].values:
            data.loc[data['Location'] == location, 'Rating'] = rating 
            my_data = data.values
            data.to_csv('knowledge_base.csv', index=False)
            print("The location has been updated.")
            for item in my_data:
                if item[0] == location:
                    spot = Location(item)
                    print(spot)
        else:
            print("Location not found: {location}")
    else:
        print("Okay, good to know.")
        return

def main():
    print()
    print("----------------------------------------  Hello, this is AITRAVEL. You must be a TRAVELLER! --------------------")
    print("----------------------------------------  I am very excited to find you a place to visit.  --------------------")
    print(f"----------------------------------------  We have {len(data)} tourist spots for you to choose from.  --------------------")
    print()
    flag = True
    while(flag):
        print("AITRAVEL => Pick one of the following options:-")
        print("-----EXIT = -1")
        print("-----1 => I know where I want to go. {Enter the location directly}")
        print("-----2 => I do not know where i want to go, suggest me a place. {A random location}")
        print("-----3 => I know what 'KIND' of a place I want to go to. I want to use filters. {Filter the options}")
        print("-----4 => I know a place I want to share. {Add new destination}")
        print("-----5 => You think that place is real. But it is not. {Delete a destionation}")
        print("-----6 => I want to share my experience. {Add feedback}")
        print("-----7 => I want to give rating. {Add Rating}")
        # Taking user input with a text prompt
        user_input = input("TRAVELLER {Pick a number} => ")
        if(user_input == "1"):
            print("AITRAVEL => Okay, Enter the location and I shall tell you what that place is like.")
            user_input = input("TRAVELLER => ")
            # we will create an array of inputs and send it to the recommend_location function. It will find the location from the database and make a location object and display it.
            # if there is no such location we just say there is no such location. Try again.
            recommend_destination(1,user_input)
        elif(user_input == "2"):
            print("AITRAVEL => Okay, get ready for a random location. We can do this all day.")
            secondFlag = True
            while(secondFlag):
                print("1 => Show me a random location.")
                print("2=> Exit")
                user_input = input("TRAVELLER => ")
                if(user_input == "1"):
                    recommend_destination(2,"random")
                elif(user_input == "2"):
                    secondFlag = False
                    print("Fine, we will exit now.")
                else:
                    print("Error try again")
        elif(user_input == "3"):
            recommend_destination(3,"features")
        elif(user_input == "4"):
            print("AITRAVEL => You will have to give me some details, buddy.")
            add_new_destination()
        elif(user_input == "5"):
            print("AITRAVEL => I can only remove a tourist spot, if you enter the right location.")
            user_input = input("TRAVELLER => ")
            notInData = True
            for item in my_data:
                if item[0] == user_input:
                    notInData = False
                    delete_destination_by_location(user_input)
            if notInData:
                print(f"{user_input} is not present in the database.")
        elif(user_input == "6"):
            print("AITRAVEL => Enter the location first and then the feedback. If there is feedback for the location it will be overwritten.")
            location = input("TRAVELLER (Enter location) => ")
            feedback = input("TRAVELLER (Feedback in 20 words) => ")
            if location in data['Location'].values:
                add_feedback(location,feedback)
            else:
                print(f"{location} is not present in the database.")
        elif(user_input == "7"):
            print("AITRAVEL => Enter the location first and then the rating. If there is rating for the location it will be overwritten.")
            location = input("TRAVELLER (Enter location) => ")
            rating = input("TRAVELLER (Rating) => ")
            if location in data['Location'].values:
                add_rating(location,rating)
            else:
                print(f"{location} is not present in the database.")
        elif(user_input == "-1"):
            print("AITRAVEL => Glad I could be of help.")
            flag = False
        else:
            print("Error. Try again.")
    
if __name__ == "__main__":
    main()

