
frac = {}
frac[2] = {'el': {}, 'mu': {}}
frac[3] = {'el': {}, 'mu': {}}
frac[4] = {'el': {}, 'mu': {}}
frac[5] = {'el': {}, 'mu': {}}

f_ca_map = {}
f_ca_map[2] = {'el': {}, 'mu': {}}
f_ca_map[3] = {'el': {}, 'mu': {}}
f_ca_map[4] = {'el': {}, 'mu': {}}
f_ca_map[5] = {'el': {}, 'mu': {}}

flav_map = {}
flav_map[2] = {}
flav_map[3] = {}
flav_map[4] = {}
flav_map[5] = {}

flav_map[2] = {'el': {}, 'mu': {}}
flav_map[3] = {'el': {}, 'mu': {}}
flav_map[4] = {'el': {}, 'mu': {}}
flav_map[5] = {'el': {}, 'mu': {}}

# nominal:
f_ca_map[2]['el'][""] =  1.057503
f_ca_map[3]['el'][""] =  1.034622
f_ca_map[4]['el'][""] =  1.016558
f_ca_map[5]['el'][""] =  0.781642
f_ca_map[2]['mu'][""] =  1.146238
f_ca_map[3]['mu'][""] =  1.057198
f_ca_map[4]['mu'][""] =  0.953141
f_ca_map[5]['mu'][""] =  0.800919

frac[2]['el'][""] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el'][""] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el'][""] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el'][""] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu'][""] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu'][""] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu'][""] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu'][""] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

flav_map[2]['el'][""] = {'bb': 1.274836, 'cc': 1.274836, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el'][""] = {'bb': 1.248908, 'cc': 1.248908, 'c': 0.979662, 'l': 0.910787}
flav_map[4]['el'][""] = {'bb': 1.223782, 'cc': 1.223782, 'c': 0.959953, 'l': 0.892464}
flav_map[5]['el'][""] = {'bb': 1.196354, 'cc': 1.196354, 'c': 0.938438, 'l': 0.872461}
flav_map[2]['mu'][""] = {'bb': 1.511162, 'cc': 1.511162, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu'][""] = {'bb': 1.455979, 'cc': 1.455979, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu'][""] = {'bb': 1.406443, 'cc': 1.406443, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu'][""] = {'bb': 1.345807, 'cc': 1.345807, 'c': 0.890578, 'l': 0.786584}


f_ca_map[2]['el']["wnorm__1up"] =  1.057503*(1+((0.005)**2 + (0.051)**2)**0.5)
f_ca_map[3]['el']["wnorm__1up"] =  1.034622*(1+((0.009)**2 + (0.034)**2)**0.5)
f_ca_map[4]['el']["wnorm__1up"] =  1.016558*(1+((0.019)**2 + (0.043)**2)**0.5)
f_ca_map[5]['el']["wnorm__1up"] =  0.781642*(1+((0.036)**2 + (0.028)**2)**0.5)
f_ca_map[2]['mu']["wnorm__1up"] =  1.146238*(1+((0.003)**2 + (0.045)**2)**0.5)
f_ca_map[3]['mu']["wnorm__1up"] =  1.057198*(1+((0.007)**2 + (0.028)**2)**0.5)
f_ca_map[4]['mu']["wnorm__1up"] =  0.953141*(1+((0.014)**2 + (0.028)**2)**0.5)
f_ca_map[5]['mu']["wnorm__1up"] =  0.800919*(1+((0.025)**2 + (0.020)**2)**0.5)

frac[2]['el']["wnorm__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["wnorm__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["wnorm__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["wnorm__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["wnorm__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["wnorm__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["wnorm__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["wnorm__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

flav_map[2]['el']["wnorm__1up"] = {'bb': 1.274836, 'cc': 1.274836, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["wnorm__1up"] = {'bb': 1.248908, 'cc': 1.248908, 'c': 0.979662, 'l': 0.910787}
flav_map[4]['el']["wnorm__1up"] = {'bb': 1.223782, 'cc': 1.223782, 'c': 0.959953, 'l': 0.892464}
flav_map[5]['el']["wnorm__1up"] = {'bb': 1.196354, 'cc': 1.196354, 'c': 0.938438, 'l': 0.872461}
flav_map[2]['mu']["wnorm__1up"] = {'bb': 1.511162, 'cc': 1.511162, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["wnorm__1up"] = {'bb': 1.455979, 'cc': 1.455979, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["wnorm__1up"] = {'bb': 1.406443, 'cc': 1.406443, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["wnorm__1up"] = {'bb': 1.345807, 'cc': 1.345807, 'c': 0.890578, 'l': 0.786584}

# W CA stat down
f_ca_map[2]['el']["wnorm__1down"] =  1.057503*(1-((0.005)**2 + (0.051)**2)**0.5)
f_ca_map[3]['el']["wnorm__1down"] =  1.034622*(1-((0.009)**2 + (0.034)**2)**0.5)
f_ca_map[4]['el']["wnorm__1down"] =  1.016558*(1-((0.019)**2 + (0.043)**2)**0.5)
f_ca_map[5]['el']["wnorm__1down"] =  0.781642*(1-((0.036)**2 + (0.028)**2)**0.5)
f_ca_map[2]['mu']["wnorm__1down"] =  1.146238*(1-((0.003)**2 + (0.045)**2)**0.5)
f_ca_map[3]['mu']["wnorm__1down"] =  1.057198*(1-((0.007)**2 + (0.028)**2)**0.5)
f_ca_map[4]['mu']["wnorm__1down"] =  0.953141*(1-((0.014)**2 + (0.028)**2)**0.5)
f_ca_map[5]['mu']["wnorm__1down"] =  0.800919*(1-((0.025)**2 + (0.020)**2)**0.5)

frac[2]['el']["wnorm__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["wnorm__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["wnorm__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["wnorm__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["wnorm__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["wnorm__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["wnorm__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["wnorm__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

flav_map[2]['el']["wnorm__1down"] = {'bb': 1.274836, 'cc': 1.274836, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["wnorm__1down"] = {'bb': 1.248908, 'cc': 1.248908, 'c': 0.979662, 'l': 0.910787}
flav_map[4]['el']["wnorm__1down"] = {'bb': 1.223782, 'cc': 1.223782, 'c': 0.959953, 'l': 0.892464}
flav_map[5]['el']["wnorm__1down"] = {'bb': 1.196354, 'cc': 1.196354, 'c': 0.938438, 'l': 0.872461}
flav_map[2]['mu']["wnorm__1down"] = {'bb': 1.511162, 'cc': 1.511162, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["wnorm__1down"] = {'bb': 1.455979, 'cc': 1.455979, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["wnorm__1down"] = {'bb': 1.406443, 'cc': 1.406443, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["wnorm__1down"] = {'bb': 1.345807, 'cc': 1.345807, 'c': 0.890578, 'l': 0.786584}

# Wbb stat up

f_ca_map[2]['el']["wbb__1up"] =  1.057503
f_ca_map[3]['el']["wbb__1up"] =  1.034622
f_ca_map[4]['el']["wbb__1up"] =  1.016558
f_ca_map[5]['el']["wbb__1up"] =  0.781642
f_ca_map[2]['mu']["wbb__1up"] =  1.146238
f_ca_map[3]['mu']["wbb__1up"] =  1.057198
f_ca_map[4]['mu']["wbb__1up"] =  0.953141
f_ca_map[5]['mu']["wbb__1up"] =  0.800919

frac[2]['el']["wbb__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["wbb__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["wbb__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["wbb__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["wbb__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["wbb__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["wbb__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["wbb__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

flav_map[2]['el']["wbb__1up"] = {'bb': 1.274836*(1+(0.044**2+0.067**2)**0.5), 'cc': 1.274836*(1+(0.044**2+0.067**2)**0.5), 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["wbb__1up"] = {'bb': 1.248908*(1+(0.044**2+0.067**2)**0.5), 'cc': 1.248908*(1+(0.044**2+0.067**2)**0.5), 'c': 0.979662, 'l': 0.910787}
flav_map[4]['el']["wbb__1up"] = {'bb': 1.223782*(1+(0.044**2+0.067**2)**0.5), 'cc': 1.223782*(1+(0.044**2+0.067**2)**0.5), 'c': 0.959953, 'l': 0.892464}
flav_map[5]['el']["wbb__1up"] = {'bb': 1.196354*(1+(0.044**2+0.067**2)**0.5), 'cc': 1.196354*(1+(0.044**2+0.067**2)**0.5), 'c': 0.938438, 'l': 0.872461}
flav_map[2]['mu']["wbb__1up"] = {'bb': 1.511162*(1+(0.028**2+0.058**2)**0.5), 'cc': 1.511162*(1+(0.028**2+0.058**2)**0.5), 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["wbb__1up"] = {'bb': 1.455979*(1+(0.028**2+0.058**2)**0.5), 'cc': 1.455979*(1+(0.028**2+0.058**2)**0.5), 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["wbb__1up"] = {'bb': 1.406443*(1+(0.028**2+0.058**2)**0.5), 'cc': 1.406443*(1+(0.028**2+0.058**2)**0.5), 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["wbb__1up"] = {'bb': 1.345807*(1+(0.028**2+0.058**2)**0.5), 'cc': 1.345807*(1+(0.028**2+0.058**2)**0.5), 'c': 0.890578, 'l': 0.786584}

# Wbb stat down

f_ca_map[2]['el']["wbb__1down"] =  1.057503
f_ca_map[3]['el']["wbb__1down"] =  1.034622
f_ca_map[4]['el']["wbb__1down"] =  1.016558
f_ca_map[5]['el']["wbb__1down"] =  0.781642
f_ca_map[2]['mu']["wbb__1down"] =  1.146238
f_ca_map[3]['mu']["wbb__1down"] =  1.057198
f_ca_map[4]['mu']["wbb__1down"] =  0.953141
f_ca_map[5]['mu']["wbb__1down"] =  0.800919

frac[2]['el']["wbb__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["wbb__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["wbb__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["wbb__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["wbb__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["wbb__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["wbb__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["wbb__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

flav_map[2]['el']["wbb__1down"] = {'bb': 1.274836*(1-(0.044**2+0.067**2)**0.5), 'cc': 1.274836*(1-(0.044**2+0.067**2)**0.5), 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["wbb__1down"] = {'bb': 1.248908*(1-(0.044**2+0.067**2)**0.5), 'cc': 1.248908*(1-(0.044**2+0.067**2)**0.5), 'c': 0.979662, 'l': 0.910787}
flav_map[4]['el']["wbb__1down"] = {'bb': 1.223782*(1-(0.044**2+0.067**2)**0.5), 'cc': 1.223782*(1-(0.044**2+0.067**2)**0.5), 'c': 0.959953, 'l': 0.892464}
flav_map[5]['el']["wbb__1down"] = {'bb': 1.196354*(1-(0.044**2+0.067**2)**0.5), 'cc': 1.196354*(1-(0.044**2+0.067**2)**0.5), 'c': 0.938438, 'l': 0.872461}
flav_map[2]['mu']["wbb__1down"] = {'bb': 1.511162*(1-(0.028**2+0.058**2)**0.5), 'cc': 1.511162*(1-(0.028**2+0.058**2)**0.5), 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["wbb__1down"] = {'bb': 1.455979*(1-(0.028**2+0.058**2)**0.5), 'cc': 1.455979*(1-(0.028**2+0.058**2)**0.5), 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["wbb__1down"] = {'bb': 1.406443*(1-(0.028**2+0.058**2)**0.5), 'cc': 1.406443*(1-(0.028**2+0.058**2)**0.5), 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["wbb__1down"] = {'bb': 1.345807*(1-(0.028**2+0.058**2)**0.5), 'cc': 1.345807*(1-(0.028**2+0.058**2)**0.5), 'c': 0.890578, 'l': 0.786584}


# Wc up


f_ca_map[2]['el']["wc__1up"] =  1.057503
f_ca_map[3]['el']["wc__1up"] =  1.034622
f_ca_map[4]['el']["wc__1up"] =  1.016558
f_ca_map[5]['el']["wc__1up"] =  0.781642
f_ca_map[2]['mu']["wc__1up"] =  1.146238
f_ca_map[3]['mu']["wc__1up"] =  1.057198
f_ca_map[4]['mu']["wc__1up"] =  0.953141
f_ca_map[5]['mu']["wc__1up"] =  0.800919

frac[2]['el']["wc__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["wc__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["wc__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["wc__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["wc__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["wc__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["wc__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["wc__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

flav_map[2]['el']["wc__1up"] = {'bb': 1.274836, 'cc': 1.274836, 'c': 1.000000*1.3, 'l': 0.929695}
flav_map[3]['el']["wc__1up"] = {'bb': 1.248908, 'cc': 1.248908, 'c': 0.979662*1.3, 'l': 0.910787}
flav_map[4]['el']["wc__1up"] = {'bb': 1.223782, 'cc': 1.223782, 'c': 0.959953*1.3, 'l': 0.892464}
flav_map[5]['el']["wc__1up"] = {'bb': 1.196354, 'cc': 1.196354, 'c': 0.938438*1.3, 'l': 0.872461}
flav_map[2]['mu']["wc__1up"] = {'bb': 1.511162, 'cc': 1.511162, 'c': 1.000000*1.3, 'l': 0.883229}
flav_map[3]['mu']["wc__1up"] = {'bb': 1.455979, 'cc': 1.455979, 'c': 0.963483*1.3, 'l': 0.850976}
flav_map[4]['mu']["wc__1up"] = {'bb': 1.406443, 'cc': 1.406443, 'c': 0.930703*1.3, 'l': 0.822024}
flav_map[5]['mu']["wc__1up"] = {'bb': 1.345807, 'cc': 1.345807, 'c': 0.890578*1.3, 'l': 0.786584}

# Wc stat down
f_ca_map[2]['el']["wc__1down"] =  1.057503
f_ca_map[3]['el']["wc__1down"] =  1.034622
f_ca_map[4]['el']["wc__1down"] =  1.016558
f_ca_map[5]['el']["wc__1down"] =  0.781642
f_ca_map[2]['mu']["wc__1down"] =  1.146238
f_ca_map[3]['mu']["wc__1down"] =  1.057198
f_ca_map[4]['mu']["wc__1down"] =  0.953141
f_ca_map[5]['mu']["wc__1down"] =  0.800919

frac[2]['el']["wc__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["wc__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["wc__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["wc__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["wc__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["wc__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["wc__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["wc__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

flav_map[2]['el']["wc__1down"] = {'bb': 1.274836, 'cc': 1.274836, 'c': 1.000000*0.7, 'l': 0.929695}
flav_map[3]['el']["wc__1down"] = {'bb': 1.248908, 'cc': 1.248908, 'c': 0.979662*0.7, 'l': 0.910787}
flav_map[4]['el']["wc__1down"] = {'bb': 1.223782, 'cc': 1.223782, 'c': 0.959953*0.7, 'l': 0.892464}
flav_map[5]['el']["wc__1down"] = {'bb': 1.196354, 'cc': 1.196354, 'c': 0.938438*0.7, 'l': 0.872461}
flav_map[2]['mu']["wc__1down"] = {'bb': 1.511162, 'cc': 1.511162, 'c': 1.000000*0.7, 'l': 0.883229}
flav_map[3]['mu']["wc__1down"] = {'bb': 1.455979, 'cc': 1.455979, 'c': 0.963483*0.7, 'l': 0.850976}
flav_map[4]['mu']["wc__1down"] = {'bb': 1.406443, 'cc': 1.406443, 'c': 0.930703*0.7, 'l': 0.822024}
flav_map[5]['mu']["wc__1down"] = {'bb': 1.345807, 'cc': 1.345807, 'c': 0.890578*0.7, 'l': 0.786584}

# Wl stat up


f_ca_map[2]['el']["wl__1up"] =  1.057503
f_ca_map[3]['el']["wl__1up"] =  1.034622
f_ca_map[4]['el']["wl__1up"] =  1.016558
f_ca_map[5]['el']["wl__1up"] =  0.781642
f_ca_map[2]['mu']["wl__1up"] =  1.146238
f_ca_map[3]['mu']["wl__1up"] =  1.057198
f_ca_map[4]['mu']["wl__1up"] =  0.953141
f_ca_map[5]['mu']["wl__1up"] =  0.800919

frac[2]['el']["wl__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["wl__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["wl__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["wl__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["wl__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["wl__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["wl__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["wl__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

flav_map[2]['el']["wl__1up"] = {'bb': 1.274836, 'cc': 1.274836, 'c': 1.000000, 'l': 0.929695*(1+(0.015**2+0.023**2)**0.5)}
flav_map[3]['el']["wl__1up"] = {'bb': 1.248908, 'cc': 1.248908, 'c': 0.979662, 'l': 0.910787*(1+(0.015**2+0.023**2)**0.5)}
flav_map[4]['el']["wl__1up"] = {'bb': 1.223782, 'cc': 1.223782, 'c': 0.959953, 'l': 0.892464*(1+(0.015**2+0.023**2)**0.5)}
flav_map[5]['el']["wl__1up"] = {'bb': 1.196354, 'cc': 1.196354, 'c': 0.938438, 'l': 0.872461*(1+(0.015**2+0.023**2)**0.5)}
flav_map[2]['mu']["wl__1up"] = {'bb': 1.511162, 'cc': 1.511162, 'c': 1.000000, 'l': 0.883229*(1+(0.011**2+0.022**2)**0.5)}
flav_map[3]['mu']["wl__1up"] = {'bb': 1.455979, 'cc': 1.455979, 'c': 0.963483, 'l': 0.850976*(1+(0.011**2+0.022**2)**0.5)}
flav_map[4]['mu']["wl__1up"] = {'bb': 1.406443, 'cc': 1.406443, 'c': 0.930703, 'l': 0.822024*(1+(0.011**2+0.022**2)**0.5)}
flav_map[5]['mu']["wl__1up"] = {'bb': 1.345807, 'cc': 1.345807, 'c': 0.890578, 'l': 0.786584*(1+(0.011**2+0.022**2)**0.5)}

# Wl stat down


f_ca_map[2]['el']["wl__1down"] =  1.057503
f_ca_map[3]['el']["wl__1down"] =  1.034622
f_ca_map[4]['el']["wl__1down"] =  1.016558
f_ca_map[5]['el']["wl__1down"] =  0.781642
f_ca_map[2]['mu']["wl__1down"] =  1.146238
f_ca_map[3]['mu']["wl__1down"] =  1.057198
f_ca_map[4]['mu']["wl__1down"] =  0.953141
f_ca_map[5]['mu']["wl__1down"] =  0.800919

frac[2]['el']["wl__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["wl__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["wl__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["wl__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["wl__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["wl__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["wl__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["wl__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

flav_map[2]['el']["wl__1down"] = {'bb': 1.274836, 'cc': 1.274836, 'c': 1.000000, 'l': 0.929695*(1-(0.015**2+0.023**2)**0.5)}
flav_map[3]['el']["wl__1down"] = {'bb': 1.248908, 'cc': 1.248908, 'c': 0.979662, 'l': 0.910787*(1-(0.015**2+0.023**2)**0.5)}
flav_map[4]['el']["wl__1down"] = {'bb': 1.223782, 'cc': 1.223782, 'c': 0.959953, 'l': 0.892464*(1-(0.015**2+0.023**2)**0.5)}
flav_map[5]['el']["wl__1down"] = {'bb': 1.196354, 'cc': 1.196354, 'c': 0.938438, 'l': 0.872461*(1-(0.015**2+0.023**2)**0.5)}
flav_map[2]['mu']["wl__1down"] = {'bb': 1.511162, 'cc': 1.511162, 'c': 1.000000, 'l': 0.883229*(1-(0.011**2+0.022**2)**0.5)}
flav_map[3]['mu']["wl__1down"] = {'bb': 1.455979, 'cc': 1.455979, 'c': 0.963483, 'l': 0.850976*(1-(0.011**2+0.022**2)**0.5)}
flav_map[4]['mu']["wl__1down"] = {'bb': 1.406443, 'cc': 1.406443, 'c': 0.930703, 'l': 0.822024*(1-(0.011**2+0.022**2)**0.5)}
flav_map[5]['mu']["wl__1down"] = {'bb': 1.345807, 'cc': 1.345807, 'c': 0.890578, 'l': 0.786584*(1-(0.011**2+0.022**2)**0.5)}

# TTree systs (1/4)

# MET_SoftTrk_ResoPara 
f_ca_map[2]['el']["MET_SoftTrk_ResoPara"] =  1.061511
f_ca_map[3]['el']["MET_SoftTrk_ResoPara"] =  1.038606
f_ca_map[4]['el']["MET_SoftTrk_ResoPara"] =  1.018302
f_ca_map[5]['el']["MET_SoftTrk_ResoPara"] =  0.774182
f_ca_map[2]['mu']["MET_SoftTrk_ResoPara"] =  1.150372
f_ca_map[3]['mu']["MET_SoftTrk_ResoPara"] =  1.054933
f_ca_map[4]['mu']["MET_SoftTrk_ResoPara"] =  0.952528
f_ca_map[5]['mu']["MET_SoftTrk_ResoPara"] =  0.799017
# MET_SoftTrk_ResoPerp 
f_ca_map[2]['el']["MET_SoftTrk_ResoPerp"] =  1.060073
f_ca_map[3]['el']["MET_SoftTrk_ResoPerp"] =  1.033530
f_ca_map[4]['el']["MET_SoftTrk_ResoPerp"] =  1.018828
f_ca_map[5]['el']["MET_SoftTrk_ResoPerp"] =  0.780565
f_ca_map[2]['mu']["MET_SoftTrk_ResoPerp"] =  1.147921
f_ca_map[3]['mu']["MET_SoftTrk_ResoPerp"] =  1.061766
f_ca_map[4]['mu']["MET_SoftTrk_ResoPerp"] =  0.950009
f_ca_map[5]['mu']["MET_SoftTrk_ResoPerp"] =  0.799326
# MET_SoftTrk_ScaleUp 
f_ca_map[2]['el']["MET_SoftTrk_ScaleUp"] =  1.054404
f_ca_map[3]['el']["MET_SoftTrk_ScaleUp"] =  1.036865
f_ca_map[4]['el']["MET_SoftTrk_ScaleUp"] =  1.020764
f_ca_map[5]['el']["MET_SoftTrk_ScaleUp"] =  0.778474
f_ca_map[2]['mu']["MET_SoftTrk_ScaleUp"] =  1.145286
f_ca_map[3]['mu']["MET_SoftTrk_ScaleUp"] =  1.056540
f_ca_map[4]['mu']["MET_SoftTrk_ScaleUp"] =  0.954789
f_ca_map[5]['mu']["MET_SoftTrk_ScaleUp"] =  0.801172
# MET_SoftTrk_ScaleDown 
f_ca_map[2]['el']["MET_SoftTrk_ScaleDown"] =  1.059378
f_ca_map[3]['el']["MET_SoftTrk_ScaleDown"] =  1.032786
f_ca_map[4]['el']["MET_SoftTrk_ScaleDown"] =  1.016354
f_ca_map[5]['el']["MET_SoftTrk_ScaleDown"] =  0.779666
f_ca_map[2]['mu']["MET_SoftTrk_ScaleDown"] =  1.147552
f_ca_map[3]['mu']["MET_SoftTrk_ScaleDown"] =  1.057653
f_ca_map[4]['mu']["MET_SoftTrk_ScaleDown"] =  0.953406
f_ca_map[5]['mu']["MET_SoftTrk_ScaleDown"] =  0.798474
# EG_RESOLUTION_ALL__1up 
f_ca_map[2]['el']["EG_RESOLUTION_ALL__1up"] =  1.058244
f_ca_map[3]['el']["EG_RESOLUTION_ALL__1up"] =  1.036680
f_ca_map[4]['el']["EG_RESOLUTION_ALL__1up"] =  1.020895
f_ca_map[5]['el']["EG_RESOLUTION_ALL__1up"] =  0.782915
f_ca_map[2]['mu']["EG_RESOLUTION_ALL__1up"] =  1.146239
f_ca_map[3]['mu']["EG_RESOLUTION_ALL__1up"] =  1.057178
f_ca_map[4]['mu']["EG_RESOLUTION_ALL__1up"] =  0.953135
f_ca_map[5]['mu']["EG_RESOLUTION_ALL__1up"] =  0.800949
# EG_RESOLUTION_ALL__1down 
f_ca_map[2]['el']["EG_RESOLUTION_ALL__1down"] =  1.061204
f_ca_map[3]['el']["EG_RESOLUTION_ALL__1down"] =  1.032608
f_ca_map[4]['el']["EG_RESOLUTION_ALL__1down"] =  1.015388
f_ca_map[5]['el']["EG_RESOLUTION_ALL__1down"] =  0.778049
f_ca_map[2]['mu']["EG_RESOLUTION_ALL__1down"] =  1.146236
f_ca_map[3]['mu']["EG_RESOLUTION_ALL__1down"] =  1.057200
f_ca_map[4]['mu']["EG_RESOLUTION_ALL__1down"] =  0.953141
f_ca_map[5]['mu']["EG_RESOLUTION_ALL__1down"] =  0.800968
# EG_SCALE_ALL__1up 
f_ca_map[2]['el']["EG_SCALE_ALL__1up"] =  1.055549
f_ca_map[3]['el']["EG_SCALE_ALL__1up"] =  1.031750
f_ca_map[4]['el']["EG_SCALE_ALL__1up"] =  1.016309
f_ca_map[5]['el']["EG_SCALE_ALL__1up"] =  0.780093
f_ca_map[2]['mu']["EG_SCALE_ALL__1up"] =  1.146236
f_ca_map[3]['mu']["EG_SCALE_ALL__1up"] =  1.057195
f_ca_map[4]['mu']["EG_SCALE_ALL__1up"] =  0.953138
f_ca_map[5]['mu']["EG_SCALE_ALL__1up"] =  0.800949
# EG_SCALE_ALL__1down 
f_ca_map[2]['el']["EG_SCALE_ALL__1down"] =  1.061164
f_ca_map[3]['el']["EG_SCALE_ALL__1down"] =  1.037254
f_ca_map[4]['el']["EG_SCALE_ALL__1down"] =  1.020946
f_ca_map[5]['el']["EG_SCALE_ALL__1down"] =  0.781741
f_ca_map[2]['mu']["EG_SCALE_ALL__1down"] =  1.146240
f_ca_map[3]['mu']["EG_SCALE_ALL__1down"] =  1.057190
f_ca_map[4]['mu']["EG_SCALE_ALL__1down"] =  0.953138
f_ca_map[5]['mu']["EG_SCALE_ALL__1down"] =  0.800969
# MUON_ID__1up 
f_ca_map[2]['el']["MUON_ID__1up"] =  1.057509
f_ca_map[3]['el']["MUON_ID__1up"] =  1.034620
f_ca_map[4]['el']["MUON_ID__1up"] =  1.016562
f_ca_map[5]['el']["MUON_ID__1up"] =  0.781641
f_ca_map[2]['mu']["MUON_ID__1up"] =  1.145012
f_ca_map[3]['mu']["MUON_ID__1up"] =  1.058962
f_ca_map[4]['mu']["MUON_ID__1up"] =  0.948231
f_ca_map[5]['mu']["MUON_ID__1up"] =  0.801743
# MUON_ID__1down 
f_ca_map[2]['el']["MUON_ID__1down"] =  1.057506
f_ca_map[3]['el']["MUON_ID__1down"] =  1.034620
f_ca_map[4]['el']["MUON_ID__1down"] =  1.016552
f_ca_map[5]['el']["MUON_ID__1down"] =  0.781645
f_ca_map[2]['mu']["MUON_ID__1down"] =  1.144756
f_ca_map[3]['mu']["MUON_ID__1down"] =  1.055818
f_ca_map[4]['mu']["MUON_ID__1down"] =  0.953988
f_ca_map[5]['mu']["MUON_ID__1down"] =  0.800829
# MUON_MS__1up 
f_ca_map[2]['el']["MUON_MS__1up"] =  1.057507
f_ca_map[3]['el']["MUON_MS__1up"] =  1.034619
f_ca_map[4]['el']["MUON_MS__1up"] =  1.016558
f_ca_map[5]['el']["MUON_MS__1up"] =  0.781641
f_ca_map[2]['mu']["MUON_MS__1up"] =  1.146350
f_ca_map[3]['mu']["MUON_MS__1up"] =  1.057174
f_ca_map[4]['mu']["MUON_MS__1up"] =  0.952558
f_ca_map[5]['mu']["MUON_MS__1up"] =  0.801460
# MUON_MS__1down 
f_ca_map[2]['el']["MUON_MS__1down"] =  1.057501
f_ca_map[3]['el']["MUON_MS__1down"] =  1.034621
f_ca_map[4]['el']["MUON_MS__1down"] =  1.016550
f_ca_map[5]['el']["MUON_MS__1down"] =  0.781658
f_ca_map[2]['mu']["MUON_MS__1down"] =  1.147626
f_ca_map[3]['mu']["MUON_MS__1down"] =  1.055570
f_ca_map[4]['mu']["MUON_MS__1down"] =  0.952993
f_ca_map[5]['mu']["MUON_MS__1down"] =  0.801044
# MUON_SCALE__1up 
f_ca_map[2]['el']["MUON_SCALE__1up"] =  1.057501
f_ca_map[3]['el']["MUON_SCALE__1up"] =  1.034623
f_ca_map[4]['el']["MUON_SCALE__1up"] =  1.016555
f_ca_map[5]['el']["MUON_SCALE__1up"] =  0.781643
f_ca_map[2]['mu']["MUON_SCALE__1up"] =  1.147402
f_ca_map[3]['mu']["MUON_SCALE__1up"] =  1.059833
f_ca_map[4]['mu']["MUON_SCALE__1up"] =  0.954265
f_ca_map[5]['mu']["MUON_SCALE__1up"] =  0.802438
# MUON_SCALE__1down 
f_ca_map[2]['el']["MUON_SCALE__1down"] =  1.057505
f_ca_map[3]['el']["MUON_SCALE__1down"] =  1.034623
f_ca_map[4]['el']["MUON_SCALE__1down"] =  1.016557
f_ca_map[5]['el']["MUON_SCALE__1down"] =  0.781641
f_ca_map[2]['mu']["MUON_SCALE__1down"] =  1.142352
f_ca_map[3]['mu']["MUON_SCALE__1down"] =  1.054883
f_ca_map[4]['mu']["MUON_SCALE__1down"] =  0.951222
f_ca_map[5]['mu']["MUON_SCALE__1down"] =  0.800606
# MUON_SAGITTA_RESBIAS__1up 
f_ca_map[2]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.057503
f_ca_map[3]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.034623
f_ca_map[4]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.016558
f_ca_map[5]['el']["MUON_SAGITTA_RESBIAS__1up"] =  0.781643
f_ca_map[2]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  1.146237
f_ca_map[3]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  1.057197
f_ca_map[4]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  0.953141
f_ca_map[5]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  0.800919
# MUON_SAGITTA_RESBIAS__1down 
f_ca_map[2]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.057503
f_ca_map[3]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.034623
f_ca_map[4]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.016558
f_ca_map[5]['el']["MUON_SAGITTA_RESBIAS__1down"] =  0.781643
f_ca_map[2]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  1.146237
f_ca_map[3]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  1.057197
f_ca_map[4]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  0.953141
f_ca_map[5]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  0.800919
# MUON_SAGITTA_RHO__1up 
f_ca_map[2]['el']["MUON_SAGITTA_RHO__1up"] =  1.057503
f_ca_map[3]['el']["MUON_SAGITTA_RHO__1up"] =  1.034623
f_ca_map[4]['el']["MUON_SAGITTA_RHO__1up"] =  1.016558
f_ca_map[5]['el']["MUON_SAGITTA_RHO__1up"] =  0.781643
f_ca_map[2]['mu']["MUON_SAGITTA_RHO__1up"] =  1.146237
f_ca_map[3]['mu']["MUON_SAGITTA_RHO__1up"] =  1.057197
f_ca_map[4]['mu']["MUON_SAGITTA_RHO__1up"] =  0.953141
f_ca_map[5]['mu']["MUON_SAGITTA_RHO__1up"] =  0.800919
# MUON_SAGITTA_RHO__1down 
f_ca_map[2]['el']["MUON_SAGITTA_RHO__1down"] =  1.057503
f_ca_map[3]['el']["MUON_SAGITTA_RHO__1down"] =  1.034623
f_ca_map[4]['el']["MUON_SAGITTA_RHO__1down"] =  1.016558
f_ca_map[5]['el']["MUON_SAGITTA_RHO__1down"] =  0.781643
f_ca_map[2]['mu']["MUON_SAGITTA_RHO__1down"] =  1.146237
f_ca_map[3]['mu']["MUON_SAGITTA_RHO__1down"] =  1.057197
f_ca_map[4]['mu']["MUON_SAGITTA_RHO__1down"] =  0.953141
f_ca_map[5]['mu']["MUON_SAGITTA_RHO__1down"] =  0.800919
# JET_JER_SINGLE_NP__1up 
f_ca_map[2]['el']["JET_JER_SINGLE_NP__1up"] =  1.037860
f_ca_map[3]['el']["JET_JER_SINGLE_NP__1up"] =  1.046758
f_ca_map[4]['el']["JET_JER_SINGLE_NP__1up"] =  0.935500
f_ca_map[5]['el']["JET_JER_SINGLE_NP__1up"] =  0.719906
f_ca_map[2]['mu']["JET_JER_SINGLE_NP__1up"] =  1.075918
f_ca_map[3]['mu']["JET_JER_SINGLE_NP__1up"] =  1.028465
f_ca_map[4]['mu']["JET_JER_SINGLE_NP__1up"] =  0.973043
f_ca_map[5]['mu']["JET_JER_SINGLE_NP__1up"] =  0.762108
# JET_21NP_JET_EtaIntercalibration_Modelling__1up 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.055697
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.010650
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  0.995438
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  0.759119
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.134295
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.030254
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  0.932417
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  0.787206
# JET_21NP_JET_EtaIntercalibration_Modelling__1down 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.091411
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.055109
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.019928
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  0.804536
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.162522
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.074006
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  0.968520
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  0.822770
# JET_21NP_JET_EtaIntercalibration_NonClosure__1up 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.059722
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.048733
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.018127
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  0.777943
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.150509
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.058162
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  0.968874
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  0.804929
# JET_21NP_JET_EtaIntercalibration_NonClosure__1down 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.061001
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.031738
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.008555
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  0.777746
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.141588
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.055871
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  0.947997
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  0.796608
# JET_21NP_JET_EtaIntercalibration_TotalStat__1up 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.047143
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.031081
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  0.996941
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  0.773280
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.135626
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.044954
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  0.955019
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  0.791204
# JET_21NP_JET_EtaIntercalibration_TotalStat__1down 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.064350
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.053386
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.026843
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  0.787205
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.151553
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.065081
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  0.971196
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  0.811957
# JET_21NP_JET_Flavor_Composition__1up 
f_ca_map[2]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  0.978030
f_ca_map[3]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  0.927342
f_ca_map[4]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  0.896825
f_ca_map[5]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  0.678488
f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  1.034873
f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  0.973241
f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  0.859011
f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  0.687933
# JET_21NP_JET_Flavor_Composition__1down 
f_ca_map[2]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.185226
f_ca_map[3]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.120303
f_ca_map[4]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.087617
f_ca_map[5]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  0.890950
f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.246026
f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.184167
f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.076082
f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  0.921550
# JET_21NP_JET_Flavor_Response__1up 
f_ca_map[2]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.096470
f_ca_map[3]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.063944
f_ca_map[4]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.037179
f_ca_map[5]['el']["JET_21NP_JET_Flavor_Response__1up"] =  0.812006
f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  1.175314
f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  1.093675
f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  0.987705
f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  0.831258
# JET_21NP_JET_Flavor_Response__1down 
f_ca_map[2]['el']["JET_21NP_JET_Flavor_Response__1down"] =  1.037694
f_ca_map[3]['el']["JET_21NP_JET_Flavor_Response__1down"] =  1.010930
f_ca_map[4]['el']["JET_21NP_JET_Flavor_Response__1down"] =  0.985211
f_ca_map[5]['el']["JET_21NP_JET_Flavor_Response__1down"] =  0.752876
f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  1.113936
f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  1.028051
f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  0.922751
f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  0.771948
# JET_21NP_JET_Pileup_OffsetMu__1up 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.059095
f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.042418
f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.015651
f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  0.777864
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.144726
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.057580
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  0.954823
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  0.801213
# JET_21NP_JET_Pileup_OffsetMu__1down 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.054799
f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.035074
f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.015227
f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  0.776367
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.145529
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.048715
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  0.959111
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  0.798990
# JET_21NP_JET_Pileup_OffsetNPV__1up 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.049078
f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.028898
f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  0.990059
f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  0.766834
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.124261
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.043792
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  0.946069
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  0.780813
# JET_21NP_JET_Pileup_OffsetNPV__1down 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.073724
f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.043109
f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.009508
f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  0.796844
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.160496
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.076496
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  0.967717
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  0.811669
# JET_21NP_JET_Pileup_PtTerm__1up 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.056559
f_ca_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.037676
f_ca_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.017149
f_ca_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  0.781837
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.148197
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.056496
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  0.948656
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  0.803721
# JET_21NP_JET_Pileup_PtTerm__1down 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.064422
f_ca_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.039917
f_ca_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.016969
f_ca_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  0.780712
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.146108
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.057589
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  0.957380
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  0.799212
# JET_21NP_JET_Pileup_RhoTopology__1up 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.008189
f_ca_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  0.959914
f_ca_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  0.939915
f_ca_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  0.709537
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.077148
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  0.980079
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  0.893851
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  0.725741
# JET_21NP_JET_Pileup_RhoTopology__1down 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.151712
f_ca_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.096174
f_ca_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.075491
f_ca_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  0.857256
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.213470
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.139018
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.028303
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  0.882090
# JET_21NP_JET_PunchThrough_MC15__1up 
f_ca_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.057428
f_ca_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.034901
f_ca_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.016586
f_ca_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  0.781749
f_ca_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.146260
f_ca_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.057195
f_ca_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  0.953128
f_ca_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  0.800893
# JET_21NP_JET_PunchThrough_MC15__1down 
f_ca_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.057499
f_ca_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.034657
f_ca_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.016621
f_ca_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  0.781643
f_ca_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.146277
f_ca_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.057187
f_ca_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  0.953081
f_ca_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  0.801043
# JET_21NP_JET_SingleParticle_HighPt__1up 
f_ca_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.057503
f_ca_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.034623
f_ca_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.016559
f_ca_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  0.781642
f_ca_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.146237
f_ca_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.057198
f_ca_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  0.953141
f_ca_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  0.800930
# JET_21NP_JET_SingleParticle_HighPt__1down 
f_ca_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.057503
f_ca_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.034623
f_ca_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.016559
f_ca_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  0.781643
f_ca_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.146237
f_ca_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.057198
f_ca_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  0.953142
f_ca_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  0.800930
# JET_21NP_JET_BJES_Response__1up 
f_ca_map[2]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.056893
f_ca_map[3]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.034032
f_ca_map[4]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.016987
f_ca_map[5]['el']["JET_21NP_JET_BJES_Response__1up"] =  0.780792
f_ca_map[2]['mu']["JET_21NP_JET_BJES_Response__1up"] =  1.146775
f_ca_map[3]['mu']["JET_21NP_JET_BJES_Response__1up"] =  1.056833
f_ca_map[4]['mu']["JET_21NP_JET_BJES_Response__1up"] =  0.952715
f_ca_map[5]['mu']["JET_21NP_JET_BJES_Response__1up"] =  0.800255
# JET_21NP_JET_BJES_Response__1down 
f_ca_map[2]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.058110
f_ca_map[3]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.036184
f_ca_map[4]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.018229
f_ca_map[5]['el']["JET_21NP_JET_BJES_Response__1down"] =  0.782205
f_ca_map[2]['mu']["JET_21NP_JET_BJES_Response__1down"] =  1.146477
f_ca_map[3]['mu']["JET_21NP_JET_BJES_Response__1down"] =  1.058664
f_ca_map[4]['mu']["JET_21NP_JET_BJES_Response__1down"] =  0.954301
f_ca_map[5]['mu']["JET_21NP_JET_BJES_Response__1down"] =  0.801830
# JET_21NP_JET_EffectiveNP_1__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.024986
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  0.996607
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  0.961180
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  0.735955
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.100894
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.010637
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  0.909670
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  0.749331
# JET_21NP_JET_EffectiveNP_1__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.112307
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.075134
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.063609
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  0.831790
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.184853
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.113698
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.007672
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  0.855337
# JET_21NP_JET_EffectiveNP_2__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.071392
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.050159
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.027012
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  0.791901
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.155297
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.066716
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  0.972491
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  0.815011
# JET_21NP_JET_EffectiveNP_2__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.047438
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.025534
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.000881
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  0.766968
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.135488
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.042277
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  0.951434
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  0.788015
# JET_21NP_JET_EffectiveNP_3__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.054766
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.037554
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.012943
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  0.778547
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.144312
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.054273
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  0.953706
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  0.799361
# JET_21NP_JET_EffectiveNP_3__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.057916
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.042297
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.021623
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  0.782045
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.147143
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.061018
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  0.954546
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  0.801714
# JET_21NP_JET_EffectiveNP_4__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.057007
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.039370
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.019944
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  0.781595
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.147791
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.057493
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  0.953233
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  0.800995
# JET_21NP_JET_EffectiveNP_4__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.056651
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.036954
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.015733
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  0.779226
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.145557
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.054697
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  0.953924
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  0.799969
# JET_21NP_JET_EffectiveNP_5__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.058602
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.034608
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.018762
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  0.777700
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.146920
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.055926
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  0.955709
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  0.800554
# JET_21NP_JET_EffectiveNP_5__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.054737
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.038179
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.016326
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  0.782207
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.144963
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.057813
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  0.951765
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  0.801610
# JET_21NP_JET_EffectiveNP_6__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.052419
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.038000
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.009022
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  0.779910
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.143187
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.056000
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  0.952896
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  0.798305
# JET_21NP_JET_EffectiveNP_6__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.058606
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.039021
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.020379
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  0.784093
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.147735
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.059699
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  0.957749
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  0.802033
# JET_21NP_JET_EffectiveNP_7__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.057830
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.045411
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.021983
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  0.785023
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.148199
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.062624
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  0.957668
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  0.803223
# JET_21NP_JET_EffectiveNP_7__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.052570
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.035012
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.010290
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  0.777981
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.141551
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.053745
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  0.953398
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  0.796532
# JET_21NP_JET_EffectiveNP_8restTerm__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.054429
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.036803
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.013803
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  0.781417
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.144020
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.058005
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  0.952120
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  0.800280
# JET_21NP_JET_EffectiveNP_8restTerm__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.058388
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.035559
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.020135
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  0.780845
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.147249
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.057509
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  0.954721
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  0.801301

# MET_SoftTrk_ResoPara 
frac[2]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.095316,'cc': 0.065615,'c': 0.209780,'l': 0.629289}
frac[3]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.118486,'cc': 0.100557,'c': 0.219561,'l': 0.561396}
frac[4]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.141309,'cc': 0.139474,'c': 0.215140,'l': 0.504077}
frac[5]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.149541,'cc': 0.152819,'c': 0.209781,'l': 0.487859}
frac[2]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.083871,'cc': 0.063682,'c': 0.205449,'l': 0.646997}
frac[3]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.107562,'cc': 0.098802,'c': 0.215783,'l': 0.577852}
frac[4]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.131115,'cc': 0.135269,'c': 0.207327,'l': 0.526289}
frac[5]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.141141,'cc': 0.148685,'c': 0.202515,'l': 0.507659}
# MET_SoftTrk_ResoPerp 
frac[2]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.095281,'cc': 0.065460,'c': 0.209728,'l': 0.629531}
frac[3]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.118524,'cc': 0.100566,'c': 0.219452,'l': 0.561459}
frac[4]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.141310,'cc': 0.139443,'c': 0.215090,'l': 0.504156}
frac[5]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.149583,'cc': 0.152747,'c': 0.209775,'l': 0.487895}
frac[2]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.083913,'cc': 0.063875,'c': 0.205226,'l': 0.646986}
frac[3]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.107581,'cc': 0.098844,'c': 0.215761,'l': 0.577814}
frac[4]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.131065,'cc': 0.135126,'c': 0.207072,'l': 0.526736}
frac[5]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.141110,'cc': 0.148570,'c': 0.202483,'l': 0.507838}
# MET_SoftTrk_ScaleUp 
frac[2]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.095325,'cc': 0.065587,'c': 0.209786,'l': 0.629302}
frac[3]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.118503,'cc': 0.100495,'c': 0.219368,'l': 0.561634}
frac[4]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.141322,'cc': 0.139391,'c': 0.215189,'l': 0.504099}
frac[5]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.149546,'cc': 0.152724,'c': 0.209811,'l': 0.487918}
frac[2]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.083910,'cc': 0.063732,'c': 0.205407,'l': 0.646950}
frac[3]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.107564,'cc': 0.098655,'c': 0.215809,'l': 0.577971}
frac[4]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.131095,'cc': 0.135069,'c': 0.207057,'l': 0.526779}
frac[5]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.141122,'cc': 0.148522,'c': 0.202316,'l': 0.508040}
# MET_SoftTrk_ScaleDown 
frac[2]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.095378,'cc': 0.065526,'c': 0.209924,'l': 0.629172}
frac[3]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.118549,'cc': 0.100628,'c': 0.219474,'l': 0.561348}
frac[4]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.141324,'cc': 0.139427,'c': 0.215341,'l': 0.503909}
frac[5]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.149518,'cc': 0.152717,'c': 0.209981,'l': 0.487784}
frac[2]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.083907,'cc': 0.063835,'c': 0.205481,'l': 0.646777}
frac[3]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.107494,'cc': 0.098573,'c': 0.215618,'l': 0.578315}
frac[4]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.130972,'cc': 0.135001,'c': 0.207349,'l': 0.526677}
frac[5]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.141045,'cc': 0.148499,'c': 0.202654,'l': 0.507802}
# EG_RESOLUTION_ALL__1up 
frac[2]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.095359,'cc': 0.065557,'c': 0.209748,'l': 0.629336}
frac[3]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.118558,'cc': 0.100590,'c': 0.219396,'l': 0.561456}
frac[4]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.141145,'cc': 0.139506,'c': 0.215140,'l': 0.504208}
frac[5]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.149435,'cc': 0.152758,'c': 0.209801,'l': 0.488006}
frac[2]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508035}
# EG_RESOLUTION_ALL__1down 
frac[2]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.095390,'cc': 0.065591,'c': 0.209988,'l': 0.629031}
frac[3]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.118541,'cc': 0.100566,'c': 0.219282,'l': 0.561611}
frac[4]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.141280,'cc': 0.139409,'c': 0.215341,'l': 0.503969}
frac[5]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.149512,'cc': 0.152741,'c': 0.209931,'l': 0.487816}
frac[2]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.141050,'cc': 0.148513,'c': 0.202402,'l': 0.508035}
# EG_SCALE_ALL__1up 
frac[2]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.095344,'cc': 0.065513,'c': 0.209900,'l': 0.629244}
frac[3]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.118607,'cc': 0.100597,'c': 0.219411,'l': 0.561384}
frac[4]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.141175,'cc': 0.139427,'c': 0.215243,'l': 0.504155}
frac[5]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.149452,'cc': 0.152708,'c': 0.209901,'l': 0.487939}
frac[2]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508035}
# EG_SCALE_ALL__1down 
frac[2]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.095363,'cc': 0.065565,'c': 0.209961,'l': 0.629111}
frac[3]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.118542,'cc': 0.100649,'c': 0.219482,'l': 0.561327}
frac[4]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.141253,'cc': 0.139445,'c': 0.215300,'l': 0.504002}
frac[5]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.149500,'cc': 0.152742,'c': 0.209926,'l': 0.487831}
frac[2]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578006}
frac[4]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.141051,'cc': 0.148513,'c': 0.202402,'l': 0.508035}
# MUON_ID__1up 
frac[2]['el']["MUON_ID__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["MUON_ID__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["MUON_ID__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["MUON_ID__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["MUON_ID__1up"] = {'bb': 0.083914,'cc': 0.063828,'c': 0.205486,'l': 0.646773}
frac[3]['mu']["MUON_ID__1up"] = {'bb': 0.107473,'cc': 0.098644,'c': 0.215810,'l': 0.578073}
frac[4]['mu']["MUON_ID__1up"] = {'bb': 0.130975,'cc': 0.134989,'c': 0.207234,'l': 0.526802}
frac[5]['mu']["MUON_ID__1up"] = {'bb': 0.141010,'cc': 0.148443,'c': 0.202495,'l': 0.508052}
# MUON_ID__1down 
frac[2]['el']["MUON_ID__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["MUON_ID__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["MUON_ID__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["MUON_ID__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["MUON_ID__1down"] = {'bb': 0.083943,'cc': 0.063814,'c': 0.205404,'l': 0.646839}
frac[3]['mu']["MUON_ID__1down"] = {'bb': 0.107497,'cc': 0.098622,'c': 0.215805,'l': 0.578076}
frac[4]['mu']["MUON_ID__1down"] = {'bb': 0.130960,'cc': 0.135024,'c': 0.207202,'l': 0.526814}
frac[5]['mu']["MUON_ID__1down"] = {'bb': 0.141004,'cc': 0.148496,'c': 0.202475,'l': 0.508025}
# MUON_MS__1up 
frac[2]['el']["MUON_MS__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["MUON_MS__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["MUON_MS__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["MUON_MS__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["MUON_MS__1up"] = {'bb': 0.083900,'cc': 0.063819,'c': 0.205379,'l': 0.646902}
frac[3]['mu']["MUON_MS__1up"] = {'bb': 0.107501,'cc': 0.098638,'c': 0.215795,'l': 0.578066}
frac[4]['mu']["MUON_MS__1up"] = {'bb': 0.131024,'cc': 0.134977,'c': 0.207126,'l': 0.526873}
frac[5]['mu']["MUON_MS__1up"] = {'bb': 0.141055,'cc': 0.148470,'c': 0.202455,'l': 0.508020}
# MUON_MS__1down 
frac[2]['el']["MUON_MS__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["MUON_MS__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["MUON_MS__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["MUON_MS__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["MUON_MS__1down"] = {'bb': 0.083919,'cc': 0.063842,'c': 0.205447,'l': 0.646792}
frac[3]['mu']["MUON_MS__1down"] = {'bb': 0.107513,'cc': 0.098610,'c': 0.215884,'l': 0.577993}
frac[4]['mu']["MUON_MS__1down"] = {'bb': 0.130970,'cc': 0.134993,'c': 0.207040,'l': 0.526997}
frac[5]['mu']["MUON_MS__1down"] = {'bb': 0.141040,'cc': 0.148465,'c': 0.202351,'l': 0.508144}
# MUON_SCALE__1up 
frac[2]['el']["MUON_SCALE__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["MUON_SCALE__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["MUON_SCALE__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["MUON_SCALE__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["MUON_SCALE__1up"] = {'bb': 0.083923,'cc': 0.063836,'c': 0.205406,'l': 0.646835}
frac[3]['mu']["MUON_SCALE__1up"] = {'bb': 0.107529,'cc': 0.098705,'c': 0.215806,'l': 0.577960}
frac[4]['mu']["MUON_SCALE__1up"] = {'bb': 0.131047,'cc': 0.135019,'c': 0.207123,'l': 0.526811}
frac[5]['mu']["MUON_SCALE__1up"] = {'bb': 0.141075,'cc': 0.148520,'c': 0.202406,'l': 0.508000}
# MUON_SCALE__1down 
frac[2]['el']["MUON_SCALE__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["MUON_SCALE__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["MUON_SCALE__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["MUON_SCALE__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["MUON_SCALE__1down"] = {'bb': 0.083904,'cc': 0.063829,'c': 0.205444,'l': 0.646823}
frac[3]['mu']["MUON_SCALE__1down"] = {'bb': 0.107550,'cc': 0.098613,'c': 0.215741,'l': 0.578097}
frac[4]['mu']["MUON_SCALE__1down"] = {'bb': 0.131016,'cc': 0.134977,'c': 0.207166,'l': 0.526841}
frac[5]['mu']["MUON_SCALE__1down"] = {'bb': 0.141052,'cc': 0.148481,'c': 0.202464,'l': 0.508004}
# MUON_SAGITTA_RESBIAS__1up 
frac[2]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# MUON_SAGITTA_RESBIAS__1down 
frac[2]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# MUON_SAGITTA_RHO__1up 
frac[2]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# MUON_SAGITTA_RHO__1down 
frac[2]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# JET_JER_SINGLE_NP__1up 
frac[2]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.094435,'cc': 0.064634,'c': 0.208378,'l': 0.632552}
frac[3]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.118550,'cc': 0.099283,'c': 0.218562,'l': 0.563605}
frac[4]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.139264,'cc': 0.136755,'c': 0.214821,'l': 0.509160}
frac[5]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.148313,'cc': 0.150222,'c': 0.209483,'l': 0.491981}
frac[2]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.083440,'cc': 0.062869,'c': 0.204469,'l': 0.649221}
frac[3]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.107605,'cc': 0.097152,'c': 0.215566,'l': 0.579676}
frac[4]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.130567,'cc': 0.133728,'c': 0.208113,'l': 0.527592}
frac[5]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.140463,'cc': 0.146997,'c': 0.203259,'l': 0.509281}
# JET_21NP_JET_EtaIntercalibration_Modelling__1up 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.095011,'cc': 0.065077,'c': 0.209634,'l': 0.630278}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.118288,'cc': 0.100141,'c': 0.219095,'l': 0.562475}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.140797,'cc': 0.138387,'c': 0.215897,'l': 0.504919}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.149087,'cc': 0.151769,'c': 0.210519,'l': 0.488625}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.083729,'cc': 0.063311,'c': 0.205460,'l': 0.647500}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.107284,'cc': 0.098114,'c': 0.215336,'l': 0.579266}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.130241,'cc': 0.133938,'c': 0.207324,'l': 0.528498}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.140407,'cc': 0.147587,'c': 0.202720,'l': 0.509287}
# JET_21NP_JET_EtaIntercalibration_Modelling__1down 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.095684,'cc': 0.065966,'c': 0.209831,'l': 0.628520}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.118977,'cc': 0.101498,'c': 0.219532,'l': 0.559993}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.141464,'cc': 0.139724,'c': 0.214627,'l': 0.504186}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.149702,'cc': 0.153202,'c': 0.209332,'l': 0.487764}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.084155,'cc': 0.064236,'c': 0.205450,'l': 0.646159}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.108034,'cc': 0.099412,'c': 0.215567,'l': 0.576987}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.131211,'cc': 0.135365,'c': 0.206190,'l': 0.527234}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.141253,'cc': 0.148987,'c': 0.201648,'l': 0.508111}
# JET_21NP_JET_EtaIntercalibration_NonClosure__1up 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.095396,'cc': 0.065510,'c': 0.210013,'l': 0.629080}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.118569,'cc': 0.100841,'c': 0.219325,'l': 0.561265}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.141587,'cc': 0.139395,'c': 0.215234,'l': 0.503783}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.149731,'cc': 0.152789,'c': 0.209803,'l': 0.487677}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.083908,'cc': 0.063827,'c': 0.205522,'l': 0.646742}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.107634,'cc': 0.098778,'c': 0.215493,'l': 0.578095}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.131250,'cc': 0.135199,'c': 0.207975,'l': 0.525576}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.141172,'cc': 0.148688,'c': 0.202899,'l': 0.507241}
# JET_21NP_JET_EtaIntercalibration_NonClosure__1down 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.095307,'cc': 0.065421,'c': 0.209692,'l': 0.629580}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.118589,'cc': 0.100355,'c': 0.219582,'l': 0.561474}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.141145,'cc': 0.139174,'c': 0.215367,'l': 0.504314}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.149463,'cc': 0.152679,'c': 0.209960,'l': 0.487898}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.083881,'cc': 0.063701,'c': 0.205371,'l': 0.647047}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.107462,'cc': 0.098380,'c': 0.215802,'l': 0.578356}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.130996,'cc': 0.134783,'c': 0.207007,'l': 0.527214}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.141030,'cc': 0.148356,'c': 0.202325,'l': 0.508289}
# JET_21NP_JET_EtaIntercalibration_TotalStat__1up 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.095171,'cc': 0.065378,'c': 0.209587,'l': 0.629863}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.118430,'cc': 0.100316,'c': 0.219455,'l': 0.561799}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.141310,'cc': 0.139125,'c': 0.215556,'l': 0.504009}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.149520,'cc': 0.152424,'c': 0.210094,'l': 0.487962}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.083863,'cc': 0.063625,'c': 0.205411,'l': 0.647101}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.107333,'cc': 0.098386,'c': 0.215647,'l': 0.578634}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.130904,'cc': 0.134765,'c': 0.207279,'l': 0.527052}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.140960,'cc': 0.148294,'c': 0.202573,'l': 0.508173}
# JET_21NP_JET_EtaIntercalibration_TotalStat__1down 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.095520,'cc': 0.065746,'c': 0.209878,'l': 0.628855}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.118632,'cc': 0.100867,'c': 0.219551,'l': 0.560949}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.141654,'cc': 0.139700,'c': 0.214942,'l': 0.503705}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.149868,'cc': 0.153084,'c': 0.209767,'l': 0.487280}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.084054,'cc': 0.064118,'c': 0.205432,'l': 0.646396}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.107732,'cc': 0.098917,'c': 0.215587,'l': 0.577764}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.131304,'cc': 0.135557,'c': 0.207124,'l': 0.526015}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.141281,'cc': 0.148982,'c': 0.202279,'l': 0.507458}
# JET_21NP_JET_Flavor_Composition__1up 
frac[2]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.092925,'cc': 0.063434,'c': 0.208968,'l': 0.634673}
frac[3]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.115841,'cc': 0.097800,'c': 0.218257,'l': 0.568103}
frac[4]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.137729,'cc': 0.134264,'c': 0.218368,'l': 0.509639}
frac[5]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.145971,'cc': 0.148195,'c': 0.212996,'l': 0.492838}
frac[2]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.081977,'cc': 0.061595,'c': 0.203742,'l': 0.652686}
frac[3]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.105023,'cc': 0.095620,'c': 0.216041,'l': 0.583317}
frac[4]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.127268,'cc': 0.130611,'c': 0.209458,'l': 0.532663}
frac[5]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.137079,'cc': 0.144627,'c': 0.205065,'l': 0.513229}
# JET_21NP_JET_Flavor_Composition__1down 
frac[2]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.097821,'cc': 0.067864,'c': 0.210627,'l': 0.623688}
frac[3]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.122245,'cc': 0.104429,'c': 0.219240,'l': 0.554086}
frac[4]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.144465,'cc': 0.141441,'c': 0.212584,'l': 0.501509}
frac[5]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.152973,'cc': 0.155197,'c': 0.207074,'l': 0.484757}
frac[2]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.085948,'cc': 0.066167,'c': 0.206246,'l': 0.641639}
frac[3]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.110908,'cc': 0.102116,'c': 0.215448,'l': 0.571528}
frac[4]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.135216,'cc': 0.138774,'c': 0.205215,'l': 0.520795}
frac[5]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.145527,'cc': 0.152064,'c': 0.200011,'l': 0.502399}
# JET_21NP_JET_Flavor_Response__1up 
frac[2]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.096069,'cc': 0.066239,'c': 0.209979,'l': 0.627713}
frac[3]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.119353,'cc': 0.101471,'c': 0.219649,'l': 0.559528}
frac[4]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.142379,'cc': 0.140327,'c': 0.214325,'l': 0.502968}
frac[5]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.150644,'cc': 0.153710,'c': 0.209043,'l': 0.486603}
frac[2]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.084495,'cc': 0.064461,'c': 0.205466,'l': 0.645578}
frac[3]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.108642,'cc': 0.099672,'c': 0.215687,'l': 0.575999}
frac[4]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.131640,'cc': 0.135745,'c': 0.205382,'l': 0.527234}
frac[5]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.141922,'cc': 0.149338,'c': 0.201058,'l': 0.507682}
# JET_21NP_JET_Flavor_Response__1down 
frac[2]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.094538,'cc': 0.064675,'c': 0.209635,'l': 0.631152}
frac[3]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.117771,'cc': 0.099865,'c': 0.218979,'l': 0.563385}
frac[4]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.140323,'cc': 0.137930,'c': 0.217030,'l': 0.504717}
frac[5]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.148517,'cc': 0.151361,'c': 0.211356,'l': 0.488766}
frac[2]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.083536,'cc': 0.063245,'c': 0.205229,'l': 0.647990}
frac[3]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.106560,'cc': 0.097708,'c': 0.215420,'l': 0.580312}
frac[4]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.129851,'cc': 0.133552,'c': 0.208058,'l': 0.528540}
frac[5]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.139865,'cc': 0.147199,'c': 0.203371,'l': 0.509564}
# JET_21NP_JET_Pileup_OffsetMu__1up 
frac[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.095445,'cc': 0.065651,'c': 0.209640,'l': 0.629264}
frac[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.118506,'cc': 0.100857,'c': 0.219714,'l': 0.560924}
frac[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.141549,'cc': 0.139430,'c': 0.215266,'l': 0.503754}
frac[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.149687,'cc': 0.152760,'c': 0.209823,'l': 0.487730}
frac[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.083978,'cc': 0.063868,'c': 0.205292,'l': 0.646862}
frac[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.107607,'cc': 0.098628,'c': 0.215578,'l': 0.578187}
frac[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.130965,'cc': 0.134998,'c': 0.207175,'l': 0.526862}
frac[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.141024,'cc': 0.148563,'c': 0.202420,'l': 0.507993}
# JET_21NP_JET_Pileup_OffsetMu__1down 
frac[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.095283,'cc': 0.065510,'c': 0.209961,'l': 0.629246}
frac[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.118614,'cc': 0.100381,'c': 0.219189,'l': 0.561817}
frac[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.141098,'cc': 0.139233,'c': 0.215230,'l': 0.504438}
frac[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.149472,'cc': 0.152616,'c': 0.209950,'l': 0.487962}
frac[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.083933,'cc': 0.063854,'c': 0.205587,'l': 0.646627}
frac[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.107407,'cc': 0.098726,'c': 0.215613,'l': 0.578254}
frac[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.131197,'cc': 0.134998,'c': 0.207075,'l': 0.526730}
frac[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.141165,'cc': 0.148529,'c': 0.202369,'l': 0.507937}
# JET_21NP_JET_Pileup_OffsetNPV__1up 
frac[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.094985,'cc': 0.065151,'c': 0.209889,'l': 0.629975}
frac[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.118238,'cc': 0.100212,'c': 0.219387,'l': 0.562162}
frac[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.141621,'cc': 0.138580,'c': 0.216344,'l': 0.503455}
frac[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.149568,'cc': 0.151940,'c': 0.210567,'l': 0.487924}
frac[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.083938,'cc': 0.063537,'c': 0.205197,'l': 0.647328}
frac[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.107280,'cc': 0.097898,'c': 0.215633,'l': 0.579189}
frac[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.130373,'cc': 0.134054,'c': 0.207322,'l': 0.528251}
frac[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.140404,'cc': 0.147367,'c': 0.202894,'l': 0.509335}
# JET_21NP_JET_Pileup_OffsetNPV__1down 
frac[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.095739,'cc': 0.065802,'c': 0.210229,'l': 0.628231}
frac[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.118630,'cc': 0.100838,'c': 0.219263,'l': 0.561269}
frac[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.141552,'cc': 0.139734,'c': 0.215323,'l': 0.503390}
frac[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.149794,'cc': 0.153171,'c': 0.209703,'l': 0.487332}
frac[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.084191,'cc': 0.064069,'c': 0.205719,'l': 0.646021}
frac[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.107922,'cc': 0.099349,'c': 0.215299,'l': 0.577430}
frac[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.131348,'cc': 0.135793,'c': 0.206509,'l': 0.526350}
frac[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.141479,'cc': 0.149313,'c': 0.201770,'l': 0.507437}
# JET_21NP_JET_Pileup_PtTerm__1up 
frac[2]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.095391,'cc': 0.065523,'c': 0.209782,'l': 0.629304}
frac[3]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.118520,'cc': 0.100572,'c': 0.219542,'l': 0.561366}
frac[4]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.141343,'cc': 0.139357,'c': 0.215093,'l': 0.504206}
frac[5]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.149566,'cc': 0.152733,'c': 0.209849,'l': 0.487853}
frac[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.083922,'cc': 0.063811,'c': 0.205250,'l': 0.647017}
frac[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.107493,'cc': 0.098581,'c': 0.215793,'l': 0.578133}
frac[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.131071,'cc': 0.134949,'c': 0.207028,'l': 0.526951}
frac[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.141103,'cc': 0.148451,'c': 0.202363,'l': 0.508083}
# JET_21NP_JET_Pileup_PtTerm__1down 
frac[2]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.095407,'cc': 0.065627,'c': 0.210076,'l': 0.628890}
frac[3]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.118533,'cc': 0.100603,'c': 0.219314,'l': 0.561549}
frac[4]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.141238,'cc': 0.139293,'c': 0.215543,'l': 0.503926}
frac[5]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.149498,'cc': 0.152659,'c': 0.210071,'l': 0.487773}
frac[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.083923,'cc': 0.063872,'c': 0.205486,'l': 0.646718}
frac[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.107557,'cc': 0.098691,'c': 0.215568,'l': 0.578185}
frac[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.131061,'cc': 0.135011,'c': 0.207234,'l': 0.526693}
frac[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.141082,'cc': 0.148565,'c': 0.202407,'l': 0.507945}
# JET_21NP_JET_Pileup_RhoTopology__1up 
frac[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.094146,'cc': 0.063763,'c': 0.209324,'l': 0.632767}
frac[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.117502,'cc': 0.098652,'c': 0.218024,'l': 0.565822}
frac[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.140182,'cc': 0.135555,'c': 0.217533,'l': 0.506730}
frac[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.148482,'cc': 0.149249,'c': 0.211891,'l': 0.490377}
frac[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.083166,'cc': 0.062303,'c': 0.204399,'l': 0.650133}
frac[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.106361,'cc': 0.096199,'c': 0.215276,'l': 0.582164}
frac[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.129989,'cc': 0.131685,'c': 0.208814,'l': 0.529512}
frac[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.139811,'cc': 0.145516,'c': 0.204293,'l': 0.510380}
# JET_21NP_JET_Pileup_RhoTopology__1down 
frac[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.096384,'cc': 0.066881,'c': 0.210699,'l': 0.626036}
frac[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.119763,'cc': 0.102992,'c': 0.219285,'l': 0.557960}
frac[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.142244,'cc': 0.141690,'c': 0.214388,'l': 0.501678}
frac[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.150397,'cc': 0.155109,'c': 0.208768,'l': 0.485726}
frac[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.084696,'cc': 0.065418,'c': 0.205902,'l': 0.643984}
frac[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.109010,'cc': 0.100913,'c': 0.215456,'l': 0.574622}
frac[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.132201,'cc': 0.137532,'c': 0.205832,'l': 0.524435}
frac[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.142390,'cc': 0.150901,'c': 0.200995,'l': 0.505713}
# JET_21NP_JET_PunchThrough_MC15__1up 
frac[2]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.095379,'cc': 0.065573,'c': 0.209862,'l': 0.629187}
frac[3]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.118560,'cc': 0.100572,'c': 0.219465,'l': 0.561403}
frac[4]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.141277,'cc': 0.139441,'c': 0.215285,'l': 0.503997}
frac[5]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.149523,'cc': 0.152729,'c': 0.209922,'l': 0.487826}
frac[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.083917,'cc': 0.063837,'c': 0.205450,'l': 0.646796}
frac[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.107546,'cc': 0.098646,'c': 0.215803,'l': 0.578006}
frac[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.131002,'cc': 0.135018,'c': 0.207117,'l': 0.526862}
frac[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.141053,'cc': 0.148513,'c': 0.202400,'l': 0.508034}
# JET_21NP_JET_PunchThrough_MC15__1down 
frac[2]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.095379,'cc': 0.065569,'c': 0.209861,'l': 0.629191}
frac[3]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.118556,'cc': 0.100587,'c': 0.219465,'l': 0.561392}
frac[4]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215287,'l': 0.503995}
frac[5]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.149523,'cc': 0.152731,'c': 0.209924,'l': 0.487822}
frac[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.083919,'cc': 0.063836,'c': 0.205450,'l': 0.646795}
frac[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.107541,'cc': 0.098648,'c': 0.215799,'l': 0.578013}
frac[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.131001,'cc': 0.135018,'c': 0.207120,'l': 0.526861}
frac[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.141050,'cc': 0.148514,'c': 0.202403,'l': 0.508033}
# JET_21NP_JET_SingleParticle_HighPt__1up 
frac[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508035}
# JET_21NP_JET_SingleParticle_HighPt__1down 
frac[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# JET_21NP_JET_BJES_Response__1up 
frac[2]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.095618,'cc': 0.065553,'c': 0.209806,'l': 0.629023}
frac[3]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.118988,'cc': 0.100539,'c': 0.219355,'l': 0.561118}
frac[4]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.141791,'cc': 0.139359,'c': 0.215156,'l': 0.503694}
frac[5]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.150077,'cc': 0.152632,'c': 0.209785,'l': 0.487507}
frac[2]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.084122,'cc': 0.063823,'c': 0.205403,'l': 0.646652}
frac[3]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.107896,'cc': 0.098607,'c': 0.215719,'l': 0.577778}
frac[4]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.131527,'cc': 0.134937,'c': 0.206993,'l': 0.526543}
frac[5]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.141615,'cc': 0.148415,'c': 0.202269,'l': 0.507700}
# JET_21NP_JET_BJES_Response__1down 
frac[2]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.095168,'cc': 0.065585,'c': 0.209911,'l': 0.629336}
frac[3]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.118141,'cc': 0.100636,'c': 0.219567,'l': 0.561655}
frac[4]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.140648,'cc': 0.139545,'c': 0.215443,'l': 0.504364}
frac[5]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.148861,'cc': 0.152850,'c': 0.210086,'l': 0.488203}
frac[2]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.083716,'cc': 0.063851,'c': 0.205494,'l': 0.646939}
frac[3]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.107189,'cc': 0.098685,'c': 0.215890,'l': 0.578235}
frac[4]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.130519,'cc': 0.135096,'c': 0.207233,'l': 0.527152}
frac[5]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.140510,'cc': 0.148608,'c': 0.202529,'l': 0.508353}
# JET_21NP_JET_EffectiveNP_1__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.094476,'cc': 0.064181,'c': 0.209384,'l': 0.631958}
frac[3]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.117918,'cc': 0.099342,'c': 0.218646,'l': 0.564094}
frac[4]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.140738,'cc': 0.136820,'c': 0.216908,'l': 0.505534}
frac[5]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.148923,'cc': 0.150532,'c': 0.211326,'l': 0.489218}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.083488,'cc': 0.062850,'c': 0.204638,'l': 0.649024}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.106787,'cc': 0.096857,'c': 0.215818,'l': 0.580538}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.129815,'cc': 0.132457,'c': 0.207916,'l': 0.529812}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.139877,'cc': 0.146275,'c': 0.203353,'l': 0.510494}
# JET_21NP_JET_EffectiveNP_1__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.096139,'cc': 0.066506,'c': 0.210228,'l': 0.627128}
frac[3]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.119339,'cc': 0.102451,'c': 0.219551,'l': 0.558659}
frac[4]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.142005,'cc': 0.140842,'c': 0.214505,'l': 0.502649}
frac[5]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.150256,'cc': 0.154337,'c': 0.209038,'l': 0.486369}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.084468,'cc': 0.064978,'c': 0.205722,'l': 0.644832}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.108606,'cc': 0.100075,'c': 0.215441,'l': 0.575878}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.131550,'cc': 0.136937,'c': 0.205610,'l': 0.525902}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.141791,'cc': 0.150231,'c': 0.201158,'l': 0.506821}
# JET_21NP_JET_EffectiveNP_2__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.095528,'cc': 0.065770,'c': 0.209860,'l': 0.628841}
frac[3]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.118695,'cc': 0.100788,'c': 0.219585,'l': 0.560932}
frac[4]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.141683,'cc': 0.139839,'c': 0.214991,'l': 0.503487}
frac[5]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.149874,'cc': 0.153150,'c': 0.209662,'l': 0.487315}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.084059,'cc': 0.064179,'c': 0.205497,'l': 0.646265}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.107783,'cc': 0.099029,'c': 0.215585,'l': 0.577602}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.131207,'cc': 0.135467,'c': 0.207041,'l': 0.526284}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.141261,'cc': 0.148957,'c': 0.202235,'l': 0.507548}
# JET_21NP_JET_EffectiveNP_2__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.095119,'cc': 0.065324,'c': 0.209582,'l': 0.629975}
frac[3]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.118429,'cc': 0.100266,'c': 0.219549,'l': 0.561756}
frac[4]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.141298,'cc': 0.138918,'c': 0.215499,'l': 0.504285}
frac[5]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.149489,'cc': 0.152325,'c': 0.210126,'l': 0.488060}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.083824,'cc': 0.063590,'c': 0.205479,'l': 0.647107}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.107256,'cc': 0.098219,'c': 0.215580,'l': 0.578944}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.130917,'cc': 0.134554,'c': 0.207521,'l': 0.527007}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.140949,'cc': 0.148135,'c': 0.202773,'l': 0.508143}
# JET_21NP_JET_EffectiveNP_3__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.095345,'cc': 0.065533,'c': 0.209885,'l': 0.629238}
frac[3]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.118530,'cc': 0.100603,'c': 0.219357,'l': 0.561510}
frac[4]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.141205,'cc': 0.139337,'c': 0.215463,'l': 0.503995}
frac[5]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.149522,'cc': 0.152665,'c': 0.210085,'l': 0.487727}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.083892,'cc': 0.063762,'c': 0.205455,'l': 0.646890}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.107446,'cc': 0.098568,'c': 0.215883,'l': 0.578103}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.131062,'cc': 0.135052,'c': 0.207083,'l': 0.526803}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.141077,'cc': 0.148537,'c': 0.202418,'l': 0.507968}
# JET_21NP_JET_EffectiveNP_3__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.095384,'cc': 0.065555,'c': 0.209925,'l': 0.629135}
frac[3]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.118658,'cc': 0.100573,'c': 0.219471,'l': 0.561298}
frac[4]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.141309,'cc': 0.139616,'c': 0.215273,'l': 0.503802}
frac[5]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.149520,'cc': 0.152886,'c': 0.209883,'l': 0.487712}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.083930,'cc': 0.063935,'c': 0.205338,'l': 0.646798}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.107612,'cc': 0.098680,'c': 0.215859,'l': 0.577849}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.131117,'cc': 0.135108,'c': 0.207164,'l': 0.526611}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.141132,'cc': 0.148611,'c': 0.202417,'l': 0.507840}
# JET_21NP_JET_EffectiveNP_4__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.095376,'cc': 0.065591,'c': 0.209862,'l': 0.629171}
frac[3]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.118630,'cc': 0.100500,'c': 0.219513,'l': 0.561357}
frac[4]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.141306,'cc': 0.139510,'c': 0.215217,'l': 0.503967}
frac[5]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.149531,'cc': 0.152808,'c': 0.209857,'l': 0.487804}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.083937,'cc': 0.063917,'c': 0.205396,'l': 0.646749}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.107557,'cc': 0.098676,'c': 0.215809,'l': 0.577959}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.131086,'cc': 0.135023,'c': 0.207124,'l': 0.526766}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.141101,'cc': 0.148520,'c': 0.202414,'l': 0.507965}
# JET_21NP_JET_EffectiveNP_4__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.095361,'cc': 0.065554,'c': 0.209898,'l': 0.629187}
frac[3]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.118522,'cc': 0.100573,'c': 0.219518,'l': 0.561387}
frac[4]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.141255,'cc': 0.139421,'c': 0.215284,'l': 0.504040}
frac[5]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.149544,'cc': 0.152732,'c': 0.209959,'l': 0.487764}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.083921,'cc': 0.063793,'c': 0.205422,'l': 0.646863}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.107484,'cc': 0.098599,'c': 0.215886,'l': 0.578031}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.131074,'cc': 0.135065,'c': 0.207071,'l': 0.526791}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.141095,'cc': 0.148558,'c': 0.202400,'l': 0.507946}
# JET_21NP_JET_EffectiveNP_5__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.095373,'cc': 0.065585,'c': 0.209942,'l': 0.629100}
frac[3]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.118600,'cc': 0.100578,'c': 0.219458,'l': 0.561364}
frac[4]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.141241,'cc': 0.139436,'c': 0.215296,'l': 0.504027}
frac[5]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.149514,'cc': 0.152777,'c': 0.209926,'l': 0.487783}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.083917,'cc': 0.063860,'c': 0.205429,'l': 0.646794}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.107547,'cc': 0.098664,'c': 0.215851,'l': 0.577939}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.131061,'cc': 0.134988,'c': 0.207089,'l': 0.526862}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.141084,'cc': 0.148507,'c': 0.202364,'l': 0.508045}
# JET_21NP_JET_EffectiveNP_5__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.095376,'cc': 0.065549,'c': 0.209838,'l': 0.629237}
frac[3]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.118526,'cc': 0.100508,'c': 0.219506,'l': 0.561460}
frac[4]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.141362,'cc': 0.139492,'c': 0.215372,'l': 0.503774}
frac[5]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.149570,'cc': 0.152749,'c': 0.209988,'l': 0.487693}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.083926,'cc': 0.063844,'c': 0.205424,'l': 0.646806}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.107484,'cc': 0.098593,'c': 0.215875,'l': 0.578048}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.131042,'cc': 0.135104,'c': 0.207056,'l': 0.526798}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.141075,'cc': 0.148561,'c': 0.202352,'l': 0.508013}
# JET_21NP_JET_EffectiveNP_6__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.095338,'cc': 0.065504,'c': 0.209840,'l': 0.629318}
frac[3]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.118500,'cc': 0.100561,'c': 0.219272,'l': 0.561667}
frac[4]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.141299,'cc': 0.139420,'c': 0.215537,'l': 0.503744}
frac[5]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.149532,'cc': 0.152706,'c': 0.210095,'l': 0.487668}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.083883,'cc': 0.063772,'c': 0.205402,'l': 0.646943}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.107449,'cc': 0.098580,'c': 0.216006,'l': 0.577965}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.130985,'cc': 0.134949,'c': 0.206926,'l': 0.527140}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.141025,'cc': 0.148463,'c': 0.202305,'l': 0.508207}
# JET_21NP_JET_EffectiveNP_6__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.095378,'cc': 0.065566,'c': 0.209986,'l': 0.629069}
frac[3]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.118685,'cc': 0.100608,'c': 0.219454,'l': 0.561253}
frac[4]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.141277,'cc': 0.139634,'c': 0.215388,'l': 0.503701}
frac[5]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.149516,'cc': 0.152904,'c': 0.209932,'l': 0.487649}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.083937,'cc': 0.063882,'c': 0.205422,'l': 0.646760}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.107612,'cc': 0.098687,'c': 0.215843,'l': 0.577858}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.131101,'cc': 0.135220,'c': 0.207164,'l': 0.526514}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.141110,'cc': 0.148677,'c': 0.202409,'l': 0.507804}
# JET_21NP_JET_EffectiveNP_7__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.095394,'cc': 0.065582,'c': 0.209889,'l': 0.629135}
frac[3]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.118685,'cc': 0.100614,'c': 0.219506,'l': 0.561195}
frac[4]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.141288,'cc': 0.139633,'c': 0.215305,'l': 0.503775}
frac[5]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.149513,'cc': 0.152895,'c': 0.209885,'l': 0.487707}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.083934,'cc': 0.063950,'c': 0.205366,'l': 0.646749}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.107607,'cc': 0.098741,'c': 0.215782,'l': 0.577870}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.131159,'cc': 0.135130,'c': 0.207285,'l': 0.526427}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.141159,'cc': 0.148616,'c': 0.202494,'l': 0.507731}
# JET_21NP_JET_EffectiveNP_7__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.095321,'cc': 0.065500,'c': 0.209871,'l': 0.629307}
frac[3]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.118480,'cc': 0.100518,'c': 0.219315,'l': 0.561686}
frac[4]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.141253,'cc': 0.139394,'c': 0.215557,'l': 0.503795}
frac[5]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.149520,'cc': 0.152692,'c': 0.210108,'l': 0.487681}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.083882,'cc': 0.063753,'c': 0.205418,'l': 0.646947}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.107410,'cc': 0.098527,'c': 0.215894,'l': 0.578169}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.130991,'cc': 0.134872,'c': 0.206938,'l': 0.527198}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.141035,'cc': 0.148404,'c': 0.202333,'l': 0.508228}
# JET_21NP_JET_EffectiveNP_8restTerm__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.095370,'cc': 0.065549,'c': 0.209888,'l': 0.629193}
frac[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.118526,'cc': 0.100562,'c': 0.219486,'l': 0.561426}
frac[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.141350,'cc': 0.139500,'c': 0.215352,'l': 0.503798}
frac[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.149570,'cc': 0.152767,'c': 0.209966,'l': 0.487697}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.083938,'cc': 0.063804,'c': 0.205469,'l': 0.646789}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.107489,'cc': 0.098606,'c': 0.215892,'l': 0.578012}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.131005,'cc': 0.135120,'c': 0.207021,'l': 0.526853}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.141046,'cc': 0.148580,'c': 0.202333,'l': 0.508041}
# JET_21NP_JET_EffectiveNP_8restTerm__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.095374,'cc': 0.065579,'c': 0.209910,'l': 0.629137}
frac[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.118624,'cc': 0.100599,'c': 0.219412,'l': 0.561365}
frac[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.141266,'cc': 0.139504,'c': 0.215284,'l': 0.503946}
frac[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.149498,'cc': 0.152773,'c': 0.209885,'l': 0.487844}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.083919,'cc': 0.063886,'c': 0.205428,'l': 0.646766}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.107557,'cc': 0.098678,'c': 0.215795,'l': 0.577971}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.131051,'cc': 0.134998,'c': 0.207124,'l': 0.526827}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.141084,'cc': 0.148507,'c': 0.202407,'l': 0.508002}

# MET_SoftTrk_ResoPara 
flav_map[2]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.249781, 'cc': 1.249781, 'c': 1.000000, 'l': 0.936123}
flav_map[3]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.226655, 'cc': 1.226655, 'c': 0.981496, 'l': 0.918801}
flav_map[4]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.204103, 'cc': 1.204103, 'c': 0.963451, 'l': 0.901909}
flav_map[5]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.179404, 'cc': 1.179404, 'c': 0.943689, 'l': 0.883409}
flav_map[2]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.542146, 'cc': 1.542146, 'c': 1.000000, 'l': 0.876359}
flav_map[3]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.482215, 'cc': 1.482215, 'c': 0.961138, 'l': 0.842302}
flav_map[4]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.428775, 'cc': 1.428775, 'c': 0.926485, 'l': 0.811933}
flav_map[5]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.364237, 'cc': 1.364237, 'c': 0.884636, 'l': 0.775258}
# MET_SoftTrk_ResoPerp 
flav_map[2]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.285074, 'cc': 1.285074, 'c': 1.000000, 'l': 0.927211}
flav_map[3]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.257918, 'cc': 1.257918, 'c': 0.978868, 'l': 0.907617}
flav_map[4]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.231694, 'cc': 1.231694, 'c': 0.958462, 'l': 0.888696}
flav_map[5]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.203049, 'cc': 1.203049, 'c': 0.936170, 'l': 0.868027}
flav_map[2]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.539724, 'cc': 1.539724, 'c': 1.000000, 'l': 0.876714}
flav_map[3]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.480253, 'cc': 1.480253, 'c': 0.961376, 'l': 0.842851}
flav_map[4]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.427348, 'cc': 1.427348, 'c': 0.927016, 'l': 0.812727}
flav_map[5]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.362832, 'cc': 1.362832, 'c': 0.885114, 'l': 0.775992}
# MET_SoftTrk_ScaleUp 
flav_map[2]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.293917, 'cc': 1.293917, 'c': 1.000000, 'l': 0.924845}
flav_map[3]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.265868, 'cc': 1.265868, 'c': 0.978323, 'l': 0.904797}
flav_map[4]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.238647, 'cc': 1.238647, 'c': 0.957285, 'l': 0.885341}
flav_map[5]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.209060, 'cc': 1.209060, 'c': 0.934419, 'l': 0.864193}
flav_map[2]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.522919, 'cc': 1.522919, 'c': 1.000000, 'l': 0.880663}
flav_map[3]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.465948, 'cc': 1.465948, 'c': 0.962591, 'l': 0.847719}
flav_map[4]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.414934, 'cc': 1.414934, 'c': 0.929094, 'l': 0.818219}
flav_map[5]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.352888, 'cc': 1.352888, 'c': 0.888352, 'l': 0.782339}
# MET_SoftTrk_ScaleDown 
flav_map[2]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.247375, 'cc': 1.247375, 'c': 1.000000, 'l': 0.936737}
flav_map[3]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.224470, 'cc': 1.224470, 'c': 0.981637, 'l': 0.919535}
flav_map[4]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.202206, 'cc': 1.202206, 'c': 0.963789, 'l': 0.902816}
flav_map[5]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.177866, 'cc': 1.177866, 'c': 0.944276, 'l': 0.884538}
flav_map[2]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.512501, 'cc': 1.512501, 'c': 1.000000, 'l': 0.882930}
flav_map[3]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.457261, 'cc': 1.457261, 'c': 0.963478, 'l': 0.850684}
flav_map[4]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.407431, 'cc': 1.407431, 'c': 0.930532, 'l': 0.821595}
flav_map[5]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.346496, 'cc': 1.346496, 'c': 0.890245, 'l': 0.786024}
# EG_RESOLUTION_ALL__1up 
flav_map[2]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.275631, 'cc': 1.275631, 'c': 1.000000, 'l': 0.929523}
flav_map[3]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.249596, 'cc': 1.249596, 'c': 0.979591, 'l': 0.910553}
flav_map[4]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.224424, 'cc': 1.224424, 'c': 0.959858, 'l': 0.892210}
flav_map[5]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.196880, 'cc': 1.196880, 'c': 0.938265, 'l': 0.872139}
flav_map[2]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.510776, 'cc': 1.510776, 'c': 1.000000, 'l': 0.883317}
flav_map[3]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.455647, 'cc': 1.455647, 'c': 0.963510, 'l': 0.851085}
flav_map[4]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.406157, 'cc': 1.406157, 'c': 0.930752, 'l': 0.822149}
flav_map[5]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.345573, 'cc': 1.345573, 'c': 0.890650, 'l': 0.786727}
# EG_RESOLUTION_ALL__1down 
flav_map[2]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.259207, 'cc': 1.259207, 'c': 1.000000, 'l': 0.933664}
flav_map[3]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.235075, 'cc': 1.235075, 'c': 0.980836, 'l': 0.915771}
flav_map[4]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.211562, 'cc': 1.211562, 'c': 0.962163, 'l': 0.898336}
flav_map[5]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.185835, 'cc': 1.185835, 'c': 0.941732, 'l': 0.879261}
flav_map[2]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.511310, 'cc': 1.511310, 'c': 1.000000, 'l': 0.883195}
flav_map[3]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.456106, 'cc': 1.456106, 'c': 0.963473, 'l': 0.850935}
flav_map[4]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.406552, 'cc': 1.406552, 'c': 0.930684, 'l': 0.821976}
flav_map[5]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.345893, 'cc': 1.345893, 'c': 0.890548, 'l': 0.786527}
# EG_SCALE_ALL__1up 
flav_map[2]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.269239, 'cc': 1.269239, 'c': 1.000000, 'l': 0.931173}
flav_map[3]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.243889, 'cc': 1.243889, 'c': 0.980027, 'l': 0.912575}
flav_map[4]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.219426, 'cc': 1.219426, 'c': 0.960753, 'l': 0.894628}
flav_map[5]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.192567, 'cc': 1.192567, 'c': 0.939592, 'l': 0.874923}
flav_map[2]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.510971, 'cc': 1.510971, 'c': 1.000000, 'l': 0.883273}
flav_map[3]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.455814, 'cc': 1.455814, 'c': 0.963496, 'l': 0.851030}
flav_map[4]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.406302, 'cc': 1.406302, 'c': 0.930727, 'l': 0.822086}
flav_map[5]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.345691, 'cc': 1.345691, 'c': 0.890613, 'l': 0.786655}
# EG_SCALE_ALL__1down 
flav_map[2]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.257158, 'cc': 1.257158, 'c': 1.000000, 'l': 0.934218}
flav_map[3]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.233183, 'cc': 1.233183, 'c': 0.980929, 'l': 0.916402}
flav_map[4]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.209935, 'cc': 1.209935, 'c': 0.962436, 'l': 0.899126}
flav_map[5]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.184456, 'cc': 1.184456, 'c': 0.942169, 'l': 0.880192}
flav_map[2]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.511112, 'cc': 1.511112, 'c': 1.000000, 'l': 0.883241}
flav_map[3]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.455936, 'cc': 1.455936, 'c': 0.963486, 'l': 0.850990}
flav_map[4]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.406406, 'cc': 1.406406, 'c': 0.930709, 'l': 0.822040}
flav_map[5]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.345773, 'cc': 1.345773, 'c': 0.890585, 'l': 0.786601}
# MUON_ID__1up 
flav_map[2]['el']["MUON_ID__1up"] = {'bb': 1.275007, 'cc': 1.275007, 'c': 1.000000, 'l': 0.929651}
flav_map[3]['el']["MUON_ID__1up"] = {'bb': 1.249060, 'cc': 1.249060, 'c': 0.979649, 'l': 0.910732}
flav_map[4]['el']["MUON_ID__1up"] = {'bb': 1.223916, 'cc': 1.223916, 'c': 0.959929, 'l': 0.892399}
flav_map[5]['el']["MUON_ID__1up"] = {'bb': 1.196469, 'cc': 1.196469, 'c': 0.938402, 'l': 0.872386}
flav_map[2]['mu']["MUON_ID__1up"] = {'bb': 1.507531, 'cc': 1.507531, 'c': 1.000000, 'l': 0.884065}
flav_map[3]['mu']["MUON_ID__1up"] = {'bb': 1.452913, 'cc': 1.452913, 'c': 0.963770, 'l': 0.852036}
flav_map[4]['mu']["MUON_ID__1up"] = {'bb': 1.403777, 'cc': 1.403777, 'c': 0.931176, 'l': 0.823221}
flav_map[5]['mu']["MUON_ID__1up"] = {'bb': 1.343782, 'cc': 1.343782, 'c': 0.891380, 'l': 0.788038}
# MUON_ID__1down 
flav_map[2]['el']["MUON_ID__1down"] = {'bb': 1.274347, 'cc': 1.274347, 'c': 1.000000, 'l': 0.929821}
flav_map[3]['el']["MUON_ID__1down"] = {'bb': 1.248474, 'cc': 1.248474, 'c': 0.979696, 'l': 0.910943}
flav_map[4]['el']["MUON_ID__1down"] = {'bb': 1.223400, 'cc': 1.223400, 'c': 0.960021, 'l': 0.892648}
flav_map[5]['el']["MUON_ID__1down"] = {'bb': 1.196026, 'cc': 1.196026, 'c': 0.938540, 'l': 0.872674}
flav_map[2]['mu']["MUON_ID__1down"] = {'bb': 1.504206, 'cc': 1.504206, 'c': 1.000000, 'l': 0.884825}
flav_map[3]['mu']["MUON_ID__1down"] = {'bb': 1.450051, 'cc': 1.450051, 'c': 0.963998, 'l': 0.852969}
flav_map[4]['mu']["MUON_ID__1down"] = {'bb': 1.401302, 'cc': 1.401302, 'c': 0.931589, 'l': 0.824293}
flav_map[5]['mu']["MUON_ID__1down"] = {'bb': 1.341687, 'cc': 1.341687, 'c': 0.891957, 'l': 0.789226}
# MUON_MS__1up 
flav_map[2]['el']["MUON_MS__1up"] = {'bb': 1.274824, 'cc': 1.274824, 'c': 1.000000, 'l': 0.929699}
flav_map[3]['el']["MUON_MS__1up"] = {'bb': 1.248897, 'cc': 1.248897, 'c': 0.979662, 'l': 0.910791}
flav_map[4]['el']["MUON_MS__1up"] = {'bb': 1.223773, 'cc': 1.223773, 'c': 0.959954, 'l': 0.892468}
flav_map[5]['el']["MUON_MS__1up"] = {'bb': 1.196346, 'cc': 1.196346, 'c': 0.938440, 'l': 0.872466}
flav_map[2]['mu']["MUON_MS__1up"] = {'bb': 1.520821, 'cc': 1.520821, 'c': 1.000000, 'l': 0.881072}
flav_map[3]['mu']["MUON_MS__1up"] = {'bb': 1.464280, 'cc': 1.464280, 'c': 0.962822, 'l': 0.848316}
flav_map[4]['mu']["MUON_MS__1up"] = {'bb': 1.413561, 'cc': 1.413561, 'c': 0.929473, 'l': 0.818932}
flav_map[5]['mu']["MUON_MS__1up"] = {'bb': 1.351622, 'cc': 1.351622, 'c': 0.888745, 'l': 0.783049}
# MUON_MS__1down 
flav_map[2]['el']["MUON_MS__1down"] = {'bb': 1.274349, 'cc': 1.274349, 'c': 1.000000, 'l': 0.929820}
flav_map[3]['el']["MUON_MS__1down"] = {'bb': 1.248476, 'cc': 1.248476, 'c': 0.979697, 'l': 0.910942}
flav_map[4]['el']["MUON_MS__1down"] = {'bb': 1.223402, 'cc': 1.223402, 'c': 0.960021, 'l': 0.892646}
flav_map[5]['el']["MUON_MS__1down"] = {'bb': 1.196027, 'cc': 1.196027, 'c': 0.938540, 'l': 0.872673}
flav_map[2]['mu']["MUON_MS__1down"] = {'bb': 1.488603, 'cc': 1.488603, 'c': 1.000000, 'l': 0.888377}
flav_map[3]['mu']["MUON_MS__1down"] = {'bb': 1.436605, 'cc': 1.436605, 'c': 0.965069, 'l': 0.857346}
flav_map[4]['mu']["MUON_MS__1down"] = {'bb': 1.389756, 'cc': 1.389756, 'c': 0.933598, 'l': 0.829387}
flav_map[5]['mu']["MUON_MS__1down"] = {'bb': 1.332194, 'cc': 1.332194, 'c': 0.894929, 'l': 0.795035}
# MUON_SCALE__1up 
flav_map[2]['el']["MUON_SCALE__1up"] = {'bb': 1.274784, 'cc': 1.274784, 'c': 1.000000, 'l': 0.929709}
flav_map[3]['el']["MUON_SCALE__1up"] = {'bb': 1.248862, 'cc': 1.248862, 'c': 0.979665, 'l': 0.910804}
flav_map[4]['el']["MUON_SCALE__1up"] = {'bb': 1.223741, 'cc': 1.223741, 'c': 0.959960, 'l': 0.892483}
flav_map[5]['el']["MUON_SCALE__1up"] = {'bb': 1.196319, 'cc': 1.196319, 'c': 0.938448, 'l': 0.872484}
flav_map[2]['mu']["MUON_SCALE__1up"] = {'bb': 1.514859, 'cc': 1.514859, 'c': 1.000000, 'l': 0.882388}
flav_map[3]['mu']["MUON_SCALE__1up"] = {'bb': 1.459111, 'cc': 1.459111, 'c': 0.963199, 'l': 0.849916}
flav_map[4]['mu']["MUON_SCALE__1up"] = {'bb': 1.409136, 'cc': 1.409136, 'c': 0.930209, 'l': 0.820806}
flav_map[5]['mu']["MUON_SCALE__1up"] = {'bb': 1.348040, 'cc': 1.348040, 'c': 0.889878, 'l': 0.785218}
# MUON_SCALE__1down 
flav_map[2]['el']["MUON_SCALE__1down"] = {'bb': 1.274799, 'cc': 1.274799, 'c': 1.000000, 'l': 0.929705}
flav_map[3]['el']["MUON_SCALE__1down"] = {'bb': 1.248875, 'cc': 1.248875, 'c': 0.979664, 'l': 0.910799}
flav_map[4]['el']["MUON_SCALE__1down"] = {'bb': 1.223753, 'cc': 1.223753, 'c': 0.959958, 'l': 0.892478}
flav_map[5]['el']["MUON_SCALE__1down"] = {'bb': 1.196329, 'cc': 1.196329, 'c': 0.938445, 'l': 0.872477}
flav_map[2]['mu']["MUON_SCALE__1down"] = {'bb': 1.512384, 'cc': 1.512384, 'c': 1.000000, 'l': 0.882973}
flav_map[3]['mu']["MUON_SCALE__1down"] = {'bb': 1.457043, 'cc': 1.457043, 'c': 0.963408, 'l': 0.850664}
flav_map[4]['mu']["MUON_SCALE__1down"] = {'bb': 1.407345, 'cc': 1.407345, 'c': 0.930547, 'l': 0.821649}
flav_map[5]['mu']["MUON_SCALE__1down"] = {'bb': 1.346539, 'cc': 1.346539, 'c': 0.890342, 'l': 0.786148}
# MUON_SAGITTA_RESBIAS__1up 
flav_map[2]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892462}
flav_map[5]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786583}
# MUON_SAGITTA_RESBIAS__1down 
flav_map[2]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892462}
flav_map[5]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786583}
# MUON_SAGITTA_RHO__1up 
flav_map[2]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892462}
flav_map[5]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786583}
# MUON_SAGITTA_RHO__1down 
flav_map[2]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892462}
flav_map[5]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786583}
# JET_JER_SINGLE_NP__1up 
flav_map[2]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.280451, 'cc': 1.280451, 'c': 1.000000, 'l': 0.929474}
flav_map[3]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.253693, 'cc': 1.253693, 'c': 0.979103, 'l': 0.910051}
flav_map[4]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.229428, 'cc': 1.229428, 'c': 0.960153, 'l': 0.892437}
flav_map[5]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.199784, 'cc': 1.199784, 'c': 0.937001, 'l': 0.870919}
flav_map[2]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.603014, 'cc': 1.603014, 'c': 1.000000, 'l': 0.864104}
flav_map[3]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.534431, 'cc': 1.534431, 'c': 0.957216, 'l': 0.827135}
flav_map[4]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.473797, 'cc': 1.473797, 'c': 0.919391, 'l': 0.794450}
flav_map[5]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.401688, 'cc': 1.401688, 'c': 0.874408, 'l': 0.755579}
# JET_21NP_JET_EtaIntercalibration_Modelling__1up 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.305565, 'cc': 1.305565, 'c': 1.000000, 'l': 0.922389}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.276100, 'cc': 1.276100, 'c': 0.977431, 'l': 0.901571}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.248005, 'cc': 1.248005, 'c': 0.955912, 'l': 0.881722}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.216984, 'cc': 1.216984, 'c': 0.932151, 'l': 0.859806}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.552975, 'cc': 1.552975, 'c': 1.000000, 'l': 0.874426}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.492041, 'cc': 1.492041, 'c': 0.960763, 'l': 0.840116}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.438314, 'cc': 1.438314, 'c': 0.926167, 'l': 0.809865}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.371076, 'cc': 1.371076, 'c': 0.882871, 'l': 0.772006}
# JET_21NP_JET_EtaIntercalibration_Modelling__1down 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.195267, 'cc': 1.195267, 'c': 1.000000, 'l': 0.949780}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.177686, 'cc': 1.177686, 'c': 0.985291, 'l': 0.935810}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.160920, 'cc': 1.160920, 'c': 0.971264, 'l': 0.922487}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.141830, 'cc': 1.141830, 'c': 0.955293, 'l': 0.907317}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.481718, 'cc': 1.481718, 'c': 1.000000, 'l': 0.889373}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.430091, 'cc': 1.430091, 'c': 0.965157, 'l': 0.858385}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.384668, 'cc': 1.384668, 'c': 0.934502, 'l': 0.831121}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.327424, 'cc': 1.327424, 'c': 0.895868, 'l': 0.796761}
# JET_21NP_JET_EtaIntercalibration_NonClosure__1up 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.301847, 'cc': 1.301847, 'c': 1.000000, 'l': 0.922793}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.272709, 'cc': 1.272709, 'c': 0.977617, 'l': 0.902139}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.244693, 'cc': 1.244693, 'c': 0.956097, 'l': 0.882280}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.214213, 'cc': 1.214213, 'c': 0.932685, 'l': 0.860675}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.557681, 'cc': 1.557681, 'c': 1.000000, 'l': 0.872609}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.495660, 'cc': 1.495660, 'c': 0.960183, 'l': 0.837865}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.440111, 'cc': 1.440111, 'c': 0.924522, 'l': 0.806746}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.373612, 'cc': 1.373612, 'c': 0.881832, 'l': 0.769494}
# JET_21NP_JET_EtaIntercalibration_NonClosure__1down 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.230547, 'cc': 1.230547, 'c': 1.000000, 'l': 0.941142}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.209466, 'cc': 1.209466, 'c': 0.982869, 'l': 0.925019}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.188999, 'cc': 1.188999, 'c': 0.966236, 'l': 0.909365}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.166130, 'cc': 1.166130, 'c': 0.947652, 'l': 0.891875}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.518339, 'cc': 1.518339, 'c': 1.000000, 'l': 0.881774}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.462305, 'cc': 1.462305, 'c': 0.963095, 'l': 0.849233}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.411839, 'cc': 1.411839, 'c': 0.929858, 'l': 0.819925}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.350027, 'cc': 1.350027, 'c': 0.889147, 'l': 0.784027}
# JET_21NP_JET_EtaIntercalibration_TotalStat__1up 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.269522, 'cc': 1.269522, 'c': 1.000000, 'l': 0.931300}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.244188, 'cc': 1.244188, 'c': 0.980045, 'l': 0.912716}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.219571, 'cc': 1.219571, 'c': 0.960654, 'l': 0.894657}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.192838, 'cc': 1.192838, 'c': 0.939597, 'l': 0.875047}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.537329, 'cc': 1.537329, 'c': 1.000000, 'l': 0.877531}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.478664, 'cc': 1.478664, 'c': 0.961840, 'l': 0.844045}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.425823, 'cc': 1.425823, 'c': 0.927468, 'l': 0.813882}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.361568, 'cc': 1.361568, 'c': 0.885671, 'l': 0.777204}
# JET_21NP_JET_EtaIntercalibration_TotalStat__1down 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.246885, 'cc': 1.246885, 'c': 1.000000, 'l': 0.936687}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.224026, 'cc': 1.224026, 'c': 0.981667, 'l': 0.919514}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.201735, 'cc': 1.201735, 'c': 0.963789, 'l': 0.902769}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.177221, 'cc': 1.177221, 'c': 0.944130, 'l': 0.884354}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.511072, 'cc': 1.511072, 'c': 1.000000, 'l': 0.882848}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.455857, 'cc': 1.455857, 'c': 0.963460, 'l': 0.850588}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.405961, 'cc': 1.405961, 'c': 0.930439, 'l': 0.821436}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.345692, 'cc': 1.345692, 'c': 0.890555, 'l': 0.786224}
# JET_21NP_JET_Flavor_Composition__1up 
flav_map[2]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.540087, 'cc': 1.540087, 'c': 1.000000, 'l': 0.866943}
flav_map[3]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.481145, 'cc': 1.481145, 'c': 0.961729, 'l': 0.833764}
flav_map[4]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.427210, 'cc': 1.427210, 'c': 0.926708, 'l': 0.803403}
flav_map[5]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.367061, 'cc': 1.367061, 'c': 0.887652, 'l': 0.769544}
flav_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.717831, 'cc': 1.717831, 'c': 1.000000, 'l': 0.842098}
flav_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.633042, 'cc': 1.633042, 'c': 0.950642, 'l': 0.800534}
flav_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.560238, 'cc': 1.560238, 'c': 0.908261, 'l': 0.764845}
flav_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.470033, 'cc': 1.470033, 'c': 0.855750, 'l': 0.720625}
# JET_21NP_JET_Flavor_Composition__1down 
flav_map[2]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.008118, 'cc': 1.008118, 'c': 1.000000, 'l': 0.997843}
flav_map[3]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.007468, 'cc': 1.007468, 'c': 0.999355, 'l': 0.997200}
flav_map[4]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.006870, 'cc': 1.006870, 'c': 0.998762, 'l': 0.996608}
flav_map[5]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.006115, 'cc': 1.006115, 'c': 0.998013, 'l': 0.995861}
flav_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.353878, 'cc': 1.353878, 'c': 1.000000, 'l': 0.916106}
flav_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.317724, 'cc': 1.317724, 'c': 0.973296, 'l': 0.891642}
flav_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.285408, 'cc': 1.285408, 'c': 0.949426, 'l': 0.869775}
flav_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.244842, 'cc': 1.244842, 'c': 0.919464, 'l': 0.842327}
# JET_21NP_JET_Flavor_Response__1up 
flav_map[2]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.154131, 'cc': 1.154131, 'c': 1.000000, 'l': 0.960146}
flav_map[3]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.140742, 'cc': 1.140742, 'c': 0.988400, 'l': 0.949008}
flav_map[4]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.127600, 'cc': 1.127600, 'c': 0.977012, 'l': 0.938075}
flav_map[5]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.112829, 'cc': 1.112829, 'c': 0.964214, 'l': 0.925786}
flav_map[2]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.472517, 'cc': 1.472517, 'c': 1.000000, 'l': 0.890975}
flav_map[3]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.421852, 'cc': 1.421852, 'c': 0.965593, 'l': 0.860318}
flav_map[4]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.377650, 'cc': 1.377650, 'c': 0.935575, 'l': 0.833573}
flav_map[5]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.320836, 'cc': 1.320836, 'c': 0.896992, 'l': 0.799197}
# JET_21NP_JET_Flavor_Response__1down 
flav_map[2]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.309183, 'cc': 1.309183, 'c': 1.000000, 'l': 0.922006}
flav_map[3]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.279313, 'cc': 1.279313, 'c': 0.977184, 'l': 0.900970}
flav_map[4]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.250812, 'cc': 1.250812, 'c': 0.955414, 'l': 0.880898}
flav_map[5]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.219636, 'cc': 1.219636, 'c': 0.931601, 'l': 0.858942}
flav_map[2]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.585124, 'cc': 1.585124, 'c': 1.000000, 'l': 0.867460}
flav_map[3]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.520346, 'cc': 1.520346, 'c': 0.959134, 'l': 0.832010}
flav_map[4]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.462196, 'cc': 1.462196, 'c': 0.922449, 'l': 0.800188}
flav_map[5]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.391105, 'cc': 1.391105, 'c': 0.877600, 'l': 0.761283}
# JET_21NP_JET_Pileup_OffsetMu__1up 
flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.234673, 'cc': 1.234673, 'c': 1.000000, 'l': 0.939922}
flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.213105, 'cc': 1.213105, 'c': 0.982531, 'l': 0.923503}
flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.192145, 'cc': 1.192145, 'c': 0.965555, 'l': 0.907546}
flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.169202, 'cc': 1.169202, 'c': 0.946974, 'l': 0.890081}
flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.525671, 'cc': 1.525671, 'c': 1.000000, 'l': 0.879854}
flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.468481, 'cc': 1.468481, 'c': 0.962515, 'l': 0.846873}
flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.417240, 'cc': 1.417240, 'c': 0.928929, 'l': 0.817322}
flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.354344, 'cc': 1.354344, 'c': 0.887704, 'l': 0.781050}
# JET_21NP_JET_Pileup_OffsetMu__1down 
flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.261990, 'cc': 1.261990, 'c': 1.000000, 'l': 0.933053}
flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.237533, 'cc': 1.237533, 'c': 0.980621, 'l': 0.914971}
flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.213833, 'cc': 1.213833, 'c': 0.961841, 'l': 0.897448}
flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.187513, 'cc': 1.187513, 'c': 0.940985, 'l': 0.877989}
flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.523493, 'cc': 1.523493, 'c': 1.000000, 'l': 0.880356}
flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.466696, 'cc': 1.466696, 'c': 0.962719, 'l': 0.847535}
flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.415450, 'cc': 1.415450, 'c': 0.929082, 'l': 0.817923}
flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.353263, 'cc': 1.353263, 'c': 0.888264, 'l': 0.781988}
# JET_21NP_JET_Pileup_OffsetNPV__1up 
flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.276901, 'cc': 1.276901, 'c': 1.000000, 'l': 0.929614}
flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.250735, 'cc': 1.250735, 'c': 0.979508, 'l': 0.910564}
flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.225255, 'cc': 1.225255, 'c': 0.959553, 'l': 0.892014}
flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.198117, 'cc': 1.198117, 'c': 0.938300, 'l': 0.872257}
flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.642911, 'cc': 1.642911, 'c': 1.000000, 'l': 0.853531}
flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.569044, 'cc': 1.569044, 'c': 0.955039, 'l': 0.815155}
flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.503629, 'cc': 1.503629, 'c': 0.915222, 'l': 0.781171}
flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.424972, 'cc': 1.424972, 'c': 0.867346, 'l': 0.740306}
# JET_21NP_JET_Pileup_OffsetNPV__1down 
flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.222506, 'cc': 1.222506, 'c': 1.000000, 'l': 0.942786}
flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.202401, 'cc': 1.202401, 'c': 0.983555, 'l': 0.927282}
flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.182551, 'cc': 1.182551, 'c': 0.967317, 'l': 0.911973}
flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.160638, 'cc': 1.160638, 'c': 0.949393, 'l': 0.895075}
flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.495831, 'cc': 1.495831, 'c': 1.000000, 'l': 0.886209}
flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.442369, 'cc': 1.442369, 'c': 0.964260, 'l': 0.854535}
flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.394632, 'cc': 1.394632, 'c': 0.932346, 'l': 0.826254}
flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.335696, 'cc': 1.335696, 'c': 0.892946, 'l': 0.791337}
# JET_21NP_JET_Pileup_PtTerm__1up 
flav_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.258051, 'cc': 1.258051, 'c': 1.000000, 'l': 0.934016}
flav_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.233993, 'cc': 1.233993, 'c': 0.980877, 'l': 0.916155}
flav_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.210636, 'cc': 1.210636, 'c': 0.962310, 'l': 0.898814}
flav_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.184949, 'cc': 1.184949, 'c': 0.941892, 'l': 0.879743}
flav_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.504757, 'cc': 1.504757, 'c': 1.000000, 'l': 0.884749}
flav_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.450526, 'cc': 1.450526, 'c': 0.963960, 'l': 0.852863}
flav_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.401672, 'cc': 1.401672, 'c': 0.931494, 'l': 0.824139}
flav_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.341934, 'cc': 1.341934, 'c': 0.891794, 'l': 0.789015}
# JET_21NP_JET_Pileup_PtTerm__1down 
flav_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.266644, 'cc': 1.266644, 'c': 1.000000, 'l': 0.931723}
flav_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.241697, 'cc': 1.241697, 'c': 0.980305, 'l': 0.913373}
flav_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.217464, 'cc': 1.217464, 'c': 0.961173, 'l': 0.895547}
flav_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.190834, 'cc': 1.190834, 'c': 0.940149, 'l': 0.875959}
flav_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.519314, 'cc': 1.519314, 'c': 1.000000, 'l': 0.881321}
flav_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.463005, 'cc': 1.463005, 'c': 0.962938, 'l': 0.848657}
flav_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.412438, 'cc': 1.412438, 'c': 0.929655, 'l': 0.819324}
flav_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.350675, 'cc': 1.350675, 'c': 0.889003, 'l': 0.783497}
# JET_21NP_JET_Pileup_RhoTopology__1up 
flav_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.445175, 'cc': 1.445175, 'c': 1.000000, 'l': 0.888905}
flav_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.398511, 'cc': 1.398511, 'c': 0.967711, 'l': 0.860203}
flav_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.355120, 'cc': 1.355120, 'c': 0.937685, 'l': 0.833513}
flav_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.307354, 'cc': 1.307354, 'c': 0.904633, 'l': 0.804133}
flav_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.654842, 'cc': 1.654842, 'c': 1.000000, 'l': 0.853477}
flav_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.580036, 'cc': 1.580036, 'c': 0.954795, 'l': 0.814896}
flav_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.512971, 'cc': 1.512971, 'c': 0.914269, 'l': 0.780308}
flav_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.432603, 'cc': 1.432603, 'c': 0.865704, 'l': 0.738858}
# JET_21NP_JET_Pileup_RhoTopology__1down 
flav_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.068705, 'cc': 1.068705, 'c': 1.000000, 'l': 0.982082}
flav_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.063063, 'cc': 1.063063, 'c': 0.994721, 'l': 0.976898}
flav_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.057580, 'cc': 1.057580, 'c': 0.989591, 'l': 0.971860}
flav_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.051272, 'cc': 1.051272, 'c': 0.983688, 'l': 0.966063}
flav_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.384964, 'cc': 1.384964, 'c': 1.000000, 'l': 0.910264}
flav_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.345608, 'cc': 1.345608, 'c': 0.971583, 'l': 0.884397}
flav_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.310555, 'cc': 1.310555, 'c': 0.946274, 'l': 0.861359}
flav_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.266114, 'cc': 1.266114, 'c': 0.914186, 'l': 0.832150}
# JET_21NP_JET_PunchThrough_MC15__1up 
flav_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.274605, 'cc': 1.274605, 'c': 1.000000, 'l': 0.929753}
flav_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.248709, 'cc': 1.248709, 'c': 0.979683, 'l': 0.910864}
flav_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.223602, 'cc': 1.223602, 'c': 0.959985, 'l': 0.892550}
flav_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.196201, 'cc': 1.196201, 'c': 0.938488, 'l': 0.872562}
flav_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.511181, 'cc': 1.511181, 'c': 1.000000, 'l': 0.883226}
flav_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.455991, 'cc': 1.455991, 'c': 0.963479, 'l': 0.850970}
flav_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.406455, 'cc': 1.406455, 'c': 0.930699, 'l': 0.822018}
flav_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.345812, 'cc': 1.345812, 'c': 0.890570, 'l': 0.786574}
# JET_21NP_JET_PunchThrough_MC15__1down 
flav_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.275475, 'cc': 1.275475, 'c': 1.000000, 'l': 0.929533}
flav_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.249475, 'cc': 1.249475, 'c': 0.979615, 'l': 0.910585}
flav_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.224280, 'cc': 1.224280, 'c': 0.959863, 'l': 0.892224}
flav_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.196780, 'cc': 1.196780, 'c': 0.938302, 'l': 0.872183}
flav_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.511081, 'cc': 1.511081, 'c': 1.000000, 'l': 0.883248}
flav_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.455909, 'cc': 1.455909, 'c': 0.963489, 'l': 0.850999}
flav_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.406383, 'cc': 1.406383, 'c': 0.930713, 'l': 0.822050}
flav_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.345754, 'cc': 1.345754, 'c': 0.890590, 'l': 0.786612}
# JET_21NP_JET_SingleParticle_HighPt__1up 
flav_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.274843, 'cc': 1.274843, 'c': 1.000000, 'l': 0.929694}
flav_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.248914, 'cc': 1.248914, 'c': 0.979661, 'l': 0.910785}
flav_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.223788, 'cc': 1.223788, 'c': 0.959952, 'l': 0.892461}
flav_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.196359, 'cc': 1.196359, 'c': 0.938436, 'l': 0.872458}
flav_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.511165, 'cc': 1.511165, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.455981, 'cc': 1.455981, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.406445, 'cc': 1.406445, 'c': 0.930703, 'l': 0.822023}
flav_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890576, 'l': 0.786583}
# JET_21NP_JET_SingleParticle_HighPt__1down 
flav_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929694}
flav_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979662, 'l': 0.910786}
flav_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892462}
flav_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872459}
flav_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.511165, 'cc': 1.511165, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.455981, 'cc': 1.455981, 'c': 0.963483, 'l': 0.850975}
flav_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.406445, 'cc': 1.406445, 'c': 0.930703, 'l': 0.822023}
flav_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890576, 'l': 0.786583}
# JET_21NP_JET_BJES_Response__1up 
flav_map[2]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.273127, 'cc': 1.273127, 'c': 1.000000, 'l': 0.930018}
flav_map[3]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.247319, 'cc': 1.247319, 'c': 0.979729, 'l': 0.911166}
flav_map[4]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.222350, 'cc': 1.222350, 'c': 0.960116, 'l': 0.892926}
flav_map[5]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.195085, 'cc': 1.195085, 'c': 0.938700, 'l': 0.873009}
flav_map[2]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.511600, 'cc': 1.511600, 'c': 1.000000, 'l': 0.882953}
flav_map[3]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.456235, 'cc': 1.456235, 'c': 0.963373, 'l': 0.850613}
flav_map[4]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.406542, 'cc': 1.406542, 'c': 0.930498, 'l': 0.821587}
flav_map[5]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.345801, 'cc': 1.345801, 'c': 0.890315, 'l': 0.786107}
# JET_21NP_JET_BJES_Response__1down 
flav_map[2]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.275347, 'cc': 1.275347, 'c': 1.000000, 'l': 0.929667}
flav_map[3]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.249438, 'cc': 1.249438, 'c': 0.979685, 'l': 0.910780}
flav_map[4]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.224321, 'cc': 1.224321, 'c': 0.959991, 'l': 0.892472}
flav_map[5]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.196855, 'cc': 1.196855, 'c': 0.938454, 'l': 0.872450}
flav_map[2]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.511304, 'cc': 1.511304, 'c': 1.000000, 'l': 0.883371}
flav_map[3]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.456222, 'cc': 1.456222, 'c': 0.963553, 'l': 0.851175}
flav_map[4]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.406743, 'cc': 1.406743, 'c': 0.930814, 'l': 0.822254}
flav_map[5]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.346169, 'cc': 1.346169, 'c': 0.890734, 'l': 0.786848}
# JET_21NP_JET_EffectiveNP_1__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.401215, 'cc': 1.401215, 'c': 1.000000, 'l': 0.899272}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.359943, 'cc': 1.359943, 'c': 0.970546, 'l': 0.872785}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.321353, 'cc': 1.321353, 'c': 0.943005, 'l': 0.848019}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.279015, 'cc': 1.279015, 'c': 0.912791, 'l': 0.820847}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.633335, 'cc': 1.633335, 'c': 1.000000, 'l': 0.857199}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.561396, 'cc': 1.561396, 'c': 0.955956, 'l': 0.819444}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.497856, 'cc': 1.497856, 'c': 0.917054, 'l': 0.786098}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.419351, 'cc': 1.419351, 'c': 0.868989, 'l': 0.744897}
# JET_21NP_JET_EffectiveNP_1__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.116713, 'cc': 1.116713, 'c': 1.000000, 'l': 0.969731}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.106779, 'cc': 1.106779, 'c': 0.991104, 'l': 0.961104}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.097186, 'cc': 1.097186, 'c': 0.982514, 'l': 0.952774}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.086134, 'cc': 1.086134, 'c': 0.972617, 'l': 0.943177}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.468273, 'cc': 1.468273, 'c': 1.000000, 'l': 0.891474}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.418318, 'cc': 1.418318, 'c': 0.965977, 'l': 0.861143}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.373950, 'cc': 1.373950, 'c': 0.935759, 'l': 0.834204}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.318408, 'cc': 1.318408, 'c': 0.897931, 'l': 0.800482}
# JET_21NP_JET_EffectiveNP_2__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.231697, 'cc': 1.231697, 'c': 1.000000, 'l': 0.940569}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.210493, 'cc': 1.210493, 'c': 0.982784, 'l': 0.924377}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.189695, 'cc': 1.189695, 'c': 0.965899, 'l': 0.908495}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.166983, 'cc': 1.166983, 'c': 0.947460, 'l': 0.891152}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.510207, 'cc': 1.510207, 'c': 1.000000, 'l': 0.882970}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.455032, 'cc': 1.455032, 'c': 0.963465, 'l': 0.850711}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.405539, 'cc': 1.405539, 'c': 0.930693, 'l': 0.821774}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.344945, 'cc': 1.344945, 'c': 0.890570, 'l': 0.786347}
# JET_21NP_JET_EffectiveNP_2__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.281361, 'cc': 1.281361, 'c': 1.000000, 'l': 0.928342}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.254664, 'cc': 1.254664, 'c': 0.979165, 'l': 0.909001}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.228880, 'cc': 1.228880, 'c': 0.959043, 'l': 0.890320}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.200685, 'cc': 1.200685, 'c': 0.937039, 'l': 0.869893}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.532582, 'cc': 1.532582, 'c': 1.000000, 'l': 0.878675}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.474782, 'cc': 1.474782, 'c': 0.962286, 'l': 0.845537}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.422421, 'cc': 1.422421, 'c': 0.928120, 'l': 0.815517}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.358785, 'cc': 1.358785, 'c': 0.886598, 'l': 0.779032}
# JET_21NP_JET_EffectiveNP_3__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.284637, 'cc': 1.284637, 'c': 1.000000, 'l': 0.927227}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.257586, 'cc': 1.257586, 'c': 0.978943, 'l': 0.907702}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.231468, 'cc': 1.231468, 'c': 0.958612, 'l': 0.888850}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.202783, 'cc': 1.202783, 'c': 0.936282, 'l': 0.868145}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.518167, 'cc': 1.518167, 'c': 1.000000, 'l': 0.881727}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.462060, 'cc': 1.462060, 'c': 0.963042, 'l': 0.849140}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.411481, 'cc': 1.411481, 'c': 0.929727, 'l': 0.819765}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.350022, 'cc': 1.350022, 'c': 0.889245, 'l': 0.784071}
# JET_21NP_JET_EffectiveNP_3__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.260170, 'cc': 1.260170, 'c': 1.000000, 'l': 0.933446}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.235848, 'cc': 1.235848, 'c': 0.980699, 'l': 0.915430}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.212217, 'cc': 1.212217, 'c': 0.961947, 'l': 0.897926}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.186497, 'cc': 1.186497, 'c': 0.941537, 'l': 0.878874}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.509543, 'cc': 1.509543, 'c': 1.000000, 'l': 0.883514}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.454557, 'cc': 1.454557, 'c': 0.963574, 'l': 0.851331}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.405128, 'cc': 1.405128, 'c': 0.930830, 'l': 0.822401}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.344783, 'cc': 1.344783, 'c': 0.890854, 'l': 0.787082}
# JET_21NP_JET_EffectiveNP_4__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.253473, 'cc': 1.253473, 'c': 1.000000, 'l': 0.935152}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.229931, 'cc': 1.229931, 'c': 0.981219, 'l': 0.917589}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.207006, 'cc': 1.207006, 'c': 0.962929, 'l': 0.900485}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.181950, 'cc': 1.181950, 'c': 0.942940, 'l': 0.881792}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.508875, 'cc': 1.508875, 'c': 1.000000, 'l': 0.883665}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.454043, 'cc': 1.454043, 'c': 0.963660, 'l': 0.851553}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.404735, 'cc': 1.404735, 'c': 0.930982, 'l': 0.822676}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.344469, 'cc': 1.344469, 'c': 0.891041, 'l': 0.787382}
# JET_21NP_JET_EffectiveNP_4__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.277704, 'cc': 1.277704, 'c': 1.000000, 'l': 0.928977}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.251459, 'cc': 1.251459, 'c': 0.979459, 'l': 0.909894}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.226032, 'cc': 1.226032, 'c': 0.959558, 'l': 0.891407}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.198173, 'cc': 1.198173, 'c': 0.937754, 'l': 0.871152}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.516995, 'cc': 1.516995, 'c': 1.000000, 'l': 0.881942}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.461034, 'cc': 1.461034, 'c': 0.963110, 'l': 0.849407}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.410634, 'cc': 1.410634, 'c': 0.929886, 'l': 0.820106}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.349283, 'cc': 1.349283, 'c': 0.889444, 'l': 0.784438}
# JET_21NP_JET_EffectiveNP_5__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.276686, 'cc': 1.276686, 'c': 1.000000, 'l': 0.929209}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.250544, 'cc': 1.250544, 'c': 0.979524, 'l': 0.910183}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.225251, 'cc': 1.225251, 'c': 0.959712, 'l': 0.891774}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.197504, 'cc': 1.197504, 'c': 0.937979, 'l': 0.871578}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.512801, 'cc': 1.512801, 'c': 1.000000, 'l': 0.882837}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.457374, 'cc': 1.457374, 'c': 0.963361, 'l': 0.850491}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.407647, 'cc': 1.407647, 'c': 0.930491, 'l': 0.821472}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.346795, 'cc': 1.346795, 'c': 0.890266, 'l': 0.785960}
# JET_21NP_JET_EffectiveNP_5__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.264437, 'cc': 1.264437, 'c': 1.000000, 'l': 0.932372}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.239705, 'cc': 1.239705, 'c': 0.980440, 'l': 0.914135}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.215572, 'cc': 1.215572, 'c': 0.961355, 'l': 0.896340}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.189393, 'cc': 1.189393, 'c': 0.940650, 'l': 0.877036}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.516863, 'cc': 1.516863, 'c': 1.000000, 'l': 0.881917}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.460972, 'cc': 1.460972, 'c': 0.963154, 'l': 0.849422}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.410569, 'cc': 1.410569, 'c': 0.929925, 'l': 0.820117}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.349303, 'cc': 1.349303, 'c': 0.889535, 'l': 0.784496}
# JET_21NP_JET_EffectiveNP_6__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.267670, 'cc': 1.267670, 'c': 1.000000, 'l': 0.931589}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.242555, 'cc': 1.242555, 'c': 0.980189, 'l': 0.913133}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.218119, 'cc': 1.218119, 'c': 0.960912, 'l': 0.895175}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.191541, 'cc': 1.191541, 'c': 0.939946, 'l': 0.875643}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.519653, 'cc': 1.519653, 'c': 1.000000, 'l': 0.881397}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.463294, 'cc': 1.463294, 'c': 0.962913, 'l': 0.848709}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.412746, 'cc': 1.412746, 'c': 0.929650, 'l': 0.819391}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.350890, 'cc': 1.350890, 'c': 0.888946, 'l': 0.783515}
# JET_21NP_JET_EffectiveNP_6__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.267065, 'cc': 1.267065, 'c': 1.000000, 'l': 0.931673}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.241957, 'cc': 1.241957, 'c': 0.980184, 'l': 0.913210}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.217624, 'cc': 1.217624, 'c': 0.960980, 'l': 0.895318}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.191130, 'cc': 1.191130, 'c': 0.940070, 'l': 0.875838}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.512973, 'cc': 1.512973, 'c': 1.000000, 'l': 0.882758}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.457477, 'cc': 1.457477, 'c': 0.963320, 'l': 0.850379}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.407565, 'cc': 1.407565, 'c': 0.930331, 'l': 0.821257}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.346897, 'cc': 1.346897, 'c': 0.890232, 'l': 0.785860}
# JET_21NP_JET_EffectiveNP_7__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.264299, 'cc': 1.264299, 'c': 1.000000, 'l': 0.932375}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.239497, 'cc': 1.239497, 'c': 0.980383, 'l': 0.914084}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.215463, 'cc': 1.215463, 'c': 0.961373, 'l': 0.896360}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.189286, 'cc': 1.189286, 'c': 0.940668, 'l': 0.877056}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.513250, 'cc': 1.513250, 'c': 1.000000, 'l': 0.882641}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.457725, 'cc': 1.457725, 'c': 0.963307, 'l': 0.850255}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.407816, 'cc': 1.407816, 'c': 0.930326, 'l': 0.821144}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.347059, 'cc': 1.347059, 'c': 0.890176, 'l': 0.785706}
# JET_21NP_JET_EffectiveNP_7__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.276743, 'cc': 1.276743, 'c': 1.000000, 'l': 0.929277}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.250627, 'cc': 1.250627, 'c': 0.979545, 'l': 0.910269}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.225237, 'cc': 1.225237, 'c': 0.959658, 'l': 0.891789}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.197596, 'cc': 1.197596, 'c': 0.938009, 'l': 0.871671}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.519751, 'cc': 1.519751, 'c': 1.000000, 'l': 0.881391}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.463467, 'cc': 1.463467, 'c': 0.962965, 'l': 0.848748}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.412864, 'cc': 1.412864, 'c': 0.929669, 'l': 0.819401}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.350929, 'cc': 1.350929, 'c': 0.888915, 'l': 0.783481}
# JET_21NP_JET_EffectiveNP_8restTerm__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.271074, 'cc': 1.271074, 'c': 1.000000, 'l': 0.930672}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.245581, 'cc': 1.245581, 'c': 0.979944, 'l': 0.912006}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.220773, 'cc': 1.220773, 'c': 0.960427, 'l': 0.893842}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.193835, 'cc': 1.193835, 'c': 0.939233, 'l': 0.874118}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.522914, 'cc': 1.522914, 'c': 1.000000, 'l': 0.880554}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.466132, 'cc': 1.466132, 'c': 0.962715, 'l': 0.847723}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.415045, 'cc': 1.415045, 'c': 0.929169, 'l': 0.818184}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.352911, 'cc': 1.352911, 'c': 0.888370, 'l': 0.782258}
# JET_21NP_JET_EffectiveNP_8restTerm__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.271246, 'cc': 1.271246, 'c': 1.000000, 'l': 0.930607}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.245699, 'cc': 1.245699, 'c': 0.979904, 'l': 0.911905}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.220958, 'cc': 1.220958, 'c': 0.960442, 'l': 0.893794}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.193991, 'cc': 1.193991, 'c': 0.939229, 'l': 0.874053}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.510879, 'cc': 1.510879, 'c': 1.000000, 'l': 0.883249}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.455733, 'cc': 1.455733, 'c': 0.963501, 'l': 0.851011}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.406239, 'cc': 1.406239, 'c': 0.930742, 'l': 0.822077}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.345622, 'cc': 1.345622, 'c': 0.890622, 'l': 0.786641}

