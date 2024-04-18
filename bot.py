from selenium import webdriver
import customtkinter as ctk
import time
import random

run = True
uptime = 0
count = 0

#For creating random random numbers from a range for sleep times throughout the script
def rand_range(min, max):
    return random.randint(min, max)

'''Login to Airline Manager 4'''
def loginAM4():
    #Login xpath: /html/body/div[4]/div/div[2]/div[1]/div/button[2]
    loginbutton1 = driver.find_element('xpath', '/html/body/div[4]/div/div[2]/div[1]/div/button[2]')
    loginbutton1.click()
    time.sleep(rand_range(3, 7))
    #Username xpath: /html/body/div[1]/div/div/div[2]/div/form/div[1]/input
    usernamefield = driver.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/form/div[1]/input')
    usernamefield.send_keys(username)
    time.sleep(rand_range(3, 7))
    #Password xpath: /html/body/div[1]/div/div/div[2]/div/form/div[2]/input
    passwordfield = driver.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/form/div[2]/input')
    passwordfield.send_keys(password)
    time.sleep(rand_range(3, 7))
    #Login xpath: /html/body/div[1]/div/div/div[2]/div/form/div[5]/button
    loginbutton2 = driver.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/form/div[5]/button')
    loginbutton2.click()
    time.sleep(rand_range(15, 30))
    print('Logged in to Airline Manager 4')
    #Reload incase of any popups
    driver.get('https://www.airlinemanager.com')
    time.sleep(rand_range(15, 30))

'''Filling fuel and co2'''
def buyFuelandCO2():
    #Fuel tab xpath: /html/body/div[11]/div/div[4]/div[3]/div
    fueltab = driver.find_element('xpath', '/html/body/div[11]/div/div[4]/div[3]/div')
    fueltab.click()
    time.sleep(rand_range(3, 7))
    #Fuel price xpath: /html/body/div[9]/div/div/div[3]/div[2]/div/div[5]/b/span
    fuelprice = str(driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div/div[5]/b/span').text)
    Sfuel = fuelprice.replace(',', '')
    Ifuel = int(Sfuel)
    print('Fuel price: ' + Sfuel)
    if Ifuel <= 600:
        #Capacity xpath: /html/body/div[9]/div/div/div[3]/div[2]/div/div[3]/span[2]
        capacityfuel = str(driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div/div[3]/span[2]').text)
        Scapacityfuel = capacityfuel.replace(',', '')
        Icapacityfuel = int(Scapacityfuel)
        if Icapacityfuel > 0:
            #Input xpath: /html/body/div[9]/div/div/div[3]/div[2]/div/div[6]/input
            inputfieldfuel = driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div/div[6]/input')
            inputfieldfuel.send_keys(Icapacityfuel)
            time.sleep(rand_range(3, 7))
            #Purchase xpath: /html/body/div[9]/div/div/div[3]/div[2]/div/div[7]/div/button[2]
            purchasebuttonfuel = driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div/div[7]/div/button[2]')
            purchasebuttonfuel.click()
            print('Purchased ' + Scapacityfuel + ' fuel for ' + Sfuel + ' each a total of $' + str((Icapacityfuel/1000) * Ifuel))
    #CO2 tab xpath: /html/body/div[9]/div/div/div[3]/div[1]/button[2]
    co2tab = driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[1]/button[2]')
    co2tab.click()
    time.sleep(rand_range(3, 7))
    #CO2 price xpath: /html/body/div[9]/div/div/div[3]/div[2]/div/div/div[6]/b/span
    co2price = str(driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div/div/div[6]/b/span').text)
    Sco2 = co2price.replace(',', '')
    Ico2 = int(Sco2)
    print('CO2 price: ' + Sco2)
    if Ico2 <= 125:
        #Capacity xpath: /html/body/div[9]/div/div/div[3]/div[2]/div/div/div[4]/span[2]
        capacityCO2 = str(driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div/div/div[4]/span[2]').text)
        ScapacityCO2 = capacityCO2.replace(',', '')
        IcapacityCO2 = int(ScapacityCO2)
        if IcapacityCO2 > 0:
            #Input xpath: /html/body/div[9]/div/div/div[3]/div[2]/div/div/div[7]/input
            inputfieldCO2 = driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div/div/div[7]/input')
            inputfieldCO2.send_keys(IcapacityCO2)
            time.sleep(rand_range(3, 7))
            #Purchase xpath: /html/body/div[9]/div/div/div[3]/div[2]/div/div/div[8]/div/button[2]
            purchasebuttonCO2 = driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div/div/div[8]/div/button[2]')
            purchasebuttonCO2.click()
            print('Purchased ' + ScapacityCO2 + ' CO2 for ' + Sco2 + ' each for a total of $' + str((IcapacityCO2/1000) * Ico2))
    #Exit fuel and co2 popup xpath: /html/body/div[9]/div/div/div[1]/div/span
    exitF02button = driver.find_element('xpath', '/html/body/div[9]/div/div/div[1]/div/span')
    exitF02button.click()

'''Departing Flights'''
def departFlights():
    #Arrivals/Departures popup xpath: /html/body/div[11]/div/div[2]/div/span
    ADpopup = driver.find_element('xpath', '/html/body/div[11]/div/div[2]/div/span')
    time.sleep(rand_range(3, 7))
    #Lets see if the ADpopup is open by checking if the xpath class ends with left or right
    if ADpopup.get_attribute('class').endswith('right'):
        #If it ends with right then we need to click it to open the popup
        ADpopup.click()
        time.sleep(rand_range(3, 7))
        #Number of planes to depart xpath: /html/body/div[11]/div/div[3]/div[5]/div[1]/div[2]/div/button[2]/span[2]
        #numdeparted = driver.find_element('xpath', '/html/body/div[11]/div/div[3]/div[5]/div[1]/div[2]/div/button[2]/span[2]')
        #Depart button xpath: /html/body/div[11]/div/div[3]/div[5]/div[1]/div[2]/div/button[2]
        try:
            #Number of planes to depart xpath: //*[@id="listDepartAmount"]
            numdeparted = driver.find_element('xpath', '//*[@id="listDepartAmount"]')
            departbutton = driver.find_element('xpath', '/html/body/div[11]/div/div[3]/div[5]/div[1]/div[2]/div/button[2]')
            departbutton.click()
            print('Departed ' + numdeparted.text + ' flights')
            time.sleep(rand_range(3, 7))
        except:
            print('No flights to depart')
    else:
        #Depart button xpath: /html/body/div[11]/div/div[3]/div[5]/div[1]/div[2]/div/button[2]
        try:
            #Number of planes to depart xpath: //*[@id="listDepartAmount"]
            numdeparted = driver.find_element('xpath', '//*[@id="listDepartAmount"]')
            departbutton = driver.find_element('xpath', '/html/body/div[11]/div/div[3]/div[5]/div[1]/div[2]/div/button[2]')
            departbutton.click()
            print('Departed ' + numdeparted.text + ' flights')
            time.sleep(rand_range(3, 7))
        except:
            print('No flights to depart')

'''Route Optimization (demand, price, capacity, upgrades)'''
def routeOptimization():
    optimDemand()
    optimPrice()
    optimCapacity()
    fleetUpgrade()

def optimDemand():
    return 0

def optimPrice():
    return 0

def optimCapacity():
    return 0

def fleetUpgrade():
    return 0

'''Fleet Maintenance'''
def fleetMaintenance():
    #Maintenance tab xpath: /html/body/div[11]/div/div[4]/div[4]/div[2]
    maintenancetab = driver.find_element('xpath', '/html/body/div[11]/div/div[4]/div[4]/div[2]')
    maintenancetab.click()
    time.sleep(rand_range(3, 5))

    #Plan maintenance xpath: /html/body/div[9]/div/div/div[3]/div[1]/button[2]
    planmaintenancebutton = driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[1]/button[2]')
    planmaintenancebutton.click()
    time.sleep(rand_range(3, 5))

    #Bulk check xpath: /html/body/div[9]/div/div/div[3]/div[2]/div[1]/div[3]/div/button[2]
    bulkcheckbutton = driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div[1]/div[3]/div/button[2]')
    bulkcheckbutton.click()
    time.sleep(rand_range(3, 5))

    # Acheck table xpath: /html/body/div[9]/div/div/div[3]/div[2]/div[3]
    # achecktable = driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div[3]')
    # print(achecktable.text)
    # We need to parse the table and if hours is less than 25 select it
    # for i in achecktable:
    #     print(achecktable[i].text)
    #     #Hours xpath: /html/body/div[9]/div/div/div[3]/div[2]/div[3]/div[2]/div[3]/b /html/body/div[9]/div/div/div[3]/div[2]/div[3]/div[2]/div[4]/b
    #     hours = driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div[3]/div[1]/div[2]')
    #     if int(hours.text) < 25:
    #         #Select xpath: /html/body/div[9]/div/div/div[3]/div[2]/div[3]/div[2]/div[3]
    #         select = driver.find_element('xpath', '/html/body/div[9]/div/div/div[3]/div[2]/div[3]/div[1]/div[1]/input')
    #         select.click()


    #Bulk repair xpath: /html/body/div[9]/div/div/div[3]/div[2]/div[1]/div[3]/div/button[1]

def bulkACheck():
    return 0
def bulkRepair():
    return 0

username = ''
password = ''
headless = False

def get_info():
    global username
    global password
    global headless
    username = username_entry.get()
    password = password_entry.get()
    is_headless = headless_check.get()
    print('Username: ' + username)
    print('Password: ' + password)
    if is_headless == 1:
        headless = True
        print('Headless')
    elif is_headless == 0:
        headless = False
        print('Not Headless')
    else:
        print('Error')

'''Tkinter GUI for inputting username and password  and headless or not'''
root = ctk.CTk()
#Username and password entry
username_label = ctk.CTkLabel(root, text='Username')
username_entry = ctk.CTkEntry(root)
password_label = ctk.CTkLabel(root, text='Password')
password_entry = ctk.CTkEntry(root, show='*')
#Checkbox for headless or not
headless_check = ctk.CTkCheckBox(root, text='Headless')
#Submit button
submit_button = ctk.CTkButton(root, text='Submit', command=get_info)
#Packing widgets
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
headless_check.pack()
submit_button.pack()
#Run tkinter main loop
root.geometry('200x200')
root.mainloop()
#Close tkinter GUI
root.quit()
#root.destroy()

'''Main loop for running the bot'''
while run:
    debug = True
    start = time.time()
    if headless == True:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif headless == False:
        driver = webdriver.Chrome()
    else:
        print('Error')
        break
    #Opening https://www.airlinemanager.com
    print('Running bot: ' + str(count))
    driver.get('https://www.airlinemanager.com')
    time.sleep(rand_range(10, 20))
    loginAM4()
    buyFuelandCO2()
    departFlights()
    #fleetMaintenance()
    buyFuelandCO2()
    #At the end of each time lets always wait a random amount of time between 5min and 10min
    driver.quit()
    sleep = rand_range(300, 800)
    runtime = time.time() - start
    uptime += sleep + runtime
    print('Runtime: ' + str(runtime) + ' seconds')
    print('Sleeping: ' + str(sleep) + ' seconds')
    print('Uptime: ' + str(uptime) + ' seconds')
    count += 1
    time.sleep(sleep)