# train test time-stamps
timestamps = {'begin_date':'2012-01-03 00:00:00',
              'end_date':'2013-12-30 23:00:00',
              'deltat':30,
              'random_train_test_split':False}

# variables
variables = {'xvar': ['Ta', 'Fg', 'VPD', 'Ts'],  ## ['Ta', 'Ws', 'Fg', 'VPD', 'Fn', 'q', 'Ts', 'Sws', 'EVI'],
             'yvar': 'Fc',    # Driver name
             'tvar':'DateTime',
             'xvar_derived': [#'day', 'month', 'week',
                              #'hour', 'minutes',
                              #'dayofyear',
                              #'sinwt', 'coswt'
                              ]
            }

# data
data = {'tower': 'Gingin', # AliceSpringsMulga  HowardSprings
        'yobs_file': 'L4',
        'file_suffix':'_Fc',
        'ancillary_files': [],
        'supplement_xvar': ['EVI'],

        'ustar':False,
        #'ustar_map':{2009:0.282, 2010:0.282, 2011:0.2822, 2012:0.2697, 2013:0.2259, 2018:0.23867},  #Gingin
        #'ustar_map':{2004:0.01, 2005:0.01, 2006:0.01, 2007:0.01, 2008:0.01, 2009:0.01, 2010:0.01, 2011:0.01, 2012:0.01, 2013:0.01, 2018:0.01},  #AliceSpringsMulga
        #'ustar_map':{2009:0.2063,2010:0.2319 ,2011:0.2063, 2012:0.2244, 2013:0.2429},   #Calperum
        'ustar_map':{2004:0.4, 2005:0.4, 2006:0.4, 2007:0.4, 2008:0.4, 2009:0.5228, 2010:0.4653, 2011:0.4610, 2012:0.5149, 2013:0.514924879899},  #Tumbarumba
        #'ustar_map':{2004:0.26,2005:0.26,2006:0.26,2007:0.26,2008:0.26,2009:0.2261,2010:0.2621,2011:0.2734,2012:0.2353,2013:0.262428731155},  #HowardSprings
        'ustar_exclude_hour':{'begin':18, 'end':7},

        'Climatology': False,
        'Climatology_xvars':['Swsi(day)'
                             #"Ahi(day)"
                             #"RHi(day)",
                             #"Wsi(day)",
                             #"Tai(day)"
                            ],
        'PanelData':False,
        'second_tower':'Gingin',

        'SOLO': False,
        'path2solo': '.',

       'fbprophet': False
        }

# solvers
solvers = [ 'Classical Linear',
            'Random Forest',
            #'eXtreme Gradient Boost',
            #'Support Vector Regression',
            #'ridge',
            #'ANN',
            #'Gradient Boost Regression',
            #'bayes_ridge',
            #'lasso',
            #'elasticnet'
           ]

solvers_layer1 = ['LGBM', 'RFE', 'SVM', 'GP', 'ANN', 'LASSO']
solvers_layer2 = ['LGBM', 'RFE', 'ANN']

# saving results
result = {'save_plots':True,
          'save_summary':True,
          'save_imputed':True}
