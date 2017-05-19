
signalList = {}
signalList['zprime'] = [
	      'zprime400',
              'zprime500',
              'zprime750',
              'zprime1000',
              'zprime1250',
              'zprime1500',
              'zprime1750',
              'zprime2000',
              'zprime2250',
              'zprime2500',
              'zprime2750',
              'zprime3000',
              'zprime4000',
              'zprime5000']

signalList['kkG'] = [
	      'kkgrav400',
              'kkgrav500',
              'kkgrav750',
              'kkgrav1000',
              'kkgrav2000',
              'kkgrav3000']

signalList['kkgluon'] = [
	      'kkg500',
	      'kkg1000',
	      'kkg1500',
	      'kkg2000',
	      'kkg2500',
	      'kkg3000',
	      'kkg3500',
	      'kkg4000',
	      'kkg4500',
              'kkg5000']

signalList['eft10'] = [
              'eftl40c10',
              'eftl45c10',
              'eftl50c10',
              'eftl55c10',
              'eftl60c10',
              #'eftl100c10',
	      ]

xs         = {}
xs['zprime'] = [
	      70.2764206532*1.3,
              40.1252717501*1.3,
              10.7025592052*1.3,
              3.69900238076*1.3,
              1.50806798183*1.3,
              0.684451508485*1.3,
              0.334388285018*1.3,
              0.172299333764*1.3,
              0.0923739492669*1.3,
              0.0510543839336*1.3,
              0.0289022800871*1.3,
              0.0166807659717*1.3,
              0.00212729713173*1.3,
              0.000330792326516*1.3]
xs['kkG'] = [
	     7.19,
             5.84,
             1.18,
			 0.289,
			 0.00498,
			 0.000248
			 ]

xs['kkgluon'] = [
	     1187.0,
             157.6,
             25.59,
             6.918,
             2.360,
             9.530e-01,
             4.383e-01,
	     2.383e-01,
             1.431e-01,
	     9.182e-02,
                ]

def sigmaEFT(c, L):
  I = 11.77
  S = 2.262
  #return 1
  return (c*I*(L**(-2)) + c**2*S*(L**(-4)))

xs['eft10'] = [
             sigmaEFT(10.0, 4.0),
             sigmaEFT(10.0, 4.5),
             sigmaEFT(10.0, 5.0),
             sigmaEFT(10.0, 5.5),
             sigmaEFT(10.0, 6.0),
             #sigmaEFT(10.0, 10.0),
	     ]

mass = {}
mass['zprime'] = [
	      0.4,
              0.5,
              0.75,
              1.0, 
              1.25,
              1.5,
              1.75,
              2.0,
              2.25,
              2.5,
              2.75,
              3,
              4,
              5]
mass['kkG'] = [
			   0.4,
			   0.5,
			   0.75,
			   1,
			   2,
			   3]

mass['kkgluon'] = [
			   0.5,
			   1.0,
			   1.5,
			   2.0,
			   2.5,
			   3.0,
			   3.5,
			   4.0,
			   4.5,
			   5.0
			   ]


mass['eft10'] = [
               4.0,
               4.5,
               5.0,
               5.5,
               6.0,
               #10.0,
	       ]

eff = {}
eff['eft10'] = [ 10*(i**(-2)) for i in mass['eft10']]

xs3 = {}
xs3['zprime'] = [
	      169.871785472*1.3,
              98.4603402069*1.3,
              26.5283913791*1.3,
              9.2179234009*1.3,
              3.47611598738*1.3,
              1.72203498739*1.3,
              0.846135076709*1.3,
              0.438917958804*1.3,
              0.237224494394*1.3,
              0.132411417881*1.3,
              0.0758661541871*1.3,
              0.0444353189615*1.3,
              0.00627056264005*1.3,
              0.00120211436455*1.3]

