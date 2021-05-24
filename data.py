prefix = "$"
routines = {
  # change nagar bhanya bujdainas? gede? add ni nagar CN EE
  # aafai extract gar Computer Network bata CN 
  # data jasto kuro change garnu hunna kya, arko function le
  # kasari use garya xa, bigrina askxa, thapanai nagar
  # tei bhako data bata nikal chaine kura change nagar
  '''
  computer network bata cn extract yesari garni la
  x = 'Computer Network'
  x = ''.join([i[0] for i in x.split()])

  kei problem aayo bhane discord ma xu

  '''

    'monday': {
        'DBMS': '  8:00 to 9:30',
        'Break': '  9:30 to 10:15',
        'Engineering Economics ': '  10:15 to 11:45',
        'Computer Network ': '  11:45 to 1:15',
    },
    'tuesday': {
        'C. Organi & Architecture ': '  8:00 to 9:30',
        'Minor Project ': '  9:30 to 11:00',
        'Break ': '  11:00 to 12:30',
        'OS ': '  12:30 to 2:00',
    },
    'wednesday': {
        'Computer Network ': '  10:15 to 11:45',
        'Break ': ' 11:45 to 12:30',
        'OS ': ' 12:30 to 2:00'
    },
    'thursday': {
        ' Engineering Economics ': '  8:00 to 9:30',
        'C. Organi & Architecture ': '  9:30 to 11:00',
        'Break  ': ' 11:00 to 11:45',
        'Filter Design ': ' 11:45 to 1:15'
    },
    'friday': {
        'DBMS ': '  8:00 to 9:30',
        'Break ': '  9:30 to 11:45',
        'Filter Design ': ' 11:45 to 1:15'
    }
}

abs_days = {'today': 0, 'hijo': -1, 'bholi': 1,
            'parsi': 2, 'nikoparsi': 3, 'asti': -2,'aaja':0}

days = ['monday', 'tuesday',
        'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

roughWords = ['lado', 'muji', 'muzi', 'puti', 'bhalu',
              'rand', 'gukha', 'gu', 'chakka','rajan','kando','radi','chikney','chikni']
            
help_str = {
  'help':{
    'title':'Help',
    'desc':'Displays this help dialog box',
    'example':f'{prefix}help'
  },
  'DayOfWeek':{
    'title':'<day_of_week>',
    'desc':'Displays the routine for the entire day',
    'example':f'''{prefix}sunday '''
  },
  'AbsDays':{
    'title':'Abstract Days',
    'desc':f'Displays the routine for that corresponding day\n Supported days are {str(abs_days.keys())[11:-2]}',
    'example':f'''{prefix}bholi
{prefix}parsi
{prefix}aaja'''
  },
  'notice':{
    'title':'Kec Website Notice',
    'desc':'Displays the current notices from kecktm.edu.np',
    'example':f'{prefix}notice'
  },
  'sqlquery':{
    'title':'MySQL',
    'desc':'Displays the result of sql query',
    'example':'''
create table table_name;
    '''
  },
  'nextSession':{
    'title':'Next Session',
    'desc':'Displays the next session of the given subject.',
    'example':f'''{prefix}next co&a\n C. Organi & Architecture  is in Tuesday from   8:00 to 9:30 
    {prefix}next d\n DBMS  is in Friday from   8:00 to 9:30
    {prefix}next o\n OS  is in Tuesday from   12:30 to 2:00
    '''
  }
}

