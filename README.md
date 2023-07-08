# mac-battery-count-tracker
How does the battery count work? This project attempts to seek an answer to this question.

## Summary
One of the things that become imperative to care for when you get your new Macbook is the battery life. However, it can be so confusing and frustrating when you make some findings to know how to prolong the life of your battery. The blogs don't come to the rescue, neither do the YouTube videos! It all becomes overwhelming with time that the only alternative is to go by your instinct. While instincts can be to one's advantage, it also poses some threat to the battery life of your system.
This aim of this work is to investigate best practices to prolong a Macbook laptop.
I must need say that this experiment is being carried out on a Macbook M1 Pro. However, I feel the code should work on any other Macbook.

It is also worth noting that this project is an iterative one, I intend to add more features to it as time goes by, perhaps extending it to work on Windows as well.

## Background
Recall that feeling when you got your first Macbook? If you got it with your personal funds, you must have made a serious sacrifice to do so unless you're a politician's child or one of the wealthy business tycoons 😁. So, yes, I was gifted the laptop as a reward for a good grade after my first semester at American University (AU), Washington DC. 

I am a meticulous person who loves being economical about most things, saving resources and looking for ways to tackle issues more efficiently and effectively. My Macbook battery was one of the things I wanted to ensure I was using properly, and so, I went on the internet to search for the best practices on how to use my battery but I returned from my search even more confused than I was.

The result of that confusion was what led me to this project.

**_So, how is this work different from others that I have seen?_**

Most works I have seen on battery tracking are to get notifications on the system when the battery reaches a particular level, but, I don't even know what level is right for me, so, how can I possibly even know what help these notifications offer to me ? 🤔

Hence, my approach was to utilize my battery and then keep track of the changes. I did this by keeping track of certain features. This process is automated and runs at certain scheduled periods of the day. These values of these features are then recorded in an Excel file. I have **intentionally** left some of the variables unclean so that I can use **pandas** to clean the file. One of the things I aim to do later is to save into a **SQL** database (SQLite, MySQL or PostgresSQL) as well as **Mongodb** - which is NoSQL.

Eventually, I intend to use **selenium** to automate the process of pushing to codes from my system to my github repo after the record is taken.

The features are given below:

`PowerAdapter`: Indicates if the adapter is **plugged** or **unplugged** at the time of the recording. 

`ChargeStatus`: Indicates if the system is **charged**, **discharging**, or using **AC**. 

`BatteryPercent`: The percentage of the battery at the time of saving the battery information.

`BatteryCondition`: The condition of the battery. It should be _normal_ if the battery is still okay. 

`BatteryHealth`: The current health, also known as maximum capacity of the battery (in %).

`CycleCount`: The cycle count which is one of the things that indicate how good the battery is. 

I know that there are lots of things I can do with this data, such as predicting my cycle count based on my pattern of usage of my Macbook.

With time, I will be updating this README file.

Stay tuned!

Johnson Odejide

&copy; July 2023