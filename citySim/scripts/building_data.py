building_data = {
    "road_straight": {
        "Information": ["Cost", "Maintenance"],
        'Type': "road_straight",
        'Category': "Roads",
        'Name': 'Straight Road',
        'Description': 'Like a laser beam on asphalt, straight from A to B',
        'Cost': 150,
        'Maintenance': 3,
        'Revenue': 0, 
        'Population': 0,
        'Score': 0,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_strt_ns.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_strt_ns.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_strt_ew.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_strt_ew.png"}}},
    "road_crossing": {
        "Information": ["Cost", "Maintenance"],
        'Type': "road_crossing",
        'Category': "Roads",
        'Name': 'Road Crossing',
        'Description': "'The human highway connection.' Look both ways!",
        'Cost': 200,
        'Maintenance': 4,
        'Revenue': 0, 
        'Population': 0,
        'Score': 1,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_cros_ns.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_cros_ns.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_cros_ew.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_cros_ew.png"}}},
    "road_uturn": {
        "Information": ["Cost", "Maintenance"],
        'Type': "road_uturn",
        'Category': "Roads",
        'Name': 'U-Turn',
        'Description': 'Because sometimes the best path is the one you just passed',
        'Cost': 100,
        'Maintenance': 2,
        'Revenue': 0, 
        'Population': 0,
        'Score': 0,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_turn_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_turn_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_turn_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_turn_w.png"}}},
    "road_curved": {
        "Information": ["Cost", "Maintenance"],
        'Type': "road_curved",
        'Category': "Roads",
        'Name': 'Curved Road',
        'Description': "Embrace the bends. Straight-line monotony is so last road",
        'Cost': 200,
        'Maintenance': 4,
        'Revenue': 0, 
        'Population': 0,
        'Score': 0,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_curv_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_curv_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_curv_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_curv_w.png"}}},
    "road_3way": {
        "Information": ["Cost", "Maintenance"],
        'Type': "road_3way",
        'Category': "Roads",
        'Name': '3-Way Intersection',
        'Description': 'Turning points, twists, and tales unfold in threes',
        'Cost': 400,
        'Maintenance': 8,
        'Revenue': 0, 
        'Population': 0,
        'Score': 0,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_3way_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_3way_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_3way_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_3way_w.png"}}},
    "road_4way": {
        "Information": ["Cost", "Maintenance"],
        'Type': "road_4way",
        'Category': "Roads",
        'Name': '4-Way Intersection',
        'Description': 'Four ways, one decision: Crossroad carnival!',
        'Cost': 600,
        'Maintenance': 12,
        'Revenue': 0, 
        'Population': 0,
        'Score': 0,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_4way_nsew.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_4way_nsew.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_4way_nsew.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/road/road_4way_nsew.png"}}},
    "util_wind": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "util_wind",
        'Category': "Utilities",
        'Name': 'Wind Turbine',
        'Description': "Like a record, baby, right 'round, 'round, 'round",
        'Cost': 250,
        'Maintenance': 15,
        'Revenue': 25, 
        'Population': 0,
        'Score': 2,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/util/util_wind_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/util/util_wind_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/util/util_wind_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/util/util_wind_w.png"}}},
    "util_powe": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "util_powe",
        'Category': "Utilities",
        'Name': 'Power Plant',
        'Description': "Watt's up? Not your bill, thank the Power Plant later",
        'Cost': 1250,
        'Maintenance': 5,
        'Revenue': 35, 
        'Population': 0,
        'Score': 3,
        "Rotations": {"north": {'Width': 2,'Height': 2,'ImagePath': "images/util/util_powe_n.png"},
                    "south": {'Width': 2,'Height': 2,'ImagePath': "images/util/util_powe_s.png"},
                    "east": {'Width': 2,'Height': 2,'ImagePath': "images/util/util_powe_e.png"},
                    "west": {'Width': 2,'Height': 2,'ImagePath': "images/util/util_powe_w.png"}}},
    "util_wate": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "util_wate",
        'Category': "Utilities",
        'Name': 'Water Tower',
        'Description': "Keeping water high, and expectations around the same",
        'Cost': 200,
        'Maintenance': 15,
        'Revenue': 20, 
        'Population': 0,
        'Score': 2,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/util/util_wate_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/util/util_wate_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/util/util_wate_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/util/util_wate_w.png"}}},
    "util_tre": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "util_tre",
        'Category': "Utilities",
        'Name': 'Water Treatment Plant',
        'Description': "Turning your gold liquid to liquid gold",
        'Cost': 550,
        'Maintenance': 5,
        'Revenue': 35, 
        'Population': 0,
        'Score': 3,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "util_land": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "util_land",
        'Category': "Utilities",
        'Name': 'Landfill Site',
        'Description': "Collecting memories you'd rather forget",
        'Cost': 550,
        'Maintenance': 5,
        'Revenue': 35, 
        'Population': 0,
        'Score': 2,
        "Rotations": {"north": {'Width': 3,'Height': 2,'ImagePath': "images/util/util_land_n.png"},
                    "south": {'Width': 3,'Height': 2,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 2,'Height': 3,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 2,'Height': 3,'ImagePath': "images/resi/resi1_w.png"}}},
    "util_cell": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "util_cell",
        'Category': "Utilities",
        'Name': 'Cell Tower',
        'Description': "Emitting signals and conspiracies circa 2023",
        'Cost': 550,
        'Maintenance': 5,
        'Revenue': 35, 
        'Population': 0,
        'Score': 2,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "serv_hall": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "serv_hall",
        'Category': "Services",
        'Name': 'City Hall',
        'Description': "Home of fading dreams and questionable decisions",
        'Cost': 550,
        'Maintenance': 5,
        'Revenue': 35, 
        'Population': 0,
        'Score': 5,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "serv_bank": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "serv_bank",
        'Category': "Services",
        'Name': 'City Bank',
        'Description': "Turning your savings into slightly more savings",
        'Cost': 550,
        'Maintenance': 5,
        'Revenue': 35, 
        'Population': 0,
        'Score': 2,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "serv_scho": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "serv_scho",
        'Category': "Services",
        'Name': 'School',
        'Description': "Teaching tomorrow's leaders how to Google today",
        'Cost': 550,
        'Maintenance': 5,
        'Revenue': 35, 
        'Population': 0,
        'Score': 3,
        "Rotations": {"north": {'Width': 5,'Height': 3,'ImagePath': "images/serv/serv_scho_n.png"},
                    "south": {'Width': 5,'Height': 3,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 3,'Height': 5,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 3,'Height': 5,'ImagePath': "images/resi/resi1_w.png"}}},
    "serv_poli": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "serv_poli",
        'Category': "Services",
        'Name': 'Police Precinct',
        'Description': "Keeping crime to a minimum, one donut at a time",
        'Cost': 550,
        'Maintenance': 5,
        'Revenue': 35, 
        'Population': 0,
        'Score': 3,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "serv_fire": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "serv_fire",
        'Category': "Services",
        'Name': 'Fire Station',
        'Description': "Home of the world's most well-rested firefighters",
        'Cost': 550,
        'Maintenance': 5,
        'Revenue': 35, 
        'Population': 0,
        'Score': 3,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "serv_hosp": {
        "Information": ["Cost", "Maintenance", "Revenue"],
        'Type': "serv_hosp",
        'Category': "Services",
        'Name': 'Hospital',
        'Description': "Where health is wealth, and beds are investments",
        'Cost': 550,
        'Maintenance': 5,
        'Revenue': 35, 
        'Population': 0,
        'Score': 3,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "resi_mobi": {
        "Information": ["Cost", "Population"],
        'Type': "resi_mobi",
        'Category': "Residential",
        'Name': 'Mobile Homes',
        'Description': 'Living large in a pocket-sized paradise',
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 100,
        'Score': 2,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "resi_subu": {
        "Information": ["Cost", "Revenue"],
        'Type': "resi_subu",
        'Category': "Residential",
        'Name': 'Suburbian Home',
        'Description': 'Four walls and a mortgage for sale - sanity not included',
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 4,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "resi_apar": {
        "Information": ["Cost", "Revenue"],
        'Type': "resi_apar",
        'Category': "Residential",
        'Name': 'Apartment Block',
        'Description': 'Personal space? Fantasy. Rent money? Reality.',
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 6,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "resi_high": {
        "Information": ["Cost", "Revenue"],
        'Type': "resi_high",
        'Category': "Residential",
        'Name': 'Luxury Tower',
        'Description': 'Because everyone dreams of a cramped penthouse',
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 8,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "comm_mark": {
        "Information": ["Cost", "Revenue"],
        'Type': "comm_mark",
        'Category': "Commercial",
        'Name': 'Town Market',
        'Description': "Welcome to the Market - where expiration dates are merely suggestions",
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 2,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "comm_shop": {
        "Information": ["Cost", "Revenue"],
        'Type': "comm_shop",
        'Category': "Commercial",
        'Name': 'Corner Shop',
        'Description': "Tiny store, huge prices - it's a surprise at every checkout",
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 4,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},     
    "comm_rest": {
        "Information": ["Cost", "Revenue"],
        'Type': "comm_rest",
        'Category': "Commercial",
        'Name': 'Fancy Restaurant',
        'Description': 'Happiness here is directly proportional to the number on the bill',
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 6,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},              
    "comm_cent": {
        "Information": ["Cost", "Revenue"],
        'Type': "comm_cent",
        'Category': "Commercial",
        'Name': 'Shopping Centre',
        'Description': 'Shop till you drop, and then shop some more',
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 8,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "indu_craf": {
        "Information": ["Cost", "Revenue"],
        'Type': "indu_craf",
        'Category': "Industrial",
        'Name': "Craftman's Corner",
        'Description': 'Mastering the art of accidental excellence',
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 2,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},       
    "indu_ware": {
        "Information": ["Cost", "Revenue"],
        'Type': "indu_ware",
        'Category': "Industrial",
        'Name': "Warehouse",
        'Description': 'Where packages are kept, along with the occasional spider',
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 4,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},         
    "indu_offi": {
        "Information": ["Cost", "Revenue"],
        'Type': "indu_offi",
        'Category': "Industrial",
        'Name': "Corporate Offices",
        'Description': 'Fancy titles, endless memos and zero excitement',
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 6,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}}, 
    "tran_busd": {
        "Information": ["Cost", "Revenue"],
        'Type': "tran_fact",
        'Category': "Transport",
        'Name': "Bus Depot",
        'Description': 'Buses: because teleportation is too predictable',
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 2,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},  
    "tran_trai": {
        "Information": ["Cost", "Revenue"],
        'Type': "tran_trai",
        'Category': "Transport",
        'Name': "Train Station",
        'Description': "Choo-choose your delay, we've got options! Many, in fact",
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 4,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},  
    "tran_tras": {
        "Information": ["Cost", "Revenue"],
        'Type': "tran_tras",
        'Category': "Transport",
        'Name': "Straight Tracks",
        'Description': "Straight tracks in a twisted world",
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 0,
        "Rotations": {"north": {'Width': 1,'Height': 4,'ImagePath': "images/tran/tran_tras_ns.png"},
                    "south": {'Width': 1,'Height': 4,'ImagePath': "images/tran/tran_tras_ns.png"},
                    "east": {'Width': 4,'Height': 1,'ImagePath': "images/tran/tran_tras_ew.png"},
                    "west": {'Width': 4,'Height': 1,'ImagePath': "images/tran/tran_tras_ew.png"}}},   
    "tran_trac": {
        "Information": ["Cost", "Revenue"],
        'Type': "tran_trac",
        'Category': "Transport",
        'Name': "Curved Tracks",
        'Description': "Twisted tracks in a tw.. wait, that's already been done",
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 0,
        "Rotations": {"north": {'Width': 2,'Height': 2,'ImagePath': "images/tran/tran_trac_n.png"},
                    "south": {'Width': 2,'Height': 2,'ImagePath': "images/tran/tran_trac_s.png"},
                    "east": {'Width': 2,'Height': 2,'ImagePath': "images/tran/tran_trac_e.png"},
                    "west": {'Width': 2,'Height': 2,'ImagePath': "images/tran/tran_trac_w.png"}}},    
    "tran_airp": {
        "Information": ["Cost", "Revenue"],
        'Type': "tran_airp",
        'Category': "Transport",
        'Name': "International Airport",
        'Description': "Uniting the skies in a symphony of missed connections",
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 8,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},    
    "ente_stad": {
        "Information": ["Cost", "Revenue"],
        'Type': "ente_stad",
        'Category': "Entertainment",
        'Name': "Intersports Stadium",
        'Description': "Goals, touchdowns, and a hundred thousand cheers.",
        'Cost': 80,
        'Maintenance': 0,
        'Revenue': 500, 
        'Population': 0,
        'Score': 10,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},
    "park_path": {
        "Information": ["Cost", "Revenue"],
        'Type': "park_path",
        'Category': "Parks",
        'Name': "Park Path",
        'Description': "Park Path.",
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 0,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},                              
    "land_path": {
        "Information": ["Cost", "Revenue"],
        'Type': "land_path",
        'Category': "Landscape",
        'Name': "Landscape Path",
        'Description': "Landscape Path.",
        'Cost': 80,
        'Maintenance': 250,
        'Revenue': 0, 
        'Population': 0,
        'Score': 0,
        "Rotations": {"north": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_n.png"},
                    "south": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_s.png"},
                    "east": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_e.png"},
                    "west": {'Width': 1,'Height': 1,'ImagePath': "images/resi/resi1_w.png"}}},                               
}