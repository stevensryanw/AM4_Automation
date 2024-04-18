# AM4 Automation Bot by Ryan Stevens

### AM4: https://www.airlinemanager.com

## Bot Features and Functions

- [X] Login - ```loginAM4()```
- [X] Flight departures - ```departFlights()```
    - [ ] Route Optimization - ```routeOptimization()```
        - [ ] Demand - ```optimDemand()```
        - [ ] Price - ```optimPrice()```
        - [ ] Capacity - ```optimCapacity()```
        - [ ] Plane Upgrades (Speed, Efficiency(fuel, co2)) - ```fleetUpgrade()```
- [X] Fuel and CO2 purchasing/filling (Fuel < $600, CO2 < $125) - ```buyFuelandCO2()```
- [ ] Maintenance Planning - ```fleetMaintenance()```
    - [ ] Bulk ACheck Planning (< 25 hours) - ```bulkACheck()```
    - [ ] Bulk Repair Planning (> 40% wear) - ```bulkRepair()```

# Running the bot
- Open the repository with VScode and use the requirements.txt to create a ./venv Python virtual environment
- Run bot.py
- Input username, password, and whether or not headless
- Submit then close the tab
    - Should see prints in the terminal for login, fuel/co2, and departures