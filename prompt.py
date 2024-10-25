prompt=[
    """
    You are an expert in converting English questions to SQL queries.
    The SQL database has the name flights_details and has the following columns:
    id,year,month,day,dep_time,sched_dep_time,dep_delay,arr_time,
    sched_arr_time,arr_delay,carrier,flight,tailnum,origin,dest,air_time,
    distance,hour,minute,time_hour,name. A question in natural english language could
    come up as, For example, Example 1: How many flights originated from EWR in July, 2023
    a equivalent query would be SELECT * FROM flights_details where month is '07';
    Following is the description of columns in the table\n\n
    id: A unique identifier for each flight record in the dataset.
    year: The year in which the flight took place (2013 in this dataset).
    month: The month in which the flight took place (1 to 12).
    day: The day of the month on which the flight took place (1 to 31).
    dep_time: The actual local departure time of the flight, in 24-hour format (hhmm).
    sched_dep_time: The scheduled local departure time of the flight, in 24-hour format (hhmm).
    dep_delay: The difference between the actual and scheduled departure times of the flight, in minutes. A positive value indicates a delayed departure, while a negative value indicates an early departure.
    arr_time: The actual local arrival time of the flight, in 24-hour format (hhmm).
    sched_arr_time: The scheduled local arrival time of the flight, in 24-hour format (hhmm).
    arr_delay: The difference between the actual and scheduled arrival times of the flight, in minutes. A positive value indicates a delayed arrival, while a negative value indicates an early arrival.
    carrier: The two-letter code of the airline carrier for the flight.
    flight: The flight number of the flight.
    tailnum: The unique identifier of the aircraft used for the flight.
    origin: The three-letter code of the airport of origin for the flight.
    dest: The three-letter code of the destination airport for the flight.
    air_time: The duration of the flight, in minutes.
    distance: The distance between the origin and destination airports, in miles.
    hour: The hour component of the scheduled departure time, in local time.
    minute: The minute component of the scheduled departure time, in local time.
    time_hour: The scheduled departure time of the flight, in local time and format (yyyy-mm-dd hh:mm:ss).
    name: The name of the airline carrier for the flight.\n\n
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

carrier = [
        'United Air Lines Inc.',
        'American Airlines Inc.',
        'JetBlue Airways',
        'Delta Air Lines Inc.',
        'ExpressJet Airlines Inc.',
        'Envoy Air',
        'US Airways Inc.',
        'Southwest Airlines Co.',
        'Virgin America',
        'AirTran Airways Corporation',
        'Alaska Airlines Inc.',
        'Endeavor Air Inc.',
        'Frontier Airlines Inc.',
        'Hawaiian Airlines Inc.',
        'Mesa Airlines Inc.',
        'SkyWest Airlines Inc.',
]

origin = [
        'EWR',
        'JFK',
        'LGA',
]

destination = [
        'IAH',
        'MIA',
        'BQN',
        'ATL',
        'ORD',
        'FLL',
        'IAD',
        'MCO',
        'PBI',
        'TPA',
        'LAX',
        'SFO',
        'DFW',
        'BOS',
        'LAS',
        'MSP',
        'DTW',
        'RSW',
        'SJU',
        'PHX',
        'BWI',
        'CLT',
        'BUF',
        'DEN',
        'SNA',
        'MSY',
        'SLC',
        'XNA',
        'MKE',
        'SEA',
        'ROC',
        'SYR',
        'SRQ',
        'RDU',
        'CMH',
        'JAX',
        'CHS',
        'MEM',
        'PIT',
        'SAN',
        'DCA',
        'CLE',
        'STL',
        'MYR',
        'JAC',
        'MDW',
        'HNL',
        'BNA',
        'AUS',
        'BTV',
        'PHL',
        'STT',
        'EGE',
        'AVL',
        'PWM',
        'IND',
        'SAV',
        'CAK',
        'HOU',
        'LGB',
        'DAY',
        'ALB',
        'BDL',
        'MHT',
        'MSN',
        'GSO',
        'CVG',
        'BUR',
        'RIC',
        'GSP',
        'GRR',
        'MCI',
        'ORF',
        'SAT',
        'SDF',
        'PDX',
        'SJC',
        'OMA',
        'CRW',
        'OAK',
        'SMF',
        'TUL',
        'TYS',
        'OKC',
        'PVD',
        'DSM',
        'PSE',
        'BHM',
        'CAE',
        'HDN',
        'BZN',
        'MTJ',
        'EYW',
        'PSP',
        'ACK',
        'BGR',
        'ABQ',
        'ILM',
        'MVY',
        'SBN',
        'LEX',
        'CHO',
        'TVC',
        'ANC',
        'LGA',
]