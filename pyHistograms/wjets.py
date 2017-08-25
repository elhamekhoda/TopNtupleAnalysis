
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

# SF systs

# ttNNLO_seq__1up 
f_ca_map[2]['el']["ttNNLO_seq__1up"] =  1.057598
f_ca_map[3]['el']["ttNNLO_seq__1up"] =  1.034637
f_ca_map[4]['el']["ttNNLO_seq__1up"] =  1.016679
f_ca_map[5]['el']["ttNNLO_seq__1up"] =  0.781583
f_ca_map[2]['mu']["ttNNLO_seq__1up"] =  1.146222
f_ca_map[3]['mu']["ttNNLO_seq__1up"] =  1.057299
f_ca_map[4]['mu']["ttNNLO_seq__1up"] =  0.953259
f_ca_map[5]['mu']["ttNNLO_seq__1up"] =  0.800876
# ttNNLO_topPt__1up 
f_ca_map[2]['el']["ttNNLO_topPt__1up"] =  1.057575
f_ca_map[3]['el']["ttNNLO_topPt__1up"] =  1.034634
f_ca_map[4]['el']["ttNNLO_topPt__1up"] =  1.016650
f_ca_map[5]['el']["ttNNLO_topPt__1up"] =  0.781597
f_ca_map[2]['mu']["ttNNLO_topPt__1up"] =  1.146223
f_ca_map[3]['mu']["ttNNLO_topPt__1up"] =  1.057293
f_ca_map[4]['mu']["ttNNLO_topPt__1up"] =  0.953253
f_ca_map[5]['mu']["ttNNLO_topPt__1up"] =  0.800878
# ttEWK__1up 
f_ca_map[2]['el']["ttEWK__1up"] =  1.057503
f_ca_map[3]['el']["ttEWK__1up"] =  1.034623
f_ca_map[4]['el']["ttEWK__1up"] =  1.016557
f_ca_map[5]['el']["ttEWK__1up"] =  0.781643
f_ca_map[2]['mu']["ttEWK__1up"] =  1.146237
f_ca_map[3]['mu']["ttEWK__1up"] =  1.057197
f_ca_map[4]['mu']["ttEWK__1up"] =  0.953141
f_ca_map[5]['mu']["ttEWK__1up"] =  0.800919
# ttEWK__1down 
f_ca_map[2]['el']["ttEWK__1down"] =  1.057503
f_ca_map[3]['el']["ttEWK__1down"] =  1.034623
f_ca_map[4]['el']["ttEWK__1down"] =  1.016558
f_ca_map[5]['el']["ttEWK__1down"] =  0.781642
f_ca_map[2]['mu']["ttEWK__1down"] =  1.146236
f_ca_map[3]['mu']["ttEWK__1down"] =  1.057198
f_ca_map[4]['mu']["ttEWK__1down"] =  0.953142
f_ca_map[5]['mu']["ttEWK__1down"] =  0.800919
# pileup__1up 
f_ca_map[2]['el']["pileup__1up"] =  1.021509
f_ca_map[3]['el']["pileup__1up"] =  1.075188
f_ca_map[4]['el']["pileup__1up"] =  1.043143
f_ca_map[5]['el']["pileup__1up"] =  0.796606
f_ca_map[2]['mu']["pileup__1up"] =  1.137544
f_ca_map[3]['mu']["pileup__1up"] =  1.064560
f_ca_map[4]['mu']["pileup__1up"] =  0.904337
f_ca_map[5]['mu']["pileup__1up"] =  0.798555
# pileup__1down 
f_ca_map[2]['el']["pileup__1down"] =  1.099497
f_ca_map[3]['el']["pileup__1down"] =  1.013009
f_ca_map[4]['el']["pileup__1down"] =  1.010245
f_ca_map[5]['el']["pileup__1down"] =  0.778215
f_ca_map[2]['mu']["pileup__1down"] =  1.151725
f_ca_map[3]['mu']["pileup__1down"] =  1.064629
f_ca_map[4]['mu']["pileup__1down"] =  0.973976
f_ca_map[5]['mu']["pileup__1down"] =  0.802592
# jvt__1up 
f_ca_map[2]['el']["jvt__1up"] =  1.054270
f_ca_map[3]['el']["jvt__1up"] =  1.029304
f_ca_map[4]['el']["jvt__1up"] =  1.010108
f_ca_map[5]['el']["jvt__1up"] =  0.774858
f_ca_map[2]['mu']["jvt__1up"] =  1.142744
f_ca_map[3]['mu']["jvt__1up"] =  1.051277
f_ca_map[4]['mu']["jvt__1up"] =  0.946874
f_ca_map[5]['mu']["jvt__1up"] =  0.794373
# jvt__1down 
f_ca_map[2]['el']["jvt__1down"] =  1.061020
f_ca_map[3]['el']["jvt__1down"] =  1.040250
f_ca_map[4]['el']["jvt__1down"] =  1.023351
f_ca_map[5]['el']["jvt__1down"] =  0.788735
f_ca_map[2]['mu']["jvt__1down"] =  1.150026
f_ca_map[3]['mu']["jvt__1down"] =  1.063400
f_ca_map[4]['mu']["jvt__1down"] =  0.959734
f_ca_map[5]['mu']["jvt__1down"] =  0.807847
# btagbSF_0__1up 
f_ca_map[2]['el']["btagbSF_0__1up"] =  1.053614
f_ca_map[3]['el']["btagbSF_0__1up"] =  1.029305
f_ca_map[4]['el']["btagbSF_0__1up"] =  1.008523
f_ca_map[5]['el']["btagbSF_0__1up"] =  0.774432
f_ca_map[2]['mu']["btagbSF_0__1up"] =  1.143374
f_ca_map[3]['mu']["btagbSF_0__1up"] =  1.051365
f_ca_map[4]['mu']["btagbSF_0__1up"] =  0.945988
f_ca_map[5]['mu']["btagbSF_0__1up"] =  0.794681
# btagbSF_0__1down 
f_ca_map[2]['el']["btagbSF_0__1down"] =  1.061422
f_ca_map[3]['el']["btagbSF_0__1down"] =  1.039884
f_ca_map[4]['el']["btagbSF_0__1down"] =  1.024596
f_ca_map[5]['el']["btagbSF_0__1down"] =  0.788766
f_ca_map[2]['mu']["btagbSF_0__1down"] =  1.149074
f_ca_map[3]['mu']["btagbSF_0__1down"] =  1.063049
f_ca_map[4]['mu']["btagbSF_0__1down"] =  0.960333
f_ca_map[5]['mu']["btagbSF_0__1down"] =  0.807069
# btagbSF_1__1up 
f_ca_map[2]['el']["btagbSF_1__1up"] =  1.058203
f_ca_map[3]['el']["btagbSF_1__1up"] =  1.035266
f_ca_map[4]['el']["btagbSF_1__1up"] =  1.017745
f_ca_map[5]['el']["btagbSF_1__1up"] =  0.782092
f_ca_map[2]['mu']["btagbSF_1__1up"] =  1.146641
f_ca_map[3]['mu']["btagbSF_1__1up"] =  1.058127
f_ca_map[4]['mu']["btagbSF_1__1up"] =  0.954183
f_ca_map[5]['mu']["btagbSF_1__1up"] =  0.801420
# btagbSF_1__1down 
f_ca_map[2]['el']["btagbSF_1__1down"] =  1.056808
f_ca_map[3]['el']["btagbSF_1__1down"] =  1.033976
f_ca_map[4]['el']["btagbSF_1__1down"] =  1.015378
f_ca_map[5]['el']["btagbSF_1__1down"] =  0.781180
f_ca_map[2]['mu']["btagbSF_1__1down"] =  1.145832
f_ca_map[3]['mu']["btagbSF_1__1down"] =  1.056275
f_ca_map[4]['mu']["btagbSF_1__1down"] =  0.952100
f_ca_map[5]['mu']["btagbSF_1__1down"] =  0.800406
# btagbSF_2__1up 
f_ca_map[2]['el']["btagbSF_2__1up"] =  1.057504
f_ca_map[3]['el']["btagbSF_2__1up"] =  1.034787
f_ca_map[4]['el']["btagbSF_2__1up"] =  1.016613
f_ca_map[5]['el']["btagbSF_2__1up"] =  0.781918
f_ca_map[2]['mu']["btagbSF_2__1up"] =  1.146306
f_ca_map[3]['mu']["btagbSF_2__1up"] =  1.057208
f_ca_map[4]['mu']["btagbSF_2__1up"] =  0.953201
f_ca_map[5]['mu']["btagbSF_2__1up"] =  0.801119
# btagbSF_2__1down 
f_ca_map[2]['el']["btagbSF_2__1down"] =  1.057501
f_ca_map[3]['el']["btagbSF_2__1down"] =  1.034458
f_ca_map[4]['el']["btagbSF_2__1down"] =  1.016502
f_ca_map[5]['el']["btagbSF_2__1down"] =  0.781365
f_ca_map[2]['mu']["btagbSF_2__1down"] =  1.146168
f_ca_map[3]['mu']["btagbSF_2__1down"] =  1.057188
f_ca_map[4]['mu']["btagbSF_2__1down"] =  0.953082
f_ca_map[5]['mu']["btagbSF_2__1down"] =  0.800718
# btagbSF_3__1up 
f_ca_map[2]['el']["btagbSF_3__1up"] =  1.057367
f_ca_map[3]['el']["btagbSF_3__1up"] =  1.034433
f_ca_map[4]['el']["btagbSF_3__1up"] =  1.016372
f_ca_map[5]['el']["btagbSF_3__1up"] =  0.781472
f_ca_map[2]['mu']["btagbSF_3__1up"] =  1.146144
f_ca_map[3]['mu']["btagbSF_3__1up"] =  1.057039
f_ca_map[4]['mu']["btagbSF_3__1up"] =  0.952934
f_ca_map[5]['mu']["btagbSF_3__1up"] =  0.800731
# btagbSF_3__1down 
f_ca_map[2]['el']["btagbSF_3__1down"] =  1.057638
f_ca_map[3]['el']["btagbSF_3__1down"] =  1.034812
f_ca_map[4]['el']["btagbSF_3__1down"] =  1.016744
f_ca_map[5]['el']["btagbSF_3__1down"] =  0.781813
f_ca_map[2]['mu']["btagbSF_3__1down"] =  1.146329
f_ca_map[3]['mu']["btagbSF_3__1down"] =  1.057356
f_ca_map[4]['mu']["btagbSF_3__1down"] =  0.953349
f_ca_map[5]['mu']["btagbSF_3__1down"] =  0.801106
# btagbSF_0_pt1__1up 
f_ca_map[2]['el']["btagbSF_0_pt1__1up"] =  1.053575
f_ca_map[3]['el']["btagbSF_0_pt1__1up"] =  1.029389
f_ca_map[4]['el']["btagbSF_0_pt1__1up"] =  1.008603
f_ca_map[5]['el']["btagbSF_0_pt1__1up"] =  0.774844
f_ca_map[2]['mu']["btagbSF_0_pt1__1up"] =  1.143388
f_ca_map[3]['mu']["btagbSF_0_pt1__1up"] =  1.051400
f_ca_map[4]['mu']["btagbSF_0_pt1__1up"] =  0.946072
f_ca_map[5]['mu']["btagbSF_0_pt1__1up"] =  0.794917
# btagbSF_0_pt1__1down 
f_ca_map[2]['el']["btagbSF_0_pt1__1down"] =  1.061472
f_ca_map[3]['el']["btagbSF_0_pt1__1down"] =  1.039799
f_ca_map[4]['el']["btagbSF_0_pt1__1down"] =  1.024537
f_ca_map[5]['el']["btagbSF_0_pt1__1down"] =  0.788353
f_ca_map[2]['mu']["btagbSF_0_pt1__1down"] =  1.149061
f_ca_map[3]['mu']["btagbSF_0_pt1__1down"] =  1.063023
f_ca_map[4]['mu']["btagbSF_0_pt1__1down"] =  0.960263
f_ca_map[5]['mu']["btagbSF_0_pt1__1down"] =  0.806839
# btagbSF_0_pt2__1up 
f_ca_map[2]['el']["btagbSF_0_pt2__1up"] =  1.057540
f_ca_map[3]['el']["btagbSF_0_pt2__1up"] =  1.034576
f_ca_map[4]['el']["btagbSF_0_pt2__1up"] =  1.016509
f_ca_map[5]['el']["btagbSF_0_pt2__1up"] =  0.781408
f_ca_map[2]['mu']["btagbSF_0_pt2__1up"] =  1.146234
f_ca_map[3]['mu']["btagbSF_0_pt2__1up"] =  1.057193
f_ca_map[4]['mu']["btagbSF_0_pt2__1up"] =  0.953111
f_ca_map[5]['mu']["btagbSF_0_pt2__1up"] =  0.800850
# btagbSF_0_pt2__1down 
f_ca_map[2]['el']["btagbSF_0_pt2__1down"] =  1.057466
f_ca_map[3]['el']["btagbSF_0_pt2__1down"] =  1.034670
f_ca_map[4]['el']["btagbSF_0_pt2__1down"] =  1.016605
f_ca_map[5]['el']["btagbSF_0_pt2__1down"] =  0.781876
f_ca_map[2]['mu']["btagbSF_0_pt2__1down"] =  1.146241
f_ca_map[3]['mu']["btagbSF_0_pt2__1down"] =  1.057202
f_ca_map[4]['mu']["btagbSF_0_pt2__1down"] =  0.953171
f_ca_map[5]['mu']["btagbSF_0_pt2__1down"] =  0.800987
# btagbSF_0_pt3__1up 
f_ca_map[2]['el']["btagbSF_0_pt3__1up"] =  1.057511
f_ca_map[3]['el']["btagbSF_0_pt3__1up"] =  1.034585
f_ca_map[4]['el']["btagbSF_0_pt3__1up"] =  1.016535
f_ca_map[5]['el']["btagbSF_0_pt3__1up"] =  0.781464
f_ca_map[2]['mu']["btagbSF_0_pt3__1up"] =  1.146227
f_ca_map[3]['mu']["btagbSF_0_pt3__1up"] =  1.057172
f_ca_map[4]['mu']["btagbSF_0_pt3__1up"] =  0.953093
f_ca_map[5]['mu']["btagbSF_0_pt3__1up"] =  0.800753
# btagbSF_0_pt3__1down 
f_ca_map[2]['el']["btagbSF_0_pt3__1down"] =  1.057496
f_ca_map[3]['el']["btagbSF_0_pt3__1down"] =  1.034660
f_ca_map[4]['el']["btagbSF_0_pt3__1down"] =  1.016580
f_ca_map[5]['el']["btagbSF_0_pt3__1down"] =  0.781822
f_ca_map[2]['mu']["btagbSF_0_pt3__1down"] =  1.146246
f_ca_map[3]['mu']["btagbSF_0_pt3__1down"] =  1.057224
f_ca_map[4]['mu']["btagbSF_0_pt3__1down"] =  0.953188
f_ca_map[5]['mu']["btagbSF_0_pt3__1down"] =  0.801083
# btagcSF_0__1up 
f_ca_map[2]['el']["btagcSF_0__1up"] =  1.051768
f_ca_map[3]['el']["btagcSF_0__1up"] =  1.031964
f_ca_map[4]['el']["btagcSF_0__1up"] =  1.008003
f_ca_map[5]['el']["btagcSF_0__1up"] =  0.777590
f_ca_map[2]['mu']["btagcSF_0__1up"] =  1.142399
f_ca_map[3]['mu']["btagcSF_0__1up"] =  1.054195
f_ca_map[4]['mu']["btagcSF_0__1up"] =  0.947874
f_ca_map[5]['mu']["btagcSF_0__1up"] =  0.794846
# btagcSF_0__1down 
f_ca_map[2]['el']["btagcSF_0__1down"] =  1.063269
f_ca_map[3]['el']["btagcSF_0__1down"] =  1.037231
f_ca_map[4]['el']["btagcSF_0__1down"] =  1.025299
f_ca_map[5]['el']["btagcSF_0__1down"] =  0.785351
f_ca_map[2]['mu']["btagcSF_0__1down"] =  1.150066
f_ca_map[3]['mu']["btagcSF_0__1down"] =  1.060213
f_ca_map[4]['mu']["btagcSF_0__1down"] =  0.958394
f_ca_map[5]['mu']["btagcSF_0__1down"] =  0.806908
# btagcSF_1__1up 
f_ca_map[2]['el']["btagcSF_1__1up"] =  1.058230
f_ca_map[3]['el']["btagcSF_1__1up"] =  1.035975
f_ca_map[4]['el']["btagcSF_1__1up"] =  1.017801
f_ca_map[5]['el']["btagcSF_1__1up"] =  0.784814
f_ca_map[2]['mu']["btagcSF_1__1up"] =  1.146878
f_ca_map[3]['mu']["btagcSF_1__1up"] =  1.058787
f_ca_map[4]['mu']["btagcSF_1__1up"] =  0.955138
f_ca_map[5]['mu']["btagcSF_1__1up"] =  0.803236
# btagcSF_1__1down 
f_ca_map[2]['el']["btagcSF_1__1down"] =  1.056775
f_ca_map[3]['el']["btagcSF_1__1down"] =  1.033254
f_ca_map[4]['el']["btagcSF_1__1down"] =  1.015284
f_ca_map[5]['el']["btagcSF_1__1down"] =  0.778476
f_ca_map[2]['mu']["btagcSF_1__1down"] =  1.145585
f_ca_map[3]['mu']["btagcSF_1__1down"] =  1.055617
f_ca_map[4]['mu']["btagcSF_1__1down"] =  0.951135
f_ca_map[5]['mu']["btagcSF_1__1down"] =  0.798609
# btagcSF_2__1up 
f_ca_map[2]['el']["btagcSF_2__1up"] =  1.057949
f_ca_map[3]['el']["btagcSF_2__1up"] =  1.034424
f_ca_map[4]['el']["btagcSF_2__1up"] =  1.016508
f_ca_map[5]['el']["btagcSF_2__1up"] =  0.782452
f_ca_map[2]['mu']["btagcSF_2__1up"] =  1.146479
f_ca_map[3]['mu']["btagcSF_2__1up"] =  1.057305
f_ca_map[4]['mu']["btagcSF_2__1up"] =  0.953257
f_ca_map[5]['mu']["btagcSF_2__1up"] =  0.800843
# btagcSF_2__1down 
f_ca_map[2]['el']["btagcSF_2__1down"] =  1.057057
f_ca_map[3]['el']["btagcSF_2__1down"] =  1.034824
f_ca_map[4]['el']["btagcSF_2__1down"] =  1.016658
f_ca_map[5]['el']["btagcSF_2__1down"] =  0.780832
f_ca_map[2]['mu']["btagcSF_2__1down"] =  1.145991
f_ca_map[3]['mu']["btagcSF_2__1down"] =  1.057104
f_ca_map[4]['mu']["btagcSF_2__1down"] =  0.953011
f_ca_map[5]['mu']["btagcSF_2__1down"] =  0.800996
# btagcSF_3__1up 
f_ca_map[2]['el']["btagcSF_3__1up"] =  1.057292
f_ca_map[3]['el']["btagcSF_3__1up"] =  1.034356
f_ca_map[4]['el']["btagcSF_3__1up"] =  1.016450
f_ca_map[5]['el']["btagcSF_3__1up"] =  0.781436
f_ca_map[2]['mu']["btagcSF_3__1up"] =  1.145878
f_ca_map[3]['mu']["btagcSF_3__1up"] =  1.056632
f_ca_map[4]['mu']["btagcSF_3__1up"] =  0.952460
f_ca_map[5]['mu']["btagcSF_3__1up"] =  0.800346
# btagcSF_3__1down 
f_ca_map[2]['el']["btagcSF_3__1down"] =  1.057715
f_ca_map[3]['el']["btagcSF_3__1down"] =  1.034892
f_ca_map[4]['el']["btagcSF_3__1down"] =  1.016676
f_ca_map[5]['el']["btagcSF_3__1down"] =  0.781844
f_ca_map[2]['mu']["btagcSF_3__1down"] =  1.146595
f_ca_map[3]['mu']["btagcSF_3__1down"] =  1.057764
f_ca_map[4]['mu']["btagcSF_3__1down"] =  0.953821
f_ca_map[5]['mu']["btagcSF_3__1down"] =  0.801490
# btagcSF_0_pt1__1up 
f_ca_map[2]['el']["btagcSF_0_pt1__1up"] =  1.052550
f_ca_map[3]['el']["btagcSF_0_pt1__1up"] =  1.031458
f_ca_map[4]['el']["btagcSF_0_pt1__1up"] =  1.009783
f_ca_map[5]['el']["btagcSF_0_pt1__1up"] =  0.775499
f_ca_map[2]['mu']["btagcSF_0_pt1__1up"] =  1.142532
f_ca_map[3]['mu']["btagcSF_0_pt1__1up"] =  1.052988
f_ca_map[4]['mu']["btagcSF_0_pt1__1up"] =  0.946920
f_ca_map[5]['mu']["btagcSF_0_pt1__1up"] =  0.794004
# btagcSF_0_pt1__1down 
f_ca_map[2]['el']["btagcSF_0_pt1__1down"] =  1.062456
f_ca_map[3]['el']["btagcSF_0_pt1__1down"] =  1.037771
f_ca_map[4]['el']["btagcSF_0_pt1__1down"] =  1.023559
f_ca_map[5]['el']["btagcSF_0_pt1__1down"] =  0.787825
f_ca_map[2]['mu']["btagcSF_0_pt1__1down"] =  1.149935
f_ca_map[3]['mu']["btagcSF_0_pt1__1down"] =  1.061420
f_ca_map[4]['mu']["btagcSF_0_pt1__1down"] =  0.959334
f_ca_map[5]['mu']["btagcSF_0_pt1__1down"] =  0.807681
# btagcSF_0_pt2__1up 
f_ca_map[2]['el']["btagcSF_0_pt2__1up"] =  1.056679
f_ca_map[3]['el']["btagcSF_0_pt2__1up"] =  1.034925
f_ca_map[4]['el']["btagcSF_0_pt2__1up"] =  1.015131
f_ca_map[5]['el']["btagcSF_0_pt2__1up"] =  0.783040
f_ca_map[2]['mu']["btagcSF_0_pt2__1up"] =  1.146120
f_ca_map[3]['mu']["btagcSF_0_pt2__1up"] =  1.058060
f_ca_map[4]['mu']["btagcSF_0_pt2__1up"] =  0.953692
f_ca_map[5]['mu']["btagcSF_0_pt2__1up"] =  0.801466
# btagcSF_0_pt2__1down 
f_ca_map[2]['el']["btagcSF_0_pt2__1down"] =  1.058349
f_ca_map[3]['el']["btagcSF_0_pt2__1down"] =  1.034332
f_ca_map[4]['el']["btagcSF_0_pt2__1down"] =  1.017876
f_ca_map[5]['el']["btagcSF_0_pt2__1down"] =  0.780211
f_ca_map[2]['mu']["btagcSF_0_pt2__1down"] =  1.146351
f_ca_map[3]['mu']["btagcSF_0_pt2__1down"] =  1.056334
f_ca_map[4]['mu']["btagcSF_0_pt2__1down"] =  0.952634
f_ca_map[5]['mu']["btagcSF_0_pt2__1down"] =  0.800374
# btagcSF_0_pt3__1up 
f_ca_map[2]['el']["btagcSF_0_pt3__1up"] =  1.057543
f_ca_map[3]['el']["btagcSF_0_pt3__1up"] =  1.034846
f_ca_map[4]['el']["btagcSF_0_pt3__1up"] =  1.016192
f_ca_map[5]['el']["btagcSF_0_pt3__1up"] =  0.782497
f_ca_map[2]['mu']["btagcSF_0_pt3__1up"] =  1.146217
f_ca_map[3]['mu']["btagcSF_0_pt3__1up"] =  1.057545
f_ca_map[4]['mu']["btagcSF_0_pt3__1up"] =  0.953558
f_ca_map[5]['mu']["btagcSF_0_pt3__1up"] =  0.801185
# btagcSF_0_pt3__1down 
f_ca_map[2]['el']["btagcSF_0_pt3__1down"] =  1.057469
f_ca_map[3]['el']["btagcSF_0_pt3__1down"] =  1.034393
f_ca_map[4]['el']["btagcSF_0_pt3__1down"] =  1.016964
f_ca_map[5]['el']["btagcSF_0_pt3__1down"] =  0.780765
f_ca_map[2]['mu']["btagcSF_0_pt3__1down"] =  1.146251
f_ca_map[3]['mu']["btagcSF_0_pt3__1down"] =  1.056859
f_ca_map[4]['mu']["btagcSF_0_pt3__1down"] =  0.952717
f_ca_map[5]['mu']["btagcSF_0_pt3__1down"] =  0.800654
# btaglSF_0__1up 
f_ca_map[2]['el']["btaglSF_0__1up"] =  1.051989
f_ca_map[3]['el']["btaglSF_0__1up"] =  1.023453
f_ca_map[4]['el']["btaglSF_0__1up"] =  1.004935
f_ca_map[5]['el']["btaglSF_0__1up"] =  0.766550
f_ca_map[2]['mu']["btaglSF_0__1up"] =  1.138203
f_ca_map[3]['mu']["btaglSF_0__1up"] =  1.047010
f_ca_map[4]['mu']["btaglSF_0__1up"] =  0.938820
f_ca_map[5]['mu']["btaglSF_0__1up"] =  0.783218
# btaglSF_0__1down 
f_ca_map[2]['el']["btaglSF_0__1down"] =  1.062834
f_ca_map[3]['el']["btaglSF_0__1down"] =  1.046193
f_ca_map[4]['el']["btaglSF_0__1down"] =  1.028207
f_ca_map[5]['el']["btaglSF_0__1down"] =  0.796983
f_ca_map[2]['mu']["btaglSF_0__1down"] =  1.154189
f_ca_map[3]['mu']["btaglSF_0__1down"] =  1.067479
f_ca_map[4]['mu']["btaglSF_0__1down"] =  0.967467
f_ca_map[5]['mu']["btaglSF_0__1down"] =  0.818970
# btaglSF_1__1up 
f_ca_map[2]['el']["btaglSF_1__1up"] =  1.061711
f_ca_map[3]['el']["btaglSF_1__1up"] =  1.042545
f_ca_map[4]['el']["btaglSF_1__1up"] =  1.025670
f_ca_map[5]['el']["btaglSF_1__1up"] =  0.792248
f_ca_map[2]['mu']["btaglSF_1__1up"] =  1.151756
f_ca_map[3]['mu']["btaglSF_1__1up"] =  1.064863
f_ca_map[4]['mu']["btaglSF_1__1up"] =  0.963252
f_ca_map[5]['mu']["btaglSF_1__1up"] =  0.813529
# btaglSF_1__1down 
f_ca_map[2]['el']["btaglSF_1__1down"] =  1.053275
f_ca_map[3]['el']["btaglSF_1__1down"] =  1.026835
f_ca_map[4]['el']["btaglSF_1__1down"] =  1.007557
f_ca_map[5]['el']["btaglSF_1__1down"] =  0.771136
f_ca_map[2]['mu']["btaglSF_1__1down"] =  1.140717
f_ca_map[3]['mu']["btaglSF_1__1down"] =  1.049595
f_ca_map[4]['mu']["btaglSF_1__1down"] =  0.943093
f_ca_map[5]['mu']["btaglSF_1__1down"] =  0.788518
# btaglSF_2__1up 
f_ca_map[2]['el']["btaglSF_2__1up"] =  1.055893
f_ca_map[3]['el']["btaglSF_2__1up"] =  1.031384
f_ca_map[4]['el']["btaglSF_2__1up"] =  1.012407
f_ca_map[5]['el']["btaglSF_2__1up"] =  0.777576
f_ca_map[2]['mu']["btaglSF_2__1up"] =  1.144218
f_ca_map[3]['mu']["btaglSF_2__1up"] =  1.054541
f_ca_map[4]['mu']["btaglSF_2__1up"] =  0.950155
f_ca_map[5]['mu']["btaglSF_2__1up"] =  0.796230
# btaglSF_2__1down 
f_ca_map[2]['el']["btaglSF_2__1down"] =  1.059117
f_ca_map[3]['el']["btaglSF_2__1down"] =  1.037875
f_ca_map[4]['el']["btaglSF_2__1down"] =  1.020726
f_ca_map[5]['el']["btaglSF_2__1down"] =  0.785709
f_ca_map[2]['mu']["btaglSF_2__1down"] =  1.148261
f_ca_map[3]['mu']["btaglSF_2__1down"] =  1.059861
f_ca_map[4]['mu']["btaglSF_2__1down"] =  0.956145
f_ca_map[5]['mu']["btaglSF_2__1down"] =  0.805630
# btaglSF_3__1up 
f_ca_map[2]['el']["btaglSF_3__1up"] =  1.057781
f_ca_map[3]['el']["btaglSF_3__1up"] =  1.034892
f_ca_map[4]['el']["btaglSF_3__1up"] =  1.016185
f_ca_map[5]['el']["btaglSF_3__1up"] =  0.781877
f_ca_map[2]['mu']["btaglSF_3__1up"] =  1.146344
f_ca_map[3]['mu']["btaglSF_3__1up"] =  1.057913
f_ca_map[4]['mu']["btaglSF_3__1up"] =  0.954548
f_ca_map[5]['mu']["btaglSF_3__1up"] =  0.801356
# btaglSF_3__1down 
f_ca_map[2]['el']["btaglSF_3__1down"] =  1.057221
f_ca_map[3]['el']["btaglSF_3__1down"] =  1.034345
f_ca_map[4]['el']["btaglSF_3__1down"] =  1.016921
f_ca_map[5]['el']["btaglSF_3__1down"] =  0.781393
f_ca_map[2]['mu']["btaglSF_3__1down"] =  1.146128
f_ca_map[3]['mu']["btaglSF_3__1down"] =  1.056484
f_ca_map[4]['mu']["btaglSF_3__1down"] =  0.951743
f_ca_map[5]['mu']["btaglSF_3__1down"] =  0.800478
# btaglSF_4__1up 
f_ca_map[2]['el']["btaglSF_4__1up"] =  1.059670
f_ca_map[3]['el']["btaglSF_4__1up"] =  1.038130
f_ca_map[4]['el']["btaglSF_4__1up"] =  1.020906
f_ca_map[5]['el']["btaglSF_4__1up"] =  0.786128
f_ca_map[2]['mu']["btaglSF_4__1up"] =  1.148527
f_ca_map[3]['mu']["btaglSF_4__1up"] =  1.060935
f_ca_map[4]['mu']["btaglSF_4__1up"] =  0.957989
f_ca_map[5]['mu']["btaglSF_4__1up"] =  0.806108
# btaglSF_4__1down 
f_ca_map[2]['el']["btaglSF_4__1down"] =  1.055344
f_ca_map[3]['el']["btaglSF_4__1down"] =  1.031128
f_ca_map[4]['el']["btaglSF_4__1down"] =  1.012232
f_ca_map[5]['el']["btaglSF_4__1down"] =  0.777182
f_ca_map[2]['mu']["btaglSF_4__1down"] =  1.143953
f_ca_map[3]['mu']["btaglSF_4__1down"] =  1.053476
f_ca_map[4]['mu']["btaglSF_4__1down"] =  0.948324
f_ca_map[5]['mu']["btaglSF_4__1down"] =  0.795758
# btaglSF_5__1up 
f_ca_map[2]['el']["btaglSF_5__1up"] =  1.056931
f_ca_map[3]['el']["btaglSF_5__1up"] =  1.033624
f_ca_map[4]['el']["btaglSF_5__1up"] =  1.015192
f_ca_map[5]['el']["btaglSF_5__1up"] =  0.780508
f_ca_map[2]['mu']["btaglSF_5__1up"] =  1.145562
f_ca_map[3]['mu']["btaglSF_5__1up"] =  1.056299
f_ca_map[4]['mu']["btaglSF_5__1up"] =  0.952096
f_ca_map[5]['mu']["btaglSF_5__1up"] =  0.799585
# btaglSF_5__1down 
f_ca_map[2]['el']["btaglSF_5__1down"] =  1.058076
f_ca_map[3]['el']["btaglSF_5__1down"] =  1.035621
f_ca_map[4]['el']["btaglSF_5__1down"] =  1.017926
f_ca_map[5]['el']["btaglSF_5__1down"] =  0.782779
f_ca_map[2]['mu']["btaglSF_5__1down"] =  1.146909
f_ca_map[3]['mu']["btaglSF_5__1down"] =  1.058098
f_ca_map[4]['mu']["btaglSF_5__1down"] =  0.954188
f_ca_map[5]['mu']["btaglSF_5__1down"] =  0.802255
# btaglSF_6__1up 
f_ca_map[2]['el']["btaglSF_6__1up"] =  1.057202
f_ca_map[3]['el']["btaglSF_6__1up"] =  1.034115
f_ca_map[4]['el']["btaglSF_6__1up"] =  1.015843
f_ca_map[5]['el']["btaglSF_6__1up"] =  0.781043
f_ca_map[2]['mu']["btaglSF_6__1up"] =  1.145890
f_ca_map[3]['mu']["btaglSF_6__1up"] =  1.056710
f_ca_map[4]['mu']["btaglSF_6__1up"] =  0.952502
f_ca_map[5]['mu']["btaglSF_6__1up"] =  0.800210
# btaglSF_6__1down 
f_ca_map[2]['el']["btaglSF_6__1down"] =  1.057804
f_ca_map[3]['el']["btaglSF_6__1down"] =  1.035130
f_ca_map[4]['el']["btaglSF_6__1down"] =  1.017273
f_ca_map[5]['el']["btaglSF_6__1down"] =  0.782242
f_ca_map[2]['mu']["btaglSF_6__1down"] =  1.146584
f_ca_map[3]['mu']["btaglSF_6__1down"] =  1.057685
f_ca_map[4]['mu']["btaglSF_6__1down"] =  0.953780
f_ca_map[5]['mu']["btaglSF_6__1down"] =  0.801629
# btaglSF_7__1up 
f_ca_map[2]['el']["btaglSF_7__1up"] =  1.057359
f_ca_map[3]['el']["btaglSF_7__1up"] =  1.034478
f_ca_map[4]['el']["btaglSF_7__1up"] =  1.016305
f_ca_map[5]['el']["btaglSF_7__1up"] =  0.781243
f_ca_map[2]['mu']["btaglSF_7__1up"] =  1.146151
f_ca_map[3]['mu']["btaglSF_7__1up"] =  1.056955
f_ca_map[4]['mu']["btaglSF_7__1up"] =  0.952832
f_ca_map[5]['mu']["btaglSF_7__1up"] =  0.800638
# btaglSF_7__1down 
f_ca_map[2]['el']["btaglSF_7__1down"] =  1.057647
f_ca_map[3]['el']["btaglSF_7__1down"] =  1.034767
f_ca_map[4]['el']["btaglSF_7__1down"] =  1.016809
f_ca_map[5]['el']["btaglSF_7__1down"] =  0.782043
f_ca_map[2]['mu']["btaglSF_7__1down"] =  1.146324
f_ca_map[3]['mu']["btaglSF_7__1down"] =  1.057440
f_ca_map[4]['mu']["btaglSF_7__1down"] =  0.953451
f_ca_map[5]['mu']["btaglSF_7__1down"] =  0.801201
# btaglSF_8__1up 
f_ca_map[2]['el']["btaglSF_8__1up"] =  1.057297
f_ca_map[3]['el']["btaglSF_8__1up"] =  1.034383
f_ca_map[4]['el']["btaglSF_8__1up"] =  1.016167
f_ca_map[5]['el']["btaglSF_8__1up"] =  0.781120
f_ca_map[2]['mu']["btaglSF_8__1up"] =  1.146083
f_ca_map[3]['mu']["btaglSF_8__1up"] =  1.056873
f_ca_map[4]['mu']["btaglSF_8__1up"] =  0.952685
f_ca_map[5]['mu']["btaglSF_8__1up"] =  0.800512
# btaglSF_8__1down 
f_ca_map[2]['el']["btaglSF_8__1down"] =  1.057707
f_ca_map[3]['el']["btaglSF_8__1down"] =  1.034862
f_ca_map[4]['el']["btaglSF_8__1down"] =  1.016947
f_ca_map[5]['el']["btaglSF_8__1down"] =  0.782166
f_ca_map[2]['mu']["btaglSF_8__1down"] =  1.146392
f_ca_map[3]['mu']["btaglSF_8__1down"] =  1.057522
f_ca_map[4]['mu']["btaglSF_8__1down"] =  0.953598
f_ca_map[5]['mu']["btaglSF_8__1down"] =  0.801327
# btaglSF_9__1up 
f_ca_map[2]['el']["btaglSF_9__1up"] =  1.057630
f_ca_map[3]['el']["btaglSF_9__1up"] =  1.034824
f_ca_map[4]['el']["btaglSF_9__1up"] =  1.016861
f_ca_map[5]['el']["btaglSF_9__1up"] =  0.781894
f_ca_map[2]['mu']["btaglSF_9__1up"] =  1.146391
f_ca_map[3]['mu']["btaglSF_9__1up"] =  1.057421
f_ca_map[4]['mu']["btaglSF_9__1up"] =  0.953411
f_ca_map[5]['mu']["btaglSF_9__1up"] =  0.801213
# btaglSF_9__1down 
f_ca_map[2]['el']["btaglSF_9__1down"] =  1.057377
f_ca_map[3]['el']["btaglSF_9__1down"] =  1.034421
f_ca_map[4]['el']["btaglSF_9__1down"] =  1.016254
f_ca_map[5]['el']["btaglSF_9__1down"] =  0.781391
f_ca_map[2]['mu']["btaglSF_9__1down"] =  1.146083
f_ca_map[3]['mu']["btaglSF_9__1down"] =  1.056975
f_ca_map[4]['mu']["btaglSF_9__1down"] =  0.952871
f_ca_map[5]['mu']["btaglSF_9__1down"] =  0.800626
# btaglSF_10__1up 
f_ca_map[2]['el']["btaglSF_10__1up"] =  1.057632
f_ca_map[3]['el']["btaglSF_10__1up"] =  1.034797
f_ca_map[4]['el']["btaglSF_10__1up"] =  1.016816
f_ca_map[5]['el']["btaglSF_10__1up"] =  0.781895
f_ca_map[2]['mu']["btaglSF_10__1up"] =  1.146345
f_ca_map[3]['mu']["btaglSF_10__1up"] =  1.057369
f_ca_map[4]['mu']["btaglSF_10__1up"] =  0.953367
f_ca_map[5]['mu']["btaglSF_10__1up"] =  0.801172
# btaglSF_10__1down 
f_ca_map[2]['el']["btaglSF_10__1down"] =  1.057373
f_ca_map[3]['el']["btaglSF_10__1down"] =  1.034446
f_ca_map[4]['el']["btaglSF_10__1down"] =  1.016299
f_ca_map[5]['el']["btaglSF_10__1down"] =  0.781390
f_ca_map[2]['mu']["btaglSF_10__1down"] =  1.146127
f_ca_map[3]['mu']["btaglSF_10__1down"] =  1.057026
f_ca_map[4]['mu']["btaglSF_10__1down"] =  0.952915
f_ca_map[5]['mu']["btaglSF_10__1down"] =  0.800666
# btageSF_0__1up 
f_ca_map[2]['el']["btageSF_0__1up"] =  1.057495
f_ca_map[3]['el']["btageSF_0__1up"] =  1.034594
f_ca_map[4]['el']["btageSF_0__1up"] =  1.016708
f_ca_map[5]['el']["btageSF_0__1up"] =  0.781513
f_ca_map[2]['mu']["btageSF_0__1up"] =  1.146253
f_ca_map[3]['mu']["btageSF_0__1up"] =  1.057224
f_ca_map[4]['mu']["btageSF_0__1up"] =  0.953129
f_ca_map[5]['mu']["btageSF_0__1up"] =  0.800949
# btageSF_0__1down 
f_ca_map[2]['el']["btageSF_0__1down"] =  1.057510
f_ca_map[3]['el']["btageSF_0__1down"] =  1.034651
f_ca_map[4]['el']["btageSF_0__1down"] =  1.016408
f_ca_map[5]['el']["btageSF_0__1down"] =  0.781772
f_ca_map[2]['mu']["btageSF_0__1down"] =  1.146220
f_ca_map[3]['mu']["btageSF_0__1down"] =  1.057171
f_ca_map[4]['mu']["btageSF_0__1down"] =  0.953152
f_ca_map[5]['mu']["btageSF_0__1down"] =  0.800890
# btageSF_1__1up 
f_ca_map[2]['el']["btageSF_1__1up"] =  1.048159
f_ca_map[3]['el']["btageSF_1__1up"] =  1.023280
f_ca_map[4]['el']["btageSF_1__1up"] =  1.000180
f_ca_map[5]['el']["btageSF_1__1up"] =  0.767057
f_ca_map[2]['mu']["btageSF_1__1up"] =  1.137548
f_ca_map[3]['mu']["btageSF_1__1up"] =  1.046099
f_ca_map[4]['mu']["btageSF_1__1up"] =  0.937505
f_ca_map[5]['mu']["btageSF_1__1up"] =  0.784665
# btageSF_1__1down 
f_ca_map[2]['el']["btageSF_1__1down"] =  1.048159
f_ca_map[3]['el']["btageSF_1__1down"] =  1.023280
f_ca_map[4]['el']["btageSF_1__1down"] =  1.000180
f_ca_map[5]['el']["btageSF_1__1down"] =  0.767057
f_ca_map[2]['mu']["btageSF_1__1down"] =  1.137548
f_ca_map[3]['mu']["btageSF_1__1down"] =  1.046099
f_ca_map[4]['mu']["btageSF_1__1down"] =  0.937505
f_ca_map[5]['mu']["btageSF_1__1down"] =  0.784665
# eTrigSF__1up 
f_ca_map[2]['el']["eTrigSF__1up"] =  1.054565
f_ca_map[3]['el']["eTrigSF__1up"] =  1.031765
f_ca_map[4]['el']["eTrigSF__1up"] =  1.013946
f_ca_map[5]['el']["eTrigSF__1up"] =  0.779575
f_ca_map[2]['mu']["eTrigSF__1up"] =  1.146237
f_ca_map[3]['mu']["eTrigSF__1up"] =  1.057198
f_ca_map[4]['mu']["eTrigSF__1up"] =  0.953141
f_ca_map[5]['mu']["eTrigSF__1up"] =  0.800919
# eTrigSF__1down 
f_ca_map[2]['el']["eTrigSF__1down"] =  1.060457
f_ca_map[3]['el']["eTrigSF__1down"] =  1.037495
f_ca_map[4]['el']["eTrigSF__1down"] =  1.019182
f_ca_map[5]['el']["eTrigSF__1down"] =  0.783720
f_ca_map[2]['mu']["eTrigSF__1down"] =  1.146237
f_ca_map[3]['mu']["eTrigSF__1down"] =  1.057198
f_ca_map[4]['mu']["eTrigSF__1down"] =  0.953141
f_ca_map[5]['mu']["eTrigSF__1down"] =  0.800919
# eRecoSF__1up 
f_ca_map[2]['el']["eRecoSF__1up"] =  1.056486
f_ca_map[3]['el']["eRecoSF__1up"] =  1.033556
f_ca_map[4]['el']["eRecoSF__1up"] =  1.015545
f_ca_map[5]['el']["eRecoSF__1up"] =  0.780705
f_ca_map[2]['mu']["eRecoSF__1up"] =  1.146237
f_ca_map[3]['mu']["eRecoSF__1up"] =  1.057198
f_ca_map[4]['mu']["eRecoSF__1up"] =  0.953141
f_ca_map[5]['mu']["eRecoSF__1up"] =  0.800919
# eRecoSF__1down 
f_ca_map[2]['el']["eRecoSF__1down"] =  1.058522
f_ca_map[3]['el']["eRecoSF__1down"] =  1.035691
f_ca_map[4]['el']["eRecoSF__1down"] =  1.017573
f_ca_map[5]['el']["eRecoSF__1down"] =  0.782582
f_ca_map[2]['mu']["eRecoSF__1down"] =  1.146237
f_ca_map[3]['mu']["eRecoSF__1down"] =  1.057198
f_ca_map[4]['mu']["eRecoSF__1down"] =  0.953141
f_ca_map[5]['mu']["eRecoSF__1down"] =  0.800919
# eIDSF__1up 
f_ca_map[2]['el']["eIDSF__1up"] =  1.050894
f_ca_map[3]['el']["eIDSF__1up"] =  1.028105
f_ca_map[4]['el']["eIDSF__1up"] =  1.010642
f_ca_map[5]['el']["eIDSF__1up"] =  0.776531
f_ca_map[2]['mu']["eIDSF__1up"] =  1.146237
f_ca_map[3]['mu']["eIDSF__1up"] =  1.057198
f_ca_map[4]['mu']["eIDSF__1up"] =  0.953141
f_ca_map[5]['mu']["eIDSF__1up"] =  0.800919
# eIDSF__1down 
f_ca_map[2]['el']["eIDSF__1down"] =  1.064192
f_ca_map[3]['el']["eIDSF__1down"] =  1.041218
f_ca_map[4]['el']["eIDSF__1down"] =  1.022539
f_ca_map[5]['el']["eIDSF__1down"] =  0.786819
f_ca_map[2]['mu']["eIDSF__1down"] =  1.146237
f_ca_map[3]['mu']["eIDSF__1down"] =  1.057198
f_ca_map[4]['mu']["eIDSF__1down"] =  0.953141
f_ca_map[5]['mu']["eIDSF__1down"] =  0.800919
# eIsolSF__1up 
f_ca_map[2]['el']["eIsolSF__1up"] =  1.057053
f_ca_map[3]['el']["eIsolSF__1up"] =  1.034354
f_ca_map[4]['el']["eIsolSF__1up"] =  1.016434
f_ca_map[5]['el']["eIsolSF__1up"] =  0.781736
f_ca_map[2]['mu']["eIsolSF__1up"] =  1.146237
f_ca_map[3]['mu']["eIsolSF__1up"] =  1.057198
f_ca_map[4]['mu']["eIsolSF__1up"] =  0.953141
f_ca_map[5]['mu']["eIsolSF__1up"] =  0.800919
# eIsolSF__1down 
f_ca_map[2]['el']["eIsolSF__1down"] =  1.057954
f_ca_map[3]['el']["eIsolSF__1down"] =  1.034891
f_ca_map[4]['el']["eIsolSF__1down"] =  1.016681
f_ca_map[5]['el']["eIsolSF__1down"] =  0.781549
f_ca_map[2]['mu']["eIsolSF__1down"] =  1.146237
f_ca_map[3]['mu']["eIsolSF__1down"] =  1.057198
f_ca_map[4]['mu']["eIsolSF__1down"] =  0.953141
f_ca_map[5]['mu']["eIsolSF__1down"] =  0.800919
# muTrigStatSF__1up 
f_ca_map[2]['el']["muTrigStatSF__1up"] =  1.057503
f_ca_map[3]['el']["muTrigStatSF__1up"] =  1.034623
f_ca_map[4]['el']["muTrigStatSF__1up"] =  1.016558
f_ca_map[5]['el']["muTrigStatSF__1up"] =  0.781642
f_ca_map[2]['mu']["muTrigStatSF__1up"] =  1.140247
f_ca_map[3]['mu']["muTrigStatSF__1up"] =  1.051762
f_ca_map[4]['mu']["muTrigStatSF__1up"] =  0.948058
f_ca_map[5]['mu']["muTrigStatSF__1up"] =  0.796730
# muTrigStatSF__1down 
f_ca_map[2]['el']["muTrigStatSF__1down"] =  1.057503
f_ca_map[3]['el']["muTrigStatSF__1down"] =  1.034623
f_ca_map[4]['el']["muTrigStatSF__1down"] =  1.016558
f_ca_map[5]['el']["muTrigStatSF__1down"] =  0.781642
f_ca_map[2]['mu']["muTrigStatSF__1down"] =  1.152406
f_ca_map[3]['mu']["muTrigStatSF__1down"] =  1.062780
f_ca_map[4]['mu']["muTrigStatSF__1down"] =  0.958363
f_ca_map[5]['mu']["muTrigStatSF__1down"] =  0.805228
# muTrigSystSF__1up 
f_ca_map[2]['el']["muTrigSystSF__1up"] =  1.057503
f_ca_map[3]['el']["muTrigSystSF__1up"] =  1.034623
f_ca_map[4]['el']["muTrigSystSF__1up"] =  1.016558
f_ca_map[5]['el']["muTrigSystSF__1up"] =  0.781642
f_ca_map[2]['mu']["muTrigSystSF__1up"] =  1.135438
f_ca_map[3]['mu']["muTrigSystSF__1up"] =  1.047046
f_ca_map[4]['mu']["muTrigSystSF__1up"] =  0.943856
f_ca_map[5]['mu']["muTrigSystSF__1up"] =  0.793179
# muTrigSystSF__1down 
f_ca_map[2]['el']["muTrigSystSF__1down"] =  1.057503
f_ca_map[3]['el']["muTrigSystSF__1down"] =  1.034623
f_ca_map[4]['el']["muTrigSystSF__1down"] =  1.016558
f_ca_map[5]['el']["muTrigSystSF__1down"] =  0.781642
f_ca_map[2]['mu']["muTrigSystSF__1down"] =  1.157021
f_ca_map[3]['mu']["muTrigSystSF__1down"] =  1.067335
f_ca_map[4]['mu']["muTrigSystSF__1down"] =  0.962415
f_ca_map[5]['mu']["muTrigSystSF__1down"] =  0.808649
# muIDStatSF__1up 
f_ca_map[2]['el']["muIDStatSF__1up"] =  1.057503
f_ca_map[3]['el']["muIDStatSF__1up"] =  1.034623
f_ca_map[4]['el']["muIDStatSF__1up"] =  1.016558
f_ca_map[5]['el']["muIDStatSF__1up"] =  0.781642
f_ca_map[2]['mu']["muIDStatSF__1up"] =  1.144137
f_ca_map[3]['mu']["muIDStatSF__1up"] =  1.055238
f_ca_map[4]['mu']["muIDStatSF__1up"] =  0.951338
f_ca_map[5]['mu']["muIDStatSF__1up"] =  0.799409
# muIDStatSF__1down 
f_ca_map[2]['el']["muIDStatSF__1down"] =  1.057503
f_ca_map[3]['el']["muIDStatSF__1down"] =  1.034623
f_ca_map[4]['el']["muIDStatSF__1down"] =  1.016558
f_ca_map[5]['el']["muIDStatSF__1down"] =  0.781642
f_ca_map[2]['mu']["muIDStatSF__1down"] =  1.148344
f_ca_map[3]['mu']["muIDStatSF__1down"] =  1.059164
f_ca_map[4]['mu']["muIDStatSF__1down"] =  0.954951
f_ca_map[5]['mu']["muIDStatSF__1down"] =  0.802435
# muIDSystSF__1up 
f_ca_map[2]['el']["muIDSystSF__1up"] =  1.057503
f_ca_map[3]['el']["muIDSystSF__1up"] =  1.034623
f_ca_map[4]['el']["muIDSystSF__1up"] =  1.016558
f_ca_map[5]['el']["muIDSystSF__1up"] =  0.781642
f_ca_map[2]['mu']["muIDSystSF__1up"] =  1.138339
f_ca_map[3]['mu']["muIDSystSF__1up"] =  1.049731
f_ca_map[4]['mu']["muIDSystSF__1up"] =  0.946391
f_ca_map[5]['mu']["muIDSystSF__1up"] =  0.795108
# muIDSystSF__1down 
f_ca_map[2]['el']["muIDSystSF__1down"] =  1.057503
f_ca_map[3]['el']["muIDSystSF__1down"] =  1.034623
f_ca_map[4]['el']["muIDSystSF__1down"] =  1.016558
f_ca_map[5]['el']["muIDSystSF__1down"] =  0.781642
f_ca_map[2]['mu']["muIDSystSF__1down"] =  1.154231
f_ca_map[3]['mu']["muIDSystSF__1down"] =  1.064756
f_ca_map[4]['mu']["muIDSystSF__1down"] =  0.959973
f_ca_map[5]['mu']["muIDSystSF__1down"] =  0.806805
# muIsolStatSF__1up 
f_ca_map[2]['el']["muIsolStatSF__1up"] =  1.057503
f_ca_map[3]['el']["muIsolStatSF__1up"] =  1.034623
f_ca_map[4]['el']["muIsolStatSF__1up"] =  1.016558
f_ca_map[5]['el']["muIsolStatSF__1up"] =  0.781642
f_ca_map[2]['mu']["muIsolStatSF__1up"] =  1.145680
f_ca_map[3]['mu']["muIsolStatSF__1up"] =  1.056712
f_ca_map[4]['mu']["muIsolStatSF__1up"] =  0.952724
f_ca_map[5]['mu']["muIsolStatSF__1up"] =  0.800592
# muIsolStatSF__1down 
f_ca_map[2]['el']["muIsolStatSF__1down"] =  1.057503
f_ca_map[3]['el']["muIsolStatSF__1down"] =  1.034623
f_ca_map[4]['el']["muIsolStatSF__1down"] =  1.016558
f_ca_map[5]['el']["muIsolStatSF__1down"] =  0.781642
f_ca_map[2]['mu']["muIsolStatSF__1down"] =  1.146795
f_ca_map[3]['mu']["muIsolStatSF__1down"] =  1.057684
f_ca_map[4]['mu']["muIsolStatSF__1down"] =  0.953559
f_ca_map[5]['mu']["muIsolStatSF__1down"] =  0.801247
# muIsolSystSF__1up 
f_ca_map[2]['el']["muIsolSystSF__1up"] =  1.057503
f_ca_map[3]['el']["muIsolSystSF__1up"] =  1.034623
f_ca_map[4]['el']["muIsolSystSF__1up"] =  1.016558
f_ca_map[5]['el']["muIsolSystSF__1up"] =  0.781642
f_ca_map[2]['mu']["muIsolSystSF__1up"] =  1.145825
f_ca_map[3]['mu']["muIsolSystSF__1up"] =  1.056804
f_ca_map[4]['mu']["muIsolSystSF__1up"] =  0.952753
f_ca_map[5]['mu']["muIsolSystSF__1up"] =  0.800530
# muIsolSystSF__1down 
f_ca_map[2]['el']["muIsolSystSF__1down"] =  1.057503
f_ca_map[3]['el']["muIsolSystSF__1down"] =  1.034623
f_ca_map[4]['el']["muIsolSystSF__1down"] =  1.016558
f_ca_map[5]['el']["muIsolSystSF__1down"] =  0.781642
f_ca_map[2]['mu']["muIsolSystSF__1down"] =  1.146649
f_ca_map[3]['mu']["muIsolSystSF__1down"] =  1.057592
f_ca_map[4]['mu']["muIsolSystSF__1down"] =  0.953529
f_ca_map[5]['mu']["muIsolSystSF__1down"] =  0.801308

# ttNNLO_seq__1up 
flav_map[2]['el']["ttNNLO_seq__1up"] = {'bb': 1.284903, 'cc': 1.284903, 'c': 1.000000, 'l': 0.927120}
flav_map[3]['el']["ttNNLO_seq__1up"] = {'bb': 1.257833, 'cc': 1.257833, 'c': 0.978932, 'l': 0.907588}
flav_map[4]['el']["ttNNLO_seq__1up"] = {'bb': 1.231639, 'cc': 1.231639, 'c': 0.958547, 'l': 0.888688}
flav_map[5]['el']["ttNNLO_seq__1up"] = {'bb': 1.203088, 'cc': 1.203088, 'c': 0.936326, 'l': 0.868087}
flav_map[2]['mu']["ttNNLO_seq__1up"] = {'bb': 1.517724, 'cc': 1.517724, 'c': 1.000000, 'l': 0.881731}
flav_map[3]['mu']["ttNNLO_seq__1up"] = {'bb': 1.461615, 'cc': 1.461615, 'c': 0.963031, 'l': 0.849134}
flav_map[4]['mu']["ttNNLO_seq__1up"] = {'bb': 1.411295, 'cc': 1.411295, 'c': 0.929876, 'l': 0.819900}
flav_map[5]['mu']["ttNNLO_seq__1up"] = {'bb': 1.349754, 'cc': 1.349754, 'c': 0.889328, 'l': 0.784148}
# ttNNLO_topPt__1up 
flav_map[2]['el']["ttNNLO_topPt__1up"] = {'bb': 1.282509, 'cc': 1.282509, 'c': 1.000000, 'l': 0.927732}
flav_map[3]['el']["ttNNLO_topPt__1up"] = {'bb': 1.255712, 'cc': 1.255712, 'c': 0.979106, 'l': 0.908348}
flav_map[4]['el']["ttNNLO_topPt__1up"] = {'bb': 1.229773, 'cc': 1.229773, 'c': 0.958881, 'l': 0.889585}
flav_map[5]['el']["ttNNLO_topPt__1up"] = {'bb': 1.201489, 'cc': 1.201489, 'c': 0.936827, 'l': 0.869125}
flav_map[2]['mu']["ttNNLO_topPt__1up"] = {'bb': 1.517373, 'cc': 1.517373, 'c': 1.000000, 'l': 0.881811}
flav_map[3]['mu']["ttNNLO_topPt__1up"] = {'bb': 1.461314, 'cc': 1.461314, 'c': 0.963055, 'l': 0.849233}
flav_map[4]['mu']["ttNNLO_topPt__1up"] = {'bb': 1.411036, 'cc': 1.411036, 'c': 0.929920, 'l': 0.820013}
flav_map[5]['mu']["ttNNLO_topPt__1up"] = {'bb': 1.349544, 'cc': 1.349544, 'c': 0.889395, 'l': 0.784278}
# ttEWK__1up 
flav_map[2]['el']["ttEWK__1up"] = {'bb': 1.274765, 'cc': 1.274765, 'c': 1.000000, 'l': 0.929713}
flav_map[3]['el']["ttEWK__1up"] = {'bb': 1.248845, 'cc': 1.248845, 'c': 0.979667, 'l': 0.910809}
flav_map[4]['el']["ttEWK__1up"] = {'bb': 1.223727, 'cc': 1.223727, 'c': 0.959963, 'l': 0.892490}
flav_map[5]['el']["ttEWK__1up"] = {'bb': 1.196306, 'cc': 1.196306, 'c': 0.938453, 'l': 0.872492}
flav_map[2]['mu']["ttEWK__1up"] = {'bb': 1.511127, 'cc': 1.511127, 'c': 1.000000, 'l': 0.883237}
flav_map[3]['mu']["ttEWK__1up"] = {'bb': 1.455949, 'cc': 1.455949, 'c': 0.963485, 'l': 0.850986}
flav_map[4]['mu']["ttEWK__1up"] = {'bb': 1.406417, 'cc': 1.406417, 'c': 0.930707, 'l': 0.822036}
flav_map[5]['mu']["ttEWK__1up"] = {'bb': 1.345786, 'cc': 1.345786, 'c': 0.890584, 'l': 0.786597}
# ttEWK__1down 
flav_map[2]['el']["ttEWK__1down"] = {'bb': 1.274914, 'cc': 1.274914, 'c': 1.000000, 'l': 0.929676}
flav_map[3]['el']["ttEWK__1down"] = {'bb': 1.248977, 'cc': 1.248977, 'c': 0.979656, 'l': 0.910762}
flav_map[4]['el']["ttEWK__1down"] = {'bb': 1.223843, 'cc': 1.223843, 'c': 0.959942, 'l': 0.892435}
flav_map[5]['el']["ttEWK__1down"] = {'bb': 1.196406, 'cc': 1.196406, 'c': 0.938421, 'l': 0.872427}
flav_map[2]['mu']["ttEWK__1down"] = {'bb': 1.511208, 'cc': 1.511208, 'c': 1.000000, 'l': 0.883219}
flav_map[3]['mu']["ttEWK__1down"] = {'bb': 1.456018, 'cc': 1.456018, 'c': 0.963480, 'l': 0.850964}
flav_map[4]['mu']["ttEWK__1down"] = {'bb': 1.406477, 'cc': 1.406477, 'c': 0.930697, 'l': 0.822010}
flav_map[5]['mu']["ttEWK__1down"] = {'bb': 1.345834, 'cc': 1.345834, 'c': 0.890569, 'l': 0.786567}
# pileup__1up 
flav_map[2]['el']["pileup__1up"] = {'bb': 1.355318, 'cc': 1.355318, 'c': 1.000000, 'l': 0.909694}
flav_map[3]['el']["pileup__1up"] = {'bb': 1.319448, 'cc': 1.319448, 'c': 0.973533, 'l': 0.885618}
flav_map[4]['el']["pileup__1up"] = {'bb': 1.286428, 'cc': 1.286428, 'c': 0.949171, 'l': 0.863455}
flav_map[5]['el']["pileup__1up"] = {'bb': 1.249658, 'cc': 1.249658, 'c': 0.922041, 'l': 0.838775}
flav_map[2]['mu']["pileup__1up"] = {'bb': 1.679201, 'cc': 1.679201, 'c': 1.000000, 'l': 0.846245}
flav_map[3]['mu']["pileup__1up"] = {'bb': 1.600876, 'cc': 1.600876, 'c': 0.953356, 'l': 0.806772}
flav_map[4]['mu']["pileup__1up"] = {'bb': 1.529733, 'cc': 1.529733, 'c': 0.910989, 'l': 0.770919}
flav_map[5]['mu']["pileup__1up"] = {'bb': 1.444607, 'cc': 1.444607, 'c': 0.860294, 'l': 0.728019}
# pileup__1down 
flav_map[2]['el']["pileup__1down"] = {'bb': 1.235798, 'cc': 1.235798, 'c': 1.000000, 'l': 0.939343}
flav_map[3]['el']["pileup__1down"] = {'bb': 1.214324, 'cc': 1.214324, 'c': 0.982623, 'l': 0.923021}
flav_map[4]['el']["pileup__1down"] = {'bb': 1.192816, 'cc': 1.192816, 'c': 0.965219, 'l': 0.906672}
flav_map[5]['el']["pileup__1down"] = {'bb': 1.169938, 'cc': 1.169938, 'c': 0.946707, 'l': 0.889283}
flav_map[2]['mu']["pileup__1down"] = {'bb': 1.417693, 'cc': 1.417693, 'c': 1.000000, 'l': 0.903967}
flav_map[3]['mu']["pileup__1down"] = {'bb': 1.374419, 'cc': 1.374419, 'c': 0.969476, 'l': 0.876374}
flav_map[4]['mu']["pileup__1down"] = {'bb': 1.335480, 'cc': 1.335480, 'c': 0.942009, 'l': 0.851545}
flav_map[5]['mu']["pileup__1down"] = {'bb': 1.288462, 'cc': 1.288462, 'c': 0.908844, 'l': 0.821565}
# jvt__1up 
flav_map[2]['el']["jvt__1up"] = {'bb': 1.274923, 'cc': 1.274923, 'c': 1.000000, 'l': 0.929740}
flav_map[3]['el']["jvt__1up"] = {'bb': 1.248984, 'cc': 1.248984, 'c': 0.979654, 'l': 0.910824}
flav_map[4]['el']["jvt__1up"] = {'bb': 1.223859, 'cc': 1.223859, 'c': 0.959947, 'l': 0.892501}
flav_map[5]['el']["jvt__1up"] = {'bb': 1.196415, 'cc': 1.196415, 'c': 0.938421, 'l': 0.872488}
flav_map[2]['mu']["jvt__1up"] = {'bb': 1.513346, 'cc': 1.513346, 'c': 1.000000, 'l': 0.882814}
flav_map[3]['mu']["jvt__1up"] = {'bb': 1.457902, 'cc': 1.457902, 'c': 0.963364, 'l': 0.850471}
flav_map[4]['mu']["jvt__1up"] = {'bb': 1.408154, 'cc': 1.408154, 'c': 0.930491, 'l': 0.821450}
flav_map[5]['mu']["jvt__1up"] = {'bb': 1.347178, 'cc': 1.347178, 'c': 0.890199, 'l': 0.785880}
# jvt__1down 
flav_map[2]['el']["jvt__1down"] = {'bb': 1.274813, 'cc': 1.274813, 'c': 1.000000, 'l': 0.929641}
flav_map[3]['el']["jvt__1down"] = {'bb': 1.248887, 'cc': 1.248887, 'c': 0.979664, 'l': 0.910736}
flav_map[4]['el']["jvt__1down"] = {'bb': 1.223755, 'cc': 1.223755, 'c': 0.959949, 'l': 0.892408}
flav_map[5]['el']["jvt__1down"] = {'bb': 1.196336, 'cc': 1.196336, 'c': 0.938441, 'l': 0.872413}
flav_map[2]['mu']["jvt__1down"] = {'bb': 1.509224, 'cc': 1.509224, 'c': 1.000000, 'l': 0.883597}
flav_map[3]['mu']["jvt__1down"] = {'bb': 1.454269, 'cc': 1.454269, 'c': 0.963587, 'l': 0.851423}
flav_map[4]['mu']["jvt__1down"] = {'bb': 1.404920, 'cc': 1.404920, 'c': 0.930889, 'l': 0.822531}
flav_map[5]['mu']["jvt__1down"] = {'bb': 1.344586, 'cc': 1.344586, 'c': 0.890912, 'l': 0.787208}
# btagbSF_0__1up 
flav_map[2]['el']["btagbSF_0__1up"] = {'bb': 1.214251, 'cc': 1.214251, 'c': 1.000000, 'l': 0.944646}
flav_map[3]['el']["btagbSF_0__1up"] = {'bb': 1.194617, 'cc': 1.194617, 'c': 0.983831, 'l': 0.929372}
flav_map[4]['el']["btagbSF_0__1up"] = {'bb': 1.175477, 'cc': 1.175477, 'c': 0.968068, 'l': 0.914482}
flav_map[5]['el']["btagbSF_0__1up"] = {'bb': 1.154416, 'cc': 1.154416, 'c': 0.950723, 'l': 0.898097}
flav_map[2]['mu']["btagbSF_0__1up"] = {'bb': 1.439747, 'cc': 1.439747, 'c': 1.000000, 'l': 0.898612}
flav_map[3]['mu']["btagbSF_0__1up"] = {'bb': 1.393639, 'cc': 1.393639, 'c': 0.967975, 'l': 0.869834}
flav_map[4]['mu']["btagbSF_0__1up"] = {'bb': 1.351930, 'cc': 1.351930, 'c': 0.939005, 'l': 0.843801}
flav_map[5]['mu']["btagbSF_0__1up"] = {'bb': 1.300440, 'cc': 1.300440, 'c': 0.903242, 'l': 0.811664}
# btagbSF_0__1down 
flav_map[2]['el']["btagbSF_0__1down"] = {'bb': 1.338924, 'cc': 1.338924, 'c': 1.000000, 'l': 0.914157}
flav_map[3]['el']["btagbSF_0__1down"] = {'bb': 1.305996, 'cc': 1.305996, 'c': 0.975407, 'l': 0.891675}
flav_map[4]['el']["btagbSF_0__1down"] = {'bb': 1.274285, 'cc': 1.274285, 'c': 0.951723, 'l': 0.870025}
flav_map[5]['el']["btagbSF_0__1down"] = {'bb': 1.239946, 'cc': 1.239946, 'c': 0.926076, 'l': 0.846579}
flav_map[2]['mu']["btagbSF_0__1down"] = {'bb': 1.586788, 'cc': 1.586788, 'c': 1.000000, 'l': 0.867182}
flav_map[3]['mu']["btagbSF_0__1down"] = {'bb': 1.521542, 'cc': 1.521542, 'c': 0.958881, 'l': 0.831524}
flav_map[4]['mu']["btagbSF_0__1down"] = {'bb': 1.463436, 'cc': 1.463436, 'c': 0.922263, 'l': 0.799770}
flav_map[5]['mu']["btagbSF_0__1down"] = {'bb': 1.392919, 'cc': 1.392919, 'c': 0.877823, 'l': 0.761232}
# btagbSF_1__1up 
flav_map[2]['el']["btagbSF_1__1up"] = {'bb': 1.296551, 'cc': 1.296551, 'c': 1.000000, 'l': 0.924253}
flav_map[3]['el']["btagbSF_1__1up"] = {'bb': 1.268197, 'cc': 1.268197, 'c': 0.978131, 'l': 0.904040}
flav_map[4]['el']["btagbSF_1__1up"] = {'bb': 1.240792, 'cc': 1.240792, 'c': 0.956995, 'l': 0.884505}
flav_map[5]['el']["btagbSF_1__1up"] = {'bb': 1.210953, 'cc': 1.210953, 'c': 0.933981, 'l': 0.863234}
flav_map[2]['mu']["btagbSF_1__1up"] = {'bb': 1.534182, 'cc': 1.534182, 'c': 1.000000, 'l': 0.878139}
flav_map[3]['mu']["btagbSF_1__1up"] = {'bb': 1.475839, 'cc': 1.475839, 'c': 0.961971, 'l': 0.844744}
flav_map[4]['mu']["btagbSF_1__1up"] = {'bb': 1.423601, 'cc': 1.423601, 'c': 0.927922, 'l': 0.814844}
flav_map[5]['mu']["btagbSF_1__1up"] = {'bb': 1.359829, 'cc': 1.359829, 'c': 0.886355, 'l': 0.778342}
# btagbSF_1__1down 
flav_map[2]['el']["btagbSF_1__1down"] = {'bb': 1.253572, 'cc': 1.253572, 'c': 1.000000, 'l': 0.935040}
flav_map[3]['el']["btagbSF_1__1down"] = {'bb': 1.229967, 'cc': 1.229967, 'c': 0.981169, 'l': 0.917433}
flav_map[4]['el']["btagbSF_1__1down"] = {'bb': 1.207034, 'cc': 1.207034, 'c': 0.962875, 'l': 0.900327}
flav_map[5]['el']["btagbSF_1__1down"] = {'bb': 1.181935, 'cc': 1.181935, 'c': 0.942853, 'l': 0.881606}
flav_map[2]['mu']["btagbSF_1__1down"] = {'bb': 1.488624, 'cc': 1.488624, 'c': 1.000000, 'l': 0.888225}
flav_map[3]['mu']["btagbSF_1__1down"] = {'bb': 1.436479, 'cc': 1.436479, 'c': 0.964971, 'l': 0.857112}
flav_map[4]['mu']["btagbSF_1__1down"] = {'bb': 1.389554, 'cc': 1.389554, 'c': 0.933449, 'l': 0.829113}
flav_map[5]['mu']["btagbSF_1__1down"] = {'bb': 1.331961, 'cc': 1.331961, 'c': 0.894760, 'l': 0.794748}
# btagbSF_2__1up 
flav_map[2]['el']["btagbSF_2__1up"] = {'bb': 1.269478, 'cc': 1.269478, 'c': 1.000000, 'l': 0.931075}
flav_map[3]['el']["btagbSF_2__1up"] = {'bb': 1.244160, 'cc': 1.244160, 'c': 0.980057, 'l': 0.912506}
flav_map[4]['el']["btagbSF_2__1up"] = {'bb': 1.219607, 'cc': 1.219607, 'c': 0.960715, 'l': 0.894498}
flav_map[5]['el']["btagbSF_2__1up"] = {'bb': 1.192783, 'cc': 1.192783, 'c': 0.939585, 'l': 0.874824}
flav_map[2]['mu']["btagbSF_2__1up"] = {'bb': 1.506450, 'cc': 1.506450, 'c': 1.000000, 'l': 0.884317}
flav_map[3]['mu']["btagbSF_2__1up"] = {'bb': 1.451942, 'cc': 1.451942, 'c': 0.963817, 'l': 0.852320}
flav_map[4]['mu']["btagbSF_2__1up"] = {'bb': 1.402984, 'cc': 1.402984, 'c': 0.931318, 'l': 0.823581}
flav_map[5]['mu']["btagbSF_2__1up"] = {'bb': 1.343015, 'cc': 1.343015, 'c': 0.891510, 'l': 0.788378}
# btagbSF_2__1down 
flav_map[2]['el']["btagbSF_2__1down"] = {'bb': 1.280235, 'cc': 1.280235, 'c': 1.000000, 'l': 0.928307}
flav_map[3]['el']["btagbSF_2__1down"] = {'bb': 1.253687, 'cc': 1.253687, 'c': 0.979263, 'l': 0.909057}
flav_map[4]['el']["btagbSF_2__1down"] = {'bb': 1.227981, 'cc': 1.227981, 'c': 0.959184, 'l': 0.890417}
flav_map[5]['el']["btagbSF_2__1down"] = {'bb': 1.199942, 'cc': 1.199942, 'c': 0.937282, 'l': 0.870086}
flav_map[2]['mu']["btagbSF_2__1down"] = {'bb': 1.515912, 'cc': 1.515912, 'c': 1.000000, 'l': 0.882133}
flav_map[3]['mu']["btagbSF_2__1down"] = {'bb': 1.460044, 'cc': 1.460044, 'c': 0.963146, 'l': 0.849623}
flav_map[4]['mu']["btagbSF_2__1down"] = {'bb': 1.409925, 'cc': 1.409925, 'c': 0.930083, 'l': 0.820457}
flav_map[5]['mu']["btagbSF_2__1down"] = {'bb': 1.348614, 'cc': 1.348614, 'c': 0.889639, 'l': 0.784780}
# btagbSF_3__1up 
flav_map[2]['el']["btagbSF_3__1up"] = {'bb': 1.271942, 'cc': 1.271942, 'c': 1.000000, 'l': 0.930422}
flav_map[3]['el']["btagbSF_3__1up"] = {'bb': 1.246329, 'cc': 1.246329, 'c': 0.979863, 'l': 0.911686}
flav_map[4]['el']["btagbSF_3__1up"] = {'bb': 1.221500, 'cc': 1.221500, 'c': 0.960342, 'l': 0.893524}
flav_map[5]['el']["btagbSF_3__1up"] = {'bb': 1.194385, 'cc': 1.194385, 'c': 0.939025, 'l': 0.873690}
flav_map[2]['mu']["btagbSF_3__1up"] = {'bb': 1.507982, 'cc': 1.507982, 'c': 1.000000, 'l': 0.883934}
flav_map[3]['mu']["btagbSF_3__1up"] = {'bb': 1.453224, 'cc': 1.453224, 'c': 0.963688, 'l': 0.851836}
flav_map[4]['mu']["btagbSF_3__1up"] = {'bb': 1.404052, 'cc': 1.404052, 'c': 0.931080, 'l': 0.823013}
flav_map[5]['mu']["btagbSF_3__1up"] = {'bb': 1.343836, 'cc': 1.343836, 'c': 0.891148, 'l': 0.787716}
# btagbSF_3__1down 
flav_map[2]['el']["btagbSF_3__1down"] = {'bb': 1.277750, 'cc': 1.277750, 'c': 1.000000, 'l': 0.928965}
flav_map[3]['el']["btagbSF_3__1down"] = {'bb': 1.251503, 'cc': 1.251503, 'c': 0.979459, 'l': 0.909882}
flav_map[4]['el']["btagbSF_3__1down"] = {'bb': 1.226079, 'cc': 1.226079, 'c': 0.959561, 'l': 0.891398}
flav_map[5]['el']["btagbSF_3__1down"] = {'bb': 1.198334, 'cc': 1.198334, 'c': 0.937847, 'l': 0.871226}
flav_map[2]['mu']["btagbSF_3__1down"] = {'bb': 1.514357, 'cc': 1.514357, 'c': 1.000000, 'l': 0.882522}
flav_map[3]['mu']["btagbSF_3__1down"] = {'bb': 1.458745, 'cc': 1.458745, 'c': 0.963277, 'l': 0.850113}
flav_map[4]['mu']["btagbSF_3__1down"] = {'bb': 1.408843, 'cc': 1.408843, 'c': 0.930324, 'l': 0.821032}
flav_map[5]['mu']["btagbSF_3__1down"] = {'bb': 1.347785, 'cc': 1.347785, 'c': 0.890005, 'l': 0.785449}
# btagbSF_0_pt1__1up 
flav_map[2]['el']["btagbSF_0_pt1__1up"] = {'bb': 1.208414, 'cc': 1.208414, 'c': 1.000000, 'l': 0.946159}
flav_map[3]['el']["btagbSF_0_pt1__1up"] = {'bb': 1.189404, 'cc': 1.189404, 'c': 0.984268, 'l': 0.931274}
flav_map[4]['el']["btagbSF_0_pt1__1up"] = {'bb': 1.170855, 'cc': 1.170855, 'c': 0.968918, 'l': 0.916751}
flav_map[5]['el']["btagbSF_0_pt1__1up"] = {'bb': 1.150433, 'cc': 1.150433, 'c': 0.952019, 'l': 0.900761}
flav_map[2]['mu']["btagbSF_0_pt1__1up"] = {'bb': 1.434390, 'cc': 1.434390, 'c': 1.000000, 'l': 0.899854}
flav_map[3]['mu']["btagbSF_0_pt1__1up"] = {'bb': 1.389005, 'cc': 1.389005, 'c': 0.968359, 'l': 0.871382}
flav_map[4]['mu']["btagbSF_0_pt1__1up"] = {'bb': 1.347922, 'cc': 1.347922, 'c': 0.939718, 'l': 0.845609}
flav_map[5]['mu']["btagbSF_0_pt1__1up"] = {'bb': 1.297177, 'cc': 1.297177, 'c': 0.904340, 'l': 0.813774}
# btagbSF_0_pt1__1down 
flav_map[2]['el']["btagbSF_0_pt1__1down"] = {'bb': 1.345364, 'cc': 1.345364, 'c': 1.000000, 'l': 0.912519}
flav_map[3]['el']["btagbSF_0_pt1__1down"] = {'bb': 1.311656, 'cc': 1.311656, 'c': 0.974945, 'l': 0.889656}
flav_map[4]['el']["btagbSF_0_pt1__1down"] = {'bb': 1.279224, 'cc': 1.279224, 'c': 0.950839, 'l': 0.867658}
flav_map[5]['el']["btagbSF_0_pt1__1down"] = {'bb': 1.244125, 'cc': 1.244125, 'c': 0.924750, 'l': 0.843852}
flav_map[2]['mu']["btagbSF_0_pt1__1down"] = {'bb': 1.592818, 'cc': 1.592818, 'c': 1.000000, 'l': 0.865808}
flav_map[3]['mu']["btagbSF_0_pt1__1down"] = {'bb': 1.526665, 'cc': 1.526665, 'c': 0.958468, 'l': 0.829849}
flav_map[4]['mu']["btagbSF_0_pt1__1down"] = {'bb': 1.467795, 'cc': 1.467795, 'c': 0.921508, 'l': 0.797849}
flav_map[5]['mu']["btagbSF_0_pt1__1down"] = {'bb': 1.396395, 'cc': 1.396395, 'c': 0.876682, 'l': 0.759039}
# btagbSF_0_pt2__1up 
flav_map[2]['el']["btagbSF_0_pt2__1up"] = {'bb': 1.279205, 'cc': 1.279205, 'c': 1.000000, 'l': 0.928575}
flav_map[3]['el']["btagbSF_0_pt2__1up"] = {'bb': 1.252780, 'cc': 1.252780, 'c': 0.979342, 'l': 0.909392}
flav_map[4]['el']["btagbSF_0_pt2__1up"] = {'bb': 1.227190, 'cc': 1.227190, 'c': 0.959338, 'l': 0.890817}
flav_map[5]['el']["btagbSF_0_pt2__1up"] = {'bb': 1.199267, 'cc': 1.199267, 'c': 0.937510, 'l': 0.870548}
flav_map[2]['mu']["btagbSF_0_pt2__1up"] = {'bb': 1.515230, 'cc': 1.515230, 'c': 1.000000, 'l': 0.882295}
flav_map[3]['mu']["btagbSF_0_pt2__1up"] = {'bb': 1.459468, 'cc': 1.459468, 'c': 0.963199, 'l': 0.849826}
flav_map[4]['mu']["btagbSF_0_pt2__1up"] = {'bb': 1.409441, 'cc': 1.409441, 'c': 0.930183, 'l': 0.820696}
flav_map[5]['mu']["btagbSF_0_pt2__1up"] = {'bb': 1.348232, 'cc': 1.348232, 'c': 0.889787, 'l': 0.785055}
# btagbSF_0_pt2__1down 
flav_map[2]['el']["btagbSF_0_pt2__1down"] = {'bb': 1.270491, 'cc': 1.270491, 'c': 1.000000, 'l': 0.930811}
flav_map[3]['el']["btagbSF_0_pt2__1down"] = {'bb': 1.245054, 'cc': 1.245054, 'c': 0.979979, 'l': 0.912175}
flav_map[4]['el']["btagbSF_0_pt2__1down"] = {'bb': 1.220388, 'cc': 1.220388, 'c': 0.960564, 'l': 0.894104}
flav_map[5]['el']["btagbSF_0_pt2__1down"] = {'bb': 1.193450, 'cc': 1.193450, 'c': 0.939362, 'l': 0.874368}
flav_map[2]['mu']["btagbSF_0_pt2__1down"] = {'bb': 1.507120, 'cc': 1.507120, 'c': 1.000000, 'l': 0.884157}
flav_map[3]['mu']["btagbSF_0_pt2__1down"] = {'bb': 1.452510, 'cc': 1.452510, 'c': 0.963765, 'l': 0.852120}
flav_map[4]['mu']["btagbSF_0_pt2__1down"] = {'bb': 1.403462, 'cc': 1.403462, 'c': 0.931221, 'l': 0.823345}
flav_map[5]['mu']["btagbSF_0_pt2__1down"] = {'bb': 1.343393, 'cc': 1.343393, 'c': 0.891364, 'l': 0.788106}
# btagbSF_0_pt3__1up 
flav_map[2]['el']["btagbSF_0_pt3__1up"] = {'bb': 1.276611, 'cc': 1.276611, 'c': 1.000000, 'l': 0.929239}
flav_map[3]['el']["btagbSF_0_pt3__1up"] = {'bb': 1.250480, 'cc': 1.250480, 'c': 0.979531, 'l': 0.910218}
flav_map[4]['el']["btagbSF_0_pt3__1up"] = {'bb': 1.225161, 'cc': 1.225161, 'c': 0.959698, 'l': 0.891789}
flav_map[5]['el']["btagbSF_0_pt3__1up"] = {'bb': 1.197527, 'cc': 1.197527, 'c': 0.938052, 'l': 0.871674}
flav_map[2]['mu']["btagbSF_0_pt3__1up"] = {'bb': 1.512793, 'cc': 1.512793, 'c': 1.000000, 'l': 0.882854}
flav_map[3]['mu']["btagbSF_0_pt3__1up"] = {'bb': 1.457375, 'cc': 1.457375, 'c': 0.963367, 'l': 0.850512}
flav_map[4]['mu']["btagbSF_0_pt3__1up"] = {'bb': 1.407635, 'cc': 1.407635, 'c': 0.930488, 'l': 0.821485}
flav_map[5]['mu']["btagbSF_0_pt3__1up"] = {'bb': 1.346758, 'cc': 1.346758, 'c': 0.890246, 'l': 0.785957}
# btagbSF_0_pt3__1down 
flav_map[2]['el']["btagbSF_0_pt3__1down"] = {'bb': 1.273081, 'cc': 1.273081, 'c': 1.000000, 'l': 0.930147}
flav_map[3]['el']["btagbSF_0_pt3__1down"] = {'bb': 1.247353, 'cc': 1.247353, 'c': 0.979791, 'l': 0.911350}
flav_map[4]['el']["btagbSF_0_pt3__1down"] = {'bb': 1.222418, 'cc': 1.222418, 'c': 0.960204, 'l': 0.893131}
flav_map[5]['el']["btagbSF_0_pt3__1down"] = {'bb': 1.195193, 'cc': 1.195193, 'c': 0.938819, 'l': 0.873240}
flav_map[2]['mu']["btagbSF_0_pt3__1down"] = {'bb': 1.509550, 'cc': 1.509550, 'c': 1.000000, 'l': 0.883602}
flav_map[3]['mu']["btagbSF_0_pt3__1down"] = {'bb': 1.454597, 'cc': 1.454597, 'c': 0.963596, 'l': 0.851436}
flav_map[4]['mu']["btagbSF_0_pt3__1down"] = {'bb': 1.405263, 'cc': 1.405263, 'c': 0.930915, 'l': 0.822559}
flav_map[5]['mu']["btagbSF_0_pt3__1down"] = {'bb': 1.344865, 'cc': 1.344865, 'c': 0.890905, 'l': 0.787205}
# btagcSF_0__1up 
flav_map[2]['el']["btagcSF_0__1up"] = {'bb': 1.249151, 'cc': 1.249151, 'c': 1.000000, 'l': 0.935493}
flav_map[3]['el']["btagcSF_0__1up"] = {'bb': 1.225739, 'cc': 1.225739, 'c': 0.981258, 'l': 0.917960}
flav_map[4]['el']["btagcSF_0__1up"] = {'bb': 1.203101, 'cc': 1.203101, 'c': 0.963134, 'l': 0.901006}
flav_map[5]['el']["btagcSF_0__1up"] = {'bb': 1.178214, 'cc': 1.178214, 'c': 0.943211, 'l': 0.882368}
flav_map[2]['mu']["btagcSF_0__1up"] = {'bb': 1.544569, 'cc': 1.544569, 'c': 1.000000, 'l': 0.874055}
flav_map[3]['mu']["btagcSF_0__1up"] = {'bb': 1.483718, 'cc': 1.483718, 'c': 0.960603, 'l': 0.839620}
flav_map[4]['mu']["btagcSF_0__1up"] = {'bb': 1.429673, 'cc': 1.429673, 'c': 0.925613, 'l': 0.809037}
flav_map[5]['mu']["btagcSF_0__1up"] = {'bb': 1.363900, 'cc': 1.363900, 'c': 0.883030, 'l': 0.771817}
# btagcSF_0__1down 
flav_map[2]['el']["btagcSF_0__1down"] = {'bb': 1.300924, 'cc': 1.300924, 'c': 1.000000, 'l': 0.923944}
flav_map[3]['el']["btagcSF_0__1down"] = {'bb': 1.272422, 'cc': 1.272422, 'c': 0.978091, 'l': 0.903701}
flav_map[4]['el']["btagcSF_0__1down"] = {'bb': 1.244735, 'cc': 1.244735, 'c': 0.956808, 'l': 0.884037}
flav_map[5]['el']["btagcSF_0__1down"] = {'bb': 1.214740, 'cc': 1.214740, 'c': 0.933751, 'l': 0.862734}
flav_map[2]['mu']["btagcSF_0__1down"] = {'bb': 1.482008, 'cc': 1.482008, 'c': 1.000000, 'l': 0.891237}
flav_map[3]['mu']["btagcSF_0__1down"] = {'bb': 1.431635, 'cc': 1.431635, 'c': 0.966011, 'l': 0.860945}
flav_map[4]['mu']["btagcSF_0__1down"] = {'bb': 1.385959, 'cc': 1.385959, 'c': 0.935190, 'l': 0.833476}
flav_map[5]['mu']["btagcSF_0__1down"] = {'bb': 1.329749, 'cc': 1.329749, 'c': 0.897261, 'l': 0.799673}
# btagcSF_1__1up 
flav_map[2]['el']["btagcSF_1__1up"] = {'bb': 1.284307, 'cc': 1.284307, 'c': 1.000000, 'l': 0.927548}
flav_map[3]['el']["btagcSF_1__1up"] = {'bb': 1.257448, 'cc': 1.257448, 'c': 0.979087, 'l': 0.908150}
flav_map[4]['el']["btagcSF_1__1up"] = {'bb': 1.231454, 'cc': 1.231454, 'c': 0.958846, 'l': 0.889376}
flav_map[5]['el']["btagcSF_1__1up"] = {'bb': 1.203092, 'cc': 1.203092, 'c': 0.936763, 'l': 0.868893}
flav_map[2]['mu']["btagcSF_1__1up"] = {'bb': 1.532286, 'cc': 1.532286, 'c': 1.000000, 'l': 0.878870}
flav_map[3]['mu']["btagcSF_1__1up"] = {'bb': 1.474410, 'cc': 1.474410, 'c': 0.962229, 'l': 0.845675}
flav_map[4]['mu']["btagcSF_1__1up"] = {'bb': 1.422554, 'cc': 1.422554, 'c': 0.928387, 'l': 0.815932}
flav_map[5]['mu']["btagcSF_1__1up"] = {'bb': 1.359275, 'cc': 1.359275, 'c': 0.887090, 'l': 0.779637}
# btagcSF_1__1down 
flav_map[2]['el']["btagcSF_1__1down"] = {'bb': 1.265566, 'cc': 1.265566, 'c': 1.000000, 'l': 0.931808}
flav_map[3]['el']["btagcSF_1__1down"] = {'bb': 1.240545, 'cc': 1.240545, 'c': 0.980230, 'l': 0.913386}
flav_map[4]['el']["btagcSF_1__1down"] = {'bb': 1.216269, 'cc': 1.216269, 'c': 0.961048, 'l': 0.895512}
flav_map[5]['el']["btagcSF_1__1down"] = {'bb': 1.189754, 'cc': 1.189754, 'c': 0.940096, 'l': 0.875990}
flav_map[2]['mu']["btagcSF_1__1down"] = {'bb': 1.490467, 'cc': 1.490467, 'c': 1.000000, 'l': 0.887526}
flav_map[3]['mu']["btagcSF_1__1down"] = {'bb': 1.437892, 'cc': 1.437892, 'c': 0.964725, 'l': 0.856219}
flav_map[4]['mu']["btagcSF_1__1down"] = {'bb': 1.390611, 'cc': 1.390611, 'c': 0.933004, 'l': 0.828065}
flav_map[5]['mu']["btagcSF_1__1down"] = {'bb': 1.332556, 'cc': 1.332556, 'c': 0.894053, 'l': 0.793495}
# btagcSF_2__1up 
flav_map[2]['el']["btagcSF_2__1up"] = {'bb': 1.280457, 'cc': 1.280457, 'c': 1.000000, 'l': 0.928235}
flav_map[3]['el']["btagcSF_2__1up"] = {'bb': 1.253884, 'cc': 1.253884, 'c': 0.979248, 'l': 0.908972}
flav_map[4]['el']["btagcSF_2__1up"] = {'bb': 1.228163, 'cc': 1.228163, 'c': 0.959160, 'l': 0.890326}
flav_map[5]['el']["btagcSF_2__1up"] = {'bb': 1.200117, 'cc': 1.200117, 'c': 0.937257, 'l': 0.869995}
flav_map[2]['mu']["btagcSF_2__1up"] = {'bb': 1.511206, 'cc': 1.511206, 'c': 1.000000, 'l': 0.883182}
flav_map[3]['mu']["btagcSF_2__1up"] = {'bb': 1.456017, 'cc': 1.456017, 'c': 0.963480, 'l': 0.850929}
flav_map[4]['mu']["btagcSF_2__1up"] = {'bb': 1.406475, 'cc': 1.406475, 'c': 0.930697, 'l': 0.821975}
flav_map[5]['mu']["btagcSF_2__1up"] = {'bb': 1.345834, 'cc': 1.345834, 'c': 0.890570, 'l': 0.786536}
# btagcSF_2__1down 
flav_map[2]['el']["btagcSF_2__1down"] = {'bb': 1.269157, 'cc': 1.269157, 'c': 1.000000, 'l': 0.931170}
flav_map[3]['el']["btagcSF_2__1down"] = {'bb': 1.243875, 'cc': 1.243875, 'c': 0.980080, 'l': 0.912620}
flav_map[4]['el']["btagcSF_2__1down"] = {'bb': 1.219349, 'cc': 1.219349, 'c': 0.960755, 'l': 0.894625}
flav_map[5]['el']["btagcSF_2__1down"] = {'bb': 1.192542, 'cc': 1.192542, 'c': 0.939633, 'l': 0.874958}
flav_map[2]['mu']["btagcSF_2__1down"] = {'bb': 1.510935, 'cc': 1.510935, 'c': 1.000000, 'l': 0.883318}
flav_map[3]['mu']["btagcSF_2__1down"] = {'bb': 1.455782, 'cc': 1.455782, 'c': 0.963498, 'l': 0.851075}
flav_map[4]['mu']["btagcSF_2__1down"] = {'bb': 1.406275, 'cc': 1.406275, 'c': 0.930732, 'l': 0.822133}
flav_map[5]['mu']["btagcSF_2__1down"] = {'bb': 1.345669, 'cc': 1.345669, 'c': 0.890620, 'l': 0.786701}
# btagcSF_3__1up 
flav_map[2]['el']["btagcSF_3__1up"] = {'bb': 1.277878, 'cc': 1.277878, 'c': 1.000000, 'l': 0.928845}
flav_map[3]['el']["btagcSF_3__1up"] = {'bb': 1.251569, 'cc': 1.251569, 'c': 0.979412, 'l': 0.909722}
flav_map[4]['el']["btagcSF_3__1up"] = {'bb': 1.226085, 'cc': 1.226085, 'c': 0.959469, 'l': 0.891198}
flav_map[5]['el']["btagcSF_3__1up"] = {'bb': 1.198282, 'cc': 1.198282, 'c': 0.937713, 'l': 0.870990}
flav_map[2]['mu']["btagcSF_3__1up"] = {'bb': 1.508163, 'cc': 1.508163, 'c': 1.000000, 'l': 0.883800}
flav_map[3]['mu']["btagcSF_3__1up"] = {'bb': 1.453321, 'cc': 1.453321, 'c': 0.963636, 'l': 0.851661}
flav_map[4]['mu']["btagcSF_3__1up"] = {'bb': 1.404087, 'cc': 1.404087, 'c': 0.930991, 'l': 0.822809}
flav_map[5]['mu']["btagcSF_3__1up"] = {'bb': 1.343820, 'cc': 1.343820, 'c': 0.891031, 'l': 0.787493}
# btagcSF_3__1down 
flav_map[2]['el']["btagcSF_3__1down"] = {'bb': 1.271809, 'cc': 1.271809, 'c': 1.000000, 'l': 0.930541}
flav_map[3]['el']["btagcSF_3__1down"] = {'bb': 1.246257, 'cc': 1.246257, 'c': 0.979909, 'l': 0.911845}
flav_map[4]['el']["btagcSF_3__1down"] = {'bb': 1.221487, 'cc': 1.221487, 'c': 0.960433, 'l': 0.893722}
flav_map[5]['el']["btagcSF_3__1down"] = {'bb': 1.194430, 'cc': 1.194430, 'c': 0.939158, 'l': 0.873925}
flav_map[2]['mu']["btagcSF_3__1down"] = {'bb': 1.514150, 'cc': 1.514150, 'c': 1.000000, 'l': 0.882663}
flav_map[3]['mu']["btagcSF_3__1down"] = {'bb': 1.458627, 'cc': 1.458627, 'c': 0.963331, 'l': 0.850297}
flav_map[4]['mu']["btagcSF_3__1down"] = {'bb': 1.408791, 'cc': 1.408791, 'c': 0.930417, 'l': 0.821245}
flav_map[5]['mu']["btagcSF_3__1down"] = {'bb': 1.347787, 'cc': 1.347787, 'c': 0.890128, 'l': 0.785683}
# btagcSF_0_pt1__1up 
flav_map[2]['el']["btagcSF_0_pt1__1up"] = {'bb': 1.254673, 'cc': 1.254673, 'c': 1.000000, 'l': 0.934009}
flav_map[3]['el']["btagcSF_0_pt1__1up"] = {'bb': 1.230613, 'cc': 1.230613, 'c': 0.980823, 'l': 0.916098}
flav_map[4]['el']["btagcSF_0_pt1__1up"] = {'bb': 1.207314, 'cc': 1.207314, 'c': 0.962254, 'l': 0.898754}
flav_map[5]['el']["btagcSF_0_pt1__1up"] = {'bb': 1.181775, 'cc': 1.181775, 'c': 0.941899, 'l': 0.879742}
flav_map[2]['mu']["btagcSF_0_pt1__1up"] = {'bb': 1.517152, 'cc': 1.517152, 'c': 1.000000, 'l': 0.880328}
flav_map[3]['mu']["btagcSF_0_pt1__1up"] = {'bb': 1.460172, 'cc': 1.460172, 'c': 0.962443, 'l': 0.847265}
flav_map[4]['mu']["btagcSF_0_pt1__1up"] = {'bb': 1.409368, 'cc': 1.409368, 'c': 0.928956, 'l': 0.817786}
flav_map[5]['mu']["btagcSF_0_pt1__1up"] = {'bb': 1.347249, 'cc': 1.347249, 'c': 0.888012, 'l': 0.781742}
# btagcSF_0_pt1__1down 
flav_map[2]['el']["btagcSF_0_pt1__1down"] = {'bb': 1.294952, 'cc': 1.294952, 'c': 1.000000, 'l': 0.925514}
flav_map[3]['el']["btagcSF_0_pt1__1down"] = {'bb': 1.267174, 'cc': 1.267174, 'c': 0.978548, 'l': 0.905660}
flav_map[4]['el']["btagcSF_0_pt1__1down"] = {'bb': 1.240233, 'cc': 1.240233, 'c': 0.957744, 'l': 0.886406}
flav_map[5]['el']["btagcSF_0_pt1__1down"] = {'bb': 1.210950, 'cc': 1.210950, 'c': 0.935131, 'l': 0.865477}
flav_map[2]['mu']["btagcSF_0_pt1__1down"] = {'bb': 1.505803, 'cc': 1.505803, 'c': 1.000000, 'l': 0.885935}
flav_map[3]['mu']["btagcSF_0_pt1__1down"] = {'bb': 1.452286, 'cc': 1.452286, 'c': 0.964459, 'l': 0.854448}
flav_map[4]['mu']["btagcSF_0_pt1__1down"] = {'bb': 1.403928, 'cc': 1.403928, 'c': 0.932345, 'l': 0.825997}
flav_map[5]['mu']["btagcSF_0_pt1__1down"] = {'bb': 1.344653, 'cc': 1.344653, 'c': 0.892980, 'l': 0.791123}
# btagcSF_0_pt2__1up 
flav_map[2]['el']["btagcSF_0_pt2__1up"] = {'bb': 1.263203, 'cc': 1.263203, 'c': 1.000000, 'l': 0.932721}
flav_map[3]['el']["btagcSF_0_pt2__1up"] = {'bb': 1.238606, 'cc': 1.238606, 'c': 0.980529, 'l': 0.914560}
flav_map[4]['el']["btagcSF_0_pt2__1up"] = {'bb': 1.214773, 'cc': 1.214773, 'c': 0.961661, 'l': 0.896961}
flav_map[5]['el']["btagcSF_0_pt2__1up"] = {'bb': 1.188662, 'cc': 1.188662, 'c': 0.940991, 'l': 0.877682}
flav_map[2]['mu']["btagcSF_0_pt2__1up"] = {'bb': 1.525501, 'cc': 1.525501, 'c': 1.000000, 'l': 0.880010}
flav_map[3]['mu']["btagcSF_0_pt2__1up"] = {'bb': 1.468375, 'cc': 1.468375, 'c': 0.962552, 'l': 0.847056}
flav_map[4]['mu']["btagcSF_0_pt2__1up"] = {'bb': 1.417192, 'cc': 1.417192, 'c': 0.929001, 'l': 0.817530}
flav_map[5]['mu']["btagcSF_0_pt2__1up"] = {'bb': 1.354710, 'cc': 1.354710, 'c': 0.888043, 'l': 0.781486}
# btagcSF_0_pt2__1down 
flav_map[2]['el']["btagcSF_0_pt2__1down"] = {'bb': 1.286777, 'cc': 1.286777, 'c': 1.000000, 'l': 0.926587}
flav_map[3]['el']["btagcSF_0_pt2__1down"] = {'bb': 1.259462, 'cc': 1.259462, 'c': 0.978772, 'l': 0.906917}
flav_map[4]['el']["btagcSF_0_pt2__1down"] = {'bb': 1.232989, 'cc': 1.232989, 'c': 0.958199, 'l': 0.887855}
flav_map[5]['el']["btagcSF_0_pt2__1down"] = {'bb': 1.204200, 'cc': 1.204200, 'c': 0.935826, 'l': 0.867124}
flav_map[2]['mu']["btagcSF_0_pt2__1down"] = {'bb': 1.497364, 'cc': 1.497364, 'c': 1.000000, 'l': 0.886329}
flav_map[3]['mu']["btagcSF_0_pt2__1down"] = {'bb': 1.444029, 'cc': 1.444029, 'c': 0.964380, 'l': 0.854758}
flav_map[4]['mu']["btagcSF_0_pt2__1down"] = {'bb': 1.396063, 'cc': 1.396063, 'c': 0.932347, 'l': 0.826366}
flav_map[5]['mu']["btagcSF_0_pt2__1down"] = {'bb': 1.337199, 'cc': 1.337199, 'c': 0.893035, 'l': 0.791523}
# btagcSF_0_pt3__1up 
flav_map[2]['el']["btagcSF_0_pt3__1up"] = {'bb': 1.280993, 'cc': 1.280993, 'c': 1.000000, 'l': 0.928126}
flav_map[3]['el']["btagcSF_0_pt3__1up"] = {'bb': 1.254376, 'cc': 1.254376, 'c': 0.979222, 'l': 0.908841}
flav_map[4]['el']["btagcSF_0_pt3__1up"] = {'bb': 1.228619, 'cc': 1.228619, 'c': 0.959115, 'l': 0.890180}
flav_map[5]['el']["btagcSF_0_pt3__1up"] = {'bb': 1.200520, 'cc': 1.200520, 'c': 0.937180, 'l': 0.869821}
flav_map[2]['mu']["btagcSF_0_pt3__1up"] = {'bb': 1.522596, 'cc': 1.522596, 'c': 1.000000, 'l': 0.880631}
flav_map[3]['mu']["btagcSF_0_pt3__1up"] = {'bb': 1.465820, 'cc': 1.465820, 'c': 0.962711, 'l': 0.847793}
flav_map[4]['mu']["btagcSF_0_pt3__1up"] = {'bb': 1.414947, 'cc': 1.414947, 'c': 0.929299, 'l': 0.818369}
flav_map[5]['mu']["btagcSF_0_pt3__1up"] = {'bb': 1.352776, 'cc': 1.352776, 'c': 0.888467, 'l': 0.782411}
# btagcSF_0_pt3__1down 
flav_map[2]['el']["btagcSF_0_pt3__1down"] = {'bb': 1.268944, 'cc': 1.268944, 'c': 1.000000, 'l': 0.931197}
flav_map[3]['el']["btagcSF_0_pt3__1down"] = {'bb': 1.243670, 'cc': 1.243670, 'c': 0.980083, 'l': 0.912650}
flav_map[4]['el']["btagcSF_0_pt3__1down"] = {'bb': 1.219145, 'cc': 1.219145, 'c': 0.960755, 'l': 0.894653}
flav_map[5]['el']["btagcSF_0_pt3__1down"] = {'bb': 1.192356, 'cc': 1.192356, 'c': 0.939644, 'l': 0.874994}
flav_map[2]['mu']["btagcSF_0_pt3__1down"] = {'bb': 1.499733, 'cc': 1.499733, 'c': 1.000000, 'l': 0.885828}
flav_map[3]['mu']["btagcSF_0_pt3__1down"] = {'bb': 1.446127, 'cc': 1.446127, 'c': 0.964256, 'l': 0.854165}
flav_map[4]['mu']["btagcSF_0_pt3__1down"] = {'bb': 1.397920, 'cc': 1.397920, 'c': 0.932113, 'l': 0.825691}
flav_map[5]['mu']["btagcSF_0_pt3__1down"] = {'bb': 1.338813, 'cc': 1.338813, 'c': 0.892701, 'l': 0.790779}
# btaglSF_0__1up 
flav_map[2]['el']["btaglSF_0__1up"] = {'bb': 1.441191, 'cc': 1.441191, 'c': 1.000000, 'l': 0.887397}
flav_map[3]['el']["btaglSF_0__1up"] = {'bb': 1.394850, 'cc': 1.394850, 'c': 0.967846, 'l': 0.858863}
flav_map[4]['el']["btaglSF_0__1up"] = {'bb': 1.350971, 'cc': 1.350971, 'c': 0.937399, 'l': 0.831845}
flav_map[5]['el']["btaglSF_0__1up"] = {'bb': 1.304133, 'cc': 1.304133, 'c': 0.904900, 'l': 0.803005}
flav_map[2]['mu']["btaglSF_0__1up"] = {'bb': 1.666427, 'cc': 1.666427, 'c': 1.000000, 'l': 0.848052}
flav_map[3]['mu']["btaglSF_0__1up"] = {'bb': 1.588240, 'cc': 1.588240, 'c': 0.953081, 'l': 0.808262}
flav_map[4]['mu']["btaglSF_0__1up"] = {'bb': 1.519282, 'cc': 1.519282, 'c': 0.911701, 'l': 0.773169}
flav_map[5]['mu']["btaglSF_0__1up"] = {'bb': 1.436836, 'cc': 1.436836, 'c': 0.862226, 'l': 0.731212}
# btaglSF_0__1down 
flav_map[2]['el']["btaglSF_0__1down"] = {'bb': 1.102551, 'cc': 1.102551, 'c': 1.000000, 'l': 0.973707}
flav_map[3]['el']["btaglSF_0__1down"] = {'bb': 1.094049, 'cc': 1.094049, 'c': 0.992289, 'l': 0.966199}
flav_map[4]['el']["btaglSF_0__1down"] = {'bb': 1.085604, 'cc': 1.085604, 'c': 0.984630, 'l': 0.958741}
flav_map[5]['el']["btaglSF_0__1down"] = {'bb': 1.076155, 'cc': 1.076155, 'c': 0.976059, 'l': 0.950396}
flav_map[2]['mu']["btaglSF_0__1down"] = {'bb': 1.351080, 'cc': 1.351080, 'c': 1.000000, 'l': 0.919644}
flav_map[3]['mu']["btaglSF_0__1down"] = {'bb': 1.316675, 'cc': 1.316675, 'c': 0.974535, 'l': 0.896225}
flav_map[4]['mu']["btaglSF_0__1down"] = {'bb': 1.285204, 'cc': 1.285204, 'c': 0.951242, 'l': 0.874804}
flav_map[5]['mu']["btaglSF_0__1down"] = {'bb': 1.245690, 'cc': 1.245690, 'c': 0.921996, 'l': 0.847908}
# btaglSF_1__1up 
flav_map[2]['el']["btaglSF_1__1up"] = {'bb': 1.198696, 'cc': 1.198696, 'c': 1.000000, 'l': 0.949100}
flav_map[3]['el']["btaglSF_1__1up"] = {'bb': 1.180931, 'cc': 1.180931, 'c': 0.985180, 'l': 0.935034}
flav_map[4]['el']["btaglSF_1__1up"] = {'bb': 1.163531, 'cc': 1.163531, 'c': 0.970664, 'l': 0.921257}
flav_map[5]['el']["btaglSF_1__1up"] = {'bb': 1.144351, 'cc': 1.144351, 'c': 0.954663, 'l': 0.906070}
flav_map[2]['mu']["btaglSF_1__1up"] = {'bb': 1.443529, 'cc': 1.443529, 'c': 1.000000, 'l': 0.898548}
flav_map[3]['mu']["btaglSF_1__1up"] = {'bb': 1.397456, 'cc': 1.397456, 'c': 0.968083, 'l': 0.869869}
flav_map[4]['mu']["btaglSF_1__1up"] = {'bb': 1.355784, 'cc': 1.355784, 'c': 0.939215, 'l': 0.843930}
flav_map[5]['mu']["btaglSF_1__1up"] = {'bb': 1.304242, 'cc': 1.304242, 'c': 0.903509, 'l': 0.811847}
# btaglSF_1__1down 
flav_map[2]['el']["btaglSF_1__1down"] = {'bb': 1.350060, 'cc': 1.350060, 'c': 1.000000, 'l': 0.910581}
flav_map[3]['el']["btaglSF_1__1down"] = {'bb': 1.315356, 'cc': 1.315356, 'c': 0.974295, 'l': 0.887174}
flav_map[4]['el']["btaglSF_1__1down"] = {'bb': 1.282073, 'cc': 1.282073, 'c': 0.949642, 'l': 0.864726}
flav_map[5]['el']["btaglSF_1__1down"] = {'bb': 1.246079, 'cc': 1.246079, 'c': 0.922981, 'l': 0.840449}
flav_map[2]['mu']["btaglSF_1__1down"] = {'bb': 1.577871, 'cc': 1.577871, 'c': 1.000000, 'l': 0.868160}
flav_map[3]['mu']["btaglSF_1__1down"] = {'bb': 1.513197, 'cc': 1.513197, 'c': 0.959012, 'l': 0.832576}
flav_map[4]['mu']["btaglSF_1__1down"] = {'bb': 1.455565, 'cc': 1.455565, 'c': 0.922487, 'l': 0.800866}
flav_map[5]['mu']["btaglSF_1__1down"] = {'bb': 1.385723, 'cc': 1.385723, 'c': 0.878223, 'l': 0.762439}
# btaglSF_2__1up 
flav_map[2]['el']["btaglSF_2__1up"] = {'bb': 1.278969, 'cc': 1.278969, 'c': 1.000000, 'l': 0.928671}
flav_map[3]['el']["btaglSF_2__1up"] = {'bb': 1.252587, 'cc': 1.252587, 'c': 0.979373, 'l': 0.909515}
flav_map[4]['el']["btaglSF_2__1up"] = {'bb': 1.227057, 'cc': 1.227057, 'c': 0.959411, 'l': 0.890977}
flav_map[5]['el']["btaglSF_2__1up"] = {'bb': 1.199145, 'cc': 1.199145, 'c': 0.937588, 'l': 0.870710}
flav_map[2]['mu']["btaglSF_2__1up"] = {'bb': 1.516388, 'cc': 1.516388, 'c': 1.000000, 'l': 0.882088}
flav_map[3]['mu']["btaglSF_2__1up"] = {'bb': 1.460517, 'cc': 1.460517, 'c': 0.963155, 'l': 0.849587}
flav_map[4]['mu']["btaglSF_2__1up"] = {'bb': 1.410428, 'cc': 1.410428, 'c': 0.930123, 'l': 0.820451}
flav_map[5]['mu']["btaglSF_2__1up"] = {'bb': 1.349061, 'cc': 1.349061, 'c': 0.889655, 'l': 0.784754}
# btaglSF_2__1down 
flav_map[2]['el']["btaglSF_2__1down"] = {'bb': 1.270876, 'cc': 1.270876, 'c': 1.000000, 'l': 0.930679}
flav_map[3]['el']["btaglSF_2__1down"] = {'bb': 1.245379, 'cc': 1.245379, 'c': 0.979937, 'l': 0.912007}
flav_map[4]['el']["btaglSF_2__1down"] = {'bb': 1.220639, 'cc': 1.220639, 'c': 0.960471, 'l': 0.893890}
flav_map[5]['el']["btaglSF_2__1down"] = {'bb': 1.193673, 'cc': 1.193673, 'c': 0.939252, 'l': 0.874142}
flav_map[2]['mu']["btaglSF_2__1down"] = {'bb': 1.506031, 'cc': 1.506031, 'c': 1.000000, 'l': 0.884350}
flav_map[3]['mu']["btaglSF_2__1down"] = {'bb': 1.451520, 'cc': 1.451520, 'c': 0.963805, 'l': 0.852341}
flav_map[4]['mu']["btaglSF_2__1down"] = {'bb': 1.402526, 'cc': 1.402526, 'c': 0.931273, 'l': 0.823571}
flav_map[5]['mu']["btaglSF_2__1down"] = {'bb': 1.342605, 'cc': 1.342605, 'c': 0.891486, 'l': 0.788385}
# btaglSF_3__1up 
flav_map[2]['el']["btaglSF_3__1up"] = {'bb': 1.264471, 'cc': 1.264471, 'c': 1.000000, 'l': 0.932343}
flav_map[3]['el']["btaglSF_3__1up"] = {'bb': 1.239697, 'cc': 1.239697, 'c': 0.980408, 'l': 0.914077}
flav_map[4]['el']["btaglSF_3__1up"] = {'bb': 1.215676, 'cc': 1.215676, 'c': 0.961410, 'l': 0.896365}
flav_map[5]['el']["btaglSF_3__1up"] = {'bb': 1.189376, 'cc': 1.189376, 'c': 0.940612, 'l': 0.876973}
flav_map[2]['mu']["btaglSF_3__1up"] = {'bb': 1.504671, 'cc': 1.504671, 'c': 1.000000, 'l': 0.884709}
flav_map[3]['mu']["btaglSF_3__1up"] = {'bb': 1.450392, 'cc': 1.450392, 'c': 0.963926, 'l': 0.852794}
flav_map[4]['mu']["btaglSF_3__1up"] = {'bb': 1.401684, 'cc': 1.401684, 'c': 0.931555, 'l': 0.824155}
flav_map[5]['mu']["btaglSF_3__1up"] = {'bb': 1.341893, 'cc': 1.341893, 'c': 0.891818, 'l': 0.789000}
# btaglSF_3__1down 
flav_map[2]['el']["btaglSF_3__1down"] = {'bb': 1.285156, 'cc': 1.285156, 'c': 1.000000, 'l': 0.927061}
flav_map[3]['el']["btaglSF_3__1down"] = {'bb': 1.258064, 'cc': 1.258064, 'c': 0.978919, 'l': 0.907518}
flav_map[4]['el']["btaglSF_3__1down"] = {'bb': 1.231828, 'cc': 1.231828, 'c': 0.958504, 'l': 0.888592}
flav_map[5]['el']["btaglSF_3__1down"] = {'bb': 1.203269, 'cc': 1.203269, 'c': 0.936282, 'l': 0.867991}
flav_map[2]['mu']["btaglSF_3__1down"] = {'bb': 1.517731, 'cc': 1.517731, 'c': 1.000000, 'l': 0.881733}
flav_map[3]['mu']["btaglSF_3__1down"] = {'bb': 1.461627, 'cc': 1.461627, 'c': 0.963034, 'l': 0.849139}
flav_map[4]['mu']["btaglSF_3__1down"] = {'bb': 1.411249, 'cc': 1.411249, 'c': 0.929842, 'l': 0.819872}
flav_map[5]['mu']["btaglSF_3__1down"] = {'bb': 1.349756, 'cc': 1.349756, 'c': 0.889325, 'l': 0.784147}
# btaglSF_4__1up 
flav_map[2]['el']["btaglSF_4__1up"] = {'bb': 1.274071, 'cc': 1.274071, 'c': 1.000000, 'l': 0.929856}
flav_map[3]['el']["btaglSF_4__1up"] = {'bb': 1.248205, 'cc': 1.248205, 'c': 0.979698, 'l': 0.910978}
flav_map[4]['el']["btaglSF_4__1up"] = {'bb': 1.223145, 'cc': 1.223145, 'c': 0.960029, 'l': 0.892689}
flav_map[5]['el']["btaglSF_4__1up"] = {'bb': 1.195790, 'cc': 1.195790, 'c': 0.938558, 'l': 0.872724}
flav_map[2]['mu']["btaglSF_4__1up"] = {'bb': 1.515334, 'cc': 1.515334, 'c': 1.000000, 'l': 0.882215}
flav_map[3]['mu']["btaglSF_4__1up"] = {'bb': 1.459508, 'cc': 1.459508, 'c': 0.963159, 'l': 0.849714}
flav_map[4]['mu']["btaglSF_4__1up"] = {'bb': 1.409458, 'cc': 1.409458, 'c': 0.930130, 'l': 0.820575}
flav_map[5]['mu']["btaglSF_4__1up"] = {'bb': 1.348222, 'cc': 1.348222, 'c': 0.889719, 'l': 0.784924}
# btaglSF_4__1down 
flav_map[2]['el']["btaglSF_4__1down"] = {'bb': 1.275671, 'cc': 1.275671, 'c': 1.000000, 'l': 0.929517}
flav_map[3]['el']["btaglSF_4__1down"] = {'bb': 1.249673, 'cc': 1.249673, 'c': 0.979620, 'l': 0.910574}
flav_map[4]['el']["btaglSF_4__1down"] = {'bb': 1.224474, 'cc': 1.224474, 'c': 0.959867, 'l': 0.892213}
flav_map[5]['el']["btaglSF_4__1down"] = {'bb': 1.196965, 'cc': 1.196965, 'c': 0.938302, 'l': 0.872168}
flav_map[2]['mu']["btaglSF_4__1down"] = {'bb': 1.507007, 'cc': 1.507007, 'c': 1.000000, 'l': 0.884238}
flav_map[3]['mu']["btaglSF_4__1down"] = {'bb': 1.452460, 'cc': 1.452460, 'c': 0.963805, 'l': 0.852233}
flav_map[4]['mu']["btaglSF_4__1down"] = {'bb': 1.403436, 'cc': 1.403436, 'c': 0.931274, 'l': 0.823468}
flav_map[5]['mu']["btaglSF_4__1down"] = {'bb': 1.343395, 'cc': 1.343395, 'c': 0.891433, 'l': 0.788239}
# btaglSF_5__1up 
flav_map[2]['el']["btaglSF_5__1up"] = {'bb': 1.274981, 'cc': 1.274981, 'c': 1.000000, 'l': 0.929669}
flav_map[3]['el']["btaglSF_5__1up"] = {'bb': 1.249040, 'cc': 1.249040, 'c': 0.979654, 'l': 0.910754}
flav_map[4]['el']["btaglSF_5__1up"] = {'bb': 1.223907, 'cc': 1.223907, 'c': 0.959942, 'l': 0.892428}
flav_map[5]['el']["btaglSF_5__1up"] = {'bb': 1.196471, 'cc': 1.196471, 'c': 0.938423, 'l': 0.872423}
flav_map[2]['mu']["btaglSF_5__1up"] = {'bb': 1.510591, 'cc': 1.510591, 'c': 1.000000, 'l': 0.883379}
flav_map[3]['mu']["btaglSF_5__1up"] = {'bb': 1.455504, 'cc': 1.455504, 'c': 0.963533, 'l': 0.851165}
flav_map[4]['mu']["btaglSF_5__1up"] = {'bb': 1.406047, 'cc': 1.406047, 'c': 0.930793, 'l': 0.822242}
flav_map[5]['mu']["btaglSF_5__1up"] = {'bb': 1.345479, 'cc': 1.345479, 'c': 0.890698, 'l': 0.786823}
# btaglSF_5__1down 
flav_map[2]['el']["btaglSF_5__1down"] = {'bb': 1.274710, 'cc': 1.274710, 'c': 1.000000, 'l': 0.929718}
flav_map[3]['el']["btaglSF_5__1down"] = {'bb': 1.248791, 'cc': 1.248791, 'c': 0.979667, 'l': 0.910814}
flav_map[4]['el']["btaglSF_5__1down"] = {'bb': 1.223671, 'cc': 1.223671, 'c': 0.959961, 'l': 0.892493}
flav_map[5]['el']["btaglSF_5__1down"] = {'bb': 1.196249, 'cc': 1.196249, 'c': 0.938448, 'l': 0.872492}
flav_map[2]['mu']["btaglSF_5__1down"] = {'bb': 1.511740, 'cc': 1.511740, 'c': 1.000000, 'l': 0.883079}
flav_map[3]['mu']["btaglSF_5__1down"] = {'bb': 1.456458, 'cc': 1.456458, 'c': 0.963432, 'l': 0.850786}
flav_map[4]['mu']["btaglSF_5__1down"] = {'bb': 1.406844, 'cc': 1.406844, 'c': 0.930612, 'l': 0.821804}
flav_map[5]['mu']["btaglSF_5__1down"] = {'bb': 1.346137, 'cc': 1.346137, 'c': 0.890456, 'l': 0.786343}
# btaglSF_6__1up 
flav_map[2]['el']["btaglSF_6__1up"] = {'bb': 1.275051, 'cc': 1.275051, 'c': 1.000000, 'l': 0.929646}
flav_map[3]['el']["btaglSF_6__1up"] = {'bb': 1.249101, 'cc': 1.249101, 'c': 0.979648, 'l': 0.910726}
flav_map[4]['el']["btaglSF_6__1up"] = {'bb': 1.223957, 'cc': 1.223957, 'c': 0.959928, 'l': 0.892393}
flav_map[5]['el']["btaglSF_6__1up"] = {'bb': 1.196508, 'cc': 1.196508, 'c': 0.938400, 'l': 0.872380}
flav_map[2]['mu']["btaglSF_6__1up"] = {'bb': 1.510509, 'cc': 1.510509, 'c': 1.000000, 'l': 0.883388}
flav_map[3]['mu']["btaglSF_6__1up"] = {'bb': 1.455425, 'cc': 1.455425, 'c': 0.963533, 'l': 0.851174}
flav_map[4]['mu']["btaglSF_6__1up"] = {'bb': 1.405972, 'cc': 1.405972, 'c': 0.930794, 'l': 0.822252}
flav_map[5]['mu']["btaglSF_6__1up"] = {'bb': 1.345423, 'cc': 1.345423, 'c': 0.890708, 'l': 0.786841}
# btaglSF_6__1down 
flav_map[2]['el']["btaglSF_6__1down"] = {'bb': 1.274632, 'cc': 1.274632, 'c': 1.000000, 'l': 0.929743}
flav_map[3]['el']["btaglSF_6__1down"] = {'bb': 1.248723, 'cc': 1.248723, 'c': 0.979674, 'l': 0.910845}
flav_map[4]['el']["btaglSF_6__1down"] = {'bb': 1.223615, 'cc': 1.223615, 'c': 0.959976, 'l': 0.892531}
flav_map[5]['el']["btaglSF_6__1down"] = {'bb': 1.196207, 'cc': 1.196207, 'c': 0.938472, 'l': 0.872538}
flav_map[2]['mu']["btaglSF_6__1down"] = {'bb': 1.511825, 'cc': 1.511825, 'c': 1.000000, 'l': 0.883069}
flav_map[3]['mu']["btaglSF_6__1down"] = {'bb': 1.456540, 'cc': 1.456540, 'c': 0.963432, 'l': 0.850776}
flav_map[4]['mu']["btaglSF_6__1down"] = {'bb': 1.406921, 'cc': 1.406921, 'c': 0.930611, 'l': 0.821793}
flav_map[5]['mu']["btaglSF_6__1down"] = {'bb': 1.346196, 'cc': 1.346196, 'c': 0.890445, 'l': 0.786324}
# btaglSF_7__1up 
flav_map[2]['el']["btaglSF_7__1up"] = {'bb': 1.273386, 'cc': 1.273386, 'c': 1.000000, 'l': 0.930068}
flav_map[3]['el']["btaglSF_7__1up"] = {'bb': 1.247624, 'cc': 1.247624, 'c': 0.979769, 'l': 0.911251}
flav_map[4]['el']["btaglSF_7__1up"] = {'bb': 1.222651, 'cc': 1.222651, 'c': 0.960157, 'l': 0.893011}
flav_map[5]['el']["btaglSF_7__1up"] = {'bb': 1.195380, 'cc': 1.195380, 'c': 0.938742, 'l': 0.873094}
flav_map[2]['mu']["btaglSF_7__1up"] = {'bb': 1.509190, 'cc': 1.509190, 'c': 1.000000, 'l': 0.883681}
flav_map[3]['mu']["btaglSF_7__1up"] = {'bb': 1.454285, 'cc': 1.454285, 'c': 0.963620, 'l': 0.851533}
flav_map[4]['mu']["btaglSF_7__1up"] = {'bb': 1.404984, 'cc': 1.404984, 'c': 0.930953, 'l': 0.822665}
flav_map[5]['mu']["btaglSF_7__1up"] = {'bb': 1.344632, 'cc': 1.344632, 'c': 0.890963, 'l': 0.787327}
# btaglSF_7__1down 
flav_map[2]['el']["btaglSF_7__1down"] = {'bb': 1.276293, 'cc': 1.276293, 'c': 1.000000, 'l': 0.929322}
flav_map[3]['el']["btaglSF_7__1down"] = {'bb': 1.250197, 'cc': 1.250197, 'c': 0.979554, 'l': 0.910321}
flav_map[4]['el']["btaglSF_7__1down"] = {'bb': 1.224918, 'cc': 1.224918, 'c': 0.959747, 'l': 0.891914}
flav_map[5]['el']["btaglSF_7__1down"] = {'bb': 1.197331, 'cc': 1.197331, 'c': 0.938132, 'l': 0.871826}
flav_map[2]['mu']["btaglSF_7__1down"] = {'bb': 1.513137, 'cc': 1.513137, 'c': 1.000000, 'l': 0.882776}
flav_map[3]['mu']["btaglSF_7__1down"] = {'bb': 1.457674, 'cc': 1.457674, 'c': 0.963346, 'l': 0.850419}
flav_map[4]['mu']["btaglSF_7__1down"] = {'bb': 1.407903, 'cc': 1.407903, 'c': 0.930453, 'l': 0.821382}
flav_map[5]['mu']["btaglSF_7__1down"] = {'bb': 1.346983, 'cc': 1.346983, 'c': 0.890192, 'l': 0.785841}
# btaglSF_8__1up 
flav_map[2]['el']["btaglSF_8__1up"] = {'bb': 1.273542, 'cc': 1.273542, 'c': 1.000000, 'l': 0.930030}
flav_map[3]['el']["btaglSF_8__1up"] = {'bb': 1.247762, 'cc': 1.247762, 'c': 0.979757, 'l': 0.911204}
flav_map[4]['el']["btaglSF_8__1up"] = {'bb': 1.222773, 'cc': 1.222773, 'c': 0.960136, 'l': 0.892955}
flav_map[5]['el']["btaglSF_8__1up"] = {'bb': 1.195488, 'cc': 1.195488, 'c': 0.938710, 'l': 0.873029}
flav_map[2]['mu']["btaglSF_8__1up"] = {'bb': 1.509473, 'cc': 1.509473, 'c': 1.000000, 'l': 0.883619}
flav_map[3]['mu']["btaglSF_8__1up"] = {'bb': 1.454530, 'cc': 1.454530, 'c': 0.963602, 'l': 0.851456}
flav_map[4]['mu']["btaglSF_8__1up"] = {'bb': 1.405197, 'cc': 1.405197, 'c': 0.930919, 'l': 0.822577}
flav_map[5]['mu']["btaglSF_8__1up"] = {'bb': 1.344804, 'cc': 1.344804, 'c': 0.890910, 'l': 0.787224}
# btaglSF_8__1down 
flav_map[2]['el']["btaglSF_8__1down"] = {'bb': 1.276144, 'cc': 1.276144, 'c': 1.000000, 'l': 0.929358}
flav_map[3]['el']["btaglSF_8__1down"] = {'bb': 1.250065, 'cc': 1.250065, 'c': 0.979564, 'l': 0.910366}
flav_map[4]['el']["btaglSF_8__1down"] = {'bb': 1.224801, 'cc': 1.224801, 'c': 0.959767, 'l': 0.891968}
flav_map[5]['el']["btaglSF_8__1down"] = {'bb': 1.197229, 'cc': 1.197229, 'c': 0.938161, 'l': 0.871888}
flav_map[2]['mu']["btaglSF_8__1down"] = {'bb': 1.512856, 'cc': 1.512856, 'c': 1.000000, 'l': 0.882838}
flav_map[3]['mu']["btaglSF_8__1down"] = {'bb': 1.457431, 'cc': 1.457431, 'c': 0.963364, 'l': 0.850495}
flav_map[4]['mu']["btaglSF_8__1down"] = {'bb': 1.407693, 'cc': 1.407693, 'c': 0.930487, 'l': 0.821469}
flav_map[5]['mu']["btaglSF_8__1down"] = {'bb': 1.346812, 'cc': 1.346812, 'c': 0.890245, 'l': 0.785942}
# btaglSF_9__1up 
flav_map[2]['el']["btaglSF_9__1up"] = {'bb': 1.274712, 'cc': 1.274712, 'c': 1.000000, 'l': 0.929725}
flav_map[3]['el']["btaglSF_9__1up"] = {'bb': 1.248796, 'cc': 1.248796, 'c': 0.979670, 'l': 0.910823}
flav_map[4]['el']["btaglSF_9__1up"] = {'bb': 1.223682, 'cc': 1.223682, 'c': 0.959968, 'l': 0.892506}
flav_map[5]['el']["btaglSF_9__1up"] = {'bb': 1.196266, 'cc': 1.196266, 'c': 0.938460, 'l': 0.872510}
flav_map[2]['mu']["btaglSF_9__1up"] = {'bb': 1.511467, 'cc': 1.511467, 'c': 1.000000, 'l': 0.883155}
flav_map[3]['mu']["btaglSF_9__1up"] = {'bb': 1.456238, 'cc': 1.456238, 'c': 0.963460, 'l': 0.850884}
flav_map[4]['mu']["btaglSF_9__1up"] = {'bb': 1.406664, 'cc': 1.406664, 'c': 0.930662, 'l': 0.821918}
flav_map[5]['mu']["btaglSF_9__1up"] = {'bb': 1.345986, 'cc': 1.345986, 'c': 0.890516, 'l': 0.786464}
# btaglSF_9__1down 
flav_map[2]['el']["btaglSF_9__1down"] = {'bb': 1.274963, 'cc': 1.274963, 'c': 1.000000, 'l': 0.929666}
flav_map[3]['el']["btaglSF_9__1down"] = {'bb': 1.249022, 'cc': 1.249022, 'c': 0.979653, 'l': 0.910750}
flav_map[4]['el']["btaglSF_9__1down"] = {'bb': 1.223884, 'cc': 1.223884, 'c': 0.959937, 'l': 0.892420}
flav_map[5]['el']["btaglSF_9__1down"] = {'bb': 1.196444, 'cc': 1.196444, 'c': 0.938414, 'l': 0.872412}
flav_map[2]['mu']["btaglSF_9__1down"] = {'bb': 1.510864, 'cc': 1.510864, 'c': 1.000000, 'l': 0.883302}
flav_map[3]['mu']["btaglSF_9__1down"] = {'bb': 1.455726, 'cc': 1.455726, 'c': 0.963505, 'l': 0.851066}
flav_map[4]['mu']["btaglSF_9__1down"] = {'bb': 1.406227, 'cc': 1.406227, 'c': 0.930744, 'l': 0.822128}
flav_map[5]['mu']["btaglSF_9__1down"] = {'bb': 1.345632, 'cc': 1.345632, 'c': 0.890637, 'l': 0.786702}
# btaglSF_10__1up 
flav_map[2]['el']["btaglSF_10__1up"] = {'bb': 1.275230, 'cc': 1.275230, 'c': 1.000000, 'l': 0.929593}
flav_map[3]['el']["btaglSF_10__1up"] = {'bb': 1.249257, 'cc': 1.249257, 'c': 0.979632, 'l': 0.910659}
flav_map[4]['el']["btaglSF_10__1up"] = {'bb': 1.224089, 'cc': 1.224089, 'c': 0.959896, 'l': 0.892312}
flav_map[5]['el']["btaglSF_10__1up"] = {'bb': 1.196615, 'cc': 1.196615, 'c': 0.938352, 'l': 0.872285}
flav_map[2]['mu']["btaglSF_10__1up"] = {'bb': 1.511239, 'cc': 1.511239, 'c': 1.000000, 'l': 0.883209}
flav_map[3]['mu']["btaglSF_10__1up"] = {'bb': 1.456041, 'cc': 1.456041, 'c': 0.963475, 'l': 0.850950}
flav_map[4]['mu']["btaglSF_10__1up"] = {'bb': 1.406496, 'cc': 1.406496, 'c': 0.930691, 'l': 0.821995}
flav_map[5]['mu']["btaglSF_10__1up"] = {'bb': 1.345848, 'cc': 1.345848, 'c': 0.890559, 'l': 0.786550}
# btaglSF_10__1down 
flav_map[2]['el']["btaglSF_10__1down"] = {'bb': 1.274448, 'cc': 1.274448, 'c': 1.000000, 'l': 0.929797}
flav_map[3]['el']["btaglSF_10__1down"] = {'bb': 1.248565, 'cc': 1.248565, 'c': 0.979690, 'l': 0.910913}
flav_map[4]['el']["btaglSF_10__1down"] = {'bb': 1.223481, 'cc': 1.223481, 'c': 0.960008, 'l': 0.892613}
flav_map[5]['el']["btaglSF_10__1down"] = {'bb': 1.196097, 'cc': 1.196097, 'c': 0.938521, 'l': 0.872634}
flav_map[2]['mu']["btaglSF_10__1down"] = {'bb': 1.511095, 'cc': 1.511095, 'c': 1.000000, 'l': 0.883248}
flav_map[3]['mu']["btaglSF_10__1down"] = {'bb': 1.455924, 'cc': 1.455924, 'c': 0.963489, 'l': 0.851000}
flav_map[4]['mu']["btaglSF_10__1down"] = {'bb': 1.406397, 'cc': 1.406397, 'c': 0.930714, 'l': 0.822051}
flav_map[5]['mu']["btaglSF_10__1down"] = {'bb': 1.345772, 'cc': 1.345772, 'c': 0.890594, 'l': 0.786615}
# btageSF_0__1up 
flav_map[2]['el']["btageSF_0__1up"] = {'bb': 1.273880, 'cc': 1.273880, 'c': 1.000000, 'l': 0.929940}
flav_map[3]['el']["btageSF_0__1up"] = {'bb': 1.248060, 'cc': 1.248060, 'c': 0.979731, 'l': 0.911091}
flav_map[4]['el']["btageSF_0__1up"] = {'bb': 1.223036, 'cc': 1.223036, 'c': 0.960087, 'l': 0.892824}
flav_map[5]['el']["btageSF_0__1up"] = {'bb': 1.195714, 'cc': 1.195714, 'c': 0.938639, 'l': 0.872878}
flav_map[2]['mu']["btageSF_0__1up"] = {'bb': 1.510665, 'cc': 1.510665, 'c': 1.000000, 'l': 0.883342}
flav_map[3]['mu']["btageSF_0__1up"] = {'bb': 1.455552, 'cc': 1.455552, 'c': 0.963517, 'l': 0.851115}
flav_map[4]['mu']["btageSF_0__1up"] = {'bb': 1.406077, 'cc': 1.406077, 'c': 0.930767, 'l': 0.822186}
flav_map[5]['mu']["btageSF_0__1up"] = {'bb': 1.345518, 'cc': 1.345518, 'c': 0.890679, 'l': 0.786774}
# btageSF_0__1down 
flav_map[2]['el']["btageSF_0__1down"] = {'bb': 1.275820, 'cc': 1.275820, 'c': 1.000000, 'l': 0.929445}
flav_map[3]['el']["btageSF_0__1down"] = {'bb': 1.249779, 'cc': 1.249779, 'c': 0.979589, 'l': 0.910475}
flav_map[4]['el']["btageSF_0__1down"] = {'bb': 1.224549, 'cc': 1.224549, 'c': 0.959813, 'l': 0.892094}
flav_map[5]['el']["btageSF_0__1down"] = {'bb': 1.197011, 'cc': 1.197011, 'c': 0.938229, 'l': 0.872033}
flav_map[2]['mu']["btageSF_0__1down"] = {'bb': 1.511605, 'cc': 1.511605, 'c': 1.000000, 'l': 0.883129}
flav_map[3]['mu']["btageSF_0__1down"] = {'bb': 1.456359, 'cc': 1.456359, 'c': 0.963452, 'l': 0.850853}
flav_map[4]['mu']["btageSF_0__1down"] = {'bb': 1.406769, 'cc': 1.406769, 'c': 0.930645, 'l': 0.821880}
flav_map[5]['mu']["btageSF_0__1down"] = {'bb': 1.346063, 'cc': 1.346063, 'c': 0.890486, 'l': 0.786414}
# btageSF_1__1up 
flav_map[2]['el']["btageSF_1__1up"] = {'bb': 1.308960, 'cc': 1.308960, 'c': 1.000000, 'l': 0.920310}
flav_map[3]['el']["btageSF_1__1up"] = {'bb': 1.278768, 'cc': 1.278768, 'c': 0.976934, 'l': 0.899082}
flav_map[4]['el']["btageSF_1__1up"] = {'bb': 1.249780, 'cc': 1.249780, 'c': 0.954789, 'l': 0.878701}
flav_map[5]['el']["btageSF_1__1up"] = {'bb': 1.218226, 'cc': 1.218226, 'c': 0.930682, 'l': 0.856516}
flav_map[2]['mu']["btageSF_1__1up"] = {'bb': 1.582293, 'cc': 1.582293, 'c': 1.000000, 'l': 0.865890}
flav_map[3]['mu']["btageSF_1__1up"] = {'bb': 1.516090, 'cc': 1.516090, 'c': 0.958160, 'l': 0.829661}
flav_map[4]['mu']["btageSF_1__1up"] = {'bb': 1.457342, 'cc': 1.457342, 'c': 0.921032, 'l': 0.797512}
flav_map[5]['mu']["btageSF_1__1up"] = {'bb': 1.386386, 'cc': 1.386386, 'c': 0.876188, 'l': 0.758683}
# btageSF_1__1down 
flav_map[2]['el']["btageSF_1__1down"] = {'bb': 1.308960, 'cc': 1.308960, 'c': 1.000000, 'l': 0.920310}
flav_map[3]['el']["btageSF_1__1down"] = {'bb': 1.278768, 'cc': 1.278768, 'c': 0.976934, 'l': 0.899082}
flav_map[4]['el']["btageSF_1__1down"] = {'bb': 1.249780, 'cc': 1.249780, 'c': 0.954789, 'l': 0.878701}
flav_map[5]['el']["btageSF_1__1down"] = {'bb': 1.218226, 'cc': 1.218226, 'c': 0.930682, 'l': 0.856516}
flav_map[2]['mu']["btageSF_1__1down"] = {'bb': 1.582293, 'cc': 1.582293, 'c': 1.000000, 'l': 0.865890}
flav_map[3]['mu']["btageSF_1__1down"] = {'bb': 1.516090, 'cc': 1.516090, 'c': 0.958160, 'l': 0.829661}
flav_map[4]['mu']["btageSF_1__1down"] = {'bb': 1.457342, 'cc': 1.457342, 'c': 0.921032, 'l': 0.797512}
flav_map[5]['mu']["btageSF_1__1down"] = {'bb': 1.386386, 'cc': 1.386386, 'c': 0.876188, 'l': 0.758683}
# eTrigSF__1up 
flav_map[2]['el']["eTrigSF__1up"] = {'bb': 1.273518, 'cc': 1.273518, 'c': 1.000000, 'l': 0.930036}
flav_map[3]['el']["eTrigSF__1up"] = {'bb': 1.247738, 'cc': 1.247738, 'c': 0.979757, 'l': 0.911209}
flav_map[4]['el']["eTrigSF__1up"] = {'bb': 1.222750, 'cc': 1.222750, 'c': 0.960136, 'l': 0.892961}
flav_map[5]['el']["eTrigSF__1up"] = {'bb': 1.195468, 'cc': 1.195468, 'c': 0.938713, 'l': 0.873037}
flav_map[2]['mu']["eTrigSF__1up"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["eTrigSF__1up"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["eTrigSF__1up"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["eTrigSF__1up"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786584}
# eTrigSF__1down 
flav_map[2]['el']["eTrigSF__1down"] = {'bb': 1.276161, 'cc': 1.276161, 'c': 1.000000, 'l': 0.929354}
flav_map[3]['el']["eTrigSF__1down"] = {'bb': 1.250083, 'cc': 1.250083, 'c': 0.979565, 'l': 0.910363}
flav_map[4]['el']["eTrigSF__1down"] = {'bb': 1.224818, 'cc': 1.224818, 'c': 0.959768, 'l': 0.891964}
flav_map[5]['el']["eTrigSF__1down"] = {'bb': 1.197243, 'cc': 1.197243, 'c': 0.938160, 'l': 0.871883}
flav_map[2]['mu']["eTrigSF__1down"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["eTrigSF__1down"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["eTrigSF__1down"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["eTrigSF__1down"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786584}
# eRecoSF__1up 
flav_map[2]['el']["eRecoSF__1up"] = {'bb': 1.274332, 'cc': 1.274332, 'c': 1.000000, 'l': 0.929821}
flav_map[3]['el']["eRecoSF__1up"] = {'bb': 1.248460, 'cc': 1.248460, 'c': 0.979697, 'l': 0.910944}
flav_map[4]['el']["eRecoSF__1up"] = {'bb': 1.223387, 'cc': 1.223387, 'c': 0.960022, 'l': 0.892649}
flav_map[5]['el']["eRecoSF__1up"] = {'bb': 1.196014, 'cc': 1.196014, 'c': 0.938542, 'l': 0.872676}
flav_map[2]['mu']["eRecoSF__1up"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["eRecoSF__1up"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["eRecoSF__1up"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["eRecoSF__1up"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786584}
# eRecoSF__1down 
flav_map[2]['el']["eRecoSF__1down"] = {'bb': 1.275341, 'cc': 1.275341, 'c': 1.000000, 'l': 0.929570}
flav_map[3]['el']["eRecoSF__1down"] = {'bb': 1.249356, 'cc': 1.249356, 'c': 0.979625, 'l': 0.910630}
flav_map[4]['el']["eRecoSF__1down"] = {'bb': 1.224178, 'cc': 1.224178, 'c': 0.959883, 'l': 0.892278}
flav_map[5]['el']["eRecoSF__1down"] = {'bb': 1.196694, 'cc': 1.196694, 'c': 0.938333, 'l': 0.872246}
flav_map[2]['mu']["eRecoSF__1down"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["eRecoSF__1down"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["eRecoSF__1down"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["eRecoSF__1down"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786584}
# eIDSF__1up 
flav_map[2]['el']["eIDSF__1up"] = {'bb': 1.271265, 'cc': 1.271265, 'c': 1.000000, 'l': 0.930596}
flav_map[3]['el']["eIDSF__1up"] = {'bb': 1.245735, 'cc': 1.245735, 'c': 0.979917, 'l': 0.911908}
flav_map[4]['el']["eIDSF__1up"] = {'bb': 1.220980, 'cc': 1.220980, 'c': 0.960445, 'l': 0.893786}
flav_map[5]['el']["eIDSF__1up"] = {'bb': 1.193939, 'cc': 1.193939, 'c': 0.939174, 'l': 0.873992}
flav_map[2]['mu']["eIDSF__1up"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["eIDSF__1up"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["eIDSF__1up"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["eIDSF__1up"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786584}
# eIDSF__1down 
flav_map[2]['el']["eIDSF__1down"] = {'bb': 1.278406, 'cc': 1.278406, 'c': 1.000000, 'l': 0.928797}
flav_map[3]['el']["eIDSF__1down"] = {'bb': 1.252078, 'cc': 1.252078, 'c': 0.979405, 'l': 0.909668}
flav_map[4]['el']["eIDSF__1down"] = {'bb': 1.226581, 'cc': 1.226581, 'c': 0.959461, 'l': 0.891144}
flav_map[5]['el']["eIDSF__1down"] = {'bb': 1.198765, 'cc': 1.198765, 'c': 0.937703, 'l': 0.870935}
flav_map[2]['mu']["eIDSF__1down"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["eIDSF__1down"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["eIDSF__1down"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["eIDSF__1down"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786584}
# eIsolSF__1up 
flav_map[2]['el']["eIsolSF__1up"] = {'bb': 1.274645, 'cc': 1.274645, 'c': 1.000000, 'l': 0.929738}
flav_map[3]['el']["eIsolSF__1up"] = {'bb': 1.248734, 'cc': 1.248734, 'c': 0.979672, 'l': 0.910838}
flav_map[4]['el']["eIsolSF__1up"] = {'bb': 1.223627, 'cc': 1.223627, 'c': 0.959975, 'l': 0.892525}
flav_map[5]['el']["eIsolSF__1up"] = {'bb': 1.196209, 'cc': 1.196209, 'c': 0.938465, 'l': 0.872526}
flav_map[2]['mu']["eIsolSF__1up"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["eIsolSF__1up"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["eIsolSF__1up"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["eIsolSF__1up"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786584}
# eIsolSF__1down 
flav_map[2]['el']["eIsolSF__1down"] = {'bb': 1.275030, 'cc': 1.275030, 'c': 1.000000, 'l': 0.929653}
flav_map[3]['el']["eIsolSF__1down"] = {'bb': 1.249085, 'cc': 1.249085, 'c': 0.979651, 'l': 0.910735}
flav_map[4]['el']["eIsolSF__1down"] = {'bb': 1.223940, 'cc': 1.223940, 'c': 0.959930, 'l': 0.892401}
flav_map[5]['el']["eIsolSF__1down"] = {'bb': 1.196501, 'cc': 1.196501, 'c': 0.938410, 'l': 0.872395}
flav_map[2]['mu']["eIsolSF__1down"] = {'bb': 1.511164, 'cc': 1.511164, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["eIsolSF__1down"] = {'bb': 1.455980, 'cc': 1.455980, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["eIsolSF__1down"] = {'bb': 1.406444, 'cc': 1.406444, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["eIsolSF__1down"] = {'bb': 1.345808, 'cc': 1.345808, 'c': 0.890577, 'l': 0.786584}
# muTrigStatSF__1up 
flav_map[2]['el']["muTrigStatSF__1up"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muTrigStatSF__1up"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muTrigStatSF__1up"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muTrigStatSF__1up"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muTrigStatSF__1up"] = {'bb': 1.508956, 'cc': 1.508956, 'c': 1.000000, 'l': 0.883728}
flav_map[3]['mu']["muTrigStatSF__1up"] = {'bb': 1.454079, 'cc': 1.454079, 'c': 0.963633, 'l': 0.851589}
flav_map[4]['mu']["muTrigStatSF__1up"] = {'bb': 1.404808, 'cc': 1.404808, 'c': 0.930980, 'l': 0.822733}
flav_map[5]['mu']["muTrigStatSF__1up"] = {'bb': 1.344477, 'cc': 1.344477, 'c': 0.890998, 'l': 0.787399}
# muTrigStatSF__1down 
flav_map[2]['el']["muTrigStatSF__1down"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muTrigStatSF__1down"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muTrigStatSF__1down"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muTrigStatSF__1down"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muTrigStatSF__1down"] = {'bb': 1.513419, 'cc': 1.513419, 'c': 1.000000, 'l': 0.882720}
flav_map[3]['mu']["muTrigStatSF__1down"] = {'bb': 1.457921, 'cc': 1.457921, 'c': 0.963330, 'l': 0.850350}
flav_map[4]['mu']["muTrigStatSF__1down"] = {'bb': 1.408115, 'cc': 1.408115, 'c': 0.930420, 'l': 0.821300}
flav_map[5]['mu']["muTrigStatSF__1down"] = {'bb': 1.347166, 'cc': 1.347166, 'c': 0.890148, 'l': 0.785751}
# muTrigSystSF__1up 
flav_map[2]['el']["muTrigSystSF__1up"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muTrigSystSF__1up"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muTrigSystSF__1up"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muTrigSystSF__1up"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muTrigSystSF__1up"] = {'bb': 1.505791, 'cc': 1.505791, 'c': 1.000000, 'l': 0.884461}
flav_map[3]['mu']["muTrigSystSF__1up"] = {'bb': 1.451360, 'cc': 1.451360, 'c': 0.963853, 'l': 0.852490}
flav_map[4]['mu']["muTrigSystSF__1up"] = {'bb': 1.402469, 'cc': 1.402469, 'c': 0.931384, 'l': 0.823772}
flav_map[5]['mu']["muTrigSystSF__1up"] = {'bb': 1.342566, 'cc': 1.342566, 'c': 0.891602, 'l': 0.788587}
# muTrigSystSF__1down 
flav_map[2]['el']["muTrigSystSF__1down"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muTrigSystSF__1down"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muTrigSystSF__1down"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muTrigSystSF__1down"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muTrigSystSF__1down"] = {'bb': 1.516430, 'cc': 1.516430, 'c': 1.000000, 'l': 0.882022}
flav_map[3]['mu']["muTrigSystSF__1down"] = {'bb': 1.460505, 'cc': 1.460505, 'c': 0.963120, 'l': 0.849493}
flav_map[4]['mu']["muTrigSystSF__1down"] = {'bb': 1.410335, 'cc': 1.410335, 'c': 0.930036, 'l': 0.820312}
flav_map[5]['mu']["muTrigSystSF__1down"] = {'bb': 1.348978, 'cc': 1.348978, 'c': 0.889575, 'l': 0.784624}
# muIDStatSF__1up 
flav_map[2]['el']["muIDStatSF__1up"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muIDStatSF__1up"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muIDStatSF__1up"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muIDStatSF__1up"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muIDStatSF__1up"] = {'bb': 1.510291, 'cc': 1.510291, 'c': 1.000000, 'l': 0.883428}
flav_map[3]['mu']["muIDStatSF__1up"] = {'bb': 1.455231, 'cc': 1.455231, 'c': 0.963544, 'l': 0.851221}
flav_map[4]['mu']["muIDStatSF__1up"] = {'bb': 1.405798, 'cc': 1.405798, 'c': 0.930813, 'l': 0.822306}
flav_map[5]['mu']["muIDStatSF__1up"] = {'bb': 1.345282, 'cc': 1.345282, 'c': 0.890744, 'l': 0.786907}
# muIDStatSF__1down 
flav_map[2]['el']["muIDStatSF__1down"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muIDStatSF__1down"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muIDStatSF__1down"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muIDStatSF__1down"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muIDStatSF__1down"] = {'bb': 1.512039, 'cc': 1.512039, 'c': 1.000000, 'l': 0.883029}
flav_map[3]['mu']["muIDStatSF__1down"] = {'bb': 1.456732, 'cc': 1.456732, 'c': 0.963422, 'l': 0.850730}
flav_map[4]['mu']["muIDStatSF__1down"] = {'bb': 1.407093, 'cc': 1.407093, 'c': 0.930593, 'l': 0.821741}
flav_map[5]['mu']["muIDStatSF__1down"] = {'bb': 1.346335, 'cc': 1.346335, 'c': 0.890410, 'l': 0.786258}
# muIDSystSF__1up 
flav_map[2]['el']["muIDSystSF__1up"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muIDSystSF__1up"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muIDSystSF__1up"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muIDSystSF__1up"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muIDSystSF__1up"] = {'bb': 1.506679, 'cc': 1.506679, 'c': 1.000000, 'l': 0.884239}
flav_map[3]['mu']["muIDSystSF__1up"] = {'bb': 1.452116, 'cc': 1.452116, 'c': 0.963786, 'l': 0.852218}
flav_map[4]['mu']["muIDSystSF__1up"] = {'bb': 1.403108, 'cc': 1.403108, 'c': 0.931259, 'l': 0.823456}
flav_map[5]['mu']["muIDSystSF__1up"] = {'bb': 1.343081, 'cc': 1.343081, 'c': 0.891418, 'l': 0.788227}
# muIDSystSF__1down 
flav_map[2]['el']["muIDSystSF__1down"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muIDSystSF__1down"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muIDSystSF__1down"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muIDSystSF__1down"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muIDSystSF__1down"] = {'bb': 1.515648, 'cc': 1.515648, 'c': 1.000000, 'l': 0.882219}
flav_map[3]['mu']["muIDSystSF__1down"] = {'bb': 1.459841, 'cc': 1.459841, 'c': 0.963179, 'l': 0.849735}
flav_map[4]['mu']["muIDSystSF__1down"] = {'bb': 1.409777, 'cc': 1.409777, 'c': 0.930148, 'l': 0.820594}
flav_map[5]['mu']["muIDSystSF__1down"] = {'bb': 1.348529, 'cc': 1.348529, 'c': 0.889738, 'l': 0.784944}
# muIsolStatSF__1up 
flav_map[2]['el']["muIsolStatSF__1up"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muIsolStatSF__1up"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muIsolStatSF__1up"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muIsolStatSF__1up"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muIsolStatSF__1up"] = {'bb': 1.510972, 'cc': 1.510972, 'c': 1.000000, 'l': 0.883274}
flav_map[3]['mu']["muIsolStatSF__1up"] = {'bb': 1.455815, 'cc': 1.455815, 'c': 0.963496, 'l': 0.851031}
flav_map[4]['mu']["muIsolStatSF__1up"] = {'bb': 1.406302, 'cc': 1.406302, 'c': 0.930727, 'l': 0.822087}
flav_map[5]['mu']["muIsolStatSF__1up"] = {'bb': 1.345692, 'cc': 1.345692, 'c': 0.890613, 'l': 0.786656}
# muIsolStatSF__1down 
flav_map[2]['el']["muIsolStatSF__1down"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muIsolStatSF__1down"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muIsolStatSF__1down"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muIsolStatSF__1down"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muIsolStatSF__1down"] = {'bb': 1.511359, 'cc': 1.511359, 'c': 1.000000, 'l': 0.883183}
flav_map[3]['mu']["muIsolStatSF__1down"] = {'bb': 1.456148, 'cc': 1.456148, 'c': 0.963469, 'l': 0.850920}
flav_map[4]['mu']["muIsolStatSF__1down"] = {'bb': 1.406589, 'cc': 1.406589, 'c': 0.930678, 'l': 0.821960}
flav_map[5]['mu']["muIsolStatSF__1down"] = {'bb': 1.345926, 'cc': 1.345926, 'c': 0.890540, 'l': 0.786510}
# muIsolSystSF__1up 
flav_map[2]['el']["muIsolSystSF__1up"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muIsolSystSF__1up"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muIsolSystSF__1up"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muIsolSystSF__1up"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muIsolSystSF__1up"] = {'bb': 1.510846, 'cc': 1.510846, 'c': 1.000000, 'l': 0.883297}
flav_map[3]['mu']["muIsolSystSF__1up"] = {'bb': 1.455705, 'cc': 1.455705, 'c': 0.963503, 'l': 0.851060}
flav_map[4]['mu']["muIsolSystSF__1up"] = {'bb': 1.406206, 'cc': 1.406206, 'c': 0.930741, 'l': 0.822121}
flav_map[5]['mu']["muIsolSystSF__1up"] = {'bb': 1.345612, 'cc': 1.345612, 'c': 0.890635, 'l': 0.786695}
# muIsolSystSF__1down 
flav_map[2]['el']["muIsolSystSF__1down"] = {'bb': 1.274839, 'cc': 1.274839, 'c': 1.000000, 'l': 0.929695}
flav_map[3]['el']["muIsolSystSF__1down"] = {'bb': 1.248911, 'cc': 1.248911, 'c': 0.979661, 'l': 0.910786}
flav_map[4]['el']["muIsolSystSF__1down"] = {'bb': 1.223785, 'cc': 1.223785, 'c': 0.959952, 'l': 0.892463}
flav_map[5]['el']["muIsolSystSF__1down"] = {'bb': 1.196356, 'cc': 1.196356, 'c': 0.938437, 'l': 0.872460}
flav_map[2]['mu']["muIsolSystSF__1down"] = {'bb': 1.511487, 'cc': 1.511487, 'c': 1.000000, 'l': 0.883160}
flav_map[3]['mu']["muIsolSystSF__1down"] = {'bb': 1.456260, 'cc': 1.456260, 'c': 0.963462, 'l': 0.850891}
flav_map[4]['mu']["muIsolSystSF__1down"] = {'bb': 1.406686, 'cc': 1.406686, 'c': 0.930664, 'l': 0.821925}
flav_map[5]['mu']["muIsolSystSF__1down"] = {'bb': 1.346007, 'cc': 1.346007, 'c': 0.890518, 'l': 0.786470}

# ttNNLO_seq__1up 
frac[2]['el']["ttNNLO_seq__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttNNLO_seq__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttNNLO_seq__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttNNLO_seq__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttNNLO_seq__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttNNLO_seq__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttNNLO_seq__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttNNLO_seq__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# ttNNLO_topPt__1up 
frac[2]['el']["ttNNLO_topPt__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttNNLO_topPt__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttNNLO_topPt__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttNNLO_topPt__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttNNLO_topPt__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttNNLO_topPt__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttNNLO_topPt__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttNNLO_topPt__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# ttEWK__1up 
frac[2]['el']["ttEWK__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttEWK__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttEWK__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttEWK__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttEWK__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttEWK__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttEWK__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttEWK__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# ttEWK__1down 
frac[2]['el']["ttEWK__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttEWK__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttEWK__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttEWK__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttEWK__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttEWK__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttEWK__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttEWK__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# pileup__1up 
frac[2]['el']["pileup__1up"] = {'bb': 0.094787,'cc': 0.065294,'c': 0.210061,'l': 0.629858}
frac[3]['el']["pileup__1up"] = {'bb': 0.118476,'cc': 0.100597,'c': 0.220006,'l': 0.560921}
frac[4]['el']["pileup__1up"] = {'bb': 0.140840,'cc': 0.138263,'c': 0.215734,'l': 0.505163}
frac[5]['el']["pileup__1up"] = {'bb': 0.149139,'cc': 0.151636,'c': 0.210413,'l': 0.488812}
frac[2]['mu']["pileup__1up"] = {'bb': 0.083570,'cc': 0.063220,'c': 0.204779,'l': 0.648431}
frac[3]['mu']["pileup__1up"] = {'bb': 0.106722,'cc': 0.096647,'c': 0.216476,'l': 0.580155}
frac[4]['mu']["pileup__1up"] = {'bb': 0.130281,'cc': 0.133491,'c': 0.206516,'l': 0.529712}
frac[5]['mu']["pileup__1up"] = {'bb': 0.140358,'cc': 0.147039,'c': 0.202154,'l': 0.510450}
# pileup__1down 
frac[2]['el']["pileup__1down"] = {'bb': 0.095814,'cc': 0.065870,'c': 0.209778,'l': 0.628538}
frac[3]['el']["pileup__1down"] = {'bb': 0.118652,'cc': 0.100765,'c': 0.219158,'l': 0.561425}
frac[4]['el']["pileup__1down"] = {'bb': 0.141779,'cc': 0.140317,'c': 0.215343,'l': 0.502561}
frac[5]['el']["pileup__1down"] = {'bb': 0.149910,'cc': 0.153487,'c': 0.209929,'l': 0.486675}
frac[2]['mu']["pileup__1down"] = {'bb': 0.084088,'cc': 0.064387,'c': 0.205732,'l': 0.645793}
frac[3]['mu']["pileup__1down"] = {'bb': 0.108105,'cc': 0.099859,'c': 0.215364,'l': 0.576672}
frac[4]['mu']["pileup__1down"] = {'bb': 0.131334,'cc': 0.136658,'c': 0.207423,'l': 0.524585}
frac[5]['mu']["pileup__1down"] = {'bb': 0.141354,'cc': 0.149785,'c': 0.202448,'l': 0.506414}
# jvt__1up 
frac[2]['el']["jvt__1up"] = {'bb': 0.095341,'cc': 0.065496,'c': 0.209824,'l': 0.629339}
frac[3]['el']["jvt__1up"] = {'bb': 0.118535,'cc': 0.100500,'c': 0.219487,'l': 0.561478}
frac[4]['el']["jvt__1up"] = {'bb': 0.141244,'cc': 0.139344,'c': 0.215339,'l': 0.504073}
frac[5]['el']["jvt__1up"] = {'bb': 0.149510,'cc': 0.152653,'c': 0.209973,'l': 0.487865}
frac[2]['mu']["jvt__1up"] = {'bb': 0.083890,'cc': 0.063782,'c': 0.205436,'l': 0.646892}
frac[3]['mu']["jvt__1up"] = {'bb': 0.107507,'cc': 0.098551,'c': 0.215811,'l': 0.578132}
frac[4]['mu']["jvt__1up"] = {'bb': 0.130943,'cc': 0.134879,'c': 0.207180,'l': 0.526998}
frac[5]['mu']["jvt__1up"] = {'bb': 0.141010,'cc': 0.148403,'c': 0.202468,'l': 0.508120}
# jvt__1down 
frac[2]['el']["jvt__1down"] = {'bb': 0.095413,'cc': 0.065639,'c': 0.209896,'l': 0.629052}
frac[3]['el']["jvt__1down"] = {'bb': 0.118576,'cc': 0.100672,'c': 0.219437,'l': 0.561316}
frac[4]['el']["jvt__1down"] = {'bb': 0.141303,'cc': 0.139536,'c': 0.215231,'l': 0.503930}
frac[5]['el']["jvt__1down"] = {'bb': 0.149532,'cc': 0.152803,'c': 0.209872,'l': 0.487793}
frac[2]['mu']["jvt__1down"] = {'bb': 0.083944,'cc': 0.063886,'c': 0.205459,'l': 0.646710}
frac[3]['mu']["jvt__1down"] = {'bb': 0.107574,'cc': 0.098734,'c': 0.215798,'l': 0.577894}
frac[4]['mu']["jvt__1down"] = {'bb': 0.131052,'cc': 0.135149,'c': 0.207058,'l': 0.526741}
frac[5]['mu']["jvt__1down"] = {'bb': 0.141083,'cc': 0.148615,'c': 0.202338,'l': 0.507964}
# btagbSF_0__1up 
frac[2]['el']["btagbSF_0__1up"] = {'bb': 0.096831,'cc': 0.065465,'c': 0.209525,'l': 0.628179}
frac[3]['el']["btagbSF_0__1up"] = {'bb': 0.121036,'cc': 0.100306,'c': 0.218845,'l': 0.559813}
frac[4]['el']["btagbSF_0__1up"] = {'bb': 0.144765,'cc': 0.138876,'c': 0.214410,'l': 0.501949}
frac[5]['el']["btagbSF_0__1up"] = {'bb': 0.153400,'cc': 0.152035,'c': 0.208965,'l': 0.485600}
frac[2]['mu']["btagbSF_0__1up"] = {'bb': 0.085172,'cc': 0.063749,'c': 0.205168,'l': 0.645911}
frac[3]['mu']["btagbSF_0__1up"] = {'bb': 0.109768,'cc': 0.098400,'c': 0.215267,'l': 0.576565}
frac[4]['mu']["btagbSF_0__1up"] = {'bb': 0.134220,'cc': 0.134518,'c': 0.206352,'l': 0.524910}
frac[5]['mu']["btagbSF_0__1up"] = {'bb': 0.144695,'cc': 0.147883,'c': 0.201543,'l': 0.505879}
# btagbSF_0__1down 
frac[2]['el']["btagbSF_0__1down"] = {'bb': 0.093939,'cc': 0.065675,'c': 0.210196,'l': 0.630190}
frac[3]['el']["btagbSF_0__1down"] = {'bb': 0.116109,'cc': 0.100868,'c': 0.220072,'l': 0.562951}
frac[4]['el']["btagbSF_0__1down"] = {'bb': 0.137829,'cc': 0.140002,'c': 0.216149,'l': 0.506019}
frac[5]['el']["btagbSF_0__1down"] = {'bb': 0.145696,'cc': 0.153418,'c': 0.210866,'l': 0.490019}
frac[2]['mu']["btagbSF_0__1down"] = {'bb': 0.082676,'cc': 0.063923,'c': 0.205728,'l': 0.647673}
frac[3]['mu']["btagbSF_0__1down"] = {'bb': 0.105343,'cc': 0.098889,'c': 0.216337,'l': 0.579431}
frac[4]['mu']["btagbSF_0__1down"] = {'bb': 0.127823,'cc': 0.135512,'c': 0.207876,'l': 0.528788}
frac[5]['mu']["btagbSF_0__1down"] = {'bb': 0.137453,'cc': 0.149135,'c': 0.203249,'l': 0.510163}
# btagbSF_1__1up 
frac[2]['el']["btagbSF_1__1up"] = {'bb': 0.095166,'cc': 0.065586,'c': 0.209911,'l': 0.629337}
frac[3]['el']["btagbSF_1__1up"] = {'bb': 0.118216,'cc': 0.100627,'c': 0.219547,'l': 0.561609}
frac[4]['el']["btagbSF_1__1up"] = {'bb': 0.140822,'cc': 0.139516,'c': 0.215398,'l': 0.504263}
frac[5]['el']["btagbSF_1__1up"] = {'bb': 0.149041,'cc': 0.152817,'c': 0.210041,'l': 0.488101}
frac[2]['mu']["btagbSF_1__1up"] = {'bb': 0.083733,'cc': 0.063850,'c': 0.205490,'l': 0.646927}
frac[3]['mu']["btagbSF_1__1up"] = {'bb': 0.107229,'cc': 0.098681,'c': 0.215881,'l': 0.578209}
frac[4]['mu']["btagbSF_1__1up"] = {'bb': 0.130578,'cc': 0.135084,'c': 0.207220,'l': 0.527118}
frac[5]['mu']["btagbSF_1__1up"] = {'bb': 0.140591,'cc': 0.148592,'c': 0.202510,'l': 0.508306}
# btagbSF_1__1down 
frac[2]['el']["btagbSF_1__1down"] = {'bb': 0.095593,'cc': 0.065555,'c': 0.209812,'l': 0.629041}
frac[3]['el']["btagbSF_1__1down"] = {'bb': 0.118899,'cc': 0.100549,'c': 0.219377,'l': 0.561175}
frac[4]['el']["btagbSF_1__1down"] = {'bb': 0.141728,'cc': 0.139369,'c': 0.215171,'l': 0.503731}
frac[5]['el']["btagbSF_1__1down"] = {'bb': 0.150004,'cc': 0.152645,'c': 0.209803,'l': 0.487548}
frac[2]['mu']["btagbSF_1__1down"] = {'bb': 0.084104,'cc': 0.063824,'c': 0.205407,'l': 0.646665}
frac[3]['mu']["btagbSF_1__1down"] = {'bb': 0.107855,'cc': 0.098612,'c': 0.215730,'l': 0.577804}
frac[4]['mu']["btagbSF_1__1down"] = {'bb': 0.131423,'cc': 0.134953,'c': 0.207018,'l': 0.526606}
frac[5]['mu']["btagbSF_1__1down"] = {'bb': 0.141507,'cc': 0.148434,'c': 0.202294,'l': 0.507765}
# btagbSF_2__1up 
frac[2]['el']["btagbSF_2__1up"] = {'bb': 0.095363,'cc': 0.065571,'c': 0.209865,'l': 0.629200}
frac[3]['el']["btagbSF_2__1up"] = {'bb': 0.118517,'cc': 0.100593,'c': 0.219472,'l': 0.561418}
frac[4]['el']["btagbSF_2__1up"] = {'bb': 0.141207,'cc': 0.139454,'c': 0.215302,'l': 0.504037}
frac[5]['el']["btagbSF_2__1up"] = {'bb': 0.149443,'cc': 0.152745,'c': 0.209942,'l': 0.487870}
frac[2]['mu']["btagbSF_2__1up"] = {'bb': 0.083905,'cc': 0.063838,'c': 0.205452,'l': 0.646805}
frac[3]['mu']["btagbSF_2__1up"] = {'bb': 0.107509,'cc': 0.098650,'c': 0.215813,'l': 0.578028}
frac[4]['mu']["btagbSF_2__1up"] = {'bb': 0.130941,'cc': 0.135028,'c': 0.207133,'l': 0.526898}
frac[5]['mu']["btagbSF_2__1up"] = {'bb': 0.140976,'cc': 0.148526,'c': 0.202419,'l': 0.508079}
# btagbSF_2__1down 
frac[2]['el']["btagbSF_2__1down"] = {'bb': 0.095395,'cc': 0.065569,'c': 0.209858,'l': 0.629178}
frac[3]['el']["btagbSF_2__1down"] = {'bb': 0.118598,'cc': 0.100584,'c': 0.219452,'l': 0.561366}
frac[4]['el']["btagbSF_2__1down"] = {'bb': 0.141342,'cc': 0.139432,'c': 0.215268,'l': 0.503958}
frac[5]['el']["btagbSF_2__1down"] = {'bb': 0.149602,'cc': 0.152717,'c': 0.209902,'l': 0.487779}
frac[2]['mu']["btagbSF_2__1down"] = {'bb': 0.083931,'cc': 0.063836,'c': 0.205446,'l': 0.646787}
frac[3]['mu']["btagbSF_2__1down"] = {'bb': 0.107574,'cc': 0.098643,'c': 0.215797,'l': 0.577986}
frac[4]['mu']["btagbSF_2__1down"] = {'bb': 0.131059,'cc': 0.135010,'c': 0.207105,'l': 0.526827}
frac[5]['mu']["btagbSF_2__1down"] = {'bb': 0.141121,'cc': 0.148501,'c': 0.202385,'l': 0.507993}
# btagbSF_3__1up 
frac[2]['el']["btagbSF_3__1up"] = {'bb': 0.095409,'cc': 0.065568,'c': 0.209855,'l': 0.629168}
frac[3]['el']["btagbSF_3__1up"] = {'bb': 0.118615,'cc': 0.100582,'c': 0.219448,'l': 0.561355}
frac[4]['el']["btagbSF_3__1up"] = {'bb': 0.141363,'cc': 0.139429,'c': 0.215263,'l': 0.503946}
frac[5]['el']["btagbSF_3__1up"] = {'bb': 0.149620,'cc': 0.152714,'c': 0.209898,'l': 0.487769}
frac[2]['mu']["btagbSF_3__1up"] = {'bb': 0.083944,'cc': 0.063835,'c': 0.205443,'l': 0.646778}
frac[3]['mu']["btagbSF_3__1up"] = {'bb': 0.107594,'cc': 0.098641,'c': 0.215793,'l': 0.577973}
frac[4]['mu']["btagbSF_3__1up"] = {'bb': 0.131079,'cc': 0.135006,'c': 0.207100,'l': 0.526814}
frac[5]['mu']["btagbSF_3__1up"] = {'bb': 0.141140,'cc': 0.148497,'c': 0.202381,'l': 0.507982}
# btagbSF_3__1down 
frac[2]['el']["btagbSF_3__1down"] = {'bb': 0.095349,'cc': 0.065572,'c': 0.209869,'l': 0.629210}
frac[3]['el']["btagbSF_3__1down"] = {'bb': 0.118499,'cc': 0.100595,'c': 0.219477,'l': 0.561429}
frac[4]['el']["btagbSF_3__1down"] = {'bb': 0.141187,'cc': 0.139457,'c': 0.215307,'l': 0.504049}
frac[5]['el']["btagbSF_3__1down"] = {'bb': 0.149424,'cc': 0.152749,'c': 0.209946,'l': 0.487881}
frac[2]['mu']["btagbSF_3__1down"] = {'bb': 0.083893,'cc': 0.063839,'c': 0.205455,'l': 0.646814}
frac[3]['mu']["btagbSF_3__1down"] = {'bb': 0.107489,'cc': 0.098652,'c': 0.215818,'l': 0.578041}
frac[4]['mu']["btagbSF_3__1down"] = {'bb': 0.130921,'cc': 0.135031,'c': 0.207138,'l': 0.526910}
frac[5]['mu']["btagbSF_3__1down"] = {'bb': 0.140957,'cc': 0.148529,'c': 0.202424,'l': 0.508090}
# btagbSF_0_pt1__1up 
frac[2]['el']["btagbSF_0_pt1__1up"] = {'bb': 0.096819,'cc': 0.065466,'c': 0.209528,'l': 0.628187}
frac[3]['el']["btagbSF_0_pt1__1up"] = {'bb': 0.121006,'cc': 0.100309,'c': 0.218853,'l': 0.559832}
frac[4]['el']["btagbSF_0_pt1__1up"] = {'bb': 0.144713,'cc': 0.138885,'c': 0.214423,'l': 0.501979}
frac[5]['el']["btagbSF_0_pt1__1up"] = {'bb': 0.153329,'cc': 0.152048,'c': 0.208982,'l': 0.485641}
frac[2]['mu']["btagbSF_0_pt1__1up"] = {'bb': 0.085162,'cc': 0.063750,'c': 0.205170,'l': 0.645918}
frac[3]['mu']["btagbSF_0_pt1__1up"] = {'bb': 0.109744,'cc': 0.098403,'c': 0.215273,'l': 0.576581}
frac[4]['mu']["btagbSF_0_pt1__1up"] = {'bb': 0.134172,'cc': 0.134526,'c': 0.206363,'l': 0.524939}
frac[5]['mu']["btagbSF_0_pt1__1up"] = {'bb': 0.144629,'cc': 0.147894,'c': 0.201558,'l': 0.505918}
# btagbSF_0_pt1__1down 
frac[2]['el']["btagbSF_0_pt1__1down"] = {'bb': 0.093951,'cc': 0.065674,'c': 0.210193,'l': 0.630182}
frac[3]['el']["btagbSF_0_pt1__1down"] = {'bb': 0.116138,'cc': 0.100865,'c': 0.220065,'l': 0.562933}
frac[4]['el']["btagbSF_0_pt1__1down"] = {'bb': 0.137880,'cc': 0.139994,'c': 0.216136,'l': 0.505990}
frac[5]['el']["btagbSF_0_pt1__1down"] = {'bb': 0.145766,'cc': 0.153406,'c': 0.210849,'l': 0.489980}
frac[2]['mu']["btagbSF_0_pt1__1down"] = {'bb': 0.082685,'cc': 0.063923,'c': 0.205725,'l': 0.647667}
frac[3]['mu']["btagbSF_0_pt1__1down"] = {'bb': 0.105366,'cc': 0.098887,'c': 0.216331,'l': 0.579416}
frac[4]['mu']["btagbSF_0_pt1__1down"] = {'bb': 0.127869,'cc': 0.135505,'c': 0.207865,'l': 0.528761}
frac[5]['mu']["btagbSF_0_pt1__1down"] = {'bb': 0.137516,'cc': 0.149124,'c': 0.203235,'l': 0.510125}
# btagbSF_0_pt2__1up 
frac[2]['el']["btagbSF_0_pt2__1up"] = {'bb': 0.095386,'cc': 0.065570,'c': 0.209860,'l': 0.629184}
frac[3]['el']["btagbSF_0_pt2__1up"] = {'bb': 0.118573,'cc': 0.100587,'c': 0.219458,'l': 0.561382}
frac[4]['el']["btagbSF_0_pt2__1up"] = {'bb': 0.141296,'cc': 0.139439,'c': 0.215280,'l': 0.503985}
frac[5]['el']["btagbSF_0_pt2__1up"] = {'bb': 0.149553,'cc': 0.152726,'c': 0.209914,'l': 0.487807}
frac[2]['mu']["btagbSF_0_pt2__1up"] = {'bb': 0.083924,'cc': 0.063836,'c': 0.205448,'l': 0.646792}
frac[3]['mu']["btagbSF_0_pt2__1up"] = {'bb': 0.107555,'cc': 0.098645,'c': 0.215802,'l': 0.577998}
frac[4]['mu']["btagbSF_0_pt2__1up"] = {'bb': 0.131022,'cc': 0.135015,'c': 0.207114,'l': 0.526849}
frac[5]['mu']["btagbSF_0_pt2__1up"] = {'bb': 0.141078,'cc': 0.148508,'c': 0.202395,'l': 0.508018}
# btagbSF_0_pt2__1down 
frac[2]['el']["btagbSF_0_pt2__1down"] = {'bb': 0.095372,'cc': 0.065571,'c': 0.209863,'l': 0.629194}
frac[3]['el']["btagbSF_0_pt2__1down"] = {'bb': 0.118541,'cc': 0.100590,'c': 0.219466,'l': 0.561403}
frac[4]['el']["btagbSF_0_pt2__1down"] = {'bb': 0.141253,'cc': 0.139446,'c': 0.215290,'l': 0.504010}
frac[5]['el']["btagbSF_0_pt2__1down"] = {'bb': 0.149492,'cc': 0.152737,'c': 0.209929,'l': 0.487842}
frac[2]['mu']["btagbSF_0_pt2__1down"] = {'bb': 0.083913,'cc': 0.063837,'c': 0.205450,'l': 0.646800}
frac[3]['mu']["btagbSF_0_pt2__1down"] = {'bb': 0.107528,'cc': 0.098648,'c': 0.215808,'l': 0.578016}
frac[4]['mu']["btagbSF_0_pt2__1down"] = {'bb': 0.130978,'cc': 0.135022,'c': 0.207124,'l': 0.526876}
frac[5]['mu']["btagbSF_0_pt2__1down"] = {'bb': 0.141019,'cc': 0.148518,'c': 0.202409,'l': 0.508053}
# btagbSF_0_pt3__1up 
frac[2]['el']["btagbSF_0_pt3__1up"] = {'bb': 0.095384,'cc': 0.065570,'c': 0.209861,'l': 0.629186}
frac[3]['el']["btagbSF_0_pt3__1up"] = {'bb': 0.118570,'cc': 0.100587,'c': 0.219459,'l': 0.561384}
frac[4]['el']["btagbSF_0_pt3__1up"] = {'bb': 0.141305,'cc': 0.139438,'c': 0.215278,'l': 0.503980}
frac[5]['el']["btagbSF_0_pt3__1up"] = {'bb': 0.149562,'cc': 0.152724,'c': 0.209912,'l': 0.487802}
frac[2]['mu']["btagbSF_0_pt3__1up"] = {'bb': 0.083923,'cc': 0.063837,'c': 0.205448,'l': 0.646793}
frac[3]['mu']["btagbSF_0_pt3__1up"] = {'bb': 0.107552,'cc': 0.098645,'c': 0.215803,'l': 0.578000}
frac[4]['mu']["btagbSF_0_pt3__1up"] = {'bb': 0.131025,'cc': 0.135015,'c': 0.207113,'l': 0.526847}
frac[5]['mu']["btagbSF_0_pt3__1up"] = {'bb': 0.141084,'cc': 0.148507,'c': 0.202394,'l': 0.508015}
# btagbSF_0_pt3__1down 
frac[2]['el']["btagbSF_0_pt3__1down"] = {'bb': 0.095374,'cc': 0.065571,'c': 0.209863,'l': 0.629193}
frac[3]['el']["btagbSF_0_pt3__1down"] = {'bb': 0.118544,'cc': 0.100590,'c': 0.219466,'l': 0.561400}
frac[4]['el']["btagbSF_0_pt3__1down"] = {'bb': 0.141245,'cc': 0.139448,'c': 0.215293,'l': 0.504015}
frac[5]['el']["btagbSF_0_pt3__1down"] = {'bb': 0.149482,'cc': 0.152738,'c': 0.209932,'l': 0.487848}
frac[2]['mu']["btagbSF_0_pt3__1down"] = {'bb': 0.083914,'cc': 0.063837,'c': 0.205450,'l': 0.646799}
frac[3]['mu']["btagbSF_0_pt3__1down"] = {'bb': 0.107531,'cc': 0.098647,'c': 0.215808,'l': 0.578014}
frac[4]['mu']["btagbSF_0_pt3__1down"] = {'bb': 0.130975,'cc': 0.135023,'c': 0.207125,'l': 0.526877}
frac[5]['mu']["btagbSF_0_pt3__1down"] = {'bb': 0.141014,'cc': 0.148519,'c': 0.202410,'l': 0.508057}
# btagcSF_0__1up 
frac[2]['el']["btagcSF_0__1up"] = {'bb': 0.095332,'cc': 0.066719,'c': 0.212037,'l': 0.625911}
frac[3]['el']["btagcSF_0__1up"] = {'bb': 0.118484,'cc': 0.102504,'c': 0.221559,'l': 0.557453}
frac[4]['el']["btagcSF_0__1up"] = {'bb': 0.141201,'cc': 0.141838,'c': 0.217125,'l': 0.499836}
frac[5]['el']["btagcSF_0__1up"] = {'bb': 0.149464,'cc': 0.155391,'c': 0.211619,'l': 0.483526}
frac[2]['mu']["btagcSF_0__1up"] = {'bb': 0.083887,'cc': 0.064982,'c': 0.207439,'l': 0.643692}
frac[3]['mu']["btagcSF_0__1up"] = {'bb': 0.107480,'cc': 0.100621,'c': 0.217732,'l': 0.574167}
frac[4]['mu']["btagcSF_0__1up"] = {'bb': 0.130905,'cc': 0.137532,'c': 0.208973,'l': 0.522590}
frac[5]['mu']["btagcSF_0__1up"] = {'bb': 0.140965,'cc': 0.151258,'c': 0.204100,'l': 0.503678}
# btagcSF_0__1down 
frac[2]['el']["btagcSF_0__1down"] = {'bb': 0.095426,'cc': 0.064430,'c': 0.207660,'l': 0.632484}
frac[3]['el']["btagcSF_0__1down"] = {'bb': 0.118629,'cc': 0.098697,'c': 0.217324,'l': 0.565350}
frac[4]['el']["btagcSF_0__1down"] = {'bb': 0.141346,'cc': 0.137097,'c': 0.213391,'l': 0.508166}
frac[5]['el']["btagcSF_0__1down"] = {'bb': 0.149580,'cc': 0.150114,'c': 0.208171,'l': 0.492135}
frac[2]['mu']["btagcSF_0__1down"] = {'bb': 0.083950,'cc': 0.062700,'c': 0.203437,'l': 0.649913}
frac[3]['mu']["btagcSF_0__1down"] = {'bb': 0.107604,'cc': 0.096688,'c': 0.213844,'l': 0.581864}
frac[4]['mu']["btagcSF_0__1down"] = {'bb': 0.131095,'cc': 0.132533,'c': 0.205224,'l': 0.531148}
frac[5]['mu']["btagcSF_0__1down"] = {'bb': 0.141131,'cc': 0.145807,'c': 0.200659,'l': 0.512404}
# btagcSF_1__1up 
frac[2]['el']["btagcSF_1__1up"] = {'bb': 0.095388,'cc': 0.065166,'c': 0.209408,'l': 0.630038}
frac[3]['el']["btagcSF_1__1up"] = {'bb': 0.118575,'cc': 0.099876,'c': 0.219142,'l': 0.562407}
frac[4]['el']["btagcSF_1__1up"] = {'bb': 0.141309,'cc': 0.138383,'c': 0.215162,'l': 0.505146}
frac[5]['el']["btagcSF_1__1up"] = {'bb': 0.149557,'cc': 0.151561,'c': 0.209878,'l': 0.489004}
frac[2]['mu']["btagcSF_1__1up"] = {'bb': 0.083930,'cc': 0.063446,'c': 0.205001,'l': 0.647623}
frac[3]['mu']["btagcSF_1__1up"] = {'bb': 0.107556,'cc': 0.097956,'c': 0.215461,'l': 0.579028}
frac[4]['mu']["btagcSF_1__1up"] = {'bb': 0.131026,'cc': 0.134039,'c': 0.206964,'l': 0.527971}
frac[5]['mu']["btagcSF_1__1up"] = {'bb': 0.141074,'cc': 0.147402,'c': 0.202336,'l': 0.509188}
# btagcSF_1__1down 
frac[2]['el']["btagcSF_1__1down"] = {'bb': 0.095370,'cc': 0.065975,'c': 0.210314,'l': 0.628341}
frac[3]['el']["btagcSF_1__1down"] = {'bb': 0.118539,'cc': 0.101301,'c': 0.219781,'l': 0.560379}
frac[4]['el']["btagcSF_1__1down"] = {'bb': 0.141240,'cc': 0.140502,'c': 0.215407,'l': 0.502851}
frac[5]['el']["btagcSF_1__1down"] = {'bb': 0.149488,'cc': 0.153900,'c': 0.209965,'l': 0.486648}
frac[2]['mu']["btagcSF_1__1down"] = {'bb': 0.083906,'cc': 0.064228,'c': 0.205896,'l': 0.645970}
frac[3]['mu']["btagcSF_1__1down"] = {'bb': 0.107527,'cc': 0.099337,'c': 0.216148,'l': 0.576987}
frac[4]['mu']["btagcSF_1__1down"] = {'bb': 0.130974,'cc': 0.135998,'c': 0.207273,'l': 0.525756}
frac[5]['mu']["btagcSF_1__1down"] = {'bb': 0.141022,'cc': 0.149624,'c': 0.202468,'l': 0.506886}
# btagcSF_2__1up 
frac[2]['el']["btagcSF_2__1up"] = {'bb': 0.095384,'cc': 0.065611,'c': 0.209830,'l': 0.629176}
frac[3]['el']["btagcSF_2__1up"] = {'bb': 0.118570,'cc': 0.100645,'c': 0.219390,'l': 0.561395}
frac[4]['el']["btagcSF_2__1up"] = {'bb': 0.141294,'cc': 0.139483,'c': 0.215257,'l': 0.503965}
frac[5]['el']["btagcSF_2__1up"] = {'bb': 0.149542,'cc': 0.152763,'c': 0.209897,'l': 0.487798}
frac[2]['mu']["btagcSF_2__1up"] = {'bb': 0.083920,'cc': 0.063876,'c': 0.205434,'l': 0.646770}
frac[3]['mu']["btagcSF_2__1up"] = {'bb': 0.107544,'cc': 0.098677,'c': 0.215808,'l': 0.577971}
frac[4]['mu']["btagcSF_2__1up"] = {'bb': 0.131015,'cc': 0.135039,'c': 0.207100,'l': 0.526846}
frac[5]['mu']["btagcSF_2__1up"] = {'bb': 0.141071,'cc': 0.148522,'c': 0.202401,'l': 0.508006}
# btagcSF_2__1down 
frac[2]['el']["btagcSF_2__1down"] = {'bb': 0.095374,'cc': 0.065530,'c': 0.209894,'l': 0.629202}
frac[3]['el']["btagcSF_2__1down"] = {'bb': 0.118544,'cc': 0.100532,'c': 0.219535,'l': 0.561389}
frac[4]['el']["btagcSF_2__1down"] = {'bb': 0.141255,'cc': 0.139403,'c': 0.215313,'l': 0.504029}
frac[5]['el']["btagcSF_2__1down"] = {'bb': 0.149502,'cc': 0.152699,'c': 0.209947,'l': 0.487851}
frac[2]['mu']["btagcSF_2__1down"] = {'bb': 0.083917,'cc': 0.063797,'c': 0.205464,'l': 0.646822}
frac[3]['mu']["btagcSF_2__1down"] = {'bb': 0.107540,'cc': 0.098616,'c': 0.215802,'l': 0.578042}
frac[4]['mu']["btagcSF_2__1down"] = {'bb': 0.130985,'cc': 0.134998,'c': 0.207138,'l': 0.526879}
frac[5]['mu']["btagcSF_2__1down"] = {'bb': 0.141026,'cc': 0.148504,'c': 0.202404,'l': 0.508066}
# btagcSF_3__1up 
frac[2]['el']["btagcSF_3__1up"] = {'bb': 0.095374,'cc': 0.065671,'c': 0.210037,'l': 0.628918}
frac[3]['el']["btagcSF_3__1up"] = {'bb': 0.118553,'cc': 0.100762,'c': 0.219629,'l': 0.561057}
frac[4]['el']["btagcSF_3__1up"] = {'bb': 0.141268,'cc': 0.139715,'c': 0.215385,'l': 0.503633}
frac[5]['el']["btagcSF_3__1up"] = {'bb': 0.149516,'cc': 0.153033,'c': 0.210008,'l': 0.487442}
frac[2]['mu']["btagcSF_3__1up"] = {'bb': 0.083912,'cc': 0.063930,'c': 0.205622,'l': 0.646536}
frac[3]['mu']["btagcSF_3__1up"] = {'bb': 0.107532,'cc': 0.098825,'c': 0.215964,'l': 0.577679}
frac[4]['mu']["btagcSF_3__1up"] = {'bb': 0.130996,'cc': 0.135262,'c': 0.207249,'l': 0.526492}
frac[5]['mu']["btagcSF_3__1up"] = {'bb': 0.141043,'cc': 0.148781,'c': 0.202528,'l': 0.507649}
# btagcSF_3__1down 
frac[2]['el']["btagcSF_3__1down"] = {'bb': 0.095384,'cc': 0.065470,'c': 0.209686,'l': 0.629460}
frac[3]['el']["btagcSF_3__1down"] = {'bb': 0.118561,'cc': 0.100415,'c': 0.219296,'l': 0.561728}
frac[4]['el']["btagcSF_3__1down"] = {'bb': 0.141282,'cc': 0.139171,'c': 0.215185,'l': 0.504362}
frac[5]['el']["btagcSF_3__1down"] = {'bb': 0.149528,'cc': 0.152429,'c': 0.209836,'l': 0.488207}
frac[2]['mu']["btagcSF_3__1down"] = {'bb': 0.083925,'cc': 0.063744,'c': 0.205276,'l': 0.647056}
frac[3]['mu']["btagcSF_3__1down"] = {'bb': 0.107552,'cc': 0.098468,'c': 0.215646,'l': 0.578334}
frac[4]['mu']["btagcSF_3__1down"] = {'bb': 0.131004,'cc': 0.134775,'c': 0.206989,'l': 0.527233}
frac[5]['mu']["btagcSF_3__1down"] = {'bb': 0.141055,'cc': 0.148246,'c': 0.202276,'l': 0.508423}
# btagcSF_0_pt1__1up 
frac[2]['el']["btagcSF_0_pt1__1up"] = {'bb': 0.095330,'cc': 0.066841,'c': 0.211973,'l': 0.625856}
frac[3]['el']["btagcSF_0_pt1__1up"] = {'bb': 0.118486,'cc': 0.102716,'c': 0.221408,'l': 0.557390}
frac[4]['el']["btagcSF_0_pt1__1up"] = {'bb': 0.141187,'cc': 0.142328,'c': 0.216766,'l': 0.499719}
frac[5]['el']["btagcSF_0_pt1__1up"] = {'bb': 0.149444,'cc': 0.155932,'c': 0.211223,'l': 0.483401}
frac[2]['mu']["btagcSF_0_pt1__1up"] = {'bb': 0.083880,'cc': 0.065064,'c': 0.207410,'l': 0.643646}
frac[3]['mu']["btagcSF_0_pt1__1up"] = {'bb': 0.107472,'cc': 0.100832,'c': 0.217615,'l': 0.574081}
frac[4]['mu']["btagcSF_0_pt1__1up"] = {'bb': 0.130897,'cc': 0.137897,'c': 0.208695,'l': 0.522512}
frac[5]['mu']["btagcSF_0_pt1__1up"] = {'bb': 0.140942,'cc': 0.151721,'c': 0.203771,'l': 0.503565}
# btagcSF_0_pt1__1down 
frac[2]['el']["btagcSF_0_pt1__1down"] = {'bb': 0.095428,'cc': 0.064310,'c': 0.207723,'l': 0.632539}
frac[3]['el']["btagcSF_0_pt1__1down"] = {'bb': 0.118627,'cc': 0.098483,'c': 0.217476,'l': 0.565414}
frac[4]['el']["btagcSF_0_pt1__1down"] = {'bb': 0.141361,'cc': 0.136585,'c': 0.213758,'l': 0.508295}
frac[5]['el']["btagcSF_0_pt1__1down"] = {'bb': 0.149601,'cc': 0.149553,'c': 0.208575,'l': 0.492271}
frac[2]['mu']["btagcSF_0_pt1__1down"] = {'bb': 0.083956,'cc': 0.062618,'c': 0.203466,'l': 0.649960}
frac[3]['mu']["btagcSF_0_pt1__1down"] = {'bb': 0.107611,'cc': 0.096480,'c': 0.213960,'l': 0.581949}
frac[4]['mu']["btagcSF_0_pt1__1down"] = {'bb': 0.131103,'cc': 0.132161,'c': 0.205505,'l': 0.531232}
frac[5]['mu']["btagcSF_0_pt1__1down"] = {'bb': 0.141154,'cc': 0.145337,'c': 0.200990,'l': 0.512519}
# btagcSF_0_pt2__1up 
frac[2]['el']["btagcSF_0_pt2__1up"] = {'bb': 0.095382,'cc': 0.065463,'c': 0.209911,'l': 0.629245}
frac[3]['el']["btagcSF_0_pt2__1up"] = {'bb': 0.118548,'cc': 0.100414,'c': 0.219591,'l': 0.561446}
frac[4]['el']["btagcSF_0_pt2__1up"] = {'bb': 0.141276,'cc': 0.139053,'c': 0.215563,'l': 0.504108}
frac[5]['el']["btagcSF_0_pt2__1up"] = {'bb': 0.149530,'cc': 0.152307,'c': 0.210208,'l': 0.487955}
frac[2]['mu']["btagcSF_0_pt2__1up"] = {'bb': 0.083924,'cc': 0.063771,'c': 0.205471,'l': 0.646835}
frac[3]['mu']["btagcSF_0_pt2__1up"] = {'bb': 0.107552,'cc': 0.098482,'c': 0.215864,'l': 0.578102}
frac[4]['mu']["btagcSF_0_pt2__1up"] = {'bb': 0.130998,'cc': 0.134757,'c': 0.207296,'l': 0.526950}
frac[5]['mu']["btagcSF_0_pt2__1up"] = {'bb': 0.141057,'cc': 0.148178,'c': 0.202605,'l': 0.508161}
# btagcSF_0_pt2__1down 
frac[2]['el']["btagcSF_0_pt2__1down"] = {'bb': 0.095376,'cc': 0.065678,'c': 0.209813,'l': 0.629133}
frac[3]['el']["btagcSF_0_pt2__1down"] = {'bb': 0.118566,'cc': 0.100761,'c': 0.219334,'l': 0.561340}
frac[4]['el']["btagcSF_0_pt2__1down"] = {'bb': 0.141273,'cc': 0.139837,'c': 0.215006,'l': 0.503883}
frac[5]['el']["btagcSF_0_pt2__1down"] = {'bb': 0.149515,'cc': 0.153157,'c': 0.209635,'l': 0.487693}
frac[2]['mu']["btagcSF_0_pt2__1down"] = {'bb': 0.083913,'cc': 0.063902,'c': 0.205427,'l': 0.646758}
frac[3]['mu']["btagcSF_0_pt2__1down"] = {'bb': 0.107531,'cc': 0.098811,'c': 0.215746,'l': 0.577912}
frac[4]['mu']["btagcSF_0_pt2__1down"] = {'bb': 0.131003,'cc': 0.135283,'c': 0.206941,'l': 0.526773}
frac[5]['mu']["btagcSF_0_pt2__1down"] = {'bb': 0.141041,'cc': 0.148848,'c': 0.202199,'l': 0.507911}
# btagcSF_0_pt3__1up 
frac[2]['el']["btagcSF_0_pt3__1up"] = {'bb': 0.095379,'cc': 0.065557,'c': 0.209877,'l': 0.629188}
frac[3]['el']["btagcSF_0_pt3__1up"] = {'bb': 0.118564,'cc': 0.100549,'c': 0.219485,'l': 0.561402}
frac[4]['el']["btagcSF_0_pt3__1up"] = {'bb': 0.141287,'cc': 0.139334,'c': 0.215370,'l': 0.504008}
frac[5]['el']["btagcSF_0_pt3__1up"] = {'bb': 0.149535,'cc': 0.152606,'c': 0.210035,'l': 0.487824}
frac[2]['mu']["btagcSF_0_pt3__1up"] = {'bb': 0.083920,'cc': 0.063821,'c': 0.205456,'l': 0.646804}
frac[3]['mu']["btagcSF_0_pt3__1up"] = {'bb': 0.107540,'cc': 0.098601,'c': 0.215862,'l': 0.577997}
frac[4]['mu']["btagcSF_0_pt3__1up"] = {'bb': 0.131011,'cc': 0.134912,'c': 0.207221,'l': 0.526856}
frac[5]['mu']["btagcSF_0_pt3__1up"] = {'bb': 0.141063,'cc': 0.148381,'c': 0.202530,'l': 0.508026}
# btagcSF_0_pt3__1down 
frac[2]['el']["btagcSF_0_pt3__1down"] = {'bb': 0.095379,'cc': 0.065584,'c': 0.209847,'l': 0.629190}
frac[3]['el']["btagcSF_0_pt3__1down"] = {'bb': 0.118550,'cc': 0.100629,'c': 0.219440,'l': 0.561382}
frac[4]['el']["btagcSF_0_pt3__1down"] = {'bb': 0.141262,'cc': 0.139553,'c': 0.215200,'l': 0.503986}
frac[5]['el']["btagcSF_0_pt3__1down"] = {'bb': 0.149509,'cc': 0.152857,'c': 0.209809,'l': 0.487825}
frac[2]['mu']["btagcSF_0_pt3__1down"] = {'bb': 0.083917,'cc': 0.063853,'c': 0.205442,'l': 0.646788}
frac[3]['mu']["btagcSF_0_pt3__1down"] = {'bb': 0.107543,'cc': 0.098691,'c': 0.215748,'l': 0.578017}
frac[4]['mu']["btagcSF_0_pt3__1down"] = {'bb': 0.130989,'cc': 0.135124,'c': 0.207017,'l': 0.526870}
frac[5]['mu']["btagcSF_0_pt3__1down"] = {'bb': 0.141034,'cc': 0.148644,'c': 0.202275,'l': 0.508047}
# btaglSF_0__1up 
frac[2]['el']["btaglSF_0__1up"] = {'bb': 0.095278,'cc': 0.065432,'c': 0.209613,'l': 0.629677}
frac[3]['el']["btaglSF_0__1up"] = {'bb': 0.118372,'cc': 0.100358,'c': 0.219303,'l': 0.561967}
frac[4]['el']["btaglSF_0__1up"] = {'bb': 0.141028,'cc': 0.139126,'c': 0.215241,'l': 0.504605}
frac[5]['el']["btaglSF_0__1up"] = {'bb': 0.149273,'cc': 0.152450,'c': 0.209943,'l': 0.488334}
frac[2]['mu']["btaglSF_0__1up"] = {'bb': 0.083824,'cc': 0.063737,'c': 0.205256,'l': 0.647183}
frac[3]['mu']["btaglSF_0__1up"] = {'bb': 0.107367,'cc': 0.098430,'c': 0.215581,'l': 0.578622}
frac[4]['mu']["btaglSF_0__1up"] = {'bb': 0.130727,'cc': 0.134844,'c': 0.207065,'l': 0.527365}
frac[5]['mu']["btaglSF_0__1up"] = {'bb': 0.140777,'cc': 0.148338,'c': 0.202385,'l': 0.508500}
# btaglSF_0__1down 
frac[2]['el']["btaglSF_0__1down"] = {'bb': 0.095480,'cc': 0.065709,'c': 0.210110,'l': 0.628700}
frac[3]['el']["btaglSF_0__1down"] = {'bb': 0.118743,'cc': 0.100819,'c': 0.219624,'l': 0.560813}
frac[4]['el']["btaglSF_0__1down"] = {'bb': 0.141522,'cc': 0.139763,'c': 0.215322,'l': 0.503393}
frac[5]['el']["btaglSF_0__1down"] = {'bb': 0.149771,'cc': 0.153015,'c': 0.209898,'l': 0.487316}
frac[2]['mu']["btaglSF_0__1down"] = {'bb': 0.084014,'cc': 0.063937,'c': 0.205643,'l': 0.646406}
frac[3]['mu']["btaglSF_0__1down"] = {'bb': 0.107717,'cc': 0.098865,'c': 0.216031,'l': 0.577386}
frac[4]['mu']["btaglSF_0__1down"] = {'bb': 0.131274,'cc': 0.135197,'c': 0.207174,'l': 0.526354}
frac[5]['mu']["btaglSF_0__1down"] = {'bb': 0.141321,'cc': 0.148695,'c': 0.202422,'l': 0.507562}
# btaglSF_1__1up 
frac[2]['el']["btaglSF_1__1up"] = {'bb': 0.095442,'cc': 0.065657,'c': 0.210028,'l': 0.628873}
frac[3]['el']["btaglSF_1__1up"] = {'bb': 0.118679,'cc': 0.100743,'c': 0.219578,'l': 0.561000}
frac[4]['el']["btaglSF_1__1up"] = {'bb': 0.141439,'cc': 0.139666,'c': 0.215321,'l': 0.503574}
frac[5]['el']["btaglSF_1__1up"] = {'bb': 0.149682,'cc': 0.152920,'c': 0.209930,'l': 0.487468}
frac[2]['mu']["btaglSF_1__1up"] = {'bb': 0.083978,'cc': 0.063907,'c': 0.205585,'l': 0.646529}
frac[3]['mu']["btaglSF_1__1up"] = {'bb': 0.107660,'cc': 0.098792,'c': 0.215951,'l': 0.577597}
frac[4]['mu']["btaglSF_1__1up"] = {'bb': 0.131173,'cc': 0.135169,'c': 0.207188,'l': 0.526470}
frac[5]['mu']["btaglSF_1__1up"] = {'bb': 0.141217,'cc': 0.148656,'c': 0.202452,'l': 0.507676}
# btaglSF_1__1down 
frac[2]['el']["btaglSF_1__1down"] = {'bb': 0.095316,'cc': 0.065484,'c': 0.209696,'l': 0.629504}
frac[3]['el']["btaglSF_1__1down"] = {'bb': 0.118436,'cc': 0.100434,'c': 0.219348,'l': 0.561782}
frac[4]['el']["btaglSF_1__1down"] = {'bb': 0.141111,'cc': 0.139221,'c': 0.215247,'l': 0.504421}
frac[5]['el']["btaglSF_1__1down"] = {'bb': 0.149363,'cc': 0.152543,'c': 0.209913,'l': 0.488181}
frac[2]['mu']["btaglSF_1__1down"] = {'bb': 0.083859,'cc': 0.063767,'c': 0.205313,'l': 0.647062}
frac[3]['mu']["btaglSF_1__1down"] = {'bb': 0.107424,'cc': 0.098501,'c': 0.215660,'l': 0.578415}
frac[4]['mu']["btaglSF_1__1down"] = {'bb': 0.130827,'cc': 0.134871,'c': 0.207050,'l': 0.527252}
frac[5]['mu']["btaglSF_1__1down"] = {'bb': 0.140881,'cc': 0.148373,'c': 0.202354,'l': 0.508393}
# btaglSF_2__1up 
frac[2]['el']["btaglSF_2__1up"] = {'bb': 0.095359,'cc': 0.065547,'c': 0.209787,'l': 0.629307}
frac[3]['el']["btaglSF_2__1up"] = {'bb': 0.118521,'cc': 0.100545,'c': 0.219439,'l': 0.561495}
frac[4]['el']["btaglSF_2__1up"] = {'bb': 0.141209,'cc': 0.139359,'c': 0.215239,'l': 0.504193}
frac[5]['el']["btaglSF_2__1up"] = {'bb': 0.149463,'cc': 0.152672,'c': 0.209884,'l': 0.487980}
frac[2]['mu']["btaglSF_2__1up"] = {'bb': 0.083900,'cc': 0.063811,'c': 0.205393,'l': 0.646895}
frac[3]['mu']["btaglSF_2__1up"] = {'bb': 0.107503,'cc': 0.098593,'c': 0.215753,'l': 0.578151}
frac[4]['mu']["btaglSF_2__1up"] = {'bb': 0.130943,'cc': 0.134890,'c': 0.207101,'l': 0.527065}
frac[5]['mu']["btaglSF_2__1up"] = {'bb': 0.140999,'cc': 0.148403,'c': 0.202383,'l': 0.508215}
# btaglSF_2__1down 
frac[2]['el']["btaglSF_2__1down"] = {'bb': 0.095399,'cc': 0.065593,'c': 0.209937,'l': 0.629072}
frac[3]['el']["btaglSF_2__1down"] = {'bb': 0.118593,'cc': 0.100632,'c': 0.219486,'l': 0.561289}
frac[4]['el']["btaglSF_2__1down"] = {'bb': 0.141340,'cc': 0.139527,'c': 0.215332,'l': 0.503800}
frac[5]['el']["btaglSF_2__1down"] = {'bb': 0.149581,'cc': 0.152790,'c': 0.209960,'l': 0.487669}
frac[2]['mu']["btaglSF_2__1down"] = {'bb': 0.083936,'cc': 0.063862,'c': 0.205505,'l': 0.646697}
frac[3]['mu']["btaglSF_2__1down"] = {'bb': 0.107580,'cc': 0.098700,'c': 0.215858,'l': 0.577862}
frac[4]['mu']["btaglSF_2__1down"] = {'bb': 0.131056,'cc': 0.135147,'c': 0.207136,'l': 0.526660}
frac[5]['mu']["btaglSF_2__1down"] = {'bb': 0.141098,'cc': 0.148623,'c': 0.202422,'l': 0.507857}
# btaglSF_3__1up 
frac[2]['el']["btaglSF_3__1up"] = {'bb': 0.095382,'cc': 0.065578,'c': 0.209849,'l': 0.629191}
frac[3]['el']["btaglSF_3__1up"] = {'bb': 0.118564,'cc': 0.100602,'c': 0.219479,'l': 0.561354}
frac[4]['el']["btaglSF_3__1up"] = {'bb': 0.141266,'cc': 0.139445,'c': 0.215247,'l': 0.504041}
frac[5]['el']["btaglSF_3__1up"] = {'bb': 0.149518,'cc': 0.152741,'c': 0.209890,'l': 0.487851}
frac[2]['mu']["btaglSF_3__1up"] = {'bb': 0.083922,'cc': 0.063837,'c': 0.205446,'l': 0.646795}
frac[3]['mu']["btaglSF_3__1up"] = {'bb': 0.107549,'cc': 0.098648,'c': 0.215804,'l': 0.577998}
frac[4]['mu']["btaglSF_3__1up"] = {'bb': 0.131007,'cc': 0.134950,'c': 0.207140,'l': 0.526904}
frac[5]['mu']["btaglSF_3__1up"] = {'bb': 0.141060,'cc': 0.148460,'c': 0.202415,'l': 0.508065}
# btaglSF_3__1down 
frac[2]['el']["btaglSF_3__1down"] = {'bb': 0.095376,'cc': 0.065562,'c': 0.209875,'l': 0.629187}
frac[3]['el']["btaglSF_3__1down"] = {'bb': 0.118550,'cc': 0.100574,'c': 0.219445,'l': 0.561430}
frac[4]['el']["btaglSF_3__1down"] = {'bb': 0.141283,'cc': 0.139440,'c': 0.215324,'l': 0.503953}
frac[5]['el']["btaglSF_3__1down"] = {'bb': 0.149527,'cc': 0.152721,'c': 0.209954,'l': 0.487799}
frac[2]['mu']["btaglSF_3__1down"] = {'bb': 0.083914,'cc': 0.063836,'c': 0.205452,'l': 0.646798}
frac[3]['mu']["btaglSF_3__1down"] = {'bb': 0.107534,'cc': 0.098645,'c': 0.215806,'l': 0.578015}
frac[4]['mu']["btaglSF_3__1down"] = {'bb': 0.130992,'cc': 0.135088,'c': 0.207098,'l': 0.526822}
frac[5]['mu']["btaglSF_3__1down"] = {'bb': 0.141037,'cc': 0.148567,'c': 0.202389,'l': 0.508007}
# btaglSF_4__1up 
frac[2]['el']["btaglSF_4__1up"] = {'bb': 0.095402,'cc': 0.065600,'c': 0.209918,'l': 0.629080}
frac[3]['el']["btaglSF_4__1up"] = {'bb': 0.118603,'cc': 0.100647,'c': 0.219514,'l': 0.561237}
frac[4]['el']["btaglSF_4__1up"] = {'bb': 0.141333,'cc': 0.139531,'c': 0.215292,'l': 0.503844}
frac[5]['el']["btaglSF_4__1up"] = {'bb': 0.149577,'cc': 0.152809,'c': 0.209932,'l': 0.487682}
frac[2]['mu']["btaglSF_4__1up"] = {'bb': 0.083940,'cc': 0.063867,'c': 0.205504,'l': 0.646689}
frac[3]['mu']["btaglSF_4__1up"] = {'bb': 0.107591,'cc': 0.098706,'c': 0.215850,'l': 0.577853}
frac[4]['mu']["btaglSF_4__1up"] = {'bb': 0.131061,'cc': 0.135086,'c': 0.207159,'l': 0.526694}
frac[5]['mu']["btaglSF_4__1up"] = {'bb': 0.141107,'cc': 0.148571,'c': 0.202440,'l': 0.507882}
# btaglSF_4__1down 
frac[2]['el']["btaglSF_4__1down"] = {'bb': 0.095356,'cc': 0.065540,'c': 0.209805,'l': 0.629298}
frac[3]['el']["btaglSF_4__1down"] = {'bb': 0.118512,'cc': 0.100530,'c': 0.219411,'l': 0.561547}
frac[4]['el']["btaglSF_4__1down"] = {'bb': 0.141216,'cc': 0.139355,'c': 0.215278,'l': 0.504150}
frac[5]['el']["btaglSF_4__1down"] = {'bb': 0.149467,'cc': 0.152654,'c': 0.209911,'l': 0.487968}
frac[2]['mu']["btaglSF_4__1down"] = {'bb': 0.083896,'cc': 0.063807,'c': 0.205394,'l': 0.646903}
frac[3]['mu']["btaglSF_4__1down"] = {'bb': 0.107493,'cc': 0.098587,'c': 0.215760,'l': 0.578161}
frac[4]['mu']["btaglSF_4__1down"] = {'bb': 0.130939,'cc': 0.134952,'c': 0.207079,'l': 0.527031}
frac[5]['mu']["btaglSF_4__1down"] = {'bb': 0.140991,'cc': 0.148456,'c': 0.202364,'l': 0.508189}
# btaglSF_5__1up 
frac[2]['el']["btaglSF_5__1up"] = {'bb': 0.095372,'cc': 0.065562,'c': 0.209845,'l': 0.629220}
frac[3]['el']["btaglSF_5__1up"] = {'bb': 0.118546,'cc': 0.100575,'c': 0.219451,'l': 0.561428}
frac[4]['el']["btaglSF_5__1up"] = {'bb': 0.141255,'cc': 0.139420,'c': 0.215277,'l': 0.504049}
frac[5]['el']["btaglSF_5__1up"] = {'bb': 0.149503,'cc': 0.152707,'c': 0.209915,'l': 0.487875}
frac[2]['mu']["btaglSF_5__1up"] = {'bb': 0.083911,'cc': 0.063828,'c': 0.205430,'l': 0.646830}
frac[3]['mu']["btaglSF_5__1up"] = {'bb': 0.107527,'cc': 0.098627,'c': 0.215792,'l': 0.578054}
frac[4]['mu']["btaglSF_5__1up"] = {'bb': 0.130984,'cc': 0.134989,'c': 0.207108,'l': 0.526919}
frac[5]['mu']["btaglSF_5__1up"] = {'bb': 0.141034,'cc': 0.148492,'c': 0.202393,'l': 0.508082}
# btaglSF_5__1down 
frac[2]['el']["btaglSF_5__1down"] = {'bb': 0.095386,'cc': 0.065578,'c': 0.209878,'l': 0.629158}
frac[3]['el']["btaglSF_5__1down"] = {'bb': 0.118568,'cc': 0.100602,'c': 0.219473,'l': 0.561357}
frac[4]['el']["btaglSF_5__1down"] = {'bb': 0.141294,'cc': 0.139466,'c': 0.215294,'l': 0.503946}
frac[5]['el']["btaglSF_5__1down"] = {'bb': 0.149541,'cc': 0.152755,'c': 0.209929,'l': 0.487774}
frac[2]['mu']["btaglSF_5__1down"] = {'bb': 0.083925,'cc': 0.063846,'c': 0.205468,'l': 0.646762}
frac[3]['mu']["btaglSF_5__1down"] = {'bb': 0.107556,'cc': 0.098665,'c': 0.215819,'l': 0.577960}
frac[4]['mu']["btaglSF_5__1down"] = {'bb': 0.131016,'cc': 0.135049,'c': 0.207130,'l': 0.526805}
frac[5]['mu']["btaglSF_5__1down"] = {'bb': 0.141063,'cc': 0.148535,'c': 0.202412,'l': 0.507990}
# btaglSF_6__1up 
frac[2]['el']["btaglSF_6__1up"] = {'bb': 0.095376,'cc': 0.065566,'c': 0.209853,'l': 0.629205}
frac[3]['el']["btaglSF_6__1up"] = {'bb': 0.118551,'cc': 0.100581,'c': 0.219456,'l': 0.561412}
frac[4]['el']["btaglSF_6__1up"] = {'bb': 0.141265,'cc': 0.139430,'c': 0.215281,'l': 0.504024}
frac[5]['el']["btaglSF_6__1up"] = {'bb': 0.149512,'cc': 0.152718,'c': 0.209919,'l': 0.487850}
frac[2]['mu']["btaglSF_6__1up"] = {'bb': 0.083915,'cc': 0.063832,'c': 0.205440,'l': 0.646813}
frac[3]['mu']["btaglSF_6__1up"] = {'bb': 0.107534,'cc': 0.098637,'c': 0.215799,'l': 0.578030}
frac[4]['mu']["btaglSF_6__1up"] = {'bb': 0.130990,'cc': 0.135005,'c': 0.207117,'l': 0.526888}
frac[5]['mu']["btaglSF_6__1up"] = {'bb': 0.141040,'cc': 0.148503,'c': 0.202400,'l': 0.508057}
# btaglSF_6__1down 
frac[2]['el']["btaglSF_6__1down"] = {'bb': 0.095382,'cc': 0.065574,'c': 0.209870,'l': 0.629173}
frac[3]['el']["btaglSF_6__1down"] = {'bb': 0.118563,'cc': 0.100596,'c': 0.219468,'l': 0.561372}
frac[4]['el']["btaglSF_6__1down"] = {'bb': 0.141285,'cc': 0.139456,'c': 0.215289,'l': 0.503970}
frac[5]['el']["btaglSF_6__1down"] = {'bb': 0.149532,'cc': 0.152744,'c': 0.209925,'l': 0.487800}
frac[2]['mu']["btaglSF_6__1down"] = {'bb': 0.083922,'cc': 0.063841,'c': 0.205458,'l': 0.646779}
frac[3]['mu']["btaglSF_6__1down"] = {'bb': 0.107549,'cc': 0.098656,'c': 0.215812,'l': 0.577984}
frac[4]['mu']["btaglSF_6__1down"] = {'bb': 0.131009,'cc': 0.135032,'c': 0.207121,'l': 0.526837}
frac[5]['mu']["btaglSF_6__1down"] = {'bb': 0.141057,'cc': 0.148523,'c': 0.202405,'l': 0.508015}
# btaglSF_7__1up 
frac[2]['el']["btaglSF_7__1up"] = {'bb': 0.095379,'cc': 0.065569,'c': 0.209858,'l': 0.629195}
frac[3]['el']["btaglSF_7__1up"] = {'bb': 0.118553,'cc': 0.100585,'c': 0.219459,'l': 0.561404}
frac[4]['el']["btaglSF_7__1up"] = {'bb': 0.141272,'cc': 0.139437,'c': 0.215288,'l': 0.504003}
frac[5]['el']["btaglSF_7__1up"] = {'bb': 0.149520,'cc': 0.152729,'c': 0.209922,'l': 0.487829}
frac[2]['mu']["btaglSF_7__1up"] = {'bb': 0.083918,'cc': 0.063835,'c': 0.205449,'l': 0.646798}
frac[3]['mu']["btaglSF_7__1up"] = {'bb': 0.107541,'cc': 0.098644,'c': 0.215805,'l': 0.578011}
frac[4]['mu']["btaglSF_7__1up"] = {'bb': 0.130999,'cc': 0.135019,'c': 0.207112,'l': 0.526871}
frac[5]['mu']["btaglSF_7__1up"] = {'bb': 0.141047,'cc': 0.148511,'c': 0.202396,'l': 0.508047}
# btaglSF_7__1down 
frac[2]['el']["btaglSF_7__1down"] = {'bb': 0.095380,'cc': 0.065572,'c': 0.209865,'l': 0.629183}
frac[3]['el']["btaglSF_7__1down"] = {'bb': 0.118561,'cc': 0.100592,'c': 0.219466,'l': 0.561381}
frac[4]['el']["btaglSF_7__1down"] = {'bb': 0.141277,'cc': 0.139448,'c': 0.215282,'l': 0.503992}
frac[5]['el']["btaglSF_7__1down"] = {'bb': 0.149524,'cc': 0.152734,'c': 0.209921,'l': 0.487821}
frac[2]['mu']["btaglSF_7__1down"] = {'bb': 0.083919,'cc': 0.063838,'c': 0.205449,'l': 0.646794}
frac[3]['mu']["btaglSF_7__1down"] = {'bb': 0.107543,'cc': 0.098648,'c': 0.215806,'l': 0.578003}
frac[4]['mu']["btaglSF_7__1down"] = {'bb': 0.131001,'cc': 0.135018,'c': 0.207126,'l': 0.526854}
frac[5]['mu']["btaglSF_7__1down"] = {'bb': 0.141051,'cc': 0.148516,'c': 0.202408,'l': 0.508025}
# btaglSF_8__1up 
frac[2]['el']["btaglSF_8__1up"] = {'bb': 0.095378,'cc': 0.065568,'c': 0.209857,'l': 0.629198}
frac[3]['el']["btaglSF_8__1up"] = {'bb': 0.118551,'cc': 0.100584,'c': 0.219457,'l': 0.561408}
frac[4]['el']["btaglSF_8__1up"] = {'bb': 0.141270,'cc': 0.139436,'c': 0.215287,'l': 0.504007}
frac[5]['el']["btaglSF_8__1up"] = {'bb': 0.149518,'cc': 0.152726,'c': 0.209922,'l': 0.487834}
frac[2]['mu']["btaglSF_8__1up"] = {'bb': 0.083917,'cc': 0.063835,'c': 0.205447,'l': 0.646801}
frac[3]['mu']["btaglSF_8__1up"] = {'bb': 0.107539,'cc': 0.098642,'c': 0.215803,'l': 0.578016}
frac[4]['mu']["btaglSF_8__1up"] = {'bb': 0.130996,'cc': 0.135015,'c': 0.207117,'l': 0.526872}
frac[5]['mu']["btaglSF_8__1up"] = {'bb': 0.141044,'cc': 0.148508,'c': 0.202400,'l': 0.508049}
# btaglSF_8__1down 
frac[2]['el']["btaglSF_8__1down"] = {'bb': 0.095380,'cc': 0.065573,'c': 0.209867,'l': 0.629180}
frac[3]['el']["btaglSF_8__1down"] = {'bb': 0.118563,'cc': 0.100593,'c': 0.219467,'l': 0.561377}
frac[4]['el']["btaglSF_8__1down"] = {'bb': 0.141279,'cc': 0.139450,'c': 0.215283,'l': 0.503988}
frac[5]['el']["btaglSF_8__1down"] = {'bb': 0.149527,'cc': 0.152736,'c': 0.209922,'l': 0.487815}
frac[2]['mu']["btaglSF_8__1down"] = {'bb': 0.083919,'cc': 0.063839,'c': 0.205451,'l': 0.646791}
frac[3]['mu']["btaglSF_8__1down"] = {'bb': 0.107545,'cc': 0.098650,'c': 0.215807,'l': 0.577998}
frac[4]['mu']["btaglSF_8__1down"] = {'bb': 0.131004,'cc': 0.135023,'c': 0.207121,'l': 0.526853}
frac[5]['mu']["btaglSF_8__1down"] = {'bb': 0.141053,'cc': 0.148519,'c': 0.202405,'l': 0.508023}
# btaglSF_9__1up 
frac[2]['el']["btaglSF_9__1up"] = {'bb': 0.095381,'cc': 0.065572,'c': 0.209865,'l': 0.629182}
frac[3]['el']["btaglSF_9__1up"] = {'bb': 0.118560,'cc': 0.100592,'c': 0.219465,'l': 0.561383}
frac[4]['el']["btaglSF_9__1up"] = {'bb': 0.141279,'cc': 0.139449,'c': 0.215286,'l': 0.503986}
frac[5]['el']["btaglSF_9__1up"] = {'bb': 0.149526,'cc': 0.152737,'c': 0.209923,'l': 0.487814}
frac[2]['mu']["btaglSF_9__1up"] = {'bb': 0.083920,'cc': 0.063839,'c': 0.205453,'l': 0.646788}
frac[3]['mu']["btaglSF_9__1up"] = {'bb': 0.107545,'cc': 0.098650,'c': 0.215808,'l': 0.577997}
frac[4]['mu']["btaglSF_9__1up"] = {'bb': 0.131004,'cc': 0.135024,'c': 0.207120,'l': 0.526852}
frac[5]['mu']["btaglSF_9__1up"] = {'bb': 0.141053,'cc': 0.148517,'c': 0.202403,'l': 0.508027}
# btaglSF_9__1down 
frac[2]['el']["btaglSF_9__1down"] = {'bb': 0.095377,'cc': 0.065568,'c': 0.209858,'l': 0.629196}
frac[3]['el']["btaglSF_9__1down"] = {'bb': 0.118554,'cc': 0.100585,'c': 0.219460,'l': 0.561401}
frac[4]['el']["btaglSF_9__1down"] = {'bb': 0.141271,'cc': 0.139437,'c': 0.215284,'l': 0.504008}
frac[5]['el']["btaglSF_9__1down"] = {'bb': 0.149518,'cc': 0.152725,'c': 0.209921,'l': 0.487836}
frac[2]['mu']["btaglSF_9__1down"] = {'bb': 0.083917,'cc': 0.063835,'c': 0.205444,'l': 0.646804}
frac[3]['mu']["btaglSF_9__1down"] = {'bb': 0.107538,'cc': 0.098642,'c': 0.215803,'l': 0.578017}
frac[4]['mu']["btaglSF_9__1down"] = {'bb': 0.130996,'cc': 0.135014,'c': 0.207118,'l': 0.526873}
frac[5]['mu']["btaglSF_9__1down"] = {'bb': 0.141045,'cc': 0.148509,'c': 0.202401,'l': 0.508044}
# btaglSF_10__1up 
frac[2]['el']["btaglSF_10__1up"] = {'bb': 0.095380,'cc': 0.065572,'c': 0.209865,'l': 0.629183}
frac[3]['el']["btaglSF_10__1up"] = {'bb': 0.118560,'cc': 0.100591,'c': 0.219465,'l': 0.561384}
frac[4]['el']["btaglSF_10__1up"] = {'bb': 0.141278,'cc': 0.139447,'c': 0.215285,'l': 0.503990}
frac[5]['el']["btaglSF_10__1up"] = {'bb': 0.149526,'cc': 0.152735,'c': 0.209922,'l': 0.487817}
frac[2]['mu']["btaglSF_10__1up"] = {'bb': 0.083919,'cc': 0.063838,'c': 0.205451,'l': 0.646791}
frac[3]['mu']["btaglSF_10__1up"] = {'bb': 0.107544,'cc': 0.098650,'c': 0.215807,'l': 0.577999}
frac[4]['mu']["btaglSF_10__1up"] = {'bb': 0.131003,'cc': 0.135022,'c': 0.207121,'l': 0.526854}
frac[5]['mu']["btaglSF_10__1up"] = {'bb': 0.141051,'cc': 0.148516,'c': 0.202404,'l': 0.508028}
# btaglSF_10__1down 
frac[2]['el']["btaglSF_10__1down"] = {'bb': 0.095378,'cc': 0.065568,'c': 0.209859,'l': 0.629195}
frac[3]['el']["btaglSF_10__1down"] = {'bb': 0.118554,'cc': 0.100586,'c': 0.219460,'l': 0.561400}
frac[4]['el']["btaglSF_10__1down"] = {'bb': 0.141272,'cc': 0.139439,'c': 0.215285,'l': 0.504005}
frac[5]['el']["btaglSF_10__1down"] = {'bb': 0.149519,'cc': 0.152727,'c': 0.209922,'l': 0.487833}
frac[2]['mu']["btaglSF_10__1down"] = {'bb': 0.083917,'cc': 0.063835,'c': 0.205447,'l': 0.646801}
frac[3]['mu']["btaglSF_10__1down"] = {'bb': 0.107539,'cc': 0.098643,'c': 0.215803,'l': 0.578015}
frac[4]['mu']["btaglSF_10__1down"] = {'bb': 0.130997,'cc': 0.135015,'c': 0.207117,'l': 0.526871}
frac[5]['mu']["btaglSF_10__1down"] = {'bb': 0.141046,'cc': 0.148510,'c': 0.202400,'l': 0.508044}
# btageSF_0__1up 
frac[2]['el']["btageSF_0__1up"] = {'bb': 0.095379,'cc': 0.065571,'c': 0.209860,'l': 0.629190}
frac[3]['el']["btageSF_0__1up"] = {'bb': 0.118554,'cc': 0.100591,'c': 0.219459,'l': 0.561396}
frac[4]['el']["btageSF_0__1up"] = {'bb': 0.141267,'cc': 0.139447,'c': 0.215285,'l': 0.504001}
frac[5]['el']["btageSF_0__1up"] = {'bb': 0.149510,'cc': 0.152740,'c': 0.209917,'l': 0.487833}
frac[2]['mu']["btageSF_0__1up"] = {'bb': 0.083917,'cc': 0.063839,'c': 0.205447,'l': 0.646796}
frac[3]['mu']["btageSF_0__1up"] = {'bb': 0.107540,'cc': 0.098649,'c': 0.215799,'l': 0.578012}
frac[4]['mu']["btageSF_0__1up"] = {'bb': 0.130994,'cc': 0.135024,'c': 0.207111,'l': 0.526871}
frac[5]['mu']["btageSF_0__1up"] = {'bb': 0.141039,'cc': 0.148519,'c': 0.202393,'l': 0.508050}
# btageSF_0__1down 
frac[2]['el']["btageSF_0__1down"] = {'bb': 0.095379,'cc': 0.065569,'c': 0.209864,'l': 0.629188}
frac[3]['el']["btageSF_0__1down"] = {'bb': 0.118560,'cc': 0.100586,'c': 0.219466,'l': 0.561388}
frac[4]['el']["btageSF_0__1down"] = {'bb': 0.141283,'cc': 0.139439,'c': 0.215285,'l': 0.503993}
frac[5]['el']["btageSF_0__1down"] = {'bb': 0.149534,'cc': 0.152722,'c': 0.209927,'l': 0.487817}
frac[2]['mu']["btageSF_0__1down"] = {'bb': 0.083919,'cc': 0.063834,'c': 0.205450,'l': 0.646796}
frac[3]['mu']["btageSF_0__1down"] = {'bb': 0.107543,'cc': 0.098643,'c': 0.215812,'l': 0.578002}
frac[4]['mu']["btageSF_0__1down"] = {'bb': 0.131006,'cc': 0.135013,'c': 0.207127,'l': 0.526854}
frac[5]['mu']["btageSF_0__1down"] = {'bb': 0.141059,'cc': 0.148508,'c': 0.202412,'l': 0.508022}
# btageSF_1__1up 
frac[2]['el']["btageSF_1__1up"] = {'bb': 0.096152,'cc': 0.065746,'c': 0.210426,'l': 0.627676}
frac[3]['el']["btageSF_1__1up"] = {'bb': 0.119899,'cc': 0.100790,'c': 0.219975,'l': 0.559336}
frac[4]['el']["btageSF_1__1up"] = {'bb': 0.143216,'cc': 0.139436,'c': 0.215708,'l': 0.501641}
frac[5]['el']["btageSF_1__1up"] = {'bb': 0.151710,'cc': 0.152736,'c': 0.210294,'l': 0.485259}
frac[2]['mu']["btageSF_1__1up"] = {'bb': 0.084589,'cc': 0.064054,'c': 0.205959,'l': 0.645398}
frac[3]['mu']["btageSF_1__1up"] = {'bb': 0.108740,'cc': 0.098944,'c': 0.216180,'l': 0.576136}
frac[4]['mu']["btageSF_1__1up"] = {'bb': 0.132738,'cc': 0.135287,'c': 0.207552,'l': 0.524422}
frac[5]['mu']["btageSF_1__1up"] = {'bb': 0.143053,'cc': 0.148744,'c': 0.202758,'l': 0.505446}
# btageSF_1__1down 
frac[2]['el']["btageSF_1__1down"] = {'bb': 0.096152,'cc': 0.065746,'c': 0.210426,'l': 0.627676}
frac[3]['el']["btageSF_1__1down"] = {'bb': 0.119899,'cc': 0.100790,'c': 0.219975,'l': 0.559336}
frac[4]['el']["btageSF_1__1down"] = {'bb': 0.143216,'cc': 0.139436,'c': 0.215708,'l': 0.501641}
frac[5]['el']["btageSF_1__1down"] = {'bb': 0.151710,'cc': 0.152736,'c': 0.210294,'l': 0.485259}
frac[2]['mu']["btageSF_1__1down"] = {'bb': 0.084589,'cc': 0.064054,'c': 0.205959,'l': 0.645398}
frac[3]['mu']["btageSF_1__1down"] = {'bb': 0.108740,'cc': 0.098944,'c': 0.216180,'l': 0.576136}
frac[4]['mu']["btageSF_1__1down"] = {'bb': 0.132738,'cc': 0.135287,'c': 0.207552,'l': 0.524422}
frac[5]['mu']["btageSF_1__1down"] = {'bb': 0.143053,'cc': 0.148744,'c': 0.202758,'l': 0.505446}
# eTrigSF__1up 
frac[2]['el']["eTrigSF__1up"] = {'bb': 0.095380,'cc': 0.065568,'c': 0.209847,'l': 0.629205}
frac[3]['el']["eTrigSF__1up"] = {'bb': 0.118559,'cc': 0.100586,'c': 0.219443,'l': 0.561412}
frac[4]['el']["eTrigSF__1up"] = {'bb': 0.141278,'cc': 0.139442,'c': 0.215264,'l': 0.504015}
frac[5]['el']["eTrigSF__1up"] = {'bb': 0.149525,'cc': 0.152731,'c': 0.209902,'l': 0.487842}
frac[2]['mu']["eTrigSF__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["eTrigSF__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["eTrigSF__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["eTrigSF__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# eTrigSF__1down 
frac[2]['el']["eTrigSF__1down"] = {'bb': 0.095378,'cc': 0.065572,'c': 0.209877,'l': 0.629173}
frac[3]['el']["eTrigSF__1down"] = {'bb': 0.118555,'cc': 0.100591,'c': 0.219482,'l': 0.561372}
frac[4]['el']["eTrigSF__1down"] = {'bb': 0.141271,'cc': 0.139444,'c': 0.215306,'l': 0.503979}
frac[5]['el']["eTrigSF__1down"] = {'bb': 0.149519,'cc': 0.152731,'c': 0.209942,'l': 0.487808}
frac[2]['mu']["eTrigSF__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["eTrigSF__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["eTrigSF__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["eTrigSF__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# eRecoSF__1up 
frac[2]['el']["eRecoSF__1up"] = {'bb': 0.095381,'cc': 0.065574,'c': 0.209861,'l': 0.629183}
frac[3]['el']["eRecoSF__1up"] = {'bb': 0.118560,'cc': 0.100593,'c': 0.219459,'l': 0.561388}
frac[4]['el']["eRecoSF__1up"] = {'bb': 0.141277,'cc': 0.139448,'c': 0.215279,'l': 0.503995}
frac[5]['el']["eRecoSF__1up"] = {'bb': 0.149526,'cc': 0.152738,'c': 0.209915,'l': 0.487821}
frac[2]['mu']["eRecoSF__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["eRecoSF__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["eRecoSF__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["eRecoSF__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# eRecoSF__1down 
frac[2]['el']["eRecoSF__1down"] = {'bb': 0.095377,'cc': 0.065567,'c': 0.209862,'l': 0.629195}
frac[3]['el']["eRecoSF__1down"] = {'bb': 0.118554,'cc': 0.100584,'c': 0.219466,'l': 0.561396}
frac[4]['el']["eRecoSF__1down"] = {'bb': 0.141272,'cc': 0.139437,'c': 0.215291,'l': 0.504000}
frac[5]['el']["eRecoSF__1down"] = {'bb': 0.149519,'cc': 0.152724,'c': 0.209929,'l': 0.487828}
frac[2]['mu']["eRecoSF__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["eRecoSF__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["eRecoSF__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["eRecoSF__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# eIDSF__1up 
frac[2]['el']["eIDSF__1up"] = {'bb': 0.095394,'cc': 0.065586,'c': 0.209826,'l': 0.629193}
frac[3]['el']["eIDSF__1up"] = {'bb': 0.118575,'cc': 0.100612,'c': 0.219410,'l': 0.561404}
frac[4]['el']["eIDSF__1up"] = {'bb': 0.141297,'cc': 0.139478,'c': 0.215217,'l': 0.504008}
frac[5]['el']["eIDSF__1up"] = {'bb': 0.149552,'cc': 0.152777,'c': 0.209847,'l': 0.487823}
frac[2]['mu']["eIDSF__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["eIDSF__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["eIDSF__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["eIDSF__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# eIDSF__1down 
frac[2]['el']["eIDSF__1down"] = {'bb': 0.095363,'cc': 0.065554,'c': 0.209898,'l': 0.629185}
frac[3]['el']["eIDSF__1down"] = {'bb': 0.118539,'cc': 0.100565,'c': 0.219515,'l': 0.561381}
frac[4]['el']["eIDSF__1down"] = {'bb': 0.141252,'cc': 0.139408,'c': 0.215354,'l': 0.503987}
frac[5]['el']["eIDSF__1down"] = {'bb': 0.149491,'cc': 0.152684,'c': 0.209998,'l': 0.487827}
frac[2]['mu']["eIDSF__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["eIDSF__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["eIDSF__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["eIDSF__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# eIsolSF__1up 
frac[2]['el']["eIsolSF__1up"] = {'bb': 0.095382,'cc': 0.065579,'c': 0.209861,'l': 0.629178}
frac[3]['el']["eIsolSF__1up"] = {'bb': 0.118562,'cc': 0.100607,'c': 0.219455,'l': 0.561376}
frac[4]['el']["eIsolSF__1up"] = {'bb': 0.141281,'cc': 0.139465,'c': 0.215268,'l': 0.503987}
frac[5]['el']["eIsolSF__1up"] = {'bb': 0.149536,'cc': 0.152764,'c': 0.209896,'l': 0.487804}
frac[2]['mu']["eIsolSF__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["eIsolSF__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["eIsolSF__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["eIsolSF__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# eIsolSF__1down 
frac[2]['el']["eIsolSF__1down"] = {'bb': 0.095376,'cc': 0.065561,'c': 0.209863,'l': 0.629200}
frac[3]['el']["eIsolSF__1down"] = {'bb': 0.118552,'cc': 0.100570,'c': 0.219470,'l': 0.561408}
frac[4]['el']["eIsolSF__1down"] = {'bb': 0.141269,'cc': 0.139421,'c': 0.215303,'l': 0.504007}
frac[5]['el']["eIsolSF__1down"] = {'bb': 0.149508,'cc': 0.152698,'c': 0.209948,'l': 0.487846}
frac[2]['mu']["eIsolSF__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["eIsolSF__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["eIsolSF__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["eIsolSF__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# muTrigStatSF__1up 
frac[2]['el']["muTrigStatSF__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muTrigStatSF__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muTrigStatSF__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muTrigStatSF__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muTrigStatSF__1up"] = {'bb': 0.083919,'cc': 0.063840,'c': 0.205457,'l': 0.646783}
frac[3]['mu']["muTrigStatSF__1up"] = {'bb': 0.107541,'cc': 0.098653,'c': 0.215819,'l': 0.577987}
frac[4]['mu']["muTrigStatSF__1up"] = {'bb': 0.131001,'cc': 0.135022,'c': 0.207140,'l': 0.526838}
frac[5]['mu']["muTrigStatSF__1up"] = {'bb': 0.141048,'cc': 0.148517,'c': 0.202421,'l': 0.508015}
# muTrigStatSF__1down 
frac[2]['el']["muTrigStatSF__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muTrigStatSF__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muTrigStatSF__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muTrigStatSF__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muTrigStatSF__1down"] = {'bb': 0.083918,'cc': 0.063833,'c': 0.205441,'l': 0.646809}
frac[3]['mu']["muTrigStatSF__1down"] = {'bb': 0.107542,'cc': 0.098639,'c': 0.215792,'l': 0.578027}
frac[4]['mu']["muTrigStatSF__1down"] = {'bb': 0.130999,'cc': 0.135016,'c': 0.207098,'l': 0.526887}
frac[5]['mu']["muTrigStatSF__1down"] = {'bb': 0.141050,'cc': 0.148510,'c': 0.202383,'l': 0.508057}
# muTrigSystSF__1up 
frac[2]['el']["muTrigSystSF__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muTrigSystSF__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muTrigSystSF__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muTrigSystSF__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muTrigSystSF__1up"] = {'bb': 0.083915,'cc': 0.063834,'c': 0.205461,'l': 0.646790}
frac[3]['mu']["muTrigSystSF__1up"] = {'bb': 0.107538,'cc': 0.098642,'c': 0.215825,'l': 0.577995}
frac[4]['mu']["muTrigSystSF__1up"] = {'bb': 0.130994,'cc': 0.135013,'c': 0.207136,'l': 0.526857}
frac[5]['mu']["muTrigSystSF__1up"] = {'bb': 0.141043,'cc': 0.148508,'c': 0.202420,'l': 0.508029}
# muTrigSystSF__1down 
frac[2]['el']["muTrigSystSF__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muTrigSystSF__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muTrigSystSF__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muTrigSystSF__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muTrigSystSF__1down"] = {'bb': 0.083921,'cc': 0.063840,'c': 0.205437,'l': 0.646802}
frac[3]['mu']["muTrigSystSF__1down"] = {'bb': 0.107545,'cc': 0.098651,'c': 0.215786,'l': 0.578019}
frac[4]['mu']["muTrigSystSF__1down"] = {'bb': 0.131006,'cc': 0.135024,'c': 0.207103,'l': 0.526867}
frac[5]['mu']["muTrigSystSF__1down"] = {'bb': 0.141054,'cc': 0.148518,'c': 0.202385,'l': 0.508043}
# muIDStatSF__1up 
frac[2]['el']["muIDStatSF__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muIDStatSF__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muIDStatSF__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muIDStatSF__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muIDStatSF__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205451,'l': 0.646794}
frac[3]['mu']["muIDStatSF__1up"] = {'bb': 0.107542,'cc': 0.098645,'c': 0.215807,'l': 0.578006}
frac[4]['mu']["muIDStatSF__1up"] = {'bb': 0.130999,'cc': 0.135020,'c': 0.207121,'l': 0.526859}
frac[5]['mu']["muIDStatSF__1up"] = {'bb': 0.141048,'cc': 0.148514,'c': 0.202405,'l': 0.508033}
# muIDStatSF__1down 
frac[2]['el']["muIDStatSF__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muIDStatSF__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muIDStatSF__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muIDStatSF__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muIDStatSF__1down"] = {'bb': 0.083919,'cc': 0.063837,'c': 0.205447,'l': 0.646798}
frac[3]['mu']["muIDStatSF__1down"] = {'bb': 0.107542,'cc': 0.098647,'c': 0.215804,'l': 0.578007}
frac[4]['mu']["muIDStatSF__1down"] = {'bb': 0.131001,'cc': 0.135017,'c': 0.207117,'l': 0.526866}
frac[5]['mu']["muIDStatSF__1down"] = {'bb': 0.141049,'cc': 0.148512,'c': 0.202400,'l': 0.508039}
# muIDSystSF__1up 
frac[2]['el']["muIDSystSF__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muIDSystSF__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muIDSystSF__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muIDSystSF__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muIDSystSF__1up"] = {'bb': 0.083925,'cc': 0.063847,'c': 0.205440,'l': 0.646789}
frac[3]['mu']["muIDSystSF__1up"] = {'bb': 0.107553,'cc': 0.098662,'c': 0.215780,'l': 0.578005}
frac[4]['mu']["muIDSystSF__1up"] = {'bb': 0.131013,'cc': 0.135040,'c': 0.207097,'l': 0.526849}
frac[5]['mu']["muIDSystSF__1up"] = {'bb': 0.141067,'cc': 0.148541,'c': 0.202376,'l': 0.508016}
# muIDSystSF__1down 
frac[2]['el']["muIDSystSF__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muIDSystSF__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muIDSystSF__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muIDSystSF__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muIDSystSF__1down"] = {'bb': 0.083912,'cc': 0.063827,'c': 0.205458,'l': 0.646803}
frac[3]['mu']["muIDSystSF__1down"] = {'bb': 0.107530,'cc': 0.098631,'c': 0.215830,'l': 0.578009}
frac[4]['mu']["muIDSystSF__1down"] = {'bb': 0.130986,'cc': 0.134997,'c': 0.207141,'l': 0.526875}
frac[5]['mu']["muIDSystSF__1down"] = {'bb': 0.141030,'cc': 0.148485,'c': 0.202429,'l': 0.508056}
# muIsolStatSF__1up 
frac[2]['el']["muIsolStatSF__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muIsolStatSF__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muIsolStatSF__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muIsolStatSF__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muIsolStatSF__1up"] = {'bb': 0.083918,'cc': 0.063836,'c': 0.205447,'l': 0.646799}
frac[3]['mu']["muIsolStatSF__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215803,'l': 0.578009}
frac[4]['mu']["muIsolStatSF__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207116,'l': 0.526865}
frac[5]['mu']["muIsolStatSF__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202400,'l': 0.508038}
# muIsolStatSF__1down 
frac[2]['el']["muIsolStatSF__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muIsolStatSF__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muIsolStatSF__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muIsolStatSF__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muIsolStatSF__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205451,'l': 0.646793}
frac[3]['mu']["muIsolStatSF__1down"] = {'bb': 0.107542,'cc': 0.098647,'c': 0.215807,'l': 0.578004}
frac[4]['mu']["muIsolStatSF__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207122,'l': 0.526860}
frac[5]['mu']["muIsolStatSF__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202404,'l': 0.508033}
# muIsolSystSF__1up 
frac[2]['el']["muIsolSystSF__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muIsolSystSF__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muIsolSystSF__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muIsolSystSF__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muIsolSystSF__1up"] = {'bb': 0.083920,'cc': 0.063840,'c': 0.205450,'l': 0.646790}
frac[3]['mu']["muIsolSystSF__1up"] = {'bb': 0.107544,'cc': 0.098651,'c': 0.215804,'l': 0.578001}
frac[4]['mu']["muIsolSystSF__1up"] = {'bb': 0.131003,'cc': 0.135023,'c': 0.207118,'l': 0.526856}
frac[5]['mu']["muIsolSystSF__1up"] = {'bb': 0.141053,'cc': 0.148519,'c': 0.202400,'l': 0.508028}
# muIsolSystSF__1down 
frac[2]['el']["muIsolSystSF__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["muIsolSystSF__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["muIsolSystSF__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["muIsolSystSF__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["muIsolSystSF__1down"] = {'bb': 0.083917,'cc': 0.063834,'c': 0.205448,'l': 0.646802}
frac[3]['mu']["muIsolSystSF__1down"] = {'bb': 0.107539,'cc': 0.098642,'c': 0.215806,'l': 0.578013}
frac[4]['mu']["muIsolSystSF__1down"] = {'bb': 0.130997,'cc': 0.135014,'c': 0.207120,'l': 0.526869}
frac[5]['mu']["muIsolSystSF__1down"] = {'bb': 0.141045,'cc': 0.148507,'c': 0.202404,'l': 0.508044}

f_ca_map[2]['el']["2to3ex"] =  1.048976
f_ca_map[3]['el']["2to3ex"] =  1.030304
f_ca_map[4]['el']["2to3ex"] =  1.005477
f_ca_map[5]['el']["2to3ex"] =  0.782520
f_ca_map[2]['mu']["2to3ex"] =  1.151000
f_ca_map[3]['mu']["2to3ex"] =  1.063095
f_ca_map[4]['mu']["2to3ex"] =  0.958678
f_ca_map[5]['mu']["2to3ex"] =  0.804181

flav_map[2]['el']["2to3ex"] = {'bb': 0.697255, 'cc': 0.697255, 'c': 0.976370, 'l': 1.085325}
flav_map[3]['el']["2to3ex"] = {'bb': 0.714130, 'cc': 0.714130, 'c': 1.000000, 'l': 1.111592}
flav_map[4]['el']["2to3ex"] = {'bb': 0.731696, 'cc': 0.731696, 'c': 1.024597, 'l': 1.138934}
flav_map[5]['el']["2to3ex"] = {'bb': 0.752472, 'cc': 0.752472, 'c': 1.053690, 'l': 1.171273}
flav_map[2]['mu']["2to3ex"] = {'bb': 1.521083, 'cc': 1.521083, 'c': 1.039923, 'l': 0.868282}
flav_map[3]['mu']["2to3ex"] = {'bb': 1.462688, 'cc': 1.462688, 'c': 1.000000, 'l': 0.834949}
flav_map[4]['mu']["2to3ex"] = {'bb': 1.411692, 'cc': 1.411692, 'c': 0.965135, 'l': 0.805838}
flav_map[5]['mu']["2to3ex"] = {'bb': 1.349661, 'cc': 1.349661, 'c': 0.922726, 'l': 0.770429}

frac[2]['el']["2to3ex"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["2to3ex"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["2to3ex"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["2to3ex"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["2to3ex"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["2to3ex"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["2to3ex"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["2to3ex"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

# CT10 
f_ca_map[2]['el']["CT10"] =  1.175582
f_ca_map[3]['el']["CT10"] =  1.275476
f_ca_map[4]['el']["CT10"] =  1.356745
f_ca_map[5]['el']["CT10"] =  1.149121
f_ca_map[2]['mu']["CT10"] =  1.192963
f_ca_map[3]['mu']["CT10"] =  1.190882
f_ca_map[4]['mu']["CT10"] =  1.174277
f_ca_map[5]['mu']["CT10"] =  1.097489
# pdf_PDF4LHC15_nlo_30_0 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_0"] =  1.175590
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_0"] =  1.275474
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_0"] =  1.356754
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_0"] =  1.149114
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_0"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_0"] =  1.190897
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_0"] =  1.174295
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_0"] =  1.097482
# pdf_PDF4LHC15_nlo_30_1 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_1"] =  1.175581
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_1"] =  1.275476
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_1"] =  1.356744
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_1"] =  1.149121
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_1"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_1"] =  1.190895
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_1"] =  1.174293
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_1"] =  1.097482
# pdf_PDF4LHC15_nlo_30_2 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_2"] =  1.175568
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_2"] =  1.275480
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_2"] =  1.356729
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_2"] =  1.149132
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_2"] =  1.192964
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_2"] =  1.190867
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_2"] =  1.174258
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_2"] =  1.097498
# pdf_PDF4LHC15_nlo_30_3 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_3"] =  1.175589
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_3"] =  1.275474
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_3"] =  1.356754
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_3"] =  1.149114
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_3"] =  1.192958
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_3"] =  1.190934
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_3"] =  1.174342
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_3"] =  1.097461
# pdf_PDF4LHC15_nlo_30_4 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_4"] =  1.175584
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_4"] =  1.275475
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_4"] =  1.356747
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_4"] =  1.149119
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_4"] =  1.192966
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_4"] =  1.190853
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_4"] =  1.174240
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_4"] =  1.097505
# pdf_PDF4LHC15_nlo_30_5 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_5"] =  1.175586
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_5"] =  1.275475
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_5"] =  1.356750
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_5"] =  1.149117
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_5"] =  1.192963
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_5"] =  1.190879
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_5"] =  1.174273
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_5"] =  1.097491
# pdf_PDF4LHC15_nlo_30_6 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_6"] =  1.175592
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_6"] =  1.275473
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_6"] =  1.356756
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_6"] =  1.149113
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_6"] =  1.192963
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_6"] =  1.190881
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_6"] =  1.174275
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_6"] =  1.097490
# pdf_PDF4LHC15_nlo_30_7 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_7"] =  1.175582
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_7"] =  1.275476
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_7"] =  1.356745
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_7"] =  1.149120
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_7"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_7"] =  1.190890
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_7"] =  1.174287
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_7"] =  1.097485
# pdf_PDF4LHC15_nlo_30_8 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_8"] =  1.175597
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_8"] =  1.275471
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_8"] =  1.356763
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_8"] =  1.149107
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_8"] =  1.192959
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_8"] =  1.190924
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_8"] =  1.174330
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_8"] =  1.097466
# pdf_PDF4LHC15_nlo_30_9 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_9"] =  1.175594
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_9"] =  1.275472
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_9"] =  1.356759
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_9"] =  1.149110
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_9"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_9"] =  1.190892
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_9"] =  1.174289
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_9"] =  1.097484
# pdf_PDF4LHC15_nlo_30_10 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_10"] =  1.175629
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_10"] =  1.275462
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_10"] =  1.356800
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_10"] =  1.149080
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_10"] =  1.192960
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_10"] =  1.190910
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_10"] =  1.174312
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_10"] =  1.097474
# pdf_PDF4LHC15_nlo_30_11 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_11"] =  1.175595
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_11"] =  1.275472
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_11"] =  1.356760
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_11"] =  1.149110
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_11"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_11"] =  1.190897
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_11"] =  1.174296
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_11"] =  1.097481
# pdf_PDF4LHC15_nlo_30_12 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_12"] =  1.175597
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_12"] =  1.275472
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_12"] =  1.356762
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_12"] =  1.149108
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_12"] =  1.192960
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_12"] =  1.190910
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_12"] =  1.174312
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_12"] =  1.097474
# pdf_PDF4LHC15_nlo_30_13 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_13"] =  1.175590
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_13"] =  1.275474
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_13"] =  1.356754
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_13"] =  1.149114
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_13"] =  1.192968
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_13"] =  1.190833
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_13"] =  1.174213
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_13"] =  1.097517
# pdf_PDF4LHC15_nlo_30_14 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_14"] =  1.175588
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_14"] =  1.275474
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_14"] =  1.356752
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_14"] =  1.149116
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_14"] =  1.192963
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_14"] =  1.190885
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_14"] =  1.174280
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_14"] =  1.097488
# pdf_PDF4LHC15_nlo_30_15 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_15"] =  1.175593
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_15"] =  1.275473
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_15"] =  1.356758
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_15"] =  1.149111
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_15"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_15"] =  1.190895
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_15"] =  1.174293
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_15"] =  1.097482
# pdf_PDF4LHC15_nlo_30_16 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_16"] =  1.175600
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_16"] =  1.275471
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_16"] =  1.356765
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_16"] =  1.149106
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_16"] =  1.192964
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_16"] =  1.190870
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_16"] =  1.174261
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_16"] =  1.097496
# pdf_PDF4LHC15_nlo_30_17 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_17"] =  1.175584
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_17"] =  1.275475
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_17"] =  1.356747
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_17"] =  1.149119
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_17"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_17"] =  1.190897
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_17"] =  1.174295
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_17"] =  1.097481
# pdf_PDF4LHC15_nlo_30_18 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_18"] =  1.175588
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_18"] =  1.275474
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_18"] =  1.356751
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_18"] =  1.149116
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_18"] =  1.192960
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_18"] =  1.190911
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_18"] =  1.174313
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_18"] =  1.097474
# pdf_PDF4LHC15_nlo_30_19 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_19"] =  1.175595
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_19"] =  1.275472
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_19"] =  1.356760
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_19"] =  1.149109
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_19"] =  1.192960
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_19"] =  1.190912
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_19"] =  1.174314
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_19"] =  1.097473
# pdf_PDF4LHC15_nlo_30_20 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_20"] =  1.175603
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_20"] =  1.275470
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_20"] =  1.356770
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_20"] =  1.149102
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_20"] =  1.192961
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_20"] =  1.190903
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_20"] =  1.174303
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_20"] =  1.097478
# pdf_PDF4LHC15_nlo_30_21 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_21"] =  1.175586
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_21"] =  1.275474
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_21"] =  1.356751
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_21"] =  1.149116
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_21"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_21"] =  1.190892
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_21"] =  1.174289
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_21"] =  1.097484
# pdf_PDF4LHC15_nlo_30_22 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_22"] =  1.175594
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_22"] =  1.275473
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_22"] =  1.356758
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_22"] =  1.149111
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_22"] =  1.192960
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_22"] =  1.190915
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_22"] =  1.174318
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_22"] =  1.097472
# pdf_PDF4LHC15_nlo_30_23 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_23"] =  1.175560
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_23"] =  1.275482
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_23"] =  1.356719
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_23"] =  1.149140
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_23"] =  1.192960
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_23"] =  1.190911
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_23"] =  1.174313
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_23"] =  1.097474
# pdf_PDF4LHC15_nlo_30_24 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_24"] =  1.175579
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_24"] =  1.275477
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_24"] =  1.356741
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_24"] =  1.149123
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_24"] =  1.192961
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_24"] =  1.190904
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_24"] =  1.174304
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_24"] =  1.097477
# pdf_PDF4LHC15_nlo_30_25 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_25"] =  1.175590
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_25"] =  1.275474
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_25"] =  1.356754
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_25"] =  1.149114
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_25"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_25"] =  1.190894
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_25"] =  1.174291
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_25"] =  1.097483
# pdf_PDF4LHC15_nlo_30_26 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_26"] =  1.175588
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_26"] =  1.275474
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_26"] =  1.356752
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_26"] =  1.149116
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_26"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_26"] =  1.190897
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_26"] =  1.174295
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_26"] =  1.097481
# pdf_PDF4LHC15_nlo_30_27 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_27"] =  1.175590
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_27"] =  1.275473
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_27"] =  1.356755
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_27"] =  1.149113
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_27"] =  1.192961
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_27"] =  1.190900
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_27"] =  1.174299
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_27"] =  1.097479
# pdf_PDF4LHC15_nlo_30_28 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_28"] =  1.175581
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_28"] =  1.275476
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_28"] =  1.356744
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_28"] =  1.149121
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_28"] =  1.192963
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_28"] =  1.190889
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_28"] =  1.174285
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_28"] =  1.097486
# pdf_PDF4LHC15_nlo_30_29 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_29"] =  1.175592
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_29"] =  1.275473
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_29"] =  1.356756
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_29"] =  1.149112
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_29"] =  1.192961
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_29"] =  1.190904
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_29"] =  1.174304
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_29"] =  1.097477
# pdf_PDF4LHC15_nlo_30_30 
f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_30"] =  1.175590
f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_30"] =  1.275474
f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_30"] =  1.356754
f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_30"] =  1.149114
f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_30"] =  1.192962
f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_30"] =  1.190887
f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_30"] =  1.174282
f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_30"] =  1.097487


# CT10 
frac[2]['el']["CT10"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["CT10"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["CT10"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["CT10"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["CT10"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["CT10"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["CT10"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["CT10"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_0 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_1 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_2 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_3 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_4 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_5 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_6 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_7 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_8 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_9 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_10 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_11 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_12 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_13 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_14 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_15 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_16 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_17 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_18 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_19 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_20 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_21 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_22 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_23 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_24 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_25 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_26 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_27 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_28 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_29 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# pdf_PDF4LHC15_nlo_30_30 
frac[2]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

# CT10 
flav_map[2]['el']["CT10"] = {'bb': 1.330862, 'cc': 1.330862, 'c': 1.000000, 'l': 0.917125}
flav_map[3]['el']["CT10"] = {'bb': 1.298874, 'cc': 1.298874, 'c': 0.975965, 'l': 0.895082}
flav_map[4]['el']["CT10"] = {'bb': 1.267850, 'cc': 1.267850, 'c': 0.952653, 'l': 0.873702}
flav_map[5]['el']["CT10"] = {'bb': 1.234665, 'cc': 1.234665, 'c': 0.927719, 'l': 0.850834}
flav_map[2]['mu']["CT10"] = {'bb': 1.544760, 'cc': 1.544760, 'c': 1.000000, 'l': 0.877165}
flav_map[3]['mu']["CT10"] = {'bb': 1.486402, 'cc': 1.486402, 'c': 0.962222, 'l': 0.844028}
flav_map[4]['mu']["CT10"] = {'bb': 1.433591, 'cc': 1.433591, 'c': 0.928035, 'l': 0.814040}
flav_map[5]['mu']["CT10"] = {'bb': 1.369742, 'cc': 1.369742, 'c': 0.886702, 'l': 0.777784}
# pdf_PDF4LHC15_nlo_30_0 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.331575, 'cc': 1.331575, 'c': 1.000000, 'l': 0.916946}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.299503, 'cc': 1.299503, 'c': 0.975914, 'l': 0.894861}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.268400, 'cc': 1.268400, 'c': 0.952556, 'l': 0.873443}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.235135, 'cc': 1.235135, 'c': 0.927574, 'l': 0.850536}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.545581, 'cc': 1.545581, 'c': 1.000000, 'l': 0.876980}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.487107, 'cc': 1.487107, 'c': 0.962167, 'l': 0.843801}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.434197, 'cc': 1.434197, 'c': 0.927934, 'l': 0.813779}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.370236, 'cc': 1.370236, 'c': 0.886551, 'l': 0.777487}
# pdf_PDF4LHC15_nlo_30_1 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.330845, 'cc': 1.330845, 'c': 1.000000, 'l': 0.917130}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.298859, 'cc': 1.298859, 'c': 0.975966, 'l': 0.895087}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.267837, 'cc': 1.267837, 'c': 0.952655, 'l': 0.873708}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.234654, 'cc': 1.234654, 'c': 0.927722, 'l': 0.850841}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.545487, 'cc': 1.545487, 'c': 1.000000, 'l': 0.877001}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.487027, 'cc': 1.487027, 'c': 0.962173, 'l': 0.843827}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.434128, 'cc': 1.434128, 'c': 0.927945, 'l': 0.813809}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.370180, 'cc': 1.370180, 'c': 0.886568, 'l': 0.777521}
# pdf_PDF4LHC15_nlo_30_2 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.329765, 'cc': 1.329765, 'c': 1.000000, 'l': 0.917400}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.297907, 'cc': 1.297907, 'c': 0.976042, 'l': 0.895422}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.267004, 'cc': 1.267004, 'c': 0.952802, 'l': 0.874101}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.233943, 'cc': 1.233943, 'c': 0.927941, 'l': 0.851293}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.543889, 'cc': 1.543889, 'c': 1.000000, 'l': 0.877361}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.485654, 'cc': 1.485654, 'c': 0.962280, 'l': 0.844267}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.432947, 'cc': 1.432947, 'c': 0.928141, 'l': 0.814315}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.369218, 'cc': 1.369218, 'c': 0.886863, 'l': 0.778099}
# pdf_PDF4LHC15_nlo_30_3 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.331522, 'cc': 1.331522, 'c': 1.000000, 'l': 0.916960}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.299456, 'cc': 1.299456, 'c': 0.975918, 'l': 0.894878}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.268358, 'cc': 1.268358, 'c': 0.952563, 'l': 0.873462}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.235099, 'cc': 1.235099, 'c': 0.927585, 'l': 0.850558}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.547740, 'cc': 1.547740, 'c': 1.000000, 'l': 0.876493}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.488961, 'cc': 1.488961, 'c': 0.962023, 'l': 0.843207}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.435791, 'cc': 1.435791, 'c': 0.927669, 'l': 0.813096}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.371534, 'cc': 1.371534, 'c': 0.886153, 'l': 0.776707}
# pdf_PDF4LHC15_nlo_30_4 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.331060, 'cc': 1.331060, 'c': 1.000000, 'l': 0.917076}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.299049, 'cc': 1.299049, 'c': 0.975951, 'l': 0.895021}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.268003, 'cc': 1.268003, 'c': 0.952626, 'l': 0.873630}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.234796, 'cc': 1.234796, 'c': 0.927678, 'l': 0.850751}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.543083, 'cc': 1.543083, 'c': 1.000000, 'l': 0.877543}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.484961, 'cc': 1.484961, 'c': 0.962334, 'l': 0.844489}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.432352, 'cc': 1.432352, 'c': 0.928240, 'l': 0.814571}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.368733, 'cc': 1.368733, 'c': 0.887012, 'l': 0.778391}
# pdf_PDF4LHC15_nlo_30_5 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.331223, 'cc': 1.331223, 'c': 1.000000, 'l': 0.917035}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.299192, 'cc': 1.299192, 'c': 0.975939, 'l': 0.894970}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.268128, 'cc': 1.268128, 'c': 0.952604, 'l': 0.873571}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.234903, 'cc': 1.234903, 'c': 0.927646, 'l': 0.850683}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.544574, 'cc': 1.544574, 'c': 1.000000, 'l': 0.877207}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.486242, 'cc': 1.486242, 'c': 0.962234, 'l': 0.844079}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.433453, 'cc': 1.433453, 'c': 0.928057, 'l': 0.814099}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.369630, 'cc': 1.369630, 'c': 0.886736, 'l': 0.777852}
# pdf_PDF4LHC15_nlo_30_6 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.331667, 'cc': 1.331667, 'c': 1.000000, 'l': 0.916923}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.299584, 'cc': 1.299584, 'c': 0.975908, 'l': 0.894832}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.268471, 'cc': 1.268471, 'c': 0.952544, 'l': 0.873409}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.235195, 'cc': 1.235195, 'c': 0.927556, 'l': 0.850497}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.544672, 'cc': 1.544672, 'c': 1.000000, 'l': 0.877185}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.486326, 'cc': 1.486326, 'c': 0.962228, 'l': 0.844052}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.433526, 'cc': 1.433526, 'c': 0.928045, 'l': 0.814068}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.369689, 'cc': 1.369689, 'c': 0.886718, 'l': 0.777816}
# pdf_PDF4LHC15_nlo_30_7 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.330908, 'cc': 1.330908, 'c': 1.000000, 'l': 0.917114}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.298915, 'cc': 1.298915, 'c': 0.975961, 'l': 0.895068}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.267885, 'cc': 1.267885, 'c': 0.952647, 'l': 0.873685}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.234696, 'cc': 1.234696, 'c': 0.927709, 'l': 0.850815}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.545225, 'cc': 1.545225, 'c': 1.000000, 'l': 0.877060}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.486802, 'cc': 1.486802, 'c': 0.962191, 'l': 0.843899}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.433934, 'cc': 1.433934, 'c': 0.927978, 'l': 0.813892}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.370022, 'cc': 1.370022, 'c': 0.886616, 'l': 0.777616}
# pdf_PDF4LHC15_nlo_30_8 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.332201, 'cc': 1.332201, 'c': 1.000000, 'l': 0.916790}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.300055, 'cc': 1.300055, 'c': 0.975870, 'l': 0.894668}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.268882, 'cc': 1.268882, 'c': 0.952470, 'l': 0.873215}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.235546, 'cc': 1.235546, 'c': 0.927447, 'l': 0.850274}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.547163, 'cc': 1.547163, 'c': 1.000000, 'l': 0.876623}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.488466, 'cc': 1.488466, 'c': 0.962062, 'l': 0.843365}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.435365, 'cc': 1.435365, 'c': 0.927740, 'l': 0.813278}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.371188, 'cc': 1.371188, 'c': 0.886259, 'l': 0.776915}
# pdf_PDF4LHC15_nlo_30_9 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.331934, 'cc': 1.331934, 'c': 1.000000, 'l': 0.916857}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.299819, 'cc': 1.299819, 'c': 0.975889, 'l': 0.894750}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.268676, 'cc': 1.268676, 'c': 0.952507, 'l': 0.873312}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.235371, 'cc': 1.235371, 'c': 0.927501, 'l': 0.850386}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.545335, 'cc': 1.545335, 'c': 1.000000, 'l': 0.877036}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.486896, 'cc': 1.486896, 'c': 0.962184, 'l': 0.843869}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.434015, 'cc': 1.434015, 'c': 0.927964, 'l': 0.813858}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.370088, 'cc': 1.370088, 'c': 0.886596, 'l': 0.777576}
# pdf_PDF4LHC15_nlo_30_10 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.334888, 'cc': 1.334888, 'c': 1.000000, 'l': 0.916117}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.302423, 'cc': 1.302423, 'c': 0.975679, 'l': 0.893836}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.270953, 'cc': 1.270953, 'c': 0.952104, 'l': 0.872239}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.237312, 'cc': 1.237312, 'c': 0.926903, 'l': 0.849152}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.546379, 'cc': 1.546379, 'c': 1.000000, 'l': 0.876800}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.487793, 'cc': 1.487793, 'c': 0.962114, 'l': 0.843582}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.434786, 'cc': 1.434786, 'c': 0.927836, 'l': 0.813527}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.370716, 'cc': 1.370716, 'c': 0.886404, 'l': 0.777199}
# pdf_PDF4LHC15_nlo_30_11 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.331984, 'cc': 1.331984, 'c': 1.000000, 'l': 0.916844}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.299863, 'cc': 1.299863, 'c': 0.975885, 'l': 0.894735}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.268715, 'cc': 1.268715, 'c': 0.952500, 'l': 0.873294}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.235403, 'cc': 1.235403, 'c': 0.927491, 'l': 0.850365}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.545618, 'cc': 1.545618, 'c': 1.000000, 'l': 0.876971}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.487139, 'cc': 1.487139, 'c': 0.962165, 'l': 0.843791}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.434225, 'cc': 1.434225, 'c': 0.927929, 'l': 0.813768}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.370258, 'cc': 1.370258, 'c': 0.886544, 'l': 0.777474}
# pdf_PDF4LHC15_nlo_30_12 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.332165, 'cc': 1.332165, 'c': 1.000000, 'l': 0.916799}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.300023, 'cc': 1.300023, 'c': 0.975872, 'l': 0.894679}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.268854, 'cc': 1.268854, 'c': 0.952475, 'l': 0.873229}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.235522, 'cc': 1.235522, 'c': 0.927455, 'l': 0.850289}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.546350, 'cc': 1.546350, 'c': 1.000000, 'l': 0.876806}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.487768, 'cc': 1.487768, 'c': 0.962116, 'l': 0.843589}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.434765, 'cc': 1.434765, 'c': 0.927840, 'l': 0.813536}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.370699, 'cc': 1.370699, 'c': 0.886409, 'l': 0.777209}
# pdf_PDF4LHC15_nlo_30_13 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.331554, 'cc': 1.331554, 'c': 1.000000, 'l': 0.916952}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.299485, 'cc': 1.299485, 'c': 0.975916, 'l': 0.894868}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.268384, 'cc': 1.268384, 'c': 0.952559, 'l': 0.873450}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.235121, 'cc': 1.235121, 'c': 0.927578, 'l': 0.850544}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.541885, 'cc': 1.541885, 'c': 1.000000, 'l': 0.877813}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.483932, 'cc': 1.483932, 'c': 0.962414, 'l': 0.844819}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.431467, 'cc': 1.431467, 'c': 0.928387, 'l': 0.814950}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.368011, 'cc': 1.368011, 'c': 0.887233, 'l': 0.778824}
# pdf_PDF4LHC15_nlo_30_14 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.331392, 'cc': 1.331392, 'c': 1.000000, 'l': 0.916992}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.299342, 'cc': 1.299342, 'c': 0.975927, 'l': 0.894918}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.268259, 'cc': 1.268259, 'c': 0.952581, 'l': 0.873509}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.235014, 'cc': 1.235014, 'c': 0.927611, 'l': 0.850612}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.544892, 'cc': 1.544892, 'c': 1.000000, 'l': 0.877135}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.486516, 'cc': 1.486516, 'c': 0.962213, 'l': 0.843991}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.433688, 'cc': 1.433688, 'c': 0.928018, 'l': 0.813998}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.369822, 'cc': 1.369822, 'c': 0.886678, 'l': 0.777736}
# pdf_PDF4LHC15_nlo_30_15 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.331821, 'cc': 1.331821, 'c': 1.000000, 'l': 0.916885}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.299720, 'cc': 1.299720, 'c': 0.975897, 'l': 0.894785}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.268590, 'cc': 1.268590, 'c': 0.952522, 'l': 0.873353}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.235297, 'cc': 1.235297, 'c': 0.927524, 'l': 0.850433}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.545510, 'cc': 1.545510, 'c': 1.000000, 'l': 0.876996}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.487047, 'cc': 1.487047, 'c': 0.962172, 'l': 0.843821}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.434145, 'cc': 1.434145, 'c': 0.927943, 'l': 0.813802}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.370194, 'cc': 1.370194, 'c': 0.886564, 'l': 0.777513}
# pdf_PDF4LHC15_nlo_30_16 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.332378, 'cc': 1.332378, 'c': 1.000000, 'l': 0.916745}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.300211, 'cc': 1.300211, 'c': 0.975857, 'l': 0.894613}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.269019, 'cc': 1.269019, 'c': 0.952446, 'l': 0.873151}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.235663, 'cc': 1.235663, 'c': 0.927411, 'l': 0.850200}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.544065, 'cc': 1.544065, 'c': 1.000000, 'l': 0.877322}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.485804, 'cc': 1.485804, 'c': 0.962268, 'l': 0.844219}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.433077, 'cc': 1.433077, 'c': 0.928120, 'l': 0.814260}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.369323, 'cc': 1.369323, 'c': 0.886830, 'l': 0.778036}
# pdf_PDF4LHC15_nlo_30_17 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.331070, 'cc': 1.331070, 'c': 1.000000, 'l': 0.917073}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.299058, 'cc': 1.299058, 'c': 0.975950, 'l': 0.895017}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.268010, 'cc': 1.268010, 'c': 0.952625, 'l': 0.873626}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.234802, 'cc': 1.234802, 'c': 0.927677, 'l': 0.850747}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.545609, 'cc': 1.545609, 'c': 1.000000, 'l': 0.876973}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.487132, 'cc': 1.487132, 'c': 0.962165, 'l': 0.843793}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.434218, 'cc': 1.434218, 'c': 0.927931, 'l': 0.813770}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.370253, 'cc': 1.370253, 'c': 0.886546, 'l': 0.777477}
# pdf_PDF4LHC15_nlo_30_18 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.331354, 'cc': 1.331354, 'c': 1.000000, 'l': 0.917001}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.299309, 'cc': 1.299309, 'c': 0.975930, 'l': 0.894929}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.268230, 'cc': 1.268230, 'c': 0.952586, 'l': 0.873523}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.234990, 'cc': 1.234990, 'c': 0.927619, 'l': 0.850628}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.546401, 'cc': 1.546401, 'c': 1.000000, 'l': 0.876795}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.487812, 'cc': 1.487812, 'c': 0.962112, 'l': 0.843575}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.434803, 'cc': 1.434803, 'c': 0.927833, 'l': 0.813520}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.370729, 'cc': 1.370729, 'c': 0.886400, 'l': 0.777191}
# pdf_PDF4LHC15_nlo_30_19 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.332012, 'cc': 1.332012, 'c': 1.000000, 'l': 0.916837}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.299888, 'cc': 1.299888, 'c': 0.975883, 'l': 0.894726}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.268737, 'cc': 1.268737, 'c': 0.952496, 'l': 0.873284}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.235422, 'cc': 1.235422, 'c': 0.927485, 'l': 0.850353}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.546442, 'cc': 1.546442, 'c': 1.000000, 'l': 0.876786}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.487847, 'cc': 1.487847, 'c': 0.962110, 'l': 0.843564}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.434833, 'cc': 1.434833, 'c': 0.927828, 'l': 0.813507}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.370754, 'cc': 1.370754, 'c': 0.886392, 'l': 0.777176}
# pdf_PDF4LHC15_nlo_30_20 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.332724, 'cc': 1.332724, 'c': 1.000000, 'l': 0.916659}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.300515, 'cc': 1.300515, 'c': 0.975833, 'l': 0.894506}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.269285, 'cc': 1.269285, 'c': 0.952399, 'l': 0.873026}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.235890, 'cc': 1.235890, 'c': 0.927341, 'l': 0.850056}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.545965, 'cc': 1.545965, 'c': 1.000000, 'l': 0.876894}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.487437, 'cc': 1.487437, 'c': 0.962141, 'l': 0.843696}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.434480, 'cc': 1.434480, 'c': 0.927887, 'l': 0.813658}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.370467, 'cc': 1.370467, 'c': 0.886480, 'l': 0.777349}
# pdf_PDF4LHC15_nlo_30_21 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.331303, 'cc': 1.331303, 'c': 1.000000, 'l': 0.917016}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.299262, 'cc': 1.299262, 'c': 0.975933, 'l': 0.894946}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.268189, 'cc': 1.268189, 'c': 0.952593, 'l': 0.873542}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.234955, 'cc': 1.234955, 'c': 0.927629, 'l': 0.850650}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.545303, 'cc': 1.545303, 'c': 1.000000, 'l': 0.877042}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.486869, 'cc': 1.486869, 'c': 0.962186, 'l': 0.843878}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.433992, 'cc': 1.433992, 'c': 0.927968, 'l': 0.813867}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.370069, 'cc': 1.370069, 'c': 0.886602, 'l': 0.777588}
# pdf_PDF4LHC15_nlo_30_22 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.331871, 'cc': 1.331871, 'c': 1.000000, 'l': 0.916873}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.299764, 'cc': 1.299764, 'c': 0.975893, 'l': 0.894770}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.268628, 'cc': 1.268628, 'c': 0.952515, 'l': 0.873335}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.235329, 'cc': 1.235329, 'c': 0.927514, 'l': 0.850412}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.546616, 'cc': 1.546616, 'c': 1.000000, 'l': 0.876746}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.487996, 'cc': 1.487996, 'c': 0.962098, 'l': 0.843516}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.434961, 'cc': 1.434961, 'c': 0.927807, 'l': 0.813452}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.370859, 'cc': 1.370859, 'c': 0.886360, 'l': 0.777113}
# pdf_PDF4LHC15_nlo_30_23 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.329010, 'cc': 1.329010, 'c': 1.000000, 'l': 0.917589}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.297241, 'cc': 1.297241, 'c': 0.976096, 'l': 0.895655}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.266421, 'cc': 1.266421, 'c': 0.952906, 'l': 0.874376}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.233446, 'cc': 1.233446, 'c': 0.928094, 'l': 0.851609}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.546405, 'cc': 1.546405, 'c': 1.000000, 'l': 0.876794}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.487815, 'cc': 1.487815, 'c': 0.962112, 'l': 0.843574}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.434805, 'cc': 1.434805, 'c': 0.927833, 'l': 0.813519}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.370732, 'cc': 1.370732, 'c': 0.886399, 'l': 0.777189}
# pdf_PDF4LHC15_nlo_30_24 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.330622, 'cc': 1.330622, 'c': 1.000000, 'l': 0.917185}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.298663, 'cc': 1.298663, 'c': 0.975982, 'l': 0.895156}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.267664, 'cc': 1.267664, 'c': 0.952686, 'l': 0.873789}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.234507, 'cc': 1.234507, 'c': 0.927767, 'l': 0.850935}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.545999, 'cc': 1.545999, 'c': 1.000000, 'l': 0.876886}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.487466, 'cc': 1.487466, 'c': 0.962139, 'l': 0.843686}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.434505, 'cc': 1.434505, 'c': 0.927883, 'l': 0.813647}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.370487, 'cc': 1.370487, 'c': 0.886474, 'l': 0.777336}
# pdf_PDF4LHC15_nlo_30_25 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.331526, 'cc': 1.331526, 'c': 1.000000, 'l': 0.916959}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.299460, 'cc': 1.299460, 'c': 0.975918, 'l': 0.894876}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.268362, 'cc': 1.268362, 'c': 0.952563, 'l': 0.873461}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.235102, 'cc': 1.235102, 'c': 0.927584, 'l': 0.850556}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.545421, 'cc': 1.545421, 'c': 1.000000, 'l': 0.877016}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.486970, 'cc': 1.486970, 'c': 0.962178, 'l': 0.843845}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.434079, 'cc': 1.434079, 'c': 0.927954, 'l': 0.813830}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.370140, 'cc': 1.370140, 'c': 0.886580, 'l': 0.777545}
# pdf_PDF4LHC15_nlo_30_26 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.331390, 'cc': 1.331390, 'c': 1.000000, 'l': 0.916993}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.299340, 'cc': 1.299340, 'c': 0.975927, 'l': 0.894918}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.268257, 'cc': 1.268257, 'c': 0.952581, 'l': 0.873510}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.235013, 'cc': 1.235013, 'c': 0.927612, 'l': 0.850613}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.545608, 'cc': 1.545608, 'c': 1.000000, 'l': 0.876974}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.487130, 'cc': 1.487130, 'c': 0.962165, 'l': 0.843794}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.434217, 'cc': 1.434217, 'c': 0.927931, 'l': 0.813771}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.370252, 'cc': 1.370252, 'c': 0.886546, 'l': 0.777478}
# pdf_PDF4LHC15_nlo_30_27 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.331593, 'cc': 1.331593, 'c': 1.000000, 'l': 0.916943}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.299518, 'cc': 1.299518, 'c': 0.975913, 'l': 0.894856}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.268413, 'cc': 1.268413, 'c': 0.952553, 'l': 0.873437}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.235146, 'cc': 1.235146, 'c': 0.927570, 'l': 0.850529}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.545798, 'cc': 1.545798, 'c': 1.000000, 'l': 0.876931}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.487294, 'cc': 1.487294, 'c': 0.962153, 'l': 0.843742}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.434357, 'cc': 1.434357, 'c': 0.927907, 'l': 0.813711}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.370367, 'cc': 1.370367, 'c': 0.886511, 'l': 0.777409}
# pdf_PDF4LHC15_nlo_30_28 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.330856, 'cc': 1.330856, 'c': 1.000000, 'l': 0.917127}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.298869, 'cc': 1.298869, 'c': 0.975965, 'l': 0.895084}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.267845, 'cc': 1.267845, 'c': 0.952654, 'l': 0.873704}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.234661, 'cc': 1.234661, 'c': 0.927720, 'l': 0.850837}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.545119, 'cc': 1.545119, 'c': 1.000000, 'l': 0.877084}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.486711, 'cc': 1.486711, 'c': 0.962198, 'l': 0.843928}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.433856, 'cc': 1.433856, 'c': 0.927991, 'l': 0.813926}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.369958, 'cc': 1.369958, 'c': 0.886636, 'l': 0.777654}
# pdf_PDF4LHC15_nlo_30_29 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.331707, 'cc': 1.331707, 'c': 1.000000, 'l': 0.916914}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.299619, 'cc': 1.299619, 'c': 0.975905, 'l': 0.894820}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.268501, 'cc': 1.268501, 'c': 0.952538, 'l': 0.873395}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.235221, 'cc': 1.235221, 'c': 0.927547, 'l': 0.850481}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.546023, 'cc': 1.546023, 'c': 1.000000, 'l': 0.876880}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.487487, 'cc': 1.487487, 'c': 0.962138, 'l': 0.843679}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.434524, 'cc': 1.434524, 'c': 0.927880, 'l': 0.813639}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.370502, 'cc': 1.370502, 'c': 0.886469, 'l': 0.777327}
# pdf_PDF4LHC15_nlo_30_30 
flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.331570, 'cc': 1.331570, 'c': 1.000000, 'l': 0.916948}
flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.299498, 'cc': 1.299498, 'c': 0.975915, 'l': 0.894863}
flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.268396, 'cc': 1.268396, 'c': 0.952557, 'l': 0.873445}
flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.235131, 'cc': 1.235131, 'c': 0.927575, 'l': 0.850538}
flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.545006, 'cc': 1.545006, 'c': 1.000000, 'l': 0.877110}
flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.486613, 'cc': 1.486613, 'c': 0.962205, 'l': 0.843960}
flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.433772, 'cc': 1.433772, 'c': 0.928004, 'l': 0.813962}
flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.369890, 'cc': 1.369890, 'c': 0.886657, 'l': 0.777695}


# ttxsecup 
f_ca_map[2]['el']["ttxsecup"] =  1.057511
f_ca_map[3]['el']["ttxsecup"] =  1.034624
f_ca_map[4]['el']["ttxsecup"] =  1.016569
f_ca_map[5]['el']["ttxsecup"] =  0.781637
f_ca_map[2]['mu']["ttxsecup"] =  1.146235
f_ca_map[3]['mu']["ttxsecup"] =  1.057216
f_ca_map[4]['mu']["ttxsecup"] =  0.953162
f_ca_map[5]['mu']["ttxsecup"] =  0.800912
# ttxsecdw 
f_ca_map[2]['el']["ttxsecdw"] =  1.057494
f_ca_map[3]['el']["ttxsecdw"] =  1.034621
f_ca_map[4]['el']["ttxsecdw"] =  1.016547
f_ca_map[5]['el']["ttxsecdw"] =  0.781647
f_ca_map[2]['mu']["ttxsecdw"] =  1.146240
f_ca_map[3]['mu']["ttxsecdw"] =  1.057183
f_ca_map[4]['mu']["ttxsecdw"] =  0.953124
f_ca_map[5]['mu']["ttxsecdw"] =  0.800926
# singletopup 
f_ca_map[2]['el']["singletopup"] =  1.055504
f_ca_map[3]['el']["singletopup"] =  1.032063
f_ca_map[4]['el']["singletopup"] =  1.013279
f_ca_map[5]['el']["singletopup"] =  0.779354
f_ca_map[2]['mu']["singletopup"] =  1.144902
f_ca_map[3]['mu']["singletopup"] =  1.054702
f_ca_map[4]['mu']["singletopup"] =  0.950468
f_ca_map[5]['mu']["singletopup"] =  0.799101
# singletopdw 
f_ca_map[2]['el']["singletopdw"] =  1.059251
f_ca_map[3]['el']["singletopdw"] =  1.036862
f_ca_map[4]['el']["singletopdw"] =  1.019424
f_ca_map[5]['el']["singletopdw"] =  0.783649
f_ca_map[2]['mu']["singletopdw"] =  1.147407
f_ca_map[3]['mu']["singletopdw"] =  1.059381
f_ca_map[4]['mu']["singletopdw"] =  0.955478
f_ca_map[5]['mu']["singletopdw"] =  0.802513
# wnorm__1up 
f_ca_map[2]['el']["wnorm__1up"] =  1.057507
f_ca_map[3]['el']["wnorm__1up"] =  1.034623
f_ca_map[4]['el']["wnorm__1up"] =  1.016564
f_ca_map[5]['el']["wnorm__1up"] =  0.781639
f_ca_map[2]['mu']["wnorm__1up"] =  1.146238
f_ca_map[3]['mu']["wnorm__1up"] =  1.057198
f_ca_map[4]['mu']["wnorm__1up"] =  0.953142
f_ca_map[5]['mu']["wnorm__1up"] =  0.800919
# wnorm__1down 
f_ca_map[2]['el']["wnorm__1down"] =  1.057497
f_ca_map[3]['el']["wnorm__1down"] =  1.034621
f_ca_map[4]['el']["wnorm__1down"] =  1.016551
f_ca_map[5]['el']["wnorm__1down"] =  0.781646
f_ca_map[2]['mu']["wnorm__1down"] =  1.146238
f_ca_map[3]['mu']["wnorm__1down"] =  1.057198
f_ca_map[4]['mu']["wnorm__1down"] =  0.953141
f_ca_map[5]['mu']["wnorm__1down"] =  0.800919
# elMisIDpos_up 
f_ca_map[2]['el']["elMisIDpos_up"] =  0.995400
f_ca_map[3]['el']["elMisIDpos_up"] =  0.973371
f_ca_map[4]['el']["elMisIDpos_up"] =  0.955435
f_ca_map[5]['el']["elMisIDpos_up"] =  0.734856
f_ca_map[2]['mu']["elMisIDpos_up"] =  1.146238
f_ca_map[3]['mu']["elMisIDpos_up"] =  1.057198
f_ca_map[4]['mu']["elMisIDpos_up"] =  0.953141
f_ca_map[5]['mu']["elMisIDpos_up"] =  0.800919
# elMisIDpos_down 
f_ca_map[2]['el']["elMisIDpos_down"] =  1.127546
f_ca_map[3]['el']["elMisIDpos_down"] =  1.103694
f_ca_map[4]['el']["elMisIDpos_down"] =  1.085491
f_ca_map[5]['el']["elMisIDpos_down"] =  0.834400
f_ca_map[2]['mu']["elMisIDpos_down"] =  1.146238
f_ca_map[3]['mu']["elMisIDpos_down"] =  1.057198
f_ca_map[4]['mu']["elMisIDpos_down"] =  0.953141
f_ca_map[5]['mu']["elMisIDpos_down"] =  0.800919

# ttxsecup 
frac[2]['el']["ttxsecup"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttxsecup"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttxsecup"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttxsecup"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttxsecup"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttxsecup"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttxsecup"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttxsecup"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# ttxsecdw 
frac[2]['el']["ttxsecdw"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttxsecdw"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttxsecdw"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttxsecdw"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttxsecdw"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttxsecdw"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttxsecdw"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttxsecdw"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# singletopup 
frac[2]['el']["singletopup"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["singletopup"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["singletopup"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["singletopup"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["singletopup"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["singletopup"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["singletopup"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["singletopup"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# singletopdw 
frac[2]['el']["singletopdw"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["singletopdw"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["singletopdw"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["singletopdw"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["singletopdw"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["singletopdw"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["singletopdw"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["singletopdw"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# wnorm__1up 
frac[2]['el']["wnorm__1up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["wnorm__1up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["wnorm__1up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["wnorm__1up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["wnorm__1up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["wnorm__1up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["wnorm__1up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["wnorm__1up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# wnorm__1down 
frac[2]['el']["wnorm__1down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["wnorm__1down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["wnorm__1down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["wnorm__1down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["wnorm__1down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["wnorm__1down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["wnorm__1down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["wnorm__1down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# elMisIDpos_up 
frac[2]['el']["elMisIDpos_up"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["elMisIDpos_up"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["elMisIDpos_up"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["elMisIDpos_up"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["elMisIDpos_up"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["elMisIDpos_up"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["elMisIDpos_up"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["elMisIDpos_up"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# elMisIDpos_down 
frac[2]['el']["elMisIDpos_down"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["elMisIDpos_down"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["elMisIDpos_down"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["elMisIDpos_down"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["elMisIDpos_down"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["elMisIDpos_down"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["elMisIDpos_down"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["elMisIDpos_down"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}

# ttxsecup 
flav_map[2]['el']["ttxsecup"] = {'bb': 1.275822, 'cc': 1.275822, 'c': 1.000000, 'l': 0.929444}
flav_map[3]['el']["ttxsecup"] = {'bb': 1.249782, 'cc': 1.249782, 'c': 0.979590, 'l': 0.910474}
flav_map[4]['el']["ttxsecup"] = {'bb': 1.224552, 'cc': 1.224552, 'c': 0.959815, 'l': 0.892094}
flav_map[5]['el']["ttxsecup"] = {'bb': 1.197014, 'cc': 1.197014, 'c': 0.938230, 'l': 0.872032}
flav_map[2]['mu']["ttxsecup"] = {'bb': 1.512310, 'cc': 1.512310, 'c': 1.000000, 'l': 0.882967}
flav_map[3]['mu']["ttxsecup"] = {'bb': 1.456965, 'cc': 1.456965, 'c': 0.963404, 'l': 0.850654}
flav_map[4]['mu']["ttxsecup"] = {'bb': 1.407293, 'cc': 1.407293, 'c': 0.930558, 'l': 0.821652}
flav_map[5]['mu']["ttxsecup"] = {'bb': 1.346498, 'cc': 1.346498, 'c': 0.890359, 'l': 0.786157}
# ttxsecdw 
flav_map[2]['el']["ttxsecdw"] = {'bb': 1.274006, 'cc': 1.274006, 'c': 1.000000, 'l': 0.929908}
flav_map[3]['el']["ttxsecdw"] = {'bb': 1.248171, 'cc': 1.248171, 'c': 0.979722, 'l': 0.911051}
flav_map[4]['el']["ttxsecdw"] = {'bb': 1.223133, 'cc': 1.223133, 'c': 0.960069, 'l': 0.892776}
flav_map[5]['el']["ttxsecdw"] = {'bb': 1.195797, 'cc': 1.195797, 'c': 0.938612, 'l': 0.872823}
flav_map[2]['mu']["ttxsecdw"] = {'bb': 1.510188, 'cc': 1.510188, 'c': 1.000000, 'l': 0.883452}
flav_map[3]['mu']["ttxsecdw"] = {'bb': 1.455142, 'cc': 1.455142, 'c': 0.963550, 'l': 0.851250}
flav_map[4]['mu']["ttxsecdw"] = {'bb': 1.405722, 'cc': 1.405722, 'c': 0.930826, 'l': 0.822340}
flav_map[5]['mu']["ttxsecdw"] = {'bb': 1.345220, 'cc': 1.345220, 'c': 0.890763, 'l': 0.786946}
# singletopup 
flav_map[2]['el']["singletopup"] = {'bb': 1.235348, 'cc': 1.235348, 'c': 1.000000, 'l': 0.939797}
flav_map[3]['el']["singletopup"] = {'bb': 1.213770, 'cc': 1.213770, 'c': 0.982533, 'l': 0.923381}
flav_map[4]['el']["singletopup"] = {'bb': 1.192738, 'cc': 1.192738, 'c': 0.965508, 'l': 0.907382}
flav_map[5]['el']["singletopup"] = {'bb': 1.169642, 'cc': 1.169642, 'c': 0.946812, 'l': 0.889811}
flav_map[2]['mu']["singletopup"] = {'bb': 1.476536, 'cc': 1.476536, 'c': 1.000000, 'l': 0.891139}
flav_map[3]['mu']["singletopup"] = {'bb': 1.426145, 'cc': 1.426145, 'c': 0.965872, 'l': 0.860726}
flav_map[4]['mu']["singletopup"] = {'bb': 1.380698, 'cc': 1.380698, 'c': 0.935093, 'l': 0.833298}
flav_map[5]['mu']["singletopup"] = {'bb': 1.324790, 'cc': 1.324790, 'c': 0.897228, 'l': 0.799555}
# singletopdw 
flav_map[2]['el']["singletopdw"] = {'bb': 1.309278, 'cc': 1.309278, 'c': 1.000000, 'l': 0.920885}
flav_map[3]['el']["singletopdw"] = {'bb': 1.279389, 'cc': 1.279389, 'c': 0.977171, 'l': 0.899862}
flav_map[4]['el']["singletopdw"] = {'bb': 1.250569, 'cc': 1.250569, 'c': 0.955159, 'l': 0.879592}
flav_map[5]['el']["singletopdw"] = {'bb': 1.219269, 'cc': 1.219269, 'c': 0.931253, 'l': 0.857577}
flav_map[2]['mu']["singletopdw"] = {'bb': 1.541406, 'cc': 1.541406, 'c': 1.000000, 'l': 0.876320}
flav_map[3]['mu']["singletopdw"] = {'bb': 1.481916, 'cc': 1.481916, 'c': 0.961406, 'l': 0.842499}
flav_map[4]['mu']["singletopdw"] = {'bb': 1.428733, 'cc': 1.428733, 'c': 0.926903, 'l': 0.812264}
flav_map[5]['mu']["singletopdw"] = {'bb': 1.363911, 'cc': 1.363911, 'c': 0.884849, 'l': 0.775411}
# wnorm__1up 
flav_map[2]['el']["wnorm__1up"] = {'bb': 1.275400, 'cc': 1.275400, 'c': 1.000000, 'l': 0.929552}
flav_map[3]['el']["wnorm__1up"] = {'bb': 1.249408, 'cc': 1.249408, 'c': 0.979620, 'l': 0.910608}
flav_map[4]['el']["wnorm__1up"] = {'bb': 1.224223, 'cc': 1.224223, 'c': 0.959874, 'l': 0.892252}
flav_map[5]['el']["wnorm__1up"] = {'bb': 1.196732, 'cc': 1.196732, 'c': 0.938319, 'l': 0.872216}
flav_map[2]['mu']["wnorm__1up"] = {'bb': 1.511170, 'cc': 1.511170, 'c': 1.000000, 'l': 0.883227}
flav_map[3]['mu']["wnorm__1up"] = {'bb': 1.455986, 'cc': 1.455986, 'c': 0.963482, 'l': 0.850974}
flav_map[4]['mu']["wnorm__1up"] = {'bb': 1.406449, 'cc': 1.406449, 'c': 0.930702, 'l': 0.822021}
flav_map[5]['mu']["wnorm__1up"] = {'bb': 1.345812, 'cc': 1.345812, 'c': 0.890576, 'l': 0.786581}
# wnorm__1down 
flav_map[2]['el']["wnorm__1down"] = {'bb': 1.274277, 'cc': 1.274277, 'c': 1.000000, 'l': 0.929839}
flav_map[3]['el']["wnorm__1down"] = {'bb': 1.248412, 'cc': 1.248412, 'c': 0.979702, 'l': 0.910965}
flav_map[4]['el']["wnorm__1down"] = {'bb': 1.223345, 'cc': 1.223345, 'c': 0.960031, 'l': 0.892674}
flav_map[5]['el']["wnorm__1down"] = {'bb': 1.195979, 'cc': 1.195979, 'c': 0.938555, 'l': 0.872705}
flav_map[2]['mu']["wnorm__1down"] = {'bb': 1.511157, 'cc': 1.511157, 'c': 1.000000, 'l': 0.883231}
flav_map[3]['mu']["wnorm__1down"] = {'bb': 1.455974, 'cc': 1.455974, 'c': 0.963483, 'l': 0.850978}
flav_map[4]['mu']["wnorm__1down"] = {'bb': 1.406439, 'cc': 1.406439, 'c': 0.930704, 'l': 0.822026}
flav_map[5]['mu']["wnorm__1down"] = {'bb': 1.345804, 'cc': 1.345804, 'c': 0.890578, 'l': 0.786586}
# elMisIDpos_up 
flav_map[2]['el']["elMisIDpos_up"] = {'bb': 1.224012, 'cc': 1.224012, 'c': 1.000000, 'l': 0.942697}
flav_map[3]['el']["elMisIDpos_up"] = {'bb': 1.203645, 'cc': 1.203645, 'c': 0.983360, 'l': 0.927010}
flav_map[4]['el']["elMisIDpos_up"] = {'bb': 1.183760, 'cc': 1.183760, 'c': 0.967115, 'l': 0.911696}
flav_map[5]['el']["elMisIDpos_up"] = {'bb': 1.161886, 'cc': 1.161886, 'c': 0.949244, 'l': 0.894849}
flav_map[2]['mu']["elMisIDpos_up"] = {'bb': 1.511162, 'cc': 1.511162, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["elMisIDpos_up"] = {'bb': 1.455979, 'cc': 1.455979, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["elMisIDpos_up"] = {'bb': 1.406443, 'cc': 1.406443, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["elMisIDpos_up"] = {'bb': 1.345807, 'cc': 1.345807, 'c': 0.890578, 'l': 0.786584}
# elMisIDpos_down 
flav_map[2]['el']["elMisIDpos_down"] = {'bb': 1.326746, 'cc': 1.326746, 'c': 1.000000, 'l': 0.916417}
flav_map[3]['el']["elMisIDpos_down"] = {'bb': 1.294788, 'cc': 1.294788, 'c': 0.975913, 'l': 0.894343}
flav_map[4]['el']["elMisIDpos_down"] = {'bb': 1.264052, 'cc': 1.264052, 'c': 0.952746, 'l': 0.873112}
flav_map[5]['el']["elMisIDpos_down"] = {'bb': 1.230757, 'cc': 1.230757, 'c': 0.927651, 'l': 0.850115}
flav_map[2]['mu']["elMisIDpos_down"] = {'bb': 1.511162, 'cc': 1.511162, 'c': 1.000000, 'l': 0.883229}
flav_map[3]['mu']["elMisIDpos_down"] = {'bb': 1.455979, 'cc': 1.455979, 'c': 0.963483, 'l': 0.850976}
flav_map[4]['mu']["elMisIDpos_down"] = {'bb': 1.406443, 'cc': 1.406443, 'c': 0.930703, 'l': 0.822024}
flav_map[5]['mu']["elMisIDpos_down"] = {'bb': 1.345807, 'cc': 1.345807, 'c': 0.890578, 'l': 0.786584}

# ttgendw 
f_ca_map[2]['el']["ttgendw"] =  1.057587
f_ca_map[3]['el']["ttgendw"] =  1.034635
f_ca_map[4]['el']["ttgendw"] =  1.016666
f_ca_map[5]['el']["ttgendw"] =  0.781589
f_ca_map[2]['mu']["ttgendw"] =  1.146232
f_ca_map[3]['mu']["ttgendw"] =  1.057242
f_ca_map[4]['mu']["ttgendw"] =  0.953193
f_ca_map[5]['mu']["ttgendw"] =  0.800901
# ttgenup 
f_ca_map[2]['el']["ttgenup"] =  1.057752
f_ca_map[3]['el']["ttgenup"] =  1.034660
f_ca_map[4]['el']["ttgenup"] =  1.016878
f_ca_map[5]['el']["ttgenup"] =  0.781487
f_ca_map[2]['mu']["ttgenup"] =  1.146219
f_ca_map[3]['mu']["ttgenup"] =  1.057326
f_ca_map[4]['mu']["ttgenup"] =  0.953291
f_ca_map[5]['mu']["ttgenup"] =  0.800865
# ttisrfsrup 
f_ca_map[2]['el']["ttisrfsrup"] =  1.057689
f_ca_map[3]['el']["ttisrfsrup"] =  1.034650
f_ca_map[4]['el']["ttisrfsrup"] =  1.016798
f_ca_map[5]['el']["ttisrfsrup"] =  0.781526
f_ca_map[2]['mu']["ttisrfsrup"] =  1.146302
f_ca_map[3]['mu']["ttisrfsrup"] =  1.056750
f_ca_map[4]['mu']["ttisrfsrup"] =  0.952616
f_ca_map[5]['mu']["ttisrfsrup"] =  0.801112
# ttisrfsrdw 
f_ca_map[2]['el']["ttisrfsrdw"] =  1.057547
f_ca_map[3]['el']["ttisrfsrdw"] =  1.034629
f_ca_map[4]['el']["ttisrfsrdw"] =  1.016615
f_ca_map[5]['el']["ttisrfsrdw"] =  0.781614
f_ca_map[2]['mu']["ttisrfsrdw"] =  1.146186
f_ca_map[3]['mu']["ttisrfsrdw"] =  1.057558
f_ca_map[4]['mu']["ttisrfsrdw"] =  0.953563
f_ca_map[5]['mu']["ttisrfsrdw"] =  0.800766
# ttpsup 
f_ca_map[2]['el']["ttpsup"] =  1.057622
f_ca_map[3]['el']["ttpsup"] =  1.034640
f_ca_map[4]['el']["ttpsup"] =  1.016711
f_ca_map[5]['el']["ttpsup"] =  0.781568
f_ca_map[2]['mu']["ttpsup"] =  1.146222
f_ca_map[3]['mu']["ttpsup"] =  1.057304
f_ca_map[4]['mu']["ttpsup"] =  0.953266
f_ca_map[5]['mu']["ttpsup"] =  0.800874
# ttpsdw 
f_ca_map[2]['el']["ttpsdw"] =  1.069348
f_ca_map[3]['el']["ttpsdw"] =  1.036230
f_ca_map[4]['el']["ttpsdw"] =  1.029466
f_ca_map[5]['el']["ttpsdw"] =  0.775953
f_ca_map[2]['mu']["ttpsdw"] =  1.146205
f_ca_map[3]['mu']["ttpsdw"] =  1.057431
f_ca_map[4]['mu']["ttpsdw"] =  0.953414
f_ca_map[5]['mu']["ttpsdw"] =  0.800820

# ttgendw 
frac[2]['el']["ttgendw"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttgendw"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttgendw"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttgendw"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttgendw"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttgendw"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttgendw"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttgendw"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# ttgenup 
frac[2]['el']["ttgenup"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttgenup"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttgenup"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttgenup"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttgenup"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttgenup"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttgenup"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttgenup"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# ttisrfsrup 
frac[2]['el']["ttisrfsrup"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttisrfsrup"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttisrfsrup"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttisrfsrup"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttisrfsrup"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttisrfsrup"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttisrfsrup"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttisrfsrup"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# ttisrfsrdw 
frac[2]['el']["ttisrfsrdw"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttisrfsrdw"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttisrfsrdw"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttisrfsrdw"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttisrfsrdw"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttisrfsrdw"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttisrfsrdw"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttisrfsrdw"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# ttpsup 
frac[2]['el']["ttpsup"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttpsup"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttpsup"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttpsup"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttpsup"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttpsup"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttpsup"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttpsup"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}
# ttpsdw 
frac[2]['el']["ttpsdw"] = {'bb': 0.095379,'cc': 0.065570,'c': 0.209862,'l': 0.629189}
frac[3]['el']["ttpsdw"] = {'bb': 0.118557,'cc': 0.100588,'c': 0.219462,'l': 0.561392}
frac[4]['el']["ttpsdw"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215285,'l': 0.503997}
frac[5]['el']["ttpsdw"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209922,'l': 0.487825}
frac[2]['mu']["ttpsdw"] = {'bb': 0.083918,'cc': 0.063837,'c': 0.205449,'l': 0.646796}
frac[3]['mu']["ttpsdw"] = {'bb': 0.107542,'cc': 0.098646,'c': 0.215805,'l': 0.578007}
frac[4]['mu']["ttpsdw"] = {'bb': 0.131000,'cc': 0.135019,'c': 0.207119,'l': 0.526862}
frac[5]['mu']["ttpsdw"] = {'bb': 0.141049,'cc': 0.148513,'c': 0.202402,'l': 0.508036}


# ttgendw 
flav_map[2]['el']["ttgendw"] = {'bb': 1.283842, 'cc': 1.283842, 'c': 1.000000, 'l': 0.927392}
flav_map[3]['el']["ttgendw"] = {'bb': 1.256893, 'cc': 1.256893, 'c': 0.979009, 'l': 0.907925}
flav_map[4]['el']["ttgendw"] = {'bb': 1.230812, 'cc': 1.230812, 'c': 0.958694, 'l': 0.889086}
flav_map[5]['el']["ttgendw"] = {'bb': 1.202380, 'cc': 1.202380, 'c': 0.936548, 'l': 0.868547}
flav_map[2]['mu']["ttgendw"] = {'bb': 1.514002, 'cc': 1.514002, 'c': 1.000000, 'l': 0.882581}
flav_map[3]['mu']["ttgendw"] = {'bb': 1.458419, 'cc': 1.458419, 'c': 0.963287, 'l': 0.850179}
flav_map[4]['mu']["ttgendw"] = {'bb': 1.408544, 'cc': 1.408544, 'c': 0.930345, 'l': 0.821104}
flav_map[5]['mu']["ttgendw"] = {'bb': 1.347517, 'cc': 1.347517, 'c': 0.890036, 'l': 0.785529}
# ttgenup 
flav_map[2]['el']["ttgenup"] = {'bb': 1.301414, 'cc': 1.301414, 'c': 1.000000, 'l': 0.922897}
flav_map[3]['el']["ttgenup"] = {'bb': 1.272442, 'cc': 1.272442, 'c': 0.977738, 'l': 0.902352}
flav_map[4]['el']["ttgenup"] = {'bb': 1.244476, 'cc': 1.244476, 'c': 0.956249, 'l': 0.882520}
flav_map[5]['el']["ttgenup"] = {'bb': 1.214068, 'cc': 1.214068, 'c': 0.932883, 'l': 0.860955}
flav_map[2]['mu']["ttgenup"] = {'bb': 1.519482, 'cc': 1.519482, 'c': 1.000000, 'l': 0.881329}
flav_map[3]['mu']["ttgenup"] = {'bb': 1.463125, 'cc': 1.463125, 'c': 0.962911, 'l': 0.848641}
flav_map[4]['mu']["ttgenup"] = {'bb': 1.412593, 'cc': 1.412593, 'c': 0.929655, 'l': 0.819331}
flav_map[5]['mu']["ttgenup"] = {'bb': 1.350810, 'cc': 1.350810, 'c': 0.888994, 'l': 0.783496}
# ttisrfsrup 
flav_map[2]['el']["ttisrfsrup"] = {'bb': 1.294748, 'cc': 1.294748, 'c': 1.000000, 'l': 0.924603}
flav_map[3]['el']["ttisrfsrup"] = {'bb': 1.266548, 'cc': 1.266548, 'c': 0.978220, 'l': 0.904464}
flav_map[4]['el']["ttisrfsrup"] = {'bb': 1.239301, 'cc': 1.239301, 'c': 0.957175, 'l': 0.885006}
flav_map[5]['el']["ttisrfsrup"] = {'bb': 1.209645, 'cc': 1.209645, 'c': 0.934270, 'l': 0.863828}
flav_map[2]['mu']["ttisrfsrup"] = {'bb': 1.482092, 'cc': 1.482092, 'c': 1.000000, 'l': 0.889870}
flav_map[3]['mu']["ttisrfsrup"] = {'bb': 1.430942, 'cc': 1.430942, 'c': 0.965488, 'l': 0.859159}
flav_map[4]['mu']["ttisrfsrup"] = {'bb': 1.384845, 'cc': 1.384845, 'c': 0.934385, 'l': 0.831482}
flav_map[5]['mu']["ttisrfsrup"] = {'bb': 1.328183, 'cc': 1.328183, 'c': 0.896154, 'l': 0.797461}
# ttisrfsrdw 
flav_map[2]['el']["ttisrfsrdw"] = {'bb': 1.279583, 'cc': 1.279583, 'c': 1.000000, 'l': 0.928481}
flav_map[3]['el']["ttisrfsrdw"] = {'bb': 1.253118, 'cc': 1.253118, 'c': 0.979318, 'l': 0.909278}
flav_map[4]['el']["ttisrfsrdw"] = {'bb': 1.227490, 'cc': 1.227490, 'c': 0.959289, 'l': 0.890682}
flav_map[5]['el']["ttisrfsrdw"] = {'bb': 1.199533, 'cc': 1.199533, 'c': 0.937441, 'l': 0.870396}
flav_map[2]['mu']["ttisrfsrdw"] = {'bb': 1.534617, 'cc': 1.534617, 'c': 1.000000, 'l': 0.877871}
flav_map[3]['mu']["ttisrfsrdw"] = {'bb': 1.476104, 'cc': 1.476104, 'c': 0.961871, 'l': 0.844399}
flav_map[4]['mu']["ttisrfsrdw"] = {'bb': 1.423746, 'cc': 1.423746, 'c': 0.927753, 'l': 0.814448}
flav_map[5]['mu']["ttisrfsrdw"] = {'bb': 1.359868, 'cc': 1.359868, 'c': 0.886128, 'l': 0.777906}
# ttpsup 
flav_map[2]['el']["ttpsup"] = {'bb': 1.287539, 'cc': 1.287539, 'c': 1.000000, 'l': 0.926446}
flav_map[3]['el']["ttpsup"] = {'bb': 1.260168, 'cc': 1.260168, 'c': 0.978742, 'l': 0.906751}
flav_map[4]['el']["ttpsup"] = {'bb': 1.233693, 'cc': 1.233693, 'c': 0.958179, 'l': 0.887701}
flav_map[5]['el']["ttpsup"] = {'bb': 1.204846, 'cc': 1.204846, 'c': 0.935775, 'l': 0.866945}
flav_map[2]['mu']["ttpsup"] = {'bb': 1.518064, 'cc': 1.518064, 'c': 1.000000, 'l': 0.881653}
flav_map[3]['mu']["ttpsup"] = {'bb': 1.461907, 'cc': 1.461907, 'c': 0.963008, 'l': 0.849039}
flav_map[4]['mu']["ttpsup"] = {'bb': 1.411545, 'cc': 1.411545, 'c': 0.929833, 'l': 0.819790}
flav_map[5]['mu']["ttpsup"] = {'bb': 1.349959, 'cc': 1.349959, 'c': 0.889264, 'l': 0.784022}
# ttpsdw 
flav_map[2]['el']["ttpsdw"] = {'bb': 2.519159, 'cc': 2.519159, 'c': 1.000000, 'l': 0.611392}
flav_map[3]['el']["ttpsdw"] = {'bb': 2.259831, 'cc': 2.259831, 'c': 0.897057, 'l': 0.548454}
flav_map[4]['el']["ttpsdw"] = {'bb': 2.047102, 'cc': 2.047102, 'c': 0.812613, 'l': 0.496826}
flav_map[5]['el']["ttpsdw"] = {'bb': 1.848773, 'cc': 1.848773, 'c': 0.733885, 'l': 0.448692}
flav_map[2]['mu']["ttpsdw"] = {'bb': 1.526322, 'cc': 1.526322, 'c': 1.000000, 'l': 0.879766}
flav_map[3]['mu']["ttpsdw"] = {'bb': 1.468995, 'cc': 1.468995, 'c': 0.962441, 'l': 0.846722}
flav_map[4]['mu']["ttpsdw"] = {'bb': 1.417640, 'cc': 1.417640, 'c': 0.928794, 'l': 0.817121}
flav_map[5]['mu']["ttpsdw"] = {'bb': 1.354911, 'cc': 1.354911, 'c': 0.887697, 'l': 0.780965}

# NNPDF30_nnlo_as_0118_0 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_0"] =  1.057527
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_0"] =  1.034623
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_0"] =  1.016598
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_0"] =  0.781657
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_0"] =  1.146228
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_0"] =  1.057240
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_0"] =  0.953119
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_0"] =  0.800967
# NNPDF30_nnlo_as_0118_1 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_1"] =  1.007355
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_1"] =  0.981596
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_1"] =  0.972263
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_1"] =  0.751927
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_1"] =  1.142433
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_1"] =  1.011194
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_1"] =  0.919393
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_1"] =  0.777049
# NNPDF30_nnlo_as_0118_2 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_2"] =  1.051428
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_2"] =  1.029482
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_2"] =  1.017071
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_2"] =  0.770232
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_2"] =  1.135085
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_2"] =  1.065629
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_2"] =  0.960780
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_2"] =  0.798168
# NNPDF30_nnlo_as_0118_3 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_3"] =  1.105508
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_3"] =  1.094985
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_3"] =  1.061540
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_3"] =  0.785750
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_3"] =  1.225060
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_3"] =  1.106303
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_3"] =  0.989841
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_3"] =  0.824213
# NNPDF30_nnlo_as_0118_4 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_4"] =  1.067491
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_4"] =  1.052921
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_4"] =  1.040196
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_4"] =  0.807740
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_4"] =  1.164649
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_4"] =  1.081803
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_4"] =  0.975666
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_4"] =  0.823238
# NNPDF30_nnlo_as_0118_5 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_5"] =  1.039714
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_5"] =  1.006546
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_5"] =  0.978152
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_5"] =  0.742121
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_5"] =  1.121122
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_5"] =  1.033274
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_5"] =  0.926171
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_5"] =  0.772694
# NNPDF30_nnlo_as_0118_6 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_6"] =  1.054649
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_6"] =  1.045518
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_6"] =  1.029152
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_6"] =  0.784335
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_6"] =  1.240053
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_6"] =  1.068447
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_6"] =  0.960913
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_6"] =  0.810236
# NNPDF30_nnlo_as_0118_7 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_7"] =  1.048974
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_7"] =  1.040615
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_7"] =  1.037100
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_7"] =  0.796733
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_7"] =  1.141896
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_7"] =  1.067816
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_7"] =  0.972099
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_7"] =  0.821369
# NNPDF30_nnlo_as_0118_8 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_8"] =  1.062042
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_8"] =  1.044337
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_8"] =  1.031149
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_8"] =  0.797452
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_8"] =  1.121395
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_8"] =  1.068427
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_8"] =  0.964804
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_8"] =  0.813016
# NNPDF30_nnlo_as_0118_9 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_9"] =  1.057037
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_9"] =  1.023215
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_9"] =  0.999774
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_9"] =  0.779733
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_9"] =  1.071035
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_9"] =  1.042822
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_9"] =  0.943363
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_9"] =  0.789766
# NNPDF30_nnlo_as_0118_10 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_10"] =  1.067507
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_10"] =  1.051152
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_10"] =  1.040805
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_10"] =  0.804173
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_10"] =  1.100374
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_10"] =  1.078266
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_10"] =  0.979123
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_10"] =  0.818399
# NNPDF30_nnlo_as_0118_11 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_11"] =  1.067557
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_11"] =  1.048276
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_11"] =  1.025847
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_11"] =  0.771193
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_11"] =  1.160437
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_11"] =  1.070249
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_11"] =  0.960713
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_11"] =  0.797204
# NNPDF30_nnlo_as_0118_12 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_12"] =  1.070102
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_12"] =  1.047429
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_12"] =  1.036201
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_12"] =  0.781825
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_12"] =  1.147558
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_12"] =  1.064580
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_12"] =  0.973181
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_12"] =  0.817511
# NNPDF30_nnlo_as_0118_13 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_13"] =  1.077150
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_13"] =  1.055673
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_13"] =  1.030649
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_13"] =  0.795566
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_13"] =  1.185498
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_13"] =  1.077081
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_13"] =  0.962363
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_13"] =  0.805174
# NNPDF30_nnlo_as_0118_14 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_14"] =  1.057933
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_14"] =  1.031783
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_14"] =  1.007431
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_14"] =  0.764520
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_14"] =  1.197136
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_14"] =  1.052415
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_14"] =  0.942887
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_14"] =  0.788647
# NNPDF30_nnlo_as_0118_15 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_15"] =  1.059887
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_15"] =  1.034446
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_15"] =  1.006841
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_15"] =  0.781116
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_15"] =  1.174424
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_15"] =  1.051978
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_15"] =  0.943438
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_15"] =  0.793273
# NNPDF30_nnlo_as_0118_16 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_16"] =  1.097501
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_16"] =  1.073061
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_16"] =  1.052883
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_16"] =  0.815095
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_16"] =  1.017217
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_16"] =  1.090142
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_16"] =  0.991586
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_16"] =  0.827828
# NNPDF30_nnlo_as_0118_17 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_17"] =  1.052937
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_17"] =  1.024405
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_17"] =  1.006497
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_17"] =  0.777363
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_17"] =  1.191876
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_17"] =  1.049240
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_17"] =  0.940372
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_17"] =  0.796790
# NNPDF30_nnlo_as_0118_18 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_18"] =  1.003687
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_18"] =  0.979719
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_18"] =  0.958918
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_18"] =  0.740814
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_18"] =  1.168522
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_18"] =  1.010444
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_18"] =  0.906915
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_18"] =  0.767379
# NNPDF30_nnlo_as_0118_19 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_19"] =  1.063800
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_19"] =  1.038923
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_19"] =  1.017162
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_19"] =  0.788267
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_19"] =  1.128487
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_19"] =  1.062829
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_19"] =  0.951170
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_19"] =  0.808467
# NNPDF30_nnlo_as_0118_20 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_20"] =  0.971490
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_20"] =  0.938942
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_20"] =  0.914665
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_20"] =  0.706251
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_20"] =  1.184156
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_20"] =  0.958054
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_20"] =  0.861246
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_20"] =  0.736082
# NNPDF30_nnlo_as_0118_21 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_21"] =  1.087766
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_21"] =  1.059404
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_21"] =  1.034042
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_21"] =  0.779698
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_21"] =  1.194547
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_21"] =  1.080513
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_21"] =  0.964549
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_21"] =  0.803604
# NNPDF30_nnlo_as_0118_22 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_22"] =  1.112987
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_22"] =  1.094033
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_22"] =  1.070841
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_22"] =  0.808213
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_22"] =  1.226087
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_22"] =  1.112600
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_22"] =  0.992462
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_22"] =  0.821754
# NNPDF30_nnlo_as_0118_23 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_23"] =  1.073079
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_23"] =  1.065010
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_23"] =  1.061915
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_23"] =  0.804134
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_23"] =  1.169800
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_23"] =  1.087508
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_23"] =  0.984665
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_23"] =  0.829155
# NNPDF30_nnlo_as_0118_24 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_24"] =  1.027407
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_24"] =  0.994827
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_24"] =  0.964456
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_24"] =  0.738527
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_24"] =  1.158137
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_24"] =  1.018837
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_24"] =  0.909371
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_24"] =  0.757771
# NNPDF30_nnlo_as_0118_25 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_25"] =  1.075936
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_25"] =  1.066855
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_25"] =  1.053943
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_25"] =  0.812752
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_25"] =  1.146205
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_25"] =  1.090520
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_25"] =  0.988907
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_25"] =  0.832019
# NNPDF30_nnlo_as_0118_26 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_26"] =  1.043424
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_26"] =  1.016809
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_26"] =  0.994078
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_26"] =  0.757254
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_26"] =  1.078188
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_26"] =  1.043010
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_26"] =  0.938876
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_26"] =  0.781693
# NNPDF30_nnlo_as_0118_27 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_27"] =  1.065467
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_27"] =  1.034169
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_27"] =  1.010252
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_27"] =  0.766667
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_27"] =  1.132688
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_27"] =  1.056136
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_27"] =  0.946574
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_27"] =  0.785658
# NNPDF30_nnlo_as_0118_28 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_28"] =  1.098042
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_28"] =  1.066207
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_28"] =  1.035608
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_28"] =  0.782933
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_28"] =  1.230366
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_28"] =  1.079179
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_28"] =  0.965855
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_28"] =  0.807652
# NNPDF30_nnlo_as_0118_29 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_29"] =  1.076486
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_29"] =  1.071568
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_29"] =  1.072288
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_29"] =  0.816897
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_29"] =  1.118374
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_29"] =  1.096618
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_29"] =  0.997494
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_29"] =  0.845342
# NNPDF30_nnlo_as_0118_30 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_30"] =  1.058265
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_30"] =  1.035404
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_30"] =  1.016038
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_30"] =  0.786886
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_30"] =  1.197256
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_30"] =  1.051025
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_30"] =  0.948260
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_30"] =  0.803458
# NNPDF30_nnlo_as_0118_31 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_31"] =  1.002635
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_31"] =  0.968673
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_31"] =  0.948842
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_31"] =  0.742085
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_31"] =  1.126207
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_31"] =  0.994109
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_31"] =  0.896506
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_31"] =  0.759152
# NNPDF30_nnlo_as_0118_32 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_32"] =  1.046038
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_32"] =  1.022715
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_32"] =  1.005527
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_32"] =  0.765998
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_32"] =  1.090613
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_32"] =  1.045924
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_32"] =  0.949265
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_32"] =  0.796160
# NNPDF30_nnlo_as_0118_33 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_33"] =  1.061144
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_33"] =  1.048914
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_33"] =  1.027792
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_33"] =  0.794989
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_33"] =  1.208492
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_33"] =  1.069501
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_33"] =  0.958408
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_33"] =  0.837188
# NNPDF30_nnlo_as_0118_34 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_34"] =  1.059557
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_34"] =  1.036923
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_34"] =  1.013524
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_34"] =  0.793250
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_34"] =  1.246438
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_34"] =  1.057130
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_34"] =  0.951346
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_34"] =  0.804737
# NNPDF30_nnlo_as_0118_35 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_35"] =  1.091308
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_35"] =  1.058139
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_35"] =  1.027794
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_35"] =  0.785327
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_35"] =  1.100345
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_35"] =  1.078013
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_35"] =  0.973470
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_35"] =  0.800129
# NNPDF30_nnlo_as_0118_36 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_36"] =  0.979822
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_36"] =  0.935539
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_36"] =  0.923045
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_36"] =  0.721584
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_36"] =  0.970383
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_36"] =  0.971243
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_36"] =  0.884423
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_36"] =  0.752774
# NNPDF30_nnlo_as_0118_37 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_37"] =  1.082672
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_37"] =  1.043068
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_37"] =  1.012494
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_37"] =  0.783551
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_37"] =  1.064516
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_37"] =  1.068248
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_37"] =  0.958976
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_37"] =  0.791491
# NNPDF30_nnlo_as_0118_38 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_38"] =  0.980509
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_38"] =  0.924435
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_38"] =  0.901554
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_38"] =  0.701394
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_38"] =  1.023062
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_38"] =  0.954877
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_38"] =  0.860513
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_38"] =  0.730581
# NNPDF30_nnlo_as_0118_39 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_39"] =  1.062232
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_39"] =  1.041790
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_39"] =  1.031708
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_39"] =  0.783207
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_39"] =  1.143074
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_39"] =  1.070039
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_39"] =  0.967495
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_39"] =  0.811591
# NNPDF30_nnlo_as_0118_40 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_40"] =  1.030290
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_40"] =  1.017430
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_40"] =  1.001740
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_40"] =  0.757733
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_40"] =  1.155306
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_40"] =  1.037628
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_40"] =  0.937994
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_40"] =  0.788519
# NNPDF30_nnlo_as_0118_41 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_41"] =  1.038040
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_41"] =  1.003686
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_41"] =  0.971354
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_41"] =  0.734268
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_41"] =  1.121400
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_41"] =  1.026290
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_41"] =  0.917888
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_41"] =  0.762522
# NNPDF30_nnlo_as_0118_42 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_42"] =  1.050885
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_42"] =  1.027457
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_42"] =  1.033009
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_42"] =  0.760522
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_42"] =  1.153058
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_42"] =  1.044118
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_42"] =  0.941487
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_42"] =  0.789720
# NNPDF30_nnlo_as_0118_43 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_43"] =  1.059202
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_43"] =  1.039287
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_43"] =  1.036066
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_43"] =  0.803266
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_43"] =  1.045509
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_43"] =  1.068849
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_43"] =  0.977423
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_43"] =  0.821635
# NNPDF30_nnlo_as_0118_44 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_44"] =  1.081543
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_44"] =  1.059096
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_44"] =  1.031761
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_44"] =  0.776234
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_44"] =  1.153907
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_44"] =  1.080650
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_44"] =  0.962766
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_44"] =  0.813168
# NNPDF30_nnlo_as_0118_45 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_45"] =  1.061986
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_45"] =  1.033183
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_45"] =  1.012354
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_45"] =  0.787471
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_45"] =  1.050121
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_45"] =  1.058905
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_45"] =  0.958695
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_45"] =  0.795646
# NNPDF30_nnlo_as_0118_46 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_46"] =  1.080922
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_46"] =  1.064122
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_46"] =  1.034856
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_46"] =  0.782597
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_46"] =  1.240811
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_46"] =  1.077145
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_46"] =  0.964185
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_46"] =  0.804213
# NNPDF30_nnlo_as_0118_47 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_47"] =  1.039146
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_47"] =  0.997417
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_47"] =  0.978280
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_47"] =  0.753462
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_47"] =  1.143832
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_47"] =  1.020933
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_47"] =  0.920302
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_47"] =  0.775014
# NNPDF30_nnlo_as_0118_48 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_48"] =  1.062350
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_48"] =  1.029200
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_48"] =  1.002302
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_48"] =  0.763666
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_48"] =  1.166959
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_48"] =  1.050122
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_48"] =  1.067799
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_48"] =  0.786936
# NNPDF30_nnlo_as_0118_49 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_49"] =  3.456397
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_49"] =  -2.552151
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_49"] =  -1.520870
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_49"] =  -2.822561
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_49"] =  1.147244
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_49"] =  0.999377
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_49"] =  0.899482
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_49"] =  0.757910
# NNPDF30_nnlo_as_0118_50 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_50"] =  1.075048
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_50"] =  1.061972
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_50"] =  1.046060
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_50"] =  0.793876
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_50"] =  1.251035
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_50"] =  1.076573
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_50"] =  0.969576
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_50"] =  0.816508
# NNPDF30_nnlo_as_0118_51 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_51"] =  1.013882
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_51"] =  1.003609
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_51"] =  0.998553
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_51"] =  0.760144
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_51"] =  1.179787
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_51"] =  1.036771
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_51"] =  0.941368
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_51"] =  0.800765
# NNPDF30_nnlo_as_0118_52 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_52"] =  1.102164
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_52"] =  1.093547
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_52"] =  1.097790
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_52"] =  0.829795
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_52"] =  1.216195
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_52"] =  1.118856
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_52"] =  1.011186
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_52"] =  0.857228
# NNPDF30_nnlo_as_0118_53 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_53"] =  1.045060
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_53"] =  1.014396
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_53"] =  0.992048
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_53"] =  0.767031
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_53"] =  1.033124
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_53"] =  1.040652
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_53"] =  0.938236
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_53"] =  0.783976
# NNPDF30_nnlo_as_0118_54 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_54"] =  1.028235
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_54"] =  0.984543
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_54"] =  0.937813
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_54"] =  0.667728
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_54"] =  1.149001
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_54"] =  0.980255
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_54"] =  0.911069
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_54"] =  0.781106
# NNPDF30_nnlo_as_0118_55 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_55"] =  1.058038
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_55"] =  1.026335
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_55"] =  0.999697
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_55"] =  0.785117
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_55"] =  1.166011
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_55"] =  1.049609
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_55"] =  0.944480
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_55"] =  0.799323
# NNPDF30_nnlo_as_0118_56 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_56"] =  1.004164
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_56"] =  1.008465
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_56"] =  1.035225
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_56"] =  0.793464
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_56"] =  1.316394
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_56"] =  1.065891
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_56"] =  0.971995
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_56"] =  0.831911
# NNPDF30_nnlo_as_0118_57 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_57"] =  1.064507
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_57"] =  1.044999
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_57"] =  1.056850
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_57"] =  0.805276
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_57"] =  1.113730
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_57"] =  1.066627
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_57"] =  0.966841
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_57"] =  0.811703
# NNPDF30_nnlo_as_0118_58 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_58"] =  1.089353
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_58"] =  1.084961
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_58"] =  1.062163
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_58"] =  0.808676
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_58"] =  1.177489
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_58"] =  1.097427
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_58"] =  0.982197
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_58"] =  0.814684
# NNPDF30_nnlo_as_0118_59 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_59"] =  1.020002
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_59"] =  0.987748
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_59"] =  0.960745
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_59"] =  0.741957
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_59"] =  1.128992
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_59"] =  1.013987
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_59"] =  0.909492
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_59"] =  0.765634
# NNPDF30_nnlo_as_0118_60 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_60"] =  1.096894
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_60"] =  1.063557
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_60"] =  1.034539
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_60"] =  0.785756
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_60"] =  1.248462
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_60"] =  1.097190
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_60"] =  0.961182
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_60"] =  0.772682
# NNPDF30_nnlo_as_0118_61 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_61"] =  1.136698
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_61"] =  1.117151
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_61"] =  1.090506
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_61"] =  0.839156
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_61"] =  1.143129
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_61"] =  1.129752
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_61"] =  1.017128
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_61"] =  0.843085
# NNPDF30_nnlo_as_0118_62 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_62"] =  1.062793
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_62"] =  1.031939
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_62"] =  1.003853
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_62"] =  0.769281
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_62"] =  1.112468
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_62"] =  1.022035
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_62"] =  0.898125
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_62"] =  0.749352
# NNPDF30_nnlo_as_0118_63 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_63"] =  1.039621
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_63"] =  1.029587
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_63"] =  1.016367
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_63"] =  0.779487
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_63"] =  1.236147
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_63"] =  1.052941
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_63"] =  0.949951
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_63"] =  0.803646
# NNPDF30_nnlo_as_0118_64 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_64"] =  1.022356
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_64"] =  0.996695
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_64"] =  0.989616
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_64"] =  0.756448
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_64"] =  1.167147
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_64"] =  1.023834
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_64"] =  0.926101
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_64"] =  0.787850
# NNPDF30_nnlo_as_0118_65 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_65"] =  1.066792
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_65"] =  1.044988
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_65"] =  1.034795
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_65"] =  0.796038
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_65"] =  1.174100
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_65"] =  1.102599
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_65"] =  0.965178
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_65"] =  0.810880
# NNPDF30_nnlo_as_0118_66 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_66"] =  1.067162
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_66"] =  1.035364
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_66"] =  1.009264
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_66"] =  0.773978
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_66"] =  1.061049
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_66"] =  1.057326
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_66"] =  0.953357
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_66"] =  0.795244
# NNPDF30_nnlo_as_0118_67 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_67"] =  1.095682
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_67"] =  1.091149
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_67"] =  1.076656
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_67"] =  0.807302
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_67"] =  1.249828
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_67"] =  1.109039
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_67"] =  0.998920
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_67"] =  0.855253
# NNPDF30_nnlo_as_0118_68 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_68"] =  1.069973
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_68"] =  1.040355
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_68"] =  1.016663
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_68"] =  0.784566
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_68"] =  1.175245
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_68"] =  1.063004
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_68"] =  0.952930
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_68"] =  0.795574
# NNPDF30_nnlo_as_0118_69 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_69"] =  1.066113
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_69"] =  1.040568
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_69"] =  1.021610
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_69"] =  0.791647
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_69"] =  1.118376
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_69"] =  1.063867
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_69"] =  0.959519
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_69"] =  0.809984
# NNPDF30_nnlo_as_0118_70 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_70"] =  1.054780
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_70"] =  1.025721
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_70"] =  0.999930
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_70"] =  0.758649
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_70"] =  1.121540
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_70"] =  1.048301
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_70"] =  0.939811
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_70"] =  0.783174
# NNPDF30_nnlo_as_0118_71 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_71"] =  1.076464
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_71"] =  1.063501
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_71"] =  1.048382
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_71"] =  0.805698
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_71"] =  1.175569
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_71"] =  1.086353
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_71"] =  0.984929
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_71"] =  0.835780
# NNPDF30_nnlo_as_0118_72 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_72"] =  0.920289
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_72"] =  0.876055
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_72"] =  0.862137
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_72"] =  0.679749
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_72"] =  1.083978
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_72"] =  0.908958
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_72"] =  0.826913
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_72"] =  0.711400
# NNPDF30_nnlo_as_0118_73 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_73"] =  1.084847
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_73"] =  1.048041
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_73"] =  1.017440
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_73"] =  0.775542
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_73"] =  1.151922
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_73"] =  1.077712
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_73"] =  0.948208
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_73"] =  0.795710
# NNPDF30_nnlo_as_0118_74 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_74"] =  1.053632
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_74"] =  1.020597
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_74"] =  1.005507
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_74"] =  0.771138
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_74"] =  1.122181
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_74"] =  1.052669
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_74"] =  0.947366
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_74"] =  0.793488
# NNPDF30_nnlo_as_0118_75 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_75"] =  1.091951
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_75"] =  1.070595
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_75"] =  1.051100
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_75"] =  0.802476
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_75"] =  1.161293
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_75"] =  1.087160
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_75"] =  0.986242
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_75"] =  0.825603
# NNPDF30_nnlo_as_0118_76 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_76"] =  1.071596
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_76"] =  1.042593
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_76"] =  1.020787
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_76"] =  0.790597
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_76"] =  1.121686
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_76"] =  1.063222
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_76"] =  0.961091
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_76"] =  0.806245
# NNPDF30_nnlo_as_0118_77 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_77"] =  1.081166
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_77"] =  1.056444
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_77"] =  1.041260
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_77"] =  0.802228
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_77"] =  1.121901
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_77"] =  1.084735
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_77"] =  0.974655
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_77"] =  0.821292
# NNPDF30_nnlo_as_0118_78 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_78"] =  1.136909
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_78"] =  1.121210
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_78"] =  1.099536
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_78"] =  0.822241
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_78"] =  1.274095
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_78"] =  1.136121
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_78"] =  1.014313
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_78"] =  0.863214
# NNPDF30_nnlo_as_0118_79 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_79"] =  1.032706
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_79"] =  1.019787
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_79"] =  1.028518
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_79"] =  0.790611
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_79"] =  1.184222
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_79"] =  1.048012
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_79"] =  0.959936
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_79"] =  0.822510
# NNPDF30_nnlo_as_0118_80 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_80"] =  1.094580
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_80"] =  1.080017
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_80"] =  1.066505
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_80"] =  0.815432
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_80"] =  1.147514
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_80"] =  1.098395
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_80"] =  0.995096
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_80"] =  0.831601
# NNPDF30_nnlo_as_0118_81 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_81"] =  1.056697
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_81"] =  1.016240
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_81"] =  0.990588
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_81"] =  0.749381
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_81"] =  1.127068
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_81"] =  1.039941
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_81"] =  0.930801
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_81"] =  0.776220
# NNPDF30_nnlo_as_0118_82 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_82"] =  1.079468
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_82"] =  1.056042
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_82"] =  1.032570
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_82"] =  0.782903
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_82"] =  1.172156
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_82"] =  1.080926
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_82"] =  0.969536
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_82"] =  0.805769
# NNPDF30_nnlo_as_0118_83 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_83"] =  1.074972
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_83"] =  1.037809
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_83"] =  1.006509
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_83"] =  0.767481
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_83"] =  0.805271
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_83"] =  1.109186
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_83"] =  1.021138
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_83"] =  0.842842
# NNPDF30_nnlo_as_0118_84 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_84"] =  1.028986
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_84"] =  1.005238
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_84"] =  0.982954
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_84"] =  0.751372
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_84"] =  1.214302
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_84"] =  1.030520
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_84"] =  0.925277
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_84"] =  0.778053
# NNPDF30_nnlo_as_0118_85 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_85"] =  1.044828
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_85"] =  1.018665
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_85"] =  1.006908
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_85"] =  0.767017
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_85"] =  1.062990
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_85"] =  1.049319
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_85"] =  0.951904
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_85"] =  0.795666
# NNPDF30_nnlo_as_0118_86 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_86"] =  1.107799
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_86"] =  1.095399
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_86"] =  1.084166
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_86"] =  0.827162
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_86"] =  1.178166
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_86"] =  1.118005
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_86"] =  1.005054
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_86"] =  0.847729
# NNPDF30_nnlo_as_0118_87 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_87"] =  1.029435
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_87"] =  1.016510
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_87"] =  1.004414
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_87"] =  0.766934
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_87"] =  1.181561
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_87"] =  1.040814
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_87"] =  0.942701
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_87"] =  0.801887
# NNPDF30_nnlo_as_0118_88 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_88"] =  1.034574
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_88"] =  1.010811
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_88"] =  0.984972
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_88"] =  0.782849
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_88"] =  1.174201
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_88"] =  1.031329
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_88"] =  0.928123
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_88"] =  0.782552
# NNPDF30_nnlo_as_0118_89 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_89"] =  1.112747
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_89"] =  1.123131
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_89"] =  1.128344
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_89"] =  0.861216
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_89"] =  1.136146
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_89"] =  1.153154
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_89"] =  1.051216
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_89"] =  0.879925
# NNPDF30_nnlo_as_0118_90 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_90"] =  1.064487
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_90"] =  1.016987
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_90"] =  0.989837
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_90"] =  0.788979
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_90"] =  0.992787
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_90"] =  1.032168
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_90"] =  0.934664
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_90"] =  0.788277
# NNPDF30_nnlo_as_0118_91 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_91"] =  1.073960
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_91"] =  1.070756
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_91"] =  1.072124
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_91"] =  0.831674
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_91"] =  1.223373
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_91"] =  1.097298
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_91"] =  0.999317
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_91"] =  0.852329
# NNPDF30_nnlo_as_0118_92 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_92"] =  1.063836
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_92"] =  1.043886
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_92"] =  1.024966
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_92"] =  0.791498
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_92"] =  1.159622
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_92"] =  1.070562
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_92"] =  0.963415
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_92"] =  0.808030
# NNPDF30_nnlo_as_0118_93 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_93"] =  1.047535
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_93"] =  1.022736
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_93"] =  1.001866
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_93"] =  0.771077
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_93"] =  1.108004
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_93"] =  1.050021
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_93"] =  0.944890
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_93"] =  0.788528
# NNPDF30_nnlo_as_0118_94 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_94"] =  1.040890
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_94"] =  1.028693
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_94"] =  1.008616
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_94"] =  0.779245
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_94"] =  1.286622
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_94"] =  1.040391
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_94"] =  0.939566
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_94"] =  0.795865
# NNPDF30_nnlo_as_0118_95 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_95"] =  1.060962
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_95"] =  0.999164
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_95"] =  0.966782
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_95"] =  0.734649
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_95"] =  1.158434
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_95"] =  1.041683
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_95"] =  0.941369
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_95"] =  0.793395
# NNPDF30_nnlo_as_0118_96 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_96"] =  1.056640
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_96"] =  1.036065
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_96"] =  1.020187
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_96"] =  0.772288
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_96"] =  1.159937
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_96"] =  1.064665
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_96"] =  0.957486
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_96"] =  0.803401
# NNPDF30_nnlo_as_0118_97 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_97"] =  1.081842
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_97"] =  1.077567
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_97"] =  1.054978
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_97"] =  0.801586
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_97"] =  1.292201
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_97"] =  1.096309
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_97"] =  0.983874
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_97"] =  0.824284
# NNPDF30_nnlo_as_0118_98 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_98"] =  1.066014
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_98"] =  1.024765
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_98"] =  1.006504
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_98"] =  0.775134
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_98"] =  1.192737
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_98"] =  1.050271
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_98"] =  0.942525
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_98"] =  0.791781
# NNPDF30_nnlo_as_0118_99 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_99"] =  1.090727
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_99"] =  1.068880
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_99"] =  1.057509
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_99"] =  0.805848
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_99"] =  1.087179
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_99"] =  1.098148
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_99"] =  0.995723
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_99"] =  0.829391
# NNPDF30_nnlo_as_0118_90 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_90"] =  1.064487
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_90"] =  1.016987
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_90"] =  0.989837
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_90"] =  0.788979
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_90"] =  0.992787
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_90"] =  1.032168
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_90"] =  0.934664
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_90"] =  0.788277
# NNPDF30_nnlo_as_0118_91 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_91"] =  1.073960
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_91"] =  1.070756
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_91"] =  1.072124
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_91"] =  0.831674
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_91"] =  1.223373
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_91"] =  1.097298
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_91"] =  0.999317
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_91"] =  0.852329
# NNPDF30_nnlo_as_0118_92 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_92"] =  1.063836
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_92"] =  1.043886
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_92"] =  1.024966
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_92"] =  0.791498
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_92"] =  1.159622
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_92"] =  1.070562
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_92"] =  0.963415
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_92"] =  0.808030
# NNPDF30_nnlo_as_0118_93 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_93"] =  1.047535
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_93"] =  1.022736
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_93"] =  1.001866
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_93"] =  0.771077
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_93"] =  1.108004
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_93"] =  1.050021
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_93"] =  0.944890
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_93"] =  0.788528
# NNPDF30_nnlo_as_0118_94 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_94"] =  1.040890
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_94"] =  1.028693
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_94"] =  1.008616
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_94"] =  0.779245
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_94"] =  1.286622
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_94"] =  1.040391
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_94"] =  0.939566
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_94"] =  0.795865
# NNPDF30_nnlo_as_0118_95 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_95"] =  1.060962
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_95"] =  0.999164
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_95"] =  0.966782
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_95"] =  0.734649
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_95"] =  1.158434
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_95"] =  1.041683
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_95"] =  0.941369
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_95"] =  0.793395
# NNPDF30_nnlo_as_0118_96 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_96"] =  1.056640
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_96"] =  1.036065
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_96"] =  1.020187
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_96"] =  0.772288
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_96"] =  1.159937
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_96"] =  1.064665
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_96"] =  0.957486
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_96"] =  0.803401
# NNPDF30_nnlo_as_0118_97 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_97"] =  1.081842
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_97"] =  1.077567
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_97"] =  1.054978
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_97"] =  0.801586
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_97"] =  1.292201
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_97"] =  1.096309
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_97"] =  0.983874
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_97"] =  0.824284
# NNPDF30_nnlo_as_0118_98 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_98"] =  1.066014
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_98"] =  1.024765
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_98"] =  1.006504
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_98"] =  0.775134
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_98"] =  1.192737
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_98"] =  1.050271
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_98"] =  0.942525
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_98"] =  0.791781
# NNPDF30_nnlo_as_0118_99 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_99"] =  1.090727
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_99"] =  1.068880
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_99"] =  1.057509
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_99"] =  0.805848
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_99"] =  1.087179
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_99"] =  1.098148
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_99"] =  0.995723
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_99"] =  0.829391
# NNPDF30_nnlo_as_0118_100 
f_ca_map[2]['el']["NNPDF30_nnlo_as_0118_100"] =  1.051866
f_ca_map[3]['el']["NNPDF30_nnlo_as_0118_100"] =  1.036895
f_ca_map[4]['el']["NNPDF30_nnlo_as_0118_100"] =  1.027505
f_ca_map[5]['el']["NNPDF30_nnlo_as_0118_100"] =  0.789638
f_ca_map[2]['mu']["NNPDF30_nnlo_as_0118_100"] =  1.171636
f_ca_map[3]['mu']["NNPDF30_nnlo_as_0118_100"] =  1.161643
f_ca_map[4]['mu']["NNPDF30_nnlo_as_0118_100"] =  0.959810
f_ca_map[5]['mu']["NNPDF30_nnlo_as_0118_100"] =  0.818693

# NNPDF30_nnlo_as_0118_0 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_0"] = {'bb': 1.274956, 'cc': 1.274956, 'c': 1.000000, 'l': 0.929666}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_0"] = {'bb': 1.249015, 'cc': 1.249015, 'c': 0.979653, 'l': 0.910750}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_0"] = {'bb': 1.223876, 'cc': 1.223876, 'c': 0.959936, 'l': 0.892419}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_0"] = {'bb': 1.196434, 'cc': 1.196434, 'c': 0.938412, 'l': 0.872409}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_0"] = {'bb': 1.510978, 'cc': 1.510978, 'c': 1.000000, 'l': 0.883273}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_0"] = {'bb': 1.455819, 'cc': 1.455819, 'c': 0.963495, 'l': 0.851029}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_0"] = {'bb': 1.406303, 'cc': 1.406303, 'c': 0.930724, 'l': 0.822083}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_0"] = {'bb': 1.345691, 'cc': 1.345691, 'c': 0.890609, 'l': 0.786651}
# NNPDF30_nnlo_as_0118_1 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_1"] = {'bb': 1.329750, 'cc': 1.329750, 'c': 1.000000, 'l': 0.915633}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_1"] = {'bb': 1.297464, 'cc': 1.297464, 'c': 0.975720, 'l': 0.893401}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_1"] = {'bb': 1.266392, 'cc': 1.266392, 'c': 0.952354, 'l': 0.872006}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_1"] = {'bb': 1.232883, 'cc': 1.232883, 'c': 0.927154, 'l': 0.848932}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_1"] = {'bb': 1.501060, 'cc': 1.501060, 'c': 1.000000, 'l': 0.886593}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_1"] = {'bb': 1.446377, 'cc': 1.446377, 'c': 0.963571, 'l': 0.854295}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_1"] = {'bb': 1.398288, 'cc': 1.398288, 'c': 0.931534, 'l': 0.825891}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_1"] = {'bb': 1.339232, 'cc': 1.339232, 'c': 0.892191, 'l': 0.791011}
# NNPDF30_nnlo_as_0118_2 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_2"] = {'bb': 1.309875, 'cc': 1.309875, 'c': 1.000000, 'l': 0.921100}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_2"] = {'bb': 1.280081, 'cc': 1.280081, 'c': 0.977254, 'l': 0.900149}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_2"] = {'bb': 1.251197, 'cc': 1.251197, 'c': 0.955203, 'l': 0.879837}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_2"] = {'bb': 1.219662, 'cc': 1.219662, 'c': 0.931128, 'l': 0.857662}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_2"] = {'bb': 1.816449, 'cc': 1.816449, 'c': 1.000000, 'l': 0.813737}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_2"] = {'bb': 1.713625, 'cc': 1.713625, 'c': 0.943393, 'l': 0.767673}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_2"] = {'bb': 1.624285, 'cc': 1.624285, 'c': 0.894209, 'l': 0.727651}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_2"] = {'bb': 1.519072, 'cc': 1.519072, 'c': 0.836287, 'l': 0.680517}
# NNPDF30_nnlo_as_0118_3 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_3"] = {'bb': 1.312260, 'cc': 1.312260, 'c': 1.000000, 'l': 0.919865}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_3"] = {'bb': 1.282241, 'cc': 1.282241, 'c': 0.977125, 'l': 0.898822}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_3"] = {'bb': 1.252836, 'cc': 1.252836, 'c': 0.954716, 'l': 0.878210}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_3"] = {'bb': 1.220720, 'cc': 1.220720, 'c': 0.930243, 'l': 0.855697}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_3"] = {'bb': 1.490092, 'cc': 1.490092, 'c': 1.000000, 'l': 0.887785}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_3"] = {'bb': 1.437480, 'cc': 1.437480, 'c': 0.964692, 'l': 0.856439}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_3"] = {'bb': 1.390467, 'cc': 1.390467, 'c': 0.933141, 'l': 0.828429}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_3"] = {'bb': 1.332825, 'cc': 1.332825, 'c': 0.894458, 'l': 0.794087}
# NNPDF30_nnlo_as_0118_4 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_4"] = {'bb': 1.320467, 'cc': 1.320467, 'c': 1.000000, 'l': 0.918109}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_4"] = {'bb': 1.289272, 'cc': 1.289272, 'c': 0.976376, 'l': 0.896420}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_4"] = {'bb': 1.259319, 'cc': 1.259319, 'c': 0.953692, 'l': 0.875594}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_4"] = {'bb': 1.226842, 'cc': 1.226842, 'c': 0.929097, 'l': 0.853012}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_4"] = {'bb': 1.565266, 'cc': 1.565266, 'c': 1.000000, 'l': 0.871490}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_4"] = {'bb': 1.502627, 'cc': 1.502627, 'c': 0.959982, 'l': 0.836615}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_4"] = {'bb': 1.446592, 'cc': 1.446592, 'c': 0.924183, 'l': 0.805417}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_4"] = {'bb': 1.378284, 'cc': 1.378284, 'c': 0.880543, 'l': 0.767385}
# NNPDF30_nnlo_as_0118_5 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_5"] = {'bb': 1.268116, 'cc': 1.268116, 'c': 1.000000, 'l': 0.931403}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_5"] = {'bb': 1.242883, 'cc': 1.242883, 'c': 0.980102, 'l': 0.912870}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_5"] = {'bb': 1.218383, 'cc': 1.218383, 'c': 0.960782, 'l': 0.894875}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_5"] = {'bb': 1.191608, 'cc': 1.191608, 'c': 0.939668, 'l': 0.875209}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_5"] = {'bb': 1.526498, 'cc': 1.526498, 'c': 1.000000, 'l': 0.879971}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_5"] = {'bb': 1.469809, 'cc': 1.469809, 'c': 0.962864, 'l': 0.847292}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_5"] = {'bb': 1.419338, 'cc': 1.419338, 'c': 0.929800, 'l': 0.818197}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_5"] = {'bb': 1.357558, 'cc': 1.357558, 'c': 0.889328, 'l': 0.782583}
# NNPDF30_nnlo_as_0118_6 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_6"] = {'bb': 1.242727, 'cc': 1.242727, 'c': 1.000000, 'l': 0.938045}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_6"] = {'bb': 1.220320, 'cc': 1.220320, 'c': 0.981969, 'l': 0.921131}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_6"] = {'bb': 1.198539, 'cc': 1.198539, 'c': 0.964443, 'l': 0.904691}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_6"] = {'bb': 1.174647, 'cc': 1.174647, 'c': 0.945217, 'l': 0.886656}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_6"] = {'bb': 1.362395, 'cc': 1.362395, 'c': 1.000000, 'l': 0.918298}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_6"] = {'bb': 1.325994, 'cc': 1.325994, 'c': 0.973281, 'l': 0.893763}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_6"] = {'bb': 1.293480, 'cc': 1.293480, 'c': 0.949416, 'l': 0.871847}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_6"] = {'bb': 1.252733, 'cc': 1.252733, 'c': 0.919507, 'l': 0.844382}
# NNPDF30_nnlo_as_0118_7 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_7"] = {'bb': 1.289120, 'cc': 1.289120, 'c': 1.000000, 'l': 0.925738}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_7"] = {'bb': 1.261537, 'cc': 1.261537, 'c': 0.978603, 'l': 0.905931}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_7"] = {'bb': 1.234882, 'cc': 1.234882, 'c': 0.957927, 'l': 0.886790}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_7"] = {'bb': 1.205862, 'cc': 1.205862, 'c': 0.935415, 'l': 0.865950}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_7"] = {'bb': 1.512583, 'cc': 1.512583, 'c': 1.000000, 'l': 0.882802}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_7"] = {'bb': 1.457032, 'cc': 1.457032, 'c': 0.963275, 'l': 0.850381}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_7"] = {'bb': 1.407166, 'cc': 1.407166, 'c': 0.930307, 'l': 0.821277}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_7"] = {'bb': 1.346388, 'cc': 1.346388, 'c': 0.890125, 'l': 0.785805}
# NNPDF30_nnlo_as_0118_8 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_8"] = {'bb': 1.296440, 'cc': 1.296440, 'c': 1.000000, 'l': 0.924381}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_8"] = {'bb': 1.268255, 'cc': 1.268255, 'c': 0.978260, 'l': 0.904284}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_8"] = {'bb': 1.240985, 'cc': 1.240985, 'c': 0.957225, 'l': 0.884841}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_8"] = {'bb': 1.211093, 'cc': 1.211093, 'c': 0.934168, 'l': 0.863527}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_8"] = {'bb': 1.536560, 'cc': 1.536560, 'c': 1.000000, 'l': 0.877394}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_8"] = {'bb': 1.478717, 'cc': 1.478717, 'c': 0.962355, 'l': 0.844365}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_8"] = {'bb': 1.426302, 'cc': 1.426302, 'c': 0.928244, 'l': 0.814435}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_8"] = {'bb': 1.361833, 'cc': 1.361833, 'c': 0.886287, 'l': 0.777623}
# NNPDF30_nnlo_as_0118_9 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_9"] = {'bb': 1.233505, 'cc': 1.233505, 'c': 1.000000, 'l': 0.940279}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_9"] = {'bb': 1.212168, 'cc': 1.212168, 'c': 0.982702, 'l': 0.924014}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_9"] = {'bb': 1.191313, 'cc': 1.191313, 'c': 0.965795, 'l': 0.908116}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_9"] = {'bb': 1.168456, 'cc': 1.168456, 'c': 0.947265, 'l': 0.890692}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_9"] = {'bb': 1.595380, 'cc': 1.595380, 'c': 1.000000, 'l': 0.862978}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_9"] = {'bb': 1.529227, 'cc': 1.529227, 'c': 0.958535, 'l': 0.827195}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_9"] = {'bb': 1.468894, 'cc': 1.468894, 'c': 0.920717, 'l': 0.794559}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_9"] = {'bb': 1.396099, 'cc': 1.396099, 'c': 0.875089, 'l': 0.755183}
# NNPDF30_nnlo_as_0118_10 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_10"] = {'bb': 1.402292, 'cc': 1.402292, 'c': 1.000000, 'l': 0.897271}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_10"] = {'bb': 1.361055, 'cc': 1.361055, 'c': 0.970593, 'l': 0.870884}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_10"] = {'bb': 1.321727, 'cc': 1.321727, 'c': 0.942548, 'l': 0.845720}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_10"] = {'bb': 1.279589, 'cc': 1.279589, 'c': 0.912498, 'l': 0.818758}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_10"] = {'bb': 1.761410, 'cc': 1.761410, 'c': 1.000000, 'l': 0.825337}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_10"] = {'bb': 1.668878, 'cc': 1.668878, 'c': 0.947467, 'l': 0.781980}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_10"] = {'bb': 1.586964, 'cc': 1.586964, 'c': 0.900962, 'l': 0.743598}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_10"] = {'bb': 1.489709, 'cc': 1.489709, 'c': 0.845748, 'l': 0.698027}
# NNPDF30_nnlo_as_0118_11 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_11"] = {'bb': 1.252018, 'cc': 1.252018, 'c': 1.000000, 'l': 0.935646}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_11"] = {'bb': 1.228547, 'cc': 1.228547, 'c': 0.981253, 'l': 0.918106}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_11"] = {'bb': 1.205774, 'cc': 1.205774, 'c': 0.963064, 'l': 0.901087}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_11"] = {'bb': 1.180761, 'cc': 1.180761, 'c': 0.943086, 'l': 0.882395}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_11"] = {'bb': 1.485922, 'cc': 1.485922, 'c': 1.000000, 'l': 0.889374}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_11"] = {'bb': 1.434022, 'cc': 1.434022, 'c': 0.965072, 'l': 0.858311}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_11"] = {'bb': 1.387311, 'cc': 1.387311, 'c': 0.933637, 'l': 0.830353}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_11"] = {'bb': 1.330046, 'cc': 1.330046, 'c': 0.895098, 'l': 0.796077}
# NNPDF30_nnlo_as_0118_12 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_12"] = {'bb': 1.453236, 'cc': 1.453236, 'c': 1.000000, 'l': 0.884799}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_12"] = {'bb': 1.405351, 'cc': 1.405351, 'c': 0.967050, 'l': 0.855645}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_12"] = {'bb': 1.360046, 'cc': 1.360046, 'c': 0.935875, 'l': 0.828061}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_12"] = {'bb': 1.311843, 'cc': 1.311843, 'c': 0.902705, 'l': 0.798712}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_12"] = {'bb': 1.696707, 'cc': 1.696707, 'c': 1.000000, 'l': 0.841954}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_12"] = {'bb': 1.614006, 'cc': 1.614006, 'c': 0.951258, 'l': 0.800916}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_12"] = {'bb': 1.540540, 'cc': 1.540540, 'c': 0.907959, 'l': 0.764459}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_12"] = {'bb': 1.453646, 'cc': 1.453646, 'c': 0.856746, 'l': 0.721340}
# NNPDF30_nnlo_as_0118_13 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_13"] = {'bb': 1.275053, 'cc': 1.275053, 'c': 1.000000, 'l': 0.929445}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_13"] = {'bb': 1.249131, 'cc': 1.249131, 'c': 0.979670, 'l': 0.910549}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_13"] = {'bb': 1.224019, 'cc': 1.224019, 'c': 0.959975, 'l': 0.892244}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_13"] = {'bb': 1.196646, 'cc': 1.196646, 'c': 0.938507, 'l': 0.872291}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_13"] = {'bb': 1.478153, 'cc': 1.478153, 'c': 1.000000, 'l': 0.890986}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_13"] = {'bb': 1.427304, 'cc': 1.427304, 'c': 0.965599, 'l': 0.860335}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_13"] = {'bb': 1.381636, 'cc': 1.381636, 'c': 0.934704, 'l': 0.832808}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_13"] = {'bb': 1.325511, 'cc': 1.325511, 'c': 0.896734, 'l': 0.798978}
# NNPDF30_nnlo_as_0118_14 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_14"] = {'bb': 1.308086, 'cc': 1.308086, 'c': 1.000000, 'l': 0.920975}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_14"] = {'bb': 1.278156, 'cc': 1.278156, 'c': 0.977119, 'l': 0.899902}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_14"] = {'bb': 1.249366, 'cc': 1.249366, 'c': 0.955110, 'l': 0.879632}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_14"] = {'bb': 1.218179, 'cc': 1.218179, 'c': 0.931268, 'l': 0.857675}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_14"] = {'bb': 1.447113, 'cc': 1.447113, 'c': 1.000000, 'l': 0.898157}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_14"] = {'bb': 1.399905, 'cc': 1.399905, 'c': 0.967378, 'l': 0.868858}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_14"] = {'bb': 1.357673, 'cc': 1.357673, 'c': 0.938194, 'l': 0.842646}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_14"] = {'bb': 1.305793, 'cc': 1.305793, 'c': 0.902343, 'l': 0.810446}
# NNPDF30_nnlo_as_0118_15 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_15"] = {'bb': 1.275961, 'cc': 1.275961, 'c': 1.000000, 'l': 0.929589}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_15"] = {'bb': 1.249799, 'cc': 1.249799, 'c': 0.979496, 'l': 0.910529}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_15"] = {'bb': 1.224554, 'cc': 1.224554, 'c': 0.959712, 'l': 0.892138}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_15"] = {'bb': 1.197147, 'cc': 1.197147, 'c': 0.938232, 'l': 0.872170}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_15"] = {'bb': 1.471877, 'cc': 1.471877, 'c': 1.000000, 'l': 0.892985}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_15"] = {'bb': 1.421691, 'cc': 1.421691, 'c': 0.965903, 'l': 0.862537}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_15"] = {'bb': 1.376744, 'cc': 1.376744, 'c': 0.935366, 'l': 0.835268}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_15"] = {'bb': 1.321295, 'cc': 1.321295, 'c': 0.897694, 'l': 0.801627}
# NNPDF30_nnlo_as_0118_16 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_16"] = {'bb': 1.141094, 'cc': 1.141094, 'c': 1.000000, 'l': 0.963774}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_16"] = {'bb': 1.129135, 'cc': 1.129135, 'c': 0.989520, 'l': 0.953673}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_16"] = {'bb': 1.117241, 'cc': 1.117241, 'c': 0.979096, 'l': 0.943627}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_16"] = {'bb': 1.103928, 'cc': 1.103928, 'c': 0.967429, 'l': 0.932383}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_16"] = {'bb': 1.701629, 'cc': 1.701629, 'c': 1.000000, 'l': 0.836479}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_16"] = {'bb': 1.621327, 'cc': 1.621327, 'c': 0.952809, 'l': 0.797005}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_16"] = {'bb': 1.546842, 'cc': 1.546842, 'c': 0.909036, 'l': 0.760390}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_16"] = {'bb': 1.457921, 'cc': 1.457921, 'c': 0.856780, 'l': 0.716678}
# NNPDF30_nnlo_as_0118_17 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_17"] = {'bb': 1.318901, 'cc': 1.318901, 'c': 1.000000, 'l': 0.918688}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_17"] = {'bb': 1.287972, 'cc': 1.287972, 'c': 0.976549, 'l': 0.897144}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_17"] = {'bb': 1.258187, 'cc': 1.258187, 'c': 0.953966, 'l': 0.876398}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_17"] = {'bb': 1.225865, 'cc': 1.225865, 'c': 0.929460, 'l': 0.853884}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_17"] = {'bb': 1.465436, 'cc': 1.465436, 'c': 1.000000, 'l': 0.894709}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_17"] = {'bb': 1.416095, 'cc': 1.416095, 'c': 0.966330, 'l': 0.864584}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_17"] = {'bb': 1.371754, 'cc': 1.371754, 'c': 0.936072, 'l': 0.837512}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_17"] = {'bb': 1.317615, 'cc': 1.317615, 'c': 0.899129, 'l': 0.804458}
# NNPDF30_nnlo_as_0118_18 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_18"] = {'bb': 1.191809, 'cc': 1.191809, 'c': 1.000000, 'l': 0.950676}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_18"] = {'bb': 1.174843, 'cc': 1.174843, 'c': 0.985764, 'l': 0.937143}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_18"] = {'bb': 1.158224, 'cc': 1.158224, 'c': 0.971820, 'l': 0.923886}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_18"] = {'bb': 1.139825, 'cc': 1.139825, 'c': 0.956382, 'l': 0.909210}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_18"] = {'bb': 1.314557, 'cc': 1.314557, 'c': 1.000000, 'l': 0.928981}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_18"] = {'bb': 1.284185, 'cc': 1.284185, 'c': 0.976895, 'l': 0.907517}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_18"] = {'bb': 1.256623, 'cc': 1.256623, 'c': 0.955929, 'l': 0.888040}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_18"] = {'bb': 1.221939, 'cc': 1.221939, 'c': 0.929545, 'l': 0.863530}
# NNPDF30_nnlo_as_0118_19 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_19"] = {'bb': 1.287016, 'cc': 1.287016, 'c': 1.000000, 'l': 0.926675}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_19"] = {'bb': 1.259753, 'cc': 1.259753, 'c': 0.978817, 'l': 0.907045}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_19"] = {'bb': 1.233457, 'cc': 1.233457, 'c': 0.958385, 'l': 0.888112}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_19"] = {'bb': 1.204549, 'cc': 1.204549, 'c': 0.935924, 'l': 0.867297}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_19"] = {'bb': 1.545377, 'cc': 1.545377, 'c': 1.000000, 'l': 0.875437}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_19"] = {'bb': 1.485813, 'cc': 1.485813, 'c': 0.961457, 'l': 0.841695}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_19"] = {'bb': 1.432689, 'cc': 1.432689, 'c': 0.927081, 'l': 0.811601}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_19"] = {'bb': 1.366967, 'cc': 1.366967, 'c': 0.884553, 'l': 0.774370}
# NNPDF30_nnlo_as_0118_20 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_20"] = {'bb': 1.249369, 'cc': 1.249369, 'c': 1.000000, 'l': 0.935981}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_20"] = {'bb': 1.226086, 'cc': 1.226086, 'c': 0.981364, 'l': 0.918538}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_20"] = {'bb': 1.203527, 'cc': 1.203527, 'c': 0.963308, 'l': 0.901638}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_20"] = {'bb': 1.179066, 'cc': 1.179066, 'c': 0.943730, 'l': 0.883313}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_20"] = {'bb': 1.259653, 'cc': 1.259653, 'c': 1.000000, 'l': 0.941413}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_20"] = {'bb': 1.234634, 'cc': 1.234634, 'c': 0.980138, 'l': 0.922715}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_20"] = {'bb': 1.212480, 'cc': 1.212480, 'c': 0.962551, 'l': 0.906158}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_20"] = {'bb': 1.184684, 'cc': 1.184684, 'c': 0.940485, 'l': 0.885384}
# NNPDF30_nnlo_as_0118_21 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_21"] = {'bb': 1.354002, 'cc': 1.354002, 'c': 1.000000, 'l': 0.909467}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_21"] = {'bb': 1.319125, 'cc': 1.319125, 'c': 0.974241, 'l': 0.886040}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_21"] = {'bb': 1.285500, 'cc': 1.285500, 'c': 0.949408, 'l': 0.863455}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_21"] = {'bb': 1.248812, 'cc': 1.248812, 'c': 0.922312, 'l': 0.838812}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_21"] = {'bb': 1.528072, 'cc': 1.528072, 'c': 1.000000, 'l': 0.879443}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_21"] = {'bb': 1.470327, 'cc': 1.470327, 'c': 0.962210, 'l': 0.846209}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_21"] = {'bb': 1.418768, 'cc': 1.418768, 'c': 0.928469, 'l': 0.816536}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_21"] = {'bb': 1.355841, 'cc': 1.355841, 'c': 0.887288, 'l': 0.780319}
# NNPDF30_nnlo_as_0118_22 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_22"] = {'bb': 1.293549, 'cc': 1.293549, 'c': 1.000000, 'l': 0.925060}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_22"] = {'bb': 1.265354, 'cc': 1.265354, 'c': 0.978204, 'l': 0.904897}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_22"] = {'bb': 1.238282, 'cc': 1.238282, 'c': 0.957275, 'l': 0.885537}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_22"] = {'bb': 1.208827, 'cc': 1.208827, 'c': 0.934504, 'l': 0.864473}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_22"] = {'bb': 1.495120, 'cc': 1.495120, 'c': 1.000000, 'l': 0.887264}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_22"] = {'bb': 1.441803, 'cc': 1.441803, 'c': 0.964339, 'l': 0.855624}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_22"] = {'bb': 1.394098, 'cc': 1.394098, 'c': 0.932432, 'l': 0.827314}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_22"] = {'bb': 1.335743, 'cc': 1.335743, 'c': 0.893402, 'l': 0.792684}
# NNPDF30_nnlo_as_0118_23 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_23"] = {'bb': 1.306641, 'cc': 1.306641, 'c': 1.000000, 'l': 0.921427}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_23"] = {'bb': 1.276908, 'cc': 1.276908, 'c': 0.977245, 'l': 0.900460}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_23"] = {'bb': 1.248320, 'cc': 1.248320, 'c': 0.955366, 'l': 0.880300}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_23"] = {'bb': 1.217322, 'cc': 1.217322, 'c': 0.931642, 'l': 0.858441}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_23"] = {'bb': 1.559170, 'cc': 1.559170, 'c': 1.000000, 'l': 0.872681}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_23"] = {'bb': 1.496970, 'cc': 1.496970, 'c': 0.960107, 'l': 0.837868}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_23"] = {'bb': 1.441691, 'cc': 1.441691, 'c': 0.924653, 'l': 0.806927}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_23"] = {'bb': 1.374492, 'cc': 1.374492, 'c': 0.881554, 'l': 0.769315}
# NNPDF30_nnlo_as_0118_24 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_24"] = {'bb': 1.242989, 'cc': 1.242989, 'c': 1.000000, 'l': 0.937790}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_24"] = {'bb': 1.220406, 'cc': 1.220406, 'c': 0.981832, 'l': 0.920753}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_24"] = {'bb': 1.198558, 'cc': 1.198558, 'c': 0.964255, 'l': 0.904269}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_24"] = {'bb': 1.174718, 'cc': 1.174718, 'c': 0.945075, 'l': 0.886283}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_24"] = {'bb': 1.398961, 'cc': 1.398961, 'c': 1.000000, 'l': 0.909172}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_24"] = {'bb': 1.358204, 'cc': 1.358204, 'c': 0.970866, 'l': 0.882684}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_24"] = {'bb': 1.321438, 'cc': 1.321438, 'c': 0.944585, 'l': 0.858790}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_24"] = {'bb': 1.275917, 'cc': 1.275917, 'c': 0.912046, 'l': 0.829207}
# NNPDF30_nnlo_as_0118_25 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_25"] = {'bb': 1.319904, 'cc': 1.319904, 'c': 1.000000, 'l': 0.918077}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_25"] = {'bb': 1.288723, 'cc': 1.288723, 'c': 0.976376, 'l': 0.896388}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_25"] = {'bb': 1.258647, 'cc': 1.258647, 'c': 0.953590, 'l': 0.875468}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_25"] = {'bb': 1.226237, 'cc': 1.226237, 'c': 0.929035, 'l': 0.852925}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_25"] = {'bb': 1.583493, 'cc': 1.583493, 'c': 1.000000, 'l': 0.866683}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_25"] = {'bb': 1.517874, 'cc': 1.517874, 'c': 0.958561, 'l': 0.830768}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_25"] = {'bb': 1.459314, 'cc': 1.459314, 'c': 0.921579, 'l': 0.798716}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_25"] = {'bb': 1.388618, 'cc': 1.388618, 'c': 0.876933, 'l': 0.760023}
# NNPDF30_nnlo_as_0118_26 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_26"] = {'bb': 1.222212, 'cc': 1.222212, 'c': 1.000000, 'l': 0.943108}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_26"] = {'bb': 1.202070, 'cc': 1.202070, 'c': 0.983520, 'l': 0.927566}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_26"] = {'bb': 1.182349, 'cc': 1.182349, 'c': 0.967384, 'l': 0.912348}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_26"] = {'bb': 1.160602, 'cc': 1.160602, 'c': 0.949592, 'l': 0.895568}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_26"] = {'bb': 1.553248, 'cc': 1.553248, 'c': 1.000000, 'l': 0.872772}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_26"] = {'bb': 1.493069, 'cc': 1.493069, 'c': 0.961256, 'l': 0.838957}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_26"] = {'bb': 1.438108, 'cc': 1.438108, 'c': 0.925871, 'l': 0.808074}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_26"] = {'bb': 1.371302, 'cc': 1.371302, 'c': 0.882861, 'l': 0.770536}
# NNPDF30_nnlo_as_0118_27 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_27"] = {'bb': 1.275940, 'cc': 1.275940, 'c': 1.000000, 'l': 0.929213}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_27"] = {'bb': 1.249819, 'cc': 1.249819, 'c': 0.979528, 'l': 0.910190}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_27"] = {'bb': 1.224559, 'cc': 1.224559, 'c': 0.959731, 'l': 0.891795}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_27"] = {'bb': 1.196968, 'cc': 1.196968, 'c': 0.938107, 'l': 0.871701}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_27"] = {'bb': 1.540034, 'cc': 1.540034, 'c': 1.000000, 'l': 0.876411}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_27"] = {'bb': 1.480869, 'cc': 1.480869, 'c': 0.961582, 'l': 0.842740}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_27"] = {'bb': 1.427739, 'cc': 1.427739, 'c': 0.927082, 'l': 0.812505}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_27"] = {'bb': 1.363164, 'cc': 1.363164, 'c': 0.885152, 'l': 0.775757}
# NNPDF30_nnlo_as_0118_28 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_28"] = {'bb': 1.279110, 'cc': 1.279110, 'c': 1.000000, 'l': 0.928171}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_28"] = {'bb': 1.252495, 'cc': 1.252495, 'c': 0.979193, 'l': 0.908858}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_28"] = {'bb': 1.226915, 'cc': 1.226915, 'c': 0.959195, 'l': 0.890297}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_28"] = {'bb': 1.198973, 'cc': 1.198973, 'c': 0.937350, 'l': 0.870021}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_28"] = {'bb': 1.397760, 'cc': 1.397760, 'c': 1.000000, 'l': 0.908818}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_28"] = {'bb': 1.357132, 'cc': 1.357132, 'c': 0.970933, 'l': 0.882402}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_28"] = {'bb': 1.320505, 'cc': 1.320505, 'c': 0.944729, 'l': 0.858587}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_28"] = {'bb': 1.275301, 'cc': 1.275301, 'c': 0.912389, 'l': 0.829196}
# NNPDF30_nnlo_as_0118_29 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_29"] = {'bb': 1.199242, 'cc': 1.199242, 'c': 1.000000, 'l': 0.949094}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_29"] = {'bb': 1.181576, 'cc': 1.181576, 'c': 0.985269, 'l': 0.935113}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_29"] = {'bb': 1.164178, 'cc': 1.164178, 'c': 0.970762, 'l': 0.921345}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_29"] = {'bb': 1.144821, 'cc': 1.144821, 'c': 0.954621, 'l': 0.906025}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_29"] = {'bb': 1.552622, 'cc': 1.552622, 'c': 1.000000, 'l': 0.873233}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_29"] = {'bb': 1.492737, 'cc': 1.492737, 'c': 0.961430, 'l': 0.839552}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_29"] = {'bb': 1.438041, 'cc': 1.438041, 'c': 0.926202, 'l': 0.808790}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_29"] = {'bb': 1.371198, 'cc': 1.371198, 'c': 0.883150, 'l': 0.771195}
# NNPDF30_nnlo_as_0118_30 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_30"] = {'bb': 1.204548, 'cc': 1.204548, 'c': 1.000000, 'l': 0.947756}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_30"] = {'bb': 1.186176, 'cc': 1.186176, 'c': 0.984748, 'l': 0.933301}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_30"] = {'bb': 1.168181, 'cc': 1.168181, 'c': 0.969808, 'l': 0.919142}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_30"] = {'bb': 1.148335, 'cc': 1.148335, 'c': 0.953333, 'l': 0.903527}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_30"] = {'bb': 1.367572, 'cc': 1.367572, 'c': 1.000000, 'l': 0.916931}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_30"] = {'bb': 1.330673, 'cc': 1.330673, 'c': 0.973019, 'l': 0.892192}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_30"] = {'bb': 1.297378, 'cc': 1.297378, 'c': 0.948673, 'l': 0.869868}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_30"] = {'bb': 1.255908, 'cc': 1.255908, 'c': 0.918349, 'l': 0.842063}
# NNPDF30_nnlo_as_0118_31 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_31"] = {'bb': 1.286364, 'cc': 1.286364, 'c': 1.000000, 'l': 0.926925}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_31"] = {'bb': 1.258940, 'cc': 1.258940, 'c': 0.978682, 'l': 0.907165}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_31"] = {'bb': 1.232547, 'cc': 1.232547, 'c': 0.958164, 'l': 0.888146}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_31"] = {'bb': 1.204019, 'cc': 1.204019, 'c': 0.935987, 'l': 0.867590}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_31"] = {'bb': 1.460057, 'cc': 1.460057, 'c': 1.000000, 'l': 0.896173}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_31"] = {'bb': 1.411278, 'cc': 1.411278, 'c': 0.966591, 'l': 0.866233}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_31"] = {'bb': 1.367786, 'cc': 1.367786, 'c': 0.936803, 'l': 0.839538}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_31"] = {'bb': 1.314074, 'cc': 1.314074, 'c': 0.900016, 'l': 0.806570}
# NNPDF30_nnlo_as_0118_32 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_32"] = {'bb': 1.290787, 'cc': 1.290787, 'c': 1.000000, 'l': 0.925675}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_32"] = {'bb': 1.263101, 'cc': 1.263101, 'c': 0.978551, 'l': 0.905821}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_32"] = {'bb': 1.236307, 'cc': 1.236307, 'c': 0.957793, 'l': 0.886606}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_32"] = {'bb': 1.207290, 'cc': 1.207290, 'c': 0.935313, 'l': 0.865797}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_32"] = {'bb': 1.598028, 'cc': 1.598028, 'c': 1.000000, 'l': 0.863779}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_32"] = {'bb': 1.530977, 'cc': 1.530977, 'c': 0.958041, 'l': 0.827536}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_32"] = {'bb': 1.470114, 'cc': 1.470114, 'c': 0.919955, 'l': 0.794638}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_32"] = {'bb': 1.396966, 'cc': 1.396966, 'c': 0.874181, 'l': 0.755099}
# NNPDF30_nnlo_as_0118_33 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_33"] = {'bb': 1.272642, 'cc': 1.272642, 'c': 1.000000, 'l': 0.930903}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_33"] = {'bb': 1.246918, 'cc': 1.246918, 'c': 0.979787, 'l': 0.912087}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_33"] = {'bb': 1.222016, 'cc': 1.222016, 'c': 0.960220, 'l': 0.893872}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_33"] = {'bb': 1.194830, 'cc': 1.194830, 'c': 0.938858, 'l': 0.873986}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_33"] = {'bb': 1.425720, 'cc': 1.425720, 'c': 1.000000, 'l': 0.904287}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_33"] = {'bb': 1.381501, 'cc': 1.381501, 'c': 0.968985, 'l': 0.876240}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_33"] = {'bb': 1.341859, 'cc': 1.341859, 'c': 0.941180, 'l': 0.851096}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_33"] = {'bb': 1.291885, 'cc': 1.291885, 'c': 0.906128, 'l': 0.819399}
# NNPDF30_nnlo_as_0118_34 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_34"] = {'bb': 1.281059, 'cc': 1.281059, 'c': 1.000000, 'l': 0.928346}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_34"] = {'bb': 1.254422, 'cc': 1.254422, 'c': 0.979207, 'l': 0.909043}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_34"] = {'bb': 1.228710, 'cc': 1.228710, 'c': 0.959136, 'l': 0.890410}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_34"] = {'bb': 1.200633, 'cc': 1.200633, 'c': 0.937219, 'l': 0.870064}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_34"] = {'bb': 1.370044, 'cc': 1.370044, 'c': 1.000000, 'l': 0.916644}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_34"] = {'bb': 1.332875, 'cc': 1.332875, 'c': 0.972870, 'l': 0.891776}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_34"] = {'bb': 1.299445, 'cc': 1.299445, 'c': 0.948470, 'l': 0.869409}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_34"] = {'bb': 1.257658, 'cc': 1.257658, 'c': 0.917969, 'l': 0.841451}
# NNPDF30_nnlo_as_0118_35 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_35"] = {'bb': 1.281118, 'cc': 1.281118, 'c': 1.000000, 'l': 0.928125}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_35"] = {'bb': 1.254527, 'cc': 1.254527, 'c': 0.979244, 'l': 0.908861}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_35"] = {'bb': 1.228749, 'cc': 1.228749, 'c': 0.959122, 'l': 0.890185}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_35"] = {'bb': 1.200525, 'cc': 1.200525, 'c': 0.937092, 'l': 0.869738}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_35"] = {'bb': 1.633243, 'cc': 1.633243, 'c': 1.000000, 'l': 0.854230}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_35"] = {'bb': 1.561576, 'cc': 1.561576, 'c': 0.956120, 'l': 0.816747}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_35"] = {'bb': 1.495993, 'cc': 1.495993, 'c': 0.915965, 'l': 0.782445}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_35"] = {'bb': 1.418086, 'cc': 1.418086, 'c': 0.868264, 'l': 0.741698}
# NNPDF30_nnlo_as_0118_36 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_36"] = {'bb': 1.206024, 'cc': 1.206024, 'c': 1.000000, 'l': 0.947321}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_36"] = {'bb': 1.187588, 'cc': 1.187588, 'c': 0.984713, 'l': 0.932840}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_36"] = {'bb': 1.169433, 'cc': 1.169433, 'c': 0.969660, 'l': 0.918580}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_36"] = {'bb': 1.149401, 'cc': 1.149401, 'c': 0.953049, 'l': 0.902844}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_36"] = {'bb': 1.642487, 'cc': 1.642487, 'c': 1.000000, 'l': 0.852063}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_36"] = {'bb': 1.570149, 'cc': 1.570149, 'c': 0.955959, 'l': 0.814537}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_36"] = {'bb': 1.503760, 'cc': 1.503760, 'c': 0.915539, 'l': 0.780097}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_36"] = {'bb': 1.423845, 'cc': 1.423845, 'c': 0.866884, 'l': 0.738640}
# NNPDF30_nnlo_as_0118_37 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_37"] = {'bb': 1.361876, 'cc': 1.361876, 'c': 1.000000, 'l': 0.907995}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_37"] = {'bb': 1.325959, 'cc': 1.325959, 'c': 0.973627, 'l': 0.884049}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_37"] = {'bb': 1.291495, 'cc': 1.291495, 'c': 0.948321, 'l': 0.861071}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_37"] = {'bb': 1.254122, 'cc': 1.254122, 'c': 0.920879, 'l': 0.836153}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_37"] = {'bb': 1.775030, 'cc': 1.775030, 'c': 1.000000, 'l': 0.822050}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_37"] = {'bb': 1.681919, 'cc': 1.681919, 'c': 0.947544, 'l': 0.778929}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_37"] = {'bb': 1.597792, 'cc': 1.597792, 'c': 0.900149, 'l': 0.739968}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_37"] = {'bb': 1.498128, 'cc': 1.498128, 'c': 0.844002, 'l': 0.693812}
# NNPDF30_nnlo_as_0118_38 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_38"] = {'bb': 1.217180, 'cc': 1.217180, 'c': 1.000000, 'l': 0.944241}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_38"] = {'bb': 1.197487, 'cc': 1.197487, 'c': 0.983821, 'l': 0.928964}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_38"] = {'bb': 1.178179, 'cc': 1.178179, 'c': 0.967958, 'l': 0.913986}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_38"] = {'bb': 1.156974, 'cc': 1.156974, 'c': 0.950536, 'l': 0.897535}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_38"] = {'bb': 1.517840, 'cc': 1.517840, 'c': 1.000000, 'l': 0.880893}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_38"] = {'bb': 1.462257, 'cc': 1.462257, 'c': 0.963380, 'l': 0.848635}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_38"] = {'bb': 1.411670, 'cc': 1.411670, 'c': 0.930051, 'l': 0.819276}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_38"] = {'bb': 1.350070, 'cc': 1.350070, 'c': 0.889468, 'l': 0.783526}
# NNPDF30_nnlo_as_0118_39 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_39"] = {'bb': 1.310026, 'cc': 1.310026, 'c': 1.000000, 'l': 0.920540}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_39"] = {'bb': 1.280031, 'cc': 1.280031, 'c': 0.977103, 'l': 0.899462}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_39"] = {'bb': 1.251056, 'cc': 1.251056, 'c': 0.954986, 'l': 0.879102}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_39"] = {'bb': 1.219478, 'cc': 1.219478, 'c': 0.930881, 'l': 0.856913}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_39"] = {'bb': 1.572544, 'cc': 1.572544, 'c': 1.000000, 'l': 0.869135}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_39"] = {'bb': 1.508386, 'cc': 1.508386, 'c': 0.959201, 'l': 0.833675}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_39"] = {'bb': 1.451173, 'cc': 1.451173, 'c': 0.922819, 'l': 0.802054}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_39"] = {'bb': 1.381753, 'cc': 1.381753, 'c': 0.878673, 'l': 0.763686}
# NNPDF30_nnlo_as_0118_40 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_40"] = {'bb': 1.235382, 'cc': 1.235382, 'c': 1.000000, 'l': 0.939840}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_40"] = {'bb': 1.213701, 'cc': 1.213701, 'c': 0.982450, 'l': 0.923345}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_40"] = {'bb': 1.192624, 'cc': 1.192624, 'c': 0.965389, 'l': 0.907311}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_40"] = {'bb': 1.169491, 'cc': 1.169491, 'c': 0.946664, 'l': 0.889712}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_40"] = {'bb': 1.411645, 'cc': 1.411645, 'c': 1.000000, 'l': 0.906428}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_40"] = {'bb': 1.369154, 'cc': 1.369154, 'c': 0.969900, 'l': 0.879144}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_40"] = {'bb': 1.331131, 'cc': 1.331131, 'c': 0.942964, 'l': 0.854729}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_40"] = {'bb': 1.284091, 'cc': 1.284091, 'c': 0.909642, 'l': 0.824525}
# NNPDF30_nnlo_as_0118_41 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_41"] = {'bb': 1.235857, 'cc': 1.235857, 'c': 1.000000, 'l': 0.939591}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_41"] = {'bb': 1.214146, 'cc': 1.214146, 'c': 0.982432, 'l': 0.923085}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_41"] = {'bb': 1.193032, 'cc': 1.193032, 'c': 0.965348, 'l': 0.907033}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_41"] = {'bb': 1.169769, 'cc': 1.169769, 'c': 0.946524, 'l': 0.889346}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_41"] = {'bb': 1.466006, 'cc': 1.466006, 'c': 1.000000, 'l': 0.893519}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_41"] = {'bb': 1.416913, 'cc': 1.416913, 'c': 0.966512, 'l': 0.863597}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_41"] = {'bb': 1.372335, 'cc': 1.372335, 'c': 0.936104, 'l': 0.836427}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_41"] = {'bb': 1.317906, 'cc': 1.317906, 'c': 0.898977, 'l': 0.803253}
# NNPDF30_nnlo_as_0118_42 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_42"] = {'bb': 1.312490, 'cc': 1.312490, 'c': 1.000000, 'l': 0.919755}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_42"] = {'bb': 1.281899, 'cc': 1.281899, 'c': 0.976692, 'l': 0.898317}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_42"] = {'bb': 1.252059, 'cc': 1.252059, 'c': 0.953957, 'l': 0.877406}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_42"] = {'bb': 1.220860, 'cc': 1.220860, 'c': 0.930186, 'l': 0.855542}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_42"] = {'bb': 1.513515, 'cc': 1.513515, 'c': 1.000000, 'l': 0.882830}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_42"] = {'bb': 1.457454, 'cc': 1.457454, 'c': 0.962960, 'l': 0.850130}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_42"] = {'bb': 1.407609, 'cc': 1.407609, 'c': 0.930027, 'l': 0.821055}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_42"] = {'bb': 1.346943, 'cc': 1.346943, 'c': 0.889944, 'l': 0.785669}
# NNPDF30_nnlo_as_0118_43 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_43"] = {'bb': 1.230022, 'cc': 1.230022, 'c': 1.000000, 'l': 0.941387}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_43"] = {'bb': 1.209215, 'cc': 1.209215, 'c': 0.983084, 'l': 0.925463}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_43"] = {'bb': 1.188728, 'cc': 1.188728, 'c': 0.966428, 'l': 0.909783}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_43"] = {'bb': 1.166019, 'cc': 1.166019, 'c': 0.947966, 'l': 0.892403}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_43"] = {'bb': 1.680183, 'cc': 1.680183, 'c': 1.000000, 'l': 0.842667}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_43"] = {'bb': 1.602438, 'cc': 1.602438, 'c': 0.953728, 'l': 0.803676}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_43"] = {'bb': 1.531385, 'cc': 1.531385, 'c': 0.911439, 'l': 0.768040}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_43"] = {'bb': 1.445191, 'cc': 1.445191, 'c': 0.860139, 'l': 0.724811}
# NNPDF30_nnlo_as_0118_44 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_44"] = {'bb': 1.249863, 'cc': 1.249863, 'c': 1.000000, 'l': 0.935920}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_44"] = {'bb': 1.226702, 'cc': 1.226702, 'c': 0.981470, 'l': 0.918577}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_44"] = {'bb': 1.204190, 'cc': 1.204190, 'c': 0.963458, 'l': 0.901719}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_44"] = {'bb': 1.179553, 'cc': 1.179553, 'c': 0.943746, 'l': 0.883271}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_44"] = {'bb': 1.501121, 'cc': 1.501121, 'c': 1.000000, 'l': 0.885282}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_44"] = {'bb': 1.447678, 'cc': 1.447678, 'c': 0.964398, 'l': 0.853764}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_44"] = {'bb': 1.399155, 'cc': 1.399155, 'c': 0.932074, 'l': 0.825148}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_44"] = {'bb': 1.339633, 'cc': 1.339633, 'c': 0.892422, 'l': 0.790045}
# NNPDF30_nnlo_as_0118_45 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_45"] = {'bb': 1.241899, 'cc': 1.241899, 'c': 1.000000, 'l': 0.939036}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_45"] = {'bb': 1.219705, 'cc': 1.219705, 'c': 0.982128, 'l': 0.922254}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_45"] = {'bb': 1.197835, 'cc': 1.197835, 'c': 0.964518, 'l': 0.905717}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_45"] = {'bb': 1.173902, 'cc': 1.173902, 'c': 0.945247, 'l': 0.887621}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_45"] = {'bb': 1.654555, 'cc': 1.654555, 'c': 1.000000, 'l': 0.848800}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_45"] = {'bb': 1.580321, 'cc': 1.580321, 'c': 0.955133, 'l': 0.810717}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_45"] = {'bb': 1.512335, 'cc': 1.512335, 'c': 0.914043, 'l': 0.775840}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_45"] = {'bb': 1.430398, 'cc': 1.430398, 'c': 0.864521, 'l': 0.733806}
# NNPDF30_nnlo_as_0118_46 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_46"] = {'bb': 1.280701, 'cc': 1.280701, 'c': 1.000000, 'l': 0.928033}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_46"] = {'bb': 1.253949, 'cc': 1.253949, 'c': 0.979112, 'l': 0.908648}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_46"] = {'bb': 1.228148, 'cc': 1.228148, 'c': 0.958966, 'l': 0.889952}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_46"] = {'bb': 1.200113, 'cc': 1.200113, 'c': 0.937076, 'l': 0.869637}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_46"] = {'bb': 1.398022, 'cc': 1.398022, 'c': 1.000000, 'l': 0.909704}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_46"] = {'bb': 1.357182, 'cc': 1.357182, 'c': 0.970787, 'l': 0.883129}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_46"] = {'bb': 1.320563, 'cc': 1.320563, 'c': 0.944594, 'l': 0.859301}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_46"] = {'bb': 1.275318, 'cc': 1.275318, 'c': 0.912231, 'l': 0.829860}
# NNPDF30_nnlo_as_0118_47 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_47"] = {'bb': 1.285988, 'cc': 1.285988, 'c': 1.000000, 'l': 0.926102}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_47"] = {'bb': 1.258809, 'cc': 1.258809, 'c': 0.978865, 'l': 0.906529}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_47"] = {'bb': 1.232470, 'cc': 1.232470, 'c': 0.958384, 'l': 0.887561}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_47"] = {'bb': 1.203903, 'cc': 1.203903, 'c': 0.936169, 'l': 0.866989}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_47"] = {'bb': 1.481113, 'cc': 1.481113, 'c': 1.000000, 'l': 0.890093}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_47"] = {'bb': 1.429509, 'cc': 1.429509, 'c': 0.965158, 'l': 0.859081}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_47"] = {'bb': 1.383499, 'cc': 1.383499, 'c': 0.934094, 'l': 0.831430}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_47"] = {'bb': 1.327131, 'cc': 1.327131, 'c': 0.896036, 'l': 0.797555}
# NNPDF30_nnlo_as_0118_48 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_48"] = {'bb': 1.215899, 'cc': 1.215899, 'c': 1.000000, 'l': 0.944856}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_48"] = {'bb': 1.196368, 'cc': 1.196368, 'c': 0.983938, 'l': 0.929680}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_48"] = {'bb': 1.177235, 'cc': 1.177235, 'c': 0.968202, 'l': 0.914811}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_48"] = {'bb': 1.156171, 'cc': 1.156171, 'c': 0.950878, 'l': 0.898443}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_48"] = {'bb': 1.432485, 'cc': 1.432485, 'c': 1.000000, 'l': 0.901597}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_48"] = {'bb': 1.387900, 'cc': 1.387900, 'c': 0.968876, 'l': 0.873536}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_48"] = {'bb': 1.343676, 'cc': 1.343676, 'c': 0.938004, 'l': 0.845702}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_48"] = {'bb': 1.297552, 'cc': 1.297552, 'c': 0.905805, 'l': 0.816671}
# NNPDF30_nnlo_as_0118_49 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_49"] = {'bb': -0.049512, 'cc': -0.049512, 'c': 1.000000, 'l': 0.191312}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_49"] = {'bb': 0.061857, 'cc': 0.061857, 'c': -1.249345, 'l': -0.239014}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_49"] = {'bb': 0.106238, 'cc': 0.106238, 'c': -2.145714, 'l': -0.410500}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_49"] = {'bb': 0.057806, 'cc': 0.057806, 'c': -1.167509, 'l': -0.223358}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_49"] = {'bb': 1.414042, 'cc': 1.414042, 'c': 1.000000, 'l': 0.906668}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_49"] = {'bb': 1.371208, 'cc': 1.371208, 'c': 0.969708, 'l': 0.879204}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_49"] = {'bb': 1.333027, 'cc': 1.333027, 'c': 0.942707, 'l': 0.854722}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_49"] = {'bb': 1.285692, 'cc': 1.285692, 'c': 0.909232, 'l': 0.824372}
# NNPDF30_nnlo_as_0118_50 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_50"] = {'bb': 1.317572, 'cc': 1.317572, 'c': 1.000000, 'l': 0.918735}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_50"] = {'bb': 1.286602, 'cc': 1.286602, 'c': 0.976495, 'l': 0.897140}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_50"] = {'bb': 1.256792, 'cc': 1.256792, 'c': 0.953870, 'l': 0.876354}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_50"] = {'bb': 1.224613, 'cc': 1.224613, 'c': 0.929447, 'l': 0.853915}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_50"] = {'bb': 1.426923, 'cc': 1.426923, 'c': 1.000000, 'l': 0.903555}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_50"] = {'bb': 1.382049, 'cc': 1.382049, 'c': 0.968552, 'l': 0.875139}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_50"] = {'bb': 1.342161, 'cc': 1.342161, 'c': 0.940598, 'l': 0.849882}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_50"] = {'bb': 1.293168, 'cc': 1.293168, 'c': 0.906263, 'l': 0.818858}
# NNPDF30_nnlo_as_0118_51 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_51"] = {'bb': 1.204346, 'cc': 1.204346, 'c': 1.000000, 'l': 0.947750}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_51"] = {'bb': 1.185989, 'cc': 1.185989, 'c': 0.984758, 'l': 0.933304}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_51"] = {'bb': 1.168061, 'cc': 1.168061, 'c': 0.969872, 'l': 0.919196}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_51"] = {'bb': 1.148147, 'cc': 1.148147, 'c': 0.953336, 'l': 0.903525}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_51"] = {'bb': 1.314767, 'cc': 1.314767, 'c': 1.000000, 'l': 0.928798}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_51"] = {'bb': 1.284157, 'cc': 1.284157, 'c': 0.976719, 'l': 0.907174}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_51"] = {'bb': 1.256558, 'cc': 1.256558, 'c': 0.955727, 'l': 0.887677}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_51"] = {'bb': 1.221817, 'cc': 1.221817, 'c': 0.929303, 'l': 0.863135}
# NNPDF30_nnlo_as_0118_52 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_52"] = {'bb': 1.254686, 'cc': 1.254686, 'c': 1.000000, 'l': 0.934751}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_52"] = {'bb': 1.231107, 'cc': 1.231107, 'c': 0.981207, 'l': 0.917185}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_52"] = {'bb': 1.208073, 'cc': 1.208073, 'c': 0.962848, 'l': 0.900023}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_52"] = {'bb': 1.182906, 'cc': 1.182906, 'c': 0.942790, 'l': 0.881274}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_52"] = {'bb': 1.487011, 'cc': 1.487011, 'c': 1.000000, 'l': 0.889041}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_52"] = {'bb': 1.435229, 'cc': 1.435229, 'c': 0.965177, 'l': 0.858083}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_52"] = {'bb': 1.388668, 'cc': 1.388668, 'c': 0.933865, 'l': 0.830245}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_52"] = {'bb': 1.331246, 'cc': 1.331246, 'c': 0.895250, 'l': 0.795914}
# NNPDF30_nnlo_as_0118_53 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_53"] = {'bb': 1.167137, 'cc': 1.167137, 'c': 1.000000, 'l': 0.957283}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_53"] = {'bb': 1.152675, 'cc': 1.152675, 'c': 0.987609, 'l': 0.945421}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_53"] = {'bb': 1.138338, 'cc': 1.138338, 'c': 0.975325, 'l': 0.933662}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_53"] = {'bb': 1.122375, 'cc': 1.122375, 'c': 0.961648, 'l': 0.920569}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_53"] = {'bb': 1.608208, 'cc': 1.608208, 'c': 1.000000, 'l': 0.859664}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_53"] = {'bb': 1.540889, 'cc': 1.540889, 'c': 0.958141, 'l': 0.823679}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_53"] = {'bb': 1.479031, 'cc': 1.479031, 'c': 0.919677, 'l': 0.790613}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_53"] = {'bb': 1.404007, 'cc': 1.404007, 'c': 0.873026, 'l': 0.750509}
# NNPDF30_nnlo_as_0118_54 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_54"] = {'bb': 1.272577, 'cc': 1.272577, 'c': 1.000000, 'l': 0.930767}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_54"] = {'bb': 1.246668, 'cc': 1.246668, 'c': 0.979641, 'l': 0.911817}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_54"] = {'bb': 1.221599, 'cc': 1.221599, 'c': 0.959941, 'l': 0.893481}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_54"] = {'bb': 1.193192, 'cc': 1.193192, 'c': 0.937619, 'l': 0.872704}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_54"] = {'bb': 1.446430, 'cc': 1.446430, 'c': 1.000000, 'l': 0.897594}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_54"] = {'bb': 1.399016, 'cc': 1.399016, 'c': 0.967220, 'l': 0.868171}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_54"] = {'bb': 1.356225, 'cc': 1.356225, 'c': 0.937636, 'l': 0.841617}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_54"] = {'bb': 1.305915, 'cc': 1.305915, 'c': 0.902854, 'l': 0.810396}
# NNPDF30_nnlo_as_0118_55 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_55"] = {'bb': 1.288635, 'cc': 1.288635, 'c': 1.000000, 'l': 0.926135}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_55"] = {'bb': 1.261059, 'cc': 1.261059, 'c': 0.978601, 'l': 0.906316}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_55"] = {'bb': 1.234544, 'cc': 1.234544, 'c': 0.958024, 'l': 0.887260}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_55"] = {'bb': 1.205560, 'cc': 1.205560, 'c': 0.935533, 'l': 0.866429}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_55"] = {'bb': 1.482301, 'cc': 1.482301, 'c': 1.000000, 'l': 0.890248}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_55"] = {'bb': 1.430710, 'cc': 1.430710, 'c': 0.965196, 'l': 0.859263}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_55"] = {'bb': 1.384491, 'cc': 1.384491, 'c': 0.934015, 'l': 0.831505}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_55"] = {'bb': 1.327706, 'cc': 1.327706, 'c': 0.895706, 'l': 0.797400}
# NNPDF30_nnlo_as_0118_56 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_56"] = {'bb': 1.490355, 'cc': 1.490355, 'c': 1.000000, 'l': 0.882529}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_56"] = {'bb': 1.437358, 'cc': 1.437358, 'c': 0.964440, 'l': 0.851146}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_56"] = {'bb': 1.385347, 'cc': 1.385347, 'c': 0.929542, 'l': 0.820348}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_56"] = {'bb': 1.331180, 'cc': 1.331180, 'c': 0.893197, 'l': 0.788272}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_56"] = {'bb': 1.421363, 'cc': 1.421363, 'c': 1.000000, 'l': 0.904198}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_56"] = {'bb': 1.378902, 'cc': 1.378902, 'c': 0.970127, 'l': 0.877186}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_56"] = {'bb': 1.339621, 'cc': 1.339621, 'c': 0.942491, 'l': 0.852198}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_56"] = {'bb': 1.290869, 'cc': 1.290869, 'c': 0.908191, 'l': 0.821184}
# NNPDF30_nnlo_as_0118_57 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_57"] = {'bb': 1.279757, 'cc': 1.279757, 'c': 1.000000, 'l': 0.928273}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_57"] = {'bb': 1.253209, 'cc': 1.253209, 'c': 0.979256, 'l': 0.909017}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_57"] = {'bb': 1.227257, 'cc': 1.227257, 'c': 0.958977, 'l': 0.890193}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_57"] = {'bb': 1.199636, 'cc': 1.199636, 'c': 0.937394, 'l': 0.870158}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_57"] = {'bb': 1.606145, 'cc': 1.606145, 'c': 1.000000, 'l': 0.861181}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_57"] = {'bb': 1.537732, 'cc': 1.537732, 'c': 0.957405, 'l': 0.824499}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_57"] = {'bb': 1.476390, 'cc': 1.476390, 'c': 0.919214, 'l': 0.791609}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_57"] = {'bb': 1.402026, 'cc': 1.402026, 'c': 0.872914, 'l': 0.751737}
# NNPDF30_nnlo_as_0118_58 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_58"] = {'bb': 1.281992, 'cc': 1.281992, 'c': 1.000000, 'l': 0.926390}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_58"] = {'bb': 1.255097, 'cc': 1.255097, 'c': 0.979021, 'l': 0.906955}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_58"] = {'bb': 1.229452, 'cc': 1.229452, 'c': 0.959017, 'l': 0.888423}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_58"] = {'bb': 1.201604, 'cc': 1.201604, 'c': 0.937294, 'l': 0.868300}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_58"] = {'bb': 1.545787, 'cc': 1.545787, 'c': 1.000000, 'l': 0.875280}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_58"] = {'bb': 1.485166, 'cc': 1.485166, 'c': 0.960783, 'l': 0.840954}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_58"] = {'bb': 1.431261, 'cc': 1.431261, 'c': 0.925911, 'l': 0.810431}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_58"] = {'bb': 1.365931, 'cc': 1.365931, 'c': 0.883648, 'l': 0.773439}
# NNPDF30_nnlo_as_0118_59 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_59"] = {'bb': 1.218807, 'cc': 1.218807, 'c': 1.000000, 'l': 0.944135}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_59"] = {'bb': 1.198926, 'cc': 1.198926, 'c': 0.983688, 'l': 0.928734}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_59"] = {'bb': 1.179569, 'cc': 1.179569, 'c': 0.967806, 'l': 0.913740}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_59"] = {'bb': 1.158244, 'cc': 1.158244, 'c': 0.950309, 'l': 0.897220}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_59"] = {'bb': 1.411779, 'cc': 1.411779, 'c': 1.000000, 'l': 0.906390}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_59"] = {'bb': 1.369630, 'cc': 1.369630, 'c': 0.970145, 'l': 0.879330}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_59"] = {'bb': 1.331487, 'cc': 1.331487, 'c': 0.943127, 'l': 0.854841}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_59"] = {'bb': 1.284342, 'cc': 1.284342, 'c': 0.909733, 'l': 0.824573}
# NNPDF30_nnlo_as_0118_60 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_60"] = {'bb': 1.292997, 'cc': 1.292997, 'c': 1.000000, 'l': 0.924977}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_60"] = {'bb': 1.265035, 'cc': 1.265035, 'c': 0.978374, 'l': 0.904973}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_60"] = {'bb': 1.237944, 'cc': 1.237944, 'c': 0.957422, 'l': 0.885593}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_60"] = {'bb': 1.208389, 'cc': 1.208389, 'c': 0.934564, 'l': 0.864450}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_60"] = {'bb': 1.915401, 'cc': 1.915401, 'c': 1.000000, 'l': 0.831576}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_60"] = {'bb': 1.792710, 'cc': 1.792710, 'c': 0.935945, 'l': 0.778309}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_60"] = {'bb': 1.677357, 'cc': 1.677357, 'c': 0.875721, 'l': 0.728228}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_60"] = {'bb': 1.550833, 'cc': 1.550833, 'c': 0.809665, 'l': 0.673298}
# NNPDF30_nnlo_as_0118_61 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_61"] = {'bb': 1.321089, 'cc': 1.321089, 'c': 1.000000, 'l': 0.918105}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_61"] = {'bb': 1.290061, 'cc': 1.290061, 'c': 0.976513, 'l': 0.896542}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_61"] = {'bb': 1.260158, 'cc': 1.260158, 'c': 0.953878, 'l': 0.875760}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_61"] = {'bb': 1.227414, 'cc': 1.227414, 'c': 0.929093, 'l': 0.853005}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_61"] = {'bb': 1.699941, 'cc': 1.699941, 'c': 1.000000, 'l': 0.839166}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_61"] = {'bb': 1.618386, 'cc': 1.618386, 'c': 0.952025, 'l': 0.798907}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_61"] = {'bb': 1.544778, 'cc': 1.544778, 'c': 0.908725, 'l': 0.762571}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_61"] = {'bb': 1.456565, 'cc': 1.456565, 'c': 0.856833, 'l': 0.719025}
# NNPDF30_nnlo_as_0118_62 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_62"] = {'bb': 1.247974, 'cc': 1.247974, 'c': 1.000000, 'l': 0.936526}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_62"] = {'bb': 1.225189, 'cc': 1.225189, 'c': 0.981742, 'l': 0.919427}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_62"] = {'bb': 1.202949, 'cc': 1.202949, 'c': 0.963921, 'l': 0.902738}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_62"] = {'bb': 1.178449, 'cc': 1.178449, 'c': 0.944290, 'l': 0.884352}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_62"] = {'bb': 1.609104, 'cc': 1.609104, 'c': 1.000000, 'l': 0.862083}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_62"] = {'bb': 1.544552, 'cc': 1.544552, 'c': 0.959883, 'l': 0.827499}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_62"] = {'bb': 1.489952, 'cc': 1.489952, 'c': 0.925951, 'l': 0.798247}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_62"] = {'bb': 1.421589, 'cc': 1.421589, 'c': 0.883466, 'l': 0.761621}
# NNPDF30_nnlo_as_0118_63 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_63"] = {'bb': 1.309414, 'cc': 1.309414, 'c': 1.000000, 'l': 0.921447}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_63"] = {'bb': 1.279443, 'cc': 1.279443, 'c': 0.977111, 'l': 0.900357}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_63"] = {'bb': 1.250640, 'cc': 1.250640, 'c': 0.955114, 'l': 0.880087}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_63"] = {'bb': 1.219255, 'cc': 1.219255, 'c': 0.931145, 'l': 0.858001}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_63"] = {'bb': 1.375957, 'cc': 1.375957, 'c': 1.000000, 'l': 0.915560}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_63"] = {'bb': 1.337927, 'cc': 1.337927, 'c': 0.972361, 'l': 0.890255}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_63"] = {'bb': 1.303847, 'cc': 1.303847, 'c': 0.947593, 'l': 0.867579}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_63"] = {'bb': 1.261306, 'cc': 1.261306, 'c': 0.916676, 'l': 0.839272}
# NNPDF30_nnlo_as_0118_64 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_64"] = {'bb': 1.235847, 'cc': 1.235847, 'c': 1.000000, 'l': 0.939423}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_64"] = {'bb': 1.214183, 'cc': 1.214183, 'c': 0.982470, 'l': 0.922955}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_64"] = {'bb': 1.193026, 'cc': 1.193026, 'c': 0.965350, 'l': 0.906872}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_64"] = {'bb': 1.169950, 'cc': 1.169950, 'c': 0.946679, 'l': 0.889332}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_64"] = {'bb': 1.385142, 'cc': 1.385142, 'c': 1.000000, 'l': 0.912742}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_64"] = {'bb': 1.345979, 'cc': 1.345979, 'c': 0.971726, 'l': 0.886936}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_64"] = {'bb': 1.310968, 'cc': 1.310968, 'c': 0.946450, 'l': 0.863865}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_64"] = {'bb': 1.267283, 'cc': 1.267283, 'c': 0.914912, 'l': 0.835079}
# NNPDF30_nnlo_as_0118_65 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_65"] = {'bb': 1.261435, 'cc': 1.261435, 'c': 1.000000, 'l': 0.933300}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_65"] = {'bb': 1.237077, 'cc': 1.237077, 'c': 0.980691, 'l': 0.915278}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_65"] = {'bb': 1.213362, 'cc': 1.213362, 'c': 0.961891, 'l': 0.897732}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_65"] = {'bb': 1.187456, 'cc': 1.187456, 'c': 0.941353, 'l': 0.878565}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_65"] = {'bb': 1.483877, 'cc': 1.483877, 'c': 1.000000, 'l': 0.890244}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_65"] = {'bb': 1.431789, 'cc': 1.431789, 'c': 0.964897, 'l': 0.858994}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_65"] = {'bb': 1.386081, 'cc': 1.386081, 'c': 0.934094, 'l': 0.831572}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_65"] = {'bb': 1.328732, 'cc': 1.328732, 'c': 0.895446, 'l': 0.797166}
# NNPDF30_nnlo_as_0118_66 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_66"] = {'bb': 1.230989, 'cc': 1.230989, 'c': 1.000000, 'l': 0.940762}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_66"] = {'bb': 1.209862, 'cc': 1.209862, 'c': 0.982837, 'l': 0.924616}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_66"] = {'bb': 1.189217, 'cc': 1.189217, 'c': 0.966066, 'l': 0.908838}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_66"] = {'bb': 1.166574, 'cc': 1.166574, 'c': 0.947671, 'l': 0.891533}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_66"] = {'bb': 1.616486, 'cc': 1.616486, 'c': 1.000000, 'l': 0.857748}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_66"] = {'bb': 1.547375, 'cc': 1.547375, 'c': 0.957247, 'l': 0.821077}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_66"] = {'bb': 1.484167, 'cc': 1.484167, 'c': 0.918144, 'l': 0.787537}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_66"] = {'bb': 1.408335, 'cc': 1.408335, 'c': 0.871233, 'l': 0.747298}
# NNPDF30_nnlo_as_0118_67 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_67"] = {'bb': 1.354530, 'cc': 1.354530, 'c': 1.000000, 'l': 0.909596}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_67"] = {'bb': 1.319455, 'cc': 1.319455, 'c': 0.974105, 'l': 0.886042}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_67"] = {'bb': 1.285579, 'cc': 1.285579, 'c': 0.949096, 'l': 0.863294}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_67"] = {'bb': 1.248679, 'cc': 1.248679, 'c': 0.921854, 'l': 0.838515}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_67"] = {'bb': 1.513106, 'cc': 1.513106, 'c': 1.000000, 'l': 0.883570}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_67"] = {'bb': 1.456690, 'cc': 1.456690, 'c': 0.962715, 'l': 0.850626}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_67"] = {'bb': 1.406985, 'cc': 1.406985, 'c': 0.929865, 'l': 0.821601}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_67"] = {'bb': 1.347727, 'cc': 1.347727, 'c': 0.890702, 'l': 0.786998}
# NNPDF30_nnlo_as_0118_68 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_68"] = {'bb': 1.364845, 'cc': 1.364845, 'c': 1.000000, 'l': 0.907043}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_68"] = {'bb': 1.328290, 'cc': 1.328290, 'c': 0.973217, 'l': 0.882749}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_68"] = {'bb': 1.293282, 'cc': 1.293282, 'c': 0.947566, 'l': 0.859483}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_68"] = {'bb': 1.255684, 'cc': 1.255684, 'c': 0.920019, 'l': 0.834497}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_68"] = {'bb': 1.566722, 'cc': 1.566722, 'c': 1.000000, 'l': 0.871173}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_68"] = {'bb': 1.503211, 'cc': 1.503211, 'c': 0.959463, 'l': 0.835858}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_68"] = {'bb': 1.446909, 'cc': 1.446909, 'c': 0.923527, 'l': 0.804551}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_68"] = {'bb': 1.378604, 'cc': 1.378604, 'c': 0.879929, 'l': 0.766570}
# NNPDF30_nnlo_as_0118_69 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_69"] = {'bb': 1.191990, 'cc': 1.191990, 'c': 1.000000, 'l': 0.950797}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_69"] = {'bb': 1.174960, 'cc': 1.174960, 'c': 0.985713, 'l': 0.937213}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_69"] = {'bb': 1.158254, 'cc': 1.158254, 'c': 0.971698, 'l': 0.923888}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_69"] = {'bb': 1.139739, 'cc': 1.139739, 'c': 0.956165, 'l': 0.909119}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_69"] = {'bb': 1.478812, 'cc': 1.478812, 'c': 1.000000, 'l': 0.890158}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_69"] = {'bb': 1.428627, 'cc': 1.428627, 'c': 0.966064, 'l': 0.859949}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_69"] = {'bb': 1.382779, 'cc': 1.382779, 'c': 0.935061, 'l': 0.832351}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_69"] = {'bb': 1.326410, 'cc': 1.326410, 'c': 0.896943, 'l': 0.798421}
# NNPDF30_nnlo_as_0118_70 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_70"] = {'bb': 1.203539, 'cc': 1.203539, 'c': 1.000000, 'l': 0.947753}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_70"] = {'bb': 1.185279, 'cc': 1.185279, 'c': 0.984828, 'l': 0.933374}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_70"] = {'bb': 1.167397, 'cc': 1.167397, 'c': 0.969971, 'l': 0.919293}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_70"] = {'bb': 1.147662, 'cc': 1.147662, 'c': 0.953573, 'l': 0.903752}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_70"] = {'bb': 1.473092, 'cc': 1.473092, 'c': 1.000000, 'l': 0.891386}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_70"] = {'bb': 1.423236, 'cc': 1.423236, 'c': 0.966155, 'l': 0.861217}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_70"] = {'bb': 1.377924, 'cc': 1.377924, 'c': 0.935396, 'l': 0.833799}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_70"] = {'bb': 1.322439, 'cc': 1.322439, 'c': 0.897730, 'l': 0.800224}
# NNPDF30_nnlo_as_0118_71 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_71"] = {'bb': 1.268934, 'cc': 1.268934, 'c': 1.000000, 'l': 0.931551}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_71"] = {'bb': 1.243839, 'cc': 1.243839, 'c': 0.980223, 'l': 0.913128}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_71"] = {'bb': 1.219453, 'cc': 1.219453, 'c': 0.961006, 'l': 0.895225}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_71"] = {'bb': 1.192479, 'cc': 1.192479, 'c': 0.939749, 'l': 0.875423}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_71"] = {'bb': 1.509748, 'cc': 1.509748, 'c': 1.000000, 'l': 0.884226}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_71"] = {'bb': 1.455058, 'cc': 1.455058, 'c': 0.963776, 'l': 0.852196}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_71"] = {'bb': 1.405835, 'cc': 1.405835, 'c': 0.931172, 'l': 0.823366}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_71"] = {'bb': 1.345196, 'cc': 1.345196, 'c': 0.891008, 'l': 0.787852}
# NNPDF30_nnlo_as_0118_72 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_72"] = {'bb': 1.233490, 'cc': 1.233490, 'c': 1.000000, 'l': 0.940318}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_72"] = {'bb': 1.211968, 'cc': 1.211968, 'c': 0.982552, 'l': 0.923911}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_72"] = {'bb': 1.190989, 'cc': 1.190989, 'c': 0.965544, 'l': 0.907919}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_72"] = {'bb': 1.168189, 'cc': 1.168189, 'c': 0.947060, 'l': 0.890538}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_72"] = {'bb': 1.347364, 'cc': 1.347364, 'c': 1.000000, 'l': 0.921789}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_72"] = {'bb': 1.312474, 'cc': 1.312474, 'c': 0.974105, 'l': 0.897920}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_72"] = {'bb': 1.281425, 'cc': 1.281425, 'c': 0.951060, 'l': 0.876677}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_72"] = {'bb': 1.242624, 'cc': 1.242624, 'c': 0.922263, 'l': 0.850132}
# NNPDF30_nnlo_as_0118_73 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_73"] = {'bb': 1.281359, 'cc': 1.281359, 'c': 1.000000, 'l': 0.928211}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_73"] = {'bb': 1.254835, 'cc': 1.254835, 'c': 0.979300, 'l': 0.908997}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_73"] = {'bb': 1.229034, 'cc': 1.229034, 'c': 0.959165, 'l': 0.890308}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_73"] = {'bb': 1.200703, 'cc': 1.200703, 'c': 0.937055, 'l': 0.869785}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_73"] = {'bb': 1.563437, 'cc': 1.563437, 'c': 1.000000, 'l': 0.871058}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_73"] = {'bb': 1.500660, 'cc': 1.500660, 'c': 0.959847, 'l': 0.836082}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_73"] = {'bb': 1.445261, 'cc': 1.445261, 'c': 0.924413, 'l': 0.805217}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_73"] = {'bb': 1.376902, 'cc': 1.376902, 'c': 0.880689, 'l': 0.767131}
# NNPDF30_nnlo_as_0118_74 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_74"] = {'bb': 1.285616, 'cc': 1.285616, 'c': 1.000000, 'l': 0.926394}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_74"] = {'bb': 1.258409, 'cc': 1.258409, 'c': 0.978838, 'l': 0.906790}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_74"] = {'bb': 1.232257, 'cc': 1.232257, 'c': 0.958496, 'l': 0.887945}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_74"] = {'bb': 1.203611, 'cc': 1.203611, 'c': 0.936213, 'l': 0.867303}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_74"] = {'bb': 1.563285, 'cc': 1.563285, 'c': 1.000000, 'l': 0.871135}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_74"] = {'bb': 1.500902, 'cc': 1.500902, 'c': 0.960095, 'l': 0.836372}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_74"] = {'bb': 1.444788, 'cc': 1.444788, 'c': 0.924200, 'l': 0.805103}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_74"] = {'bb': 1.376764, 'cc': 1.376764, 'c': 0.880687, 'l': 0.767197}
# NNPDF30_nnlo_as_0118_75 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_75"] = {'bb': 1.367464, 'cc': 1.367464, 'c': 1.000000, 'l': 0.906238}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_75"] = {'bb': 1.330690, 'cc': 1.330690, 'c': 0.973108, 'l': 0.881867}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_75"] = {'bb': 1.295435, 'cc': 1.295435, 'c': 0.947327, 'l': 0.858503}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_75"] = {'bb': 1.257073, 'cc': 1.257073, 'c': 0.919273, 'l': 0.833080}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_75"] = {'bb': 1.622311, 'cc': 1.622311, 'c': 1.000000, 'l': 0.858130}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_75"] = {'bb': 1.551254, 'cc': 1.551254, 'c': 0.956200, 'l': 0.820544}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_75"] = {'bb': 1.488215, 'cc': 1.488215, 'c': 0.917343, 'l': 0.787199}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_75"] = {'bb': 1.411565, 'cc': 1.411565, 'c': 0.870095, 'l': 0.746655}
# NNPDF30_nnlo_as_0118_76 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_76"] = {'bb': 1.265577, 'cc': 1.265577, 'c': 1.000000, 'l': 0.931880}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_76"] = {'bb': 1.240644, 'cc': 1.240644, 'c': 0.980299, 'l': 0.913521}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_76"] = {'bb': 1.216479, 'cc': 1.216479, 'c': 0.961205, 'l': 0.895727}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_76"] = {'bb': 1.190234, 'cc': 1.190234, 'c': 0.940467, 'l': 0.876402}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_76"] = {'bb': 1.578220, 'cc': 1.578220, 'c': 1.000000, 'l': 0.867684}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_76"] = {'bb': 1.513731, 'cc': 1.513731, 'c': 0.959138, 'l': 0.832228}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_76"] = {'bb': 1.455822, 'cc': 1.455822, 'c': 0.922445, 'l': 0.800391}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_76"] = {'bb': 1.385606, 'cc': 1.385606, 'c': 0.877955, 'l': 0.761787}
# NNPDF30_nnlo_as_0118_77 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_77"] = {'bb': 1.319031, 'cc': 1.319031, 'c': 1.000000, 'l': 0.918128}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_77"] = {'bb': 1.288100, 'cc': 1.288100, 'c': 0.976550, 'l': 0.896598}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_77"] = {'bb': 1.258428, 'cc': 1.258428, 'c': 0.954055, 'l': 0.875945}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_77"] = {'bb': 1.225964, 'cc': 1.225964, 'c': 0.929443, 'l': 0.853347}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_77"] = {'bb': 1.608137, 'cc': 1.608137, 'c': 1.000000, 'l': 0.860318}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_77"] = {'bb': 1.539332, 'cc': 1.539332, 'c': 0.957214, 'l': 0.823509}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_77"] = {'bb': 1.477813, 'cc': 1.477813, 'c': 0.918959, 'l': 0.790597}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_77"] = {'bb': 1.403680, 'cc': 1.403680, 'c': 0.872861, 'l': 0.750938}
# NNPDF30_nnlo_as_0118_78 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_78"] = {'bb': 1.280041, 'cc': 1.280041, 'c': 1.000000, 'l': 0.927997}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_78"] = {'bb': 1.253395, 'cc': 1.253395, 'c': 0.979184, 'l': 0.908679}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_78"] = {'bb': 1.227670, 'cc': 1.227670, 'c': 0.959086, 'l': 0.890029}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_78"] = {'bb': 1.199570, 'cc': 1.199570, 'c': 0.937134, 'l': 0.869657}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_78"] = {'bb': 1.436726, 'cc': 1.436726, 'c': 1.000000, 'l': 0.900562}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_78"] = {'bb': 1.390950, 'cc': 1.390950, 'c': 0.968139, 'l': 0.871869}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_78"] = {'bb': 1.349964, 'cc': 1.349964, 'c': 0.939611, 'l': 0.846178}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_78"] = {'bb': 1.300256, 'cc': 1.300256, 'c': 0.905014, 'l': 0.815021}
# NNPDF30_nnlo_as_0118_79 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_79"] = {'bb': 1.246742, 'cc': 1.246742, 'c': 1.000000, 'l': 0.936851}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_79"] = {'bb': 1.223788, 'cc': 1.223788, 'c': 0.981588, 'l': 0.919602}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_79"] = {'bb': 1.201574, 'cc': 1.201574, 'c': 0.963771, 'l': 0.902910}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_79"] = {'bb': 1.177218, 'cc': 1.177218, 'c': 0.944235, 'l': 0.884607}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_79"] = {'bb': 1.411169, 'cc': 1.411169, 'c': 1.000000, 'l': 0.906847}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_79"] = {'bb': 1.368693, 'cc': 1.368693, 'c': 0.969900, 'l': 0.879551}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_79"] = {'bb': 1.330745, 'cc': 1.330745, 'c': 0.943009, 'l': 0.855164}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_79"] = {'bb': 1.283642, 'cc': 1.283642, 'c': 0.909630, 'l': 0.824895}
# NNPDF30_nnlo_as_0118_80 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_80"] = {'bb': 1.286516, 'cc': 1.286516, 'c': 1.000000, 'l': 0.926683}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_80"] = {'bb': 1.259289, 'cc': 1.259289, 'c': 0.978836, 'l': 0.907071}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_80"] = {'bb': 1.232864, 'cc': 1.232864, 'c': 0.958297, 'l': 0.888038}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_80"] = {'bb': 1.204008, 'cc': 1.204008, 'c': 0.935867, 'l': 0.867253}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_80"] = {'bb': 1.600997, 'cc': 1.600997, 'c': 1.000000, 'l': 0.861100}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_80"] = {'bb': 1.533467, 'cc': 1.533467, 'c': 0.957820, 'l': 0.824779}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_80"] = {'bb': 1.472869, 'cc': 1.472869, 'c': 0.919970, 'l': 0.792186}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_80"] = {'bb': 1.399235, 'cc': 1.399235, 'c': 0.873977, 'l': 0.752582}
# NNPDF30_nnlo_as_0118_81 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_81"] = {'bb': 1.371729, 'cc': 1.371729, 'c': 1.000000, 'l': 0.904844}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_81"] = {'bb': 1.334143, 'cc': 1.334143, 'c': 0.972600, 'l': 0.880051}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_81"] = {'bb': 1.298297, 'cc': 1.298297, 'c': 0.946468, 'l': 0.856405}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_81"] = {'bb': 1.259795, 'cc': 1.259795, 'c': 0.918399, 'l': 0.831008}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_81"] = {'bb': 1.637001, 'cc': 1.637001, 'c': 1.000000, 'l': 0.854202}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_81"] = {'bb': 1.562981, 'cc': 1.562981, 'c': 0.954783, 'l': 0.815577}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_81"] = {'bb': 1.497651, 'cc': 1.497651, 'c': 0.914875, 'l': 0.781488}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_81"] = {'bb': 1.419524, 'cc': 1.419524, 'c': 0.867149, 'l': 0.740720}
# NNPDF30_nnlo_as_0118_82 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_82"] = {'bb': 1.294252, 'cc': 1.294252, 'c': 1.000000, 'l': 0.924489}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_82"] = {'bb': 1.265923, 'cc': 1.265923, 'c': 0.978111, 'l': 0.904253}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_82"] = {'bb': 1.238741, 'cc': 1.238741, 'c': 0.957109, 'l': 0.884838}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_82"] = {'bb': 1.209113, 'cc': 1.209113, 'c': 0.934217, 'l': 0.863674}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_82"] = {'bb': 1.501967, 'cc': 1.501967, 'c': 1.000000, 'l': 0.885331}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_82"] = {'bb': 1.447870, 'cc': 1.447870, 'c': 0.963982, 'l': 0.853443}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_82"] = {'bb': 1.399156, 'cc': 1.399156, 'c': 0.931549, 'l': 0.824729}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_82"] = {'bb': 1.339746, 'cc': 1.339746, 'c': 0.891994, 'l': 0.789710}
# NNPDF30_nnlo_as_0118_83 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_83"] = {'bb': 1.255819, 'cc': 1.255819, 'c': 1.000000, 'l': 0.934544}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_83"] = {'bb': 1.232016, 'cc': 1.232016, 'c': 0.981045, 'l': 0.916830}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_83"] = {'bb': 1.208891, 'cc': 1.208891, 'c': 0.962631, 'l': 0.899621}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_83"] = {'bb': 1.183503, 'cc': 1.183503, 'c': 0.942415, 'l': 0.880728}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_83"] = {'bb': 2.271286, 'cc': 2.271286, 'c': 1.000000, 'l': 0.726936}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_83"] = {'bb': 2.040844, 'cc': 2.040844, 'c': 0.898541, 'l': 0.653182}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_83"] = {'bb': 1.864412, 'cc': 1.864412, 'c': 0.820862, 'l': 0.596714}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_83"] = {'bb': 1.675221, 'cc': 1.675221, 'c': 0.737565, 'l': 0.536162}
# NNPDF30_nnlo_as_0118_84 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_84"] = {'bb': 1.298874, 'cc': 1.298874, 'c': 1.000000, 'l': 0.923572}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_84"] = {'bb': 1.270056, 'cc': 1.270056, 'c': 0.977813, 'l': 0.903081}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_84"] = {'bb': 1.242274, 'cc': 1.242274, 'c': 0.956424, 'l': 0.883326}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_84"] = {'bb': 1.212250, 'cc': 1.212250, 'c': 0.933308, 'l': 0.861977}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_84"] = {'bb': 1.390479, 'cc': 1.390479, 'c': 1.000000, 'l': 0.911914}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_84"] = {'bb': 1.350343, 'cc': 1.350343, 'c': 0.971135, 'l': 0.885591}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_84"] = {'bb': 1.314608, 'cc': 1.314608, 'c': 0.945435, 'l': 0.862156}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_84"] = {'bb': 1.270385, 'cc': 1.270385, 'c': 0.913631, 'l': 0.833153}
# NNPDF30_nnlo_as_0118_85 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_85"] = {'bb': 1.311296, 'cc': 1.311296, 'c': 1.000000, 'l': 0.920521}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_85"] = {'bb': 1.281239, 'cc': 1.281239, 'c': 0.977078, 'l': 0.899421}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_85"] = {'bb': 1.252185, 'cc': 1.252185, 'c': 0.954921, 'l': 0.879025}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_85"] = {'bb': 1.220500, 'cc': 1.220500, 'c': 0.930758, 'l': 0.856783}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_85"] = {'bb': 1.688262, 'cc': 1.688262, 'c': 1.000000, 'l': 0.841813}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_85"] = {'bb': 1.607983, 'cc': 1.607983, 'c': 0.952449, 'l': 0.801784}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_85"] = {'bb': 1.535788, 'cc': 1.535788, 'c': 0.909686, 'l': 0.765785}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_85"] = {'bb': 1.449412, 'cc': 1.449412, 'c': 0.858523, 'l': 0.722716}
# NNPDF30_nnlo_as_0118_86 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_86"] = {'bb': 1.232203, 'cc': 1.232203, 'c': 1.000000, 'l': 0.940365}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_86"] = {'bb': 1.211060, 'cc': 1.211060, 'c': 0.982842, 'l': 0.924230}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_86"] = {'bb': 1.190431, 'cc': 1.190431, 'c': 0.966100, 'l': 0.908486}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_86"] = {'bb': 1.167593, 'cc': 1.167593, 'c': 0.947566, 'l': 0.891057}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_86"] = {'bb': 1.511427, 'cc': 1.511427, 'c': 1.000000, 'l': 0.882996}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_86"] = {'bb': 1.456193, 'cc': 1.456193, 'c': 0.963456, 'l': 0.850727}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_86"] = {'bb': 1.406516, 'cc': 1.406516, 'c': 0.930588, 'l': 0.821705}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_86"] = {'bb': 1.345554, 'cc': 1.345554, 'c': 0.890254, 'l': 0.786091}
# NNPDF30_nnlo_as_0118_87 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_87"] = {'bb': 1.195520, 'cc': 1.195520, 'c': 1.000000, 'l': 0.949931}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_87"] = {'bb': 1.178005, 'cc': 1.178005, 'c': 0.985349, 'l': 0.936013}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_87"] = {'bb': 1.160924, 'cc': 1.160924, 'c': 0.971062, 'l': 0.922442}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_87"] = {'bb': 1.142023, 'cc': 1.142023, 'c': 0.955252, 'l': 0.907423}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_87"] = {'bb': 1.333129, 'cc': 1.333129, 'c': 1.000000, 'l': 0.924445}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_87"] = {'bb': 1.300424, 'cc': 1.300424, 'c': 0.975468, 'l': 0.901766}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_87"] = {'bb': 1.270818, 'cc': 1.270818, 'c': 0.953260, 'l': 0.881236}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_87"] = {'bb': 1.233760, 'cc': 1.233760, 'c': 0.925462, 'l': 0.855538}
# NNPDF30_nnlo_as_0118_88 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_88"] = {'bb': 1.195930, 'cc': 1.195930, 'c': 1.000000, 'l': 0.949836}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_88"] = {'bb': 1.178431, 'cc': 1.178431, 'c': 0.985368, 'l': 0.935938}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_88"] = {'bb': 1.161308, 'cc': 1.161308, 'c': 0.971050, 'l': 0.922338}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_88"] = {'bb': 1.142869, 'cc': 1.142869, 'c': 0.955631, 'l': 0.907693}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_88"] = {'bb': 1.346627, 'cc': 1.346627, 'c': 1.000000, 'l': 0.921300}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_88"] = {'bb': 1.312431, 'cc': 1.312431, 'c': 0.974606, 'l': 0.897904}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_88"] = {'bb': 1.281292, 'cc': 1.281292, 'c': 0.951483, 'l': 0.876601}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_88"] = {'bb': 1.242492, 'cc': 1.242492, 'c': 0.922669, 'l': 0.850056}
# NNPDF30_nnlo_as_0118_89 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_89"] = {'bb': 1.296448, 'cc': 1.296448, 'c': 1.000000, 'l': 0.924096}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_89"] = {'bb': 1.268223, 'cc': 1.268223, 'c': 0.978229, 'l': 0.903977}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_89"] = {'bb': 1.240873, 'cc': 1.240873, 'c': 0.957133, 'l': 0.884483}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_89"] = {'bb': 1.210866, 'cc': 1.210866, 'c': 0.933988, 'l': 0.863094}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_89"] = {'bb': 1.672756, 'cc': 1.672756, 'c': 1.000000, 'l': 0.845180}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_89"] = {'bb': 1.594932, 'cc': 1.594932, 'c': 0.953476, 'l': 0.805858}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_89"] = {'bb': 1.524880, 'cc': 1.524880, 'c': 0.911597, 'l': 0.770463}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_89"] = {'bb': 1.440857, 'cc': 1.440857, 'c': 0.861367, 'l': 0.728010}
# NNPDF30_nnlo_as_0118_90 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.084839, 'cc': 1.084839, 'c': 1.000000, 'l': 0.978275}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.077958, 'cc': 1.077958, 'c': 0.993657, 'l': 0.972070}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.071062, 'cc': 1.071062, 'c': 0.987301, 'l': 0.965852}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.063344, 'cc': 1.063344, 'c': 0.980186, 'l': 0.958892}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.598670, 'cc': 1.598670, 'c': 1.000000, 'l': 0.860369}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.533620, 'cc': 1.533620, 'c': 0.959310, 'l': 0.825361}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.472570, 'cc': 1.472570, 'c': 0.921122, 'l': 0.792505}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.398750, 'cc': 1.398750, 'c': 0.874946, 'l': 0.752777}
# NNPDF30_nnlo_as_0118_91 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.315329, 'cc': 1.315329, 'c': 1.000000, 'l': 0.919315}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.284770, 'cc': 1.284770, 'c': 0.976767, 'l': 0.897957}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.255307, 'cc': 1.255307, 'c': 0.954368, 'l': 0.877365}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.223262, 'cc': 1.223262, 'c': 0.930005, 'l': 0.854967}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.452196, 'cc': 1.452196, 'c': 1.000000, 'l': 0.897448}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.404568, 'cc': 1.404568, 'c': 0.967202, 'l': 0.868014}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.361914, 'cc': 1.361914, 'c': 0.937831, 'l': 0.841655}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.309357, 'cc': 1.309357, 'c': 0.901639, 'l': 0.809174}
# NNPDF30_nnlo_as_0118_92 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.261131, 'cc': 1.261131, 'c': 1.000000, 'l': 0.933076}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.236682, 'cc': 1.236682, 'c': 0.980614, 'l': 0.914987}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.213005, 'cc': 1.213005, 'c': 0.961839, 'l': 0.897469}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.187103, 'cc': 1.187103, 'c': 0.941300, 'l': 0.878305}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.482389, 'cc': 1.482389, 'c': 1.000000, 'l': 0.889822}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.431088, 'cc': 1.431088, 'c': 0.965393, 'l': 0.859028}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.384833, 'cc': 1.384833, 'c': 0.934190, 'l': 0.831263}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.328113, 'cc': 1.328113, 'c': 0.895927, 'l': 0.797216}
# NNPDF30_nnlo_as_0118_93 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.270979, 'cc': 1.270979, 'c': 1.000000, 'l': 0.930847}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.245547, 'cc': 1.245547, 'c': 0.979990, 'l': 0.912221}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.220849, 'cc': 1.220849, 'c': 0.960558, 'l': 0.894133}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.193811, 'cc': 1.193811, 'c': 0.939284, 'l': 0.874330}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.555984, 'cc': 1.555984, 'c': 1.000000, 'l': 0.873021}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.494942, 'cc': 1.494942, 'c': 0.960770, 'l': 0.838772}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.439881, 'cc': 1.439881, 'c': 0.925383, 'l': 0.807879}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.372802, 'cc': 1.372802, 'c': 0.882273, 'l': 0.770243}
# NNPDF30_nnlo_as_0118_94 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.296219, 'cc': 1.296219, 'c': 1.000000, 'l': 0.924323}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.267682, 'cc': 1.267682, 'c': 0.977985, 'l': 0.903974}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.240326, 'cc': 1.240326, 'c': 0.956880, 'l': 0.884467}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.210484, 'cc': 1.210484, 'c': 0.933857, 'l': 0.863186}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.282950, 'cc': 1.282950, 'c': 1.000000, 'l': 0.936567}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.255662, 'cc': 1.255662, 'c': 0.978730, 'l': 0.916646}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.231395, 'cc': 1.231395, 'c': 0.959815, 'l': 0.898931}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.200794, 'cc': 1.200794, 'c': 0.935963, 'l': 0.876592}
# NNPDF30_nnlo_as_0118_95 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.177414, 'cc': 1.177414, 'c': 1.000000, 'l': 0.955054}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.162628, 'cc': 1.162628, 'c': 0.987442, 'l': 0.943061}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.148608, 'cc': 1.148608, 'c': 0.975535, 'l': 0.931689}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.132613, 'cc': 1.132613, 'c': 0.961949, 'l': 0.918714}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.439301, 'cc': 1.439301, 'c': 1.000000, 'l': 0.900521}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.393742, 'cc': 1.393742, 'c': 0.968346, 'l': 0.872016}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.352770, 'cc': 1.352770, 'c': 0.939880, 'l': 0.846381}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.301676, 'cc': 1.301676, 'c': 0.904380, 'l': 0.814414}
# NNPDF30_nnlo_as_0118_96 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.269745, 'cc': 1.269745, 'c': 1.000000, 'l': 0.930843}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.244358, 'cc': 1.244358, 'c': 0.980006, 'l': 0.912233}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.219734, 'cc': 1.219734, 'c': 0.960614, 'l': 0.894181}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.192801, 'cc': 1.192801, 'c': 0.939402, 'l': 0.874436}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.512547, 'cc': 1.512547, 'c': 1.000000, 'l': 0.884516}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.456943, 'cc': 1.456943, 'c': 0.963238, 'l': 0.851999}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.407024, 'cc': 1.407024, 'c': 0.930234, 'l': 0.822807}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.345996, 'cc': 1.345996, 'c': 0.889886, 'l': 0.787118}
# NNPDF30_nnlo_as_0118_97 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.328251, 'cc': 1.328251, 'c': 1.000000, 'l': 0.916106}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.296217, 'cc': 1.296217, 'c': 0.975883, 'l': 0.894012}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.265318, 'cc': 1.265318, 'c': 0.952620, 'l': 0.872701}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.231953, 'cc': 1.231953, 'c': 0.927500, 'l': 0.849689}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.407743, 'cc': 1.407743, 'c': 1.000000, 'l': 0.908043}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.365486, 'cc': 1.365486, 'c': 0.969983, 'l': 0.880786}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.328378, 'cc': 1.328378, 'c': 0.943623, 'l': 0.856850}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.282050, 'cc': 1.282050, 'c': 0.910713, 'l': 0.826967}
# NNPDF30_nnlo_as_0118_98 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.257444, 'cc': 1.257444, 'c': 1.000000, 'l': 0.933949}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.233193, 'cc': 1.233193, 'c': 0.980714, 'l': 0.915937}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.210093, 'cc': 1.210093, 'c': 0.962344, 'l': 0.898780}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.184680, 'cc': 1.184680, 'c': 0.942133, 'l': 0.879904}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.423144, 'cc': 1.423144, 'c': 1.000000, 'l': 0.903744}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.379264, 'cc': 1.379264, 'c': 0.969167, 'l': 0.875879}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.339923, 'cc': 1.339923, 'c': 0.941523, 'l': 0.850896}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.291261, 'cc': 1.291261, 'c': 0.907330, 'l': 0.819994}
# NNPDF30_nnlo_as_0118_99 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.343292, 'cc': 1.343292, 'c': 1.000000, 'l': 0.912074}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.309333, 'cc': 1.309333, 'c': 0.974719, 'l': 0.889016}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.276705, 'cc': 1.276705, 'c': 0.950430, 'l': 0.866862}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.241444, 'cc': 1.241444, 'c': 0.924180, 'l': 0.842920}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.739160, 'cc': 1.739160, 'c': 1.000000, 'l': 0.829178}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.650902, 'cc': 1.650902, 'c': 0.949253, 'l': 0.787100}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.571449, 'cc': 1.571449, 'c': 0.903568, 'l': 0.749219}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.477635, 'cc': 1.477635, 'c': 0.849626, 'l': 0.704491}
# NNPDF30_nnlo_as_0118_90 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.084839, 'cc': 1.084839, 'c': 1.000000, 'l': 0.978275}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.077958, 'cc': 1.077958, 'c': 0.993657, 'l': 0.972070}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.071062, 'cc': 1.071062, 'c': 0.987301, 'l': 0.965852}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.063344, 'cc': 1.063344, 'c': 0.980186, 'l': 0.958892}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.598670, 'cc': 1.598670, 'c': 1.000000, 'l': 0.860369}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.533620, 'cc': 1.533620, 'c': 0.959310, 'l': 0.825361}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.472570, 'cc': 1.472570, 'c': 0.921122, 'l': 0.792505}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 1.398750, 'cc': 1.398750, 'c': 0.874946, 'l': 0.752777}
# NNPDF30_nnlo_as_0118_91 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.315329, 'cc': 1.315329, 'c': 1.000000, 'l': 0.919315}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.284770, 'cc': 1.284770, 'c': 0.976767, 'l': 0.897957}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.255307, 'cc': 1.255307, 'c': 0.954368, 'l': 0.877365}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.223262, 'cc': 1.223262, 'c': 0.930005, 'l': 0.854967}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.452196, 'cc': 1.452196, 'c': 1.000000, 'l': 0.897448}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.404568, 'cc': 1.404568, 'c': 0.967202, 'l': 0.868014}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.361914, 'cc': 1.361914, 'c': 0.937831, 'l': 0.841655}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 1.309357, 'cc': 1.309357, 'c': 0.901639, 'l': 0.809174}
# NNPDF30_nnlo_as_0118_92 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.261131, 'cc': 1.261131, 'c': 1.000000, 'l': 0.933076}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.236682, 'cc': 1.236682, 'c': 0.980614, 'l': 0.914987}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.213005, 'cc': 1.213005, 'c': 0.961839, 'l': 0.897469}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.187103, 'cc': 1.187103, 'c': 0.941300, 'l': 0.878305}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.482389, 'cc': 1.482389, 'c': 1.000000, 'l': 0.889822}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.431088, 'cc': 1.431088, 'c': 0.965393, 'l': 0.859028}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.384833, 'cc': 1.384833, 'c': 0.934190, 'l': 0.831263}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 1.328113, 'cc': 1.328113, 'c': 0.895927, 'l': 0.797216}
# NNPDF30_nnlo_as_0118_93 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.270979, 'cc': 1.270979, 'c': 1.000000, 'l': 0.930847}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.245547, 'cc': 1.245547, 'c': 0.979990, 'l': 0.912221}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.220849, 'cc': 1.220849, 'c': 0.960558, 'l': 0.894133}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.193811, 'cc': 1.193811, 'c': 0.939284, 'l': 0.874330}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.555984, 'cc': 1.555984, 'c': 1.000000, 'l': 0.873021}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.494942, 'cc': 1.494942, 'c': 0.960770, 'l': 0.838772}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.439881, 'cc': 1.439881, 'c': 0.925383, 'l': 0.807879}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 1.372802, 'cc': 1.372802, 'c': 0.882273, 'l': 0.770243}
# NNPDF30_nnlo_as_0118_94 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.296219, 'cc': 1.296219, 'c': 1.000000, 'l': 0.924323}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.267682, 'cc': 1.267682, 'c': 0.977985, 'l': 0.903974}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.240326, 'cc': 1.240326, 'c': 0.956880, 'l': 0.884467}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.210484, 'cc': 1.210484, 'c': 0.933857, 'l': 0.863186}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.282950, 'cc': 1.282950, 'c': 1.000000, 'l': 0.936567}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.255662, 'cc': 1.255662, 'c': 0.978730, 'l': 0.916646}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.231395, 'cc': 1.231395, 'c': 0.959815, 'l': 0.898931}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 1.200794, 'cc': 1.200794, 'c': 0.935963, 'l': 0.876592}
# NNPDF30_nnlo_as_0118_95 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.177414, 'cc': 1.177414, 'c': 1.000000, 'l': 0.955054}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.162628, 'cc': 1.162628, 'c': 0.987442, 'l': 0.943061}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.148608, 'cc': 1.148608, 'c': 0.975535, 'l': 0.931689}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.132613, 'cc': 1.132613, 'c': 0.961949, 'l': 0.918714}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.439301, 'cc': 1.439301, 'c': 1.000000, 'l': 0.900521}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.393742, 'cc': 1.393742, 'c': 0.968346, 'l': 0.872016}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.352770, 'cc': 1.352770, 'c': 0.939880, 'l': 0.846381}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 1.301676, 'cc': 1.301676, 'c': 0.904380, 'l': 0.814414}
# NNPDF30_nnlo_as_0118_96 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.269745, 'cc': 1.269745, 'c': 1.000000, 'l': 0.930843}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.244358, 'cc': 1.244358, 'c': 0.980006, 'l': 0.912233}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.219734, 'cc': 1.219734, 'c': 0.960614, 'l': 0.894181}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.192801, 'cc': 1.192801, 'c': 0.939402, 'l': 0.874436}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.512547, 'cc': 1.512547, 'c': 1.000000, 'l': 0.884516}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.456943, 'cc': 1.456943, 'c': 0.963238, 'l': 0.851999}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.407024, 'cc': 1.407024, 'c': 0.930234, 'l': 0.822807}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 1.345996, 'cc': 1.345996, 'c': 0.889886, 'l': 0.787118}
# NNPDF30_nnlo_as_0118_97 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.328251, 'cc': 1.328251, 'c': 1.000000, 'l': 0.916106}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.296217, 'cc': 1.296217, 'c': 0.975883, 'l': 0.894012}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.265318, 'cc': 1.265318, 'c': 0.952620, 'l': 0.872701}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.231953, 'cc': 1.231953, 'c': 0.927500, 'l': 0.849689}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.407743, 'cc': 1.407743, 'c': 1.000000, 'l': 0.908043}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.365486, 'cc': 1.365486, 'c': 0.969983, 'l': 0.880786}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.328378, 'cc': 1.328378, 'c': 0.943623, 'l': 0.856850}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 1.282050, 'cc': 1.282050, 'c': 0.910713, 'l': 0.826967}
# NNPDF30_nnlo_as_0118_98 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.257444, 'cc': 1.257444, 'c': 1.000000, 'l': 0.933949}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.233193, 'cc': 1.233193, 'c': 0.980714, 'l': 0.915937}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.210093, 'cc': 1.210093, 'c': 0.962344, 'l': 0.898780}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.184680, 'cc': 1.184680, 'c': 0.942133, 'l': 0.879904}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.423144, 'cc': 1.423144, 'c': 1.000000, 'l': 0.903744}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.379264, 'cc': 1.379264, 'c': 0.969167, 'l': 0.875879}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.339923, 'cc': 1.339923, 'c': 0.941523, 'l': 0.850896}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 1.291261, 'cc': 1.291261, 'c': 0.907330, 'l': 0.819994}
# NNPDF30_nnlo_as_0118_99 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.343292, 'cc': 1.343292, 'c': 1.000000, 'l': 0.912074}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.309333, 'cc': 1.309333, 'c': 0.974719, 'l': 0.889016}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.276705, 'cc': 1.276705, 'c': 0.950430, 'l': 0.866862}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.241444, 'cc': 1.241444, 'c': 0.924180, 'l': 0.842920}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.739160, 'cc': 1.739160, 'c': 1.000000, 'l': 0.829178}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.650902, 'cc': 1.650902, 'c': 0.949253, 'l': 0.787100}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.571449, 'cc': 1.571449, 'c': 0.903568, 'l': 0.749219}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 1.477635, 'cc': 1.477635, 'c': 0.849626, 'l': 0.704491}
# NNPDF30_nnlo_as_0118_100 
flav_map[2]['el']["NNPDF30_nnlo_as_0118_100"] = {'bb': 1.259771, 'cc': 1.259771, 'c': 1.000000, 'l': 0.933458}
flav_map[3]['el']["NNPDF30_nnlo_as_0118_100"] = {'bb': 1.235580, 'cc': 1.235580, 'c': 0.980797, 'l': 0.915532}
flav_map[4]['el']["NNPDF30_nnlo_as_0118_100"] = {'bb': 1.212035, 'cc': 1.212035, 'c': 0.962107, 'l': 0.898087}
flav_map[5]['el']["NNPDF30_nnlo_as_0118_100"] = {'bb': 1.186185, 'cc': 1.186185, 'c': 0.941587, 'l': 0.878932}
flav_map[2]['mu']["NNPDF30_nnlo_as_0118_100"] = {'bb': 1.450148, 'cc': 1.450148, 'c': 1.000000, 'l': 0.897763}
flav_map[3]['mu']["NNPDF30_nnlo_as_0118_100"] = {'bb': 1.401093, 'cc': 1.401093, 'c': 0.966173, 'l': 0.867394}
flav_map[4]['mu']["NNPDF30_nnlo_as_0118_100"] = {'bb': 1.360758, 'cc': 1.360758, 'c': 0.938358, 'l': 0.842424}
flav_map[5]['mu']["NNPDF30_nnlo_as_0118_100"] = {'bb': 1.308319, 'cc': 1.308319, 'c': 0.902197, 'l': 0.809960}

# NNPDF30_nnlo_as_0118_0 
frac[2]['el']["NNPDF30_nnlo_as_0118_0"] = {'bb': 0.095377,'cc': 0.065570,'c': 0.209864,'l': 0.629188}
frac[3]['el']["NNPDF30_nnlo_as_0118_0"] = {'bb': 0.118554,'cc': 0.100588,'c': 0.219467,'l': 0.561391}
frac[4]['el']["NNPDF30_nnlo_as_0118_0"] = {'bb': 0.141275,'cc': 0.139443,'c': 0.215282,'l': 0.504001}
frac[5]['el']["NNPDF30_nnlo_as_0118_0"] = {'bb': 0.149522,'cc': 0.152731,'c': 0.209920,'l': 0.487827}
frac[2]['mu']["NNPDF30_nnlo_as_0118_0"] = {'bb': 0.083917,'cc': 0.063837,'c': 0.205450,'l': 0.646796}
frac[3]['mu']["NNPDF30_nnlo_as_0118_0"] = {'bb': 0.107540,'cc': 0.098647,'c': 0.215807,'l': 0.578006}
frac[4]['mu']["NNPDF30_nnlo_as_0118_0"] = {'bb': 0.130997,'cc': 0.135025,'c': 0.207117,'l': 0.526861}
frac[5]['mu']["NNPDF30_nnlo_as_0118_0"] = {'bb': 0.141046,'cc': 0.148520,'c': 0.202400,'l': 0.508034}
# NNPDF30_nnlo_as_0118_1 
frac[2]['el']["NNPDF30_nnlo_as_0118_1"] = {'bb': 0.095406,'cc': 0.065637,'c': 0.209519,'l': 0.629438}
frac[3]['el']["NNPDF30_nnlo_as_0118_1"] = {'bb': 0.118532,'cc': 0.100572,'c': 0.219479,'l': 0.561417}
frac[4]['el']["NNPDF30_nnlo_as_0118_1"] = {'bb': 0.141322,'cc': 0.139378,'c': 0.215186,'l': 0.504114}
frac[5]['el']["NNPDF30_nnlo_as_0118_1"] = {'bb': 0.149538,'cc': 0.152594,'c': 0.209972,'l': 0.487896}
frac[2]['mu']["NNPDF30_nnlo_as_0118_1"] = {'bb': 0.083617,'cc': 0.063411,'c': 0.203362,'l': 0.649610}
frac[3]['mu']["NNPDF30_nnlo_as_0118_1"] = {'bb': 0.107791,'cc': 0.098561,'c': 0.215303,'l': 0.578345}
frac[4]['mu']["NNPDF30_nnlo_as_0118_1"] = {'bb': 0.131001,'cc': 0.134952,'c': 0.207094,'l': 0.526952}
frac[5]['mu']["NNPDF30_nnlo_as_0118_1"] = {'bb': 0.140987,'cc': 0.148475,'c': 0.202477,'l': 0.508061}
# NNPDF30_nnlo_as_0118_2 
frac[2]['el']["NNPDF30_nnlo_as_0118_2"] = {'bb': 0.095148,'cc': 0.064945,'c': 0.211146,'l': 0.628761}
frac[3]['el']["NNPDF30_nnlo_as_0118_2"] = {'bb': 0.118399,'cc': 0.099745,'c': 0.220101,'l': 0.561755}
frac[4]['el']["NNPDF30_nnlo_as_0118_2"] = {'bb': 0.141313,'cc': 0.138523,'c': 0.215521,'l': 0.504643}
frac[5]['el']["NNPDF30_nnlo_as_0118_2"] = {'bb': 0.149645,'cc': 0.151892,'c': 0.209786,'l': 0.488677}
frac[2]['mu']["NNPDF30_nnlo_as_0118_2"] = {'bb': 0.084218,'cc': 0.063078,'c': 0.207057,'l': 0.645646}
frac[3]['mu']["NNPDF30_nnlo_as_0118_2"] = {'bb': 0.107789,'cc': 0.097704,'c': 0.215912,'l': 0.578595}
frac[4]['mu']["NNPDF30_nnlo_as_0118_2"] = {'bb': 0.131210,'cc': 0.134052,'c': 0.207171,'l': 0.527566}
frac[5]['mu']["NNPDF30_nnlo_as_0118_2"] = {'bb': 0.141208,'cc': 0.147623,'c': 0.202452,'l': 0.508717}
# NNPDF30_nnlo_as_0118_3 
frac[2]['el']["NNPDF30_nnlo_as_0118_3"] = {'bb': 0.095366,'cc': 0.066030,'c': 0.209692,'l': 0.628912}
frac[3]['el']["NNPDF30_nnlo_as_0118_3"] = {'bb': 0.117870,'cc': 0.101269,'c': 0.219094,'l': 0.561767}
frac[4]['el']["NNPDF30_nnlo_as_0118_3"] = {'bb': 0.141066,'cc': 0.140218,'c': 0.214543,'l': 0.504174}
frac[5]['el']["NNPDF30_nnlo_as_0118_3"] = {'bb': 0.149537,'cc': 0.153662,'c': 0.208699,'l': 0.488102}
frac[2]['mu']["NNPDF30_nnlo_as_0118_3"] = {'bb': 0.083996,'cc': 0.064148,'c': 0.204842,'l': 0.647013}
frac[3]['mu']["NNPDF30_nnlo_as_0118_3"] = {'bb': 0.107550,'cc': 0.099400,'c': 0.215370,'l': 0.577680}
frac[4]['mu']["NNPDF30_nnlo_as_0118_3"] = {'bb': 0.131046,'cc': 0.135736,'c': 0.206554,'l': 0.526663}
frac[5]['mu']["NNPDF30_nnlo_as_0118_3"] = {'bb': 0.141028,'cc': 0.149274,'c': 0.201768,'l': 0.507930}
# NNPDF30_nnlo_as_0118_4 
frac[2]['el']["NNPDF30_nnlo_as_0118_4"] = {'bb': 0.095781,'cc': 0.064926,'c': 0.210384,'l': 0.628909}
frac[3]['el']["NNPDF30_nnlo_as_0118_4"] = {'bb': 0.119335,'cc': 0.099517,'c': 0.220168,'l': 0.560980}
frac[4]['el']["NNPDF30_nnlo_as_0118_4"] = {'bb': 0.142174,'cc': 0.137990,'c': 0.216396,'l': 0.503440}
frac[5]['el']["NNPDF30_nnlo_as_0118_4"] = {'bb': 0.150377,'cc': 0.151231,'c': 0.211351,'l': 0.487041}
frac[2]['mu']["NNPDF30_nnlo_as_0118_4"] = {'bb': 0.083958,'cc': 0.063111,'c': 0.206028,'l': 0.646903}
frac[3]['mu']["NNPDF30_nnlo_as_0118_4"] = {'bb': 0.107604,'cc': 0.097601,'c': 0.216552,'l': 0.578242}
frac[4]['mu']["NNPDF30_nnlo_as_0118_4"] = {'bb': 0.131092,'cc': 0.133778,'c': 0.208437,'l': 0.526693}
frac[5]['mu']["NNPDF30_nnlo_as_0118_4"] = {'bb': 0.141149,'cc': 0.147294,'c': 0.203880,'l': 0.507677}
# NNPDF30_nnlo_as_0118_5 
frac[2]['el']["NNPDF30_nnlo_as_0118_5"] = {'bb': 0.095324,'cc': 0.065869,'c': 0.208780,'l': 0.630027}
frac[3]['el']["NNPDF30_nnlo_as_0118_5"] = {'bb': 0.118439,'cc': 0.101120,'c': 0.218243,'l': 0.562198}
frac[4]['el']["NNPDF30_nnlo_as_0118_5"] = {'bb': 0.141126,'cc': 0.140194,'c': 0.214182,'l': 0.504498}
frac[5]['el']["NNPDF30_nnlo_as_0118_5"] = {'bb': 0.149476,'cc': 0.153508,'c': 0.208642,'l': 0.488375}
frac[2]['mu']["NNPDF30_nnlo_as_0118_5"] = {'bb': 0.083766,'cc': 0.064012,'c': 0.204001,'l': 0.648220}
frac[3]['mu']["NNPDF30_nnlo_as_0118_5"] = {'bb': 0.106282,'cc': 0.099196,'c': 0.214534,'l': 0.579988}
frac[4]['mu']["NNPDF30_nnlo_as_0118_5"] = {'bb': 0.127768,'cc': 0.136286,'c': 0.206705,'l': 0.529241}
frac[5]['mu']["NNPDF30_nnlo_as_0118_5"] = {'bb': 0.137100,'cc': 0.150011,'c': 0.202207,'l': 0.510682}
# NNPDF30_nnlo_as_0118_6 
frac[2]['el']["NNPDF30_nnlo_as_0118_6"] = {'bb': 0.095360,'cc': 0.065165,'c': 0.210572,'l': 0.628903}
frac[3]['el']["NNPDF30_nnlo_as_0118_6"] = {'bb': 0.118637,'cc': 0.100200,'c': 0.220173,'l': 0.560990}
frac[4]['el']["NNPDF30_nnlo_as_0118_6"] = {'bb': 0.141379,'cc': 0.139103,'c': 0.215730,'l': 0.503788}
frac[5]['el']["NNPDF30_nnlo_as_0118_6"] = {'bb': 0.149653,'cc': 0.152407,'c': 0.210073,'l': 0.487867}
frac[2]['mu']["NNPDF30_nnlo_as_0118_6"] = {'bb': 0.083529,'cc': 0.062851,'c': 0.204336,'l': 0.649284}
frac[3]['mu']["NNPDF30_nnlo_as_0118_6"] = {'bb': 0.107871,'cc': 0.098166,'c': 0.216072,'l': 0.577891}
frac[4]['mu']["NNPDF30_nnlo_as_0118_6"] = {'bb': 0.131136,'cc': 0.134645,'c': 0.207442,'l': 0.526777}
frac[5]['mu']["NNPDF30_nnlo_as_0118_6"] = {'bb': 0.141127,'cc': 0.148199,'c': 0.202693,'l': 0.507982}
# NNPDF30_nnlo_as_0118_7 
frac[2]['el']["NNPDF30_nnlo_as_0118_7"] = {'bb': 0.095469,'cc': 0.065962,'c': 0.210077,'l': 0.628492}
frac[3]['el']["NNPDF30_nnlo_as_0118_7"] = {'bb': 0.118502,'cc': 0.101150,'c': 0.219614,'l': 0.560734}
frac[4]['el']["NNPDF30_nnlo_as_0118_7"] = {'bb': 0.141103,'cc': 0.140175,'c': 0.215072,'l': 0.503650}
frac[5]['el']["NNPDF30_nnlo_as_0118_7"] = {'bb': 0.149433,'cc': 0.153466,'c': 0.209437,'l': 0.487664}
frac[2]['mu']["NNPDF30_nnlo_as_0118_7"] = {'bb': 0.084007,'cc': 0.063973,'c': 0.204803,'l': 0.647216}
frac[3]['mu']["NNPDF30_nnlo_as_0118_7"] = {'bb': 0.107590,'cc': 0.098953,'c': 0.215422,'l': 0.578035}
frac[4]['mu']["NNPDF30_nnlo_as_0118_7"] = {'bb': 0.130990,'cc': 0.135574,'c': 0.206785,'l': 0.526650}
frac[5]['mu']["NNPDF30_nnlo_as_0118_7"] = {'bb': 0.141017,'cc': 0.149131,'c': 0.202005,'l': 0.507848}
# NNPDF30_nnlo_as_0118_8 
frac[2]['el']["NNPDF30_nnlo_as_0118_8"] = {'bb': 0.095539,'cc': 0.064643,'c': 0.211884,'l': 0.627935}
frac[3]['el']["NNPDF30_nnlo_as_0118_8"] = {'bb': 0.118785,'cc': 0.099377,'c': 0.220492,'l': 0.561345}
frac[4]['el']["NNPDF30_nnlo_as_0118_8"] = {'bb': 0.141582,'cc': 0.137913,'c': 0.215775,'l': 0.504730}
frac[5]['el']["NNPDF30_nnlo_as_0118_8"] = {'bb': 0.149848,'cc': 0.151218,'c': 0.210493,'l': 0.488440}
frac[2]['mu']["NNPDF30_nnlo_as_0118_8"] = {'bb': 0.084360,'cc': 0.063016,'c': 0.207666,'l': 0.644958}
frac[3]['mu']["NNPDF30_nnlo_as_0118_8"] = {'bb': 0.107876,'cc': 0.097241,'c': 0.216277,'l': 0.578606}
frac[4]['mu']["NNPDF30_nnlo_as_0118_8"] = {'bb': 0.131304,'cc': 0.133411,'c': 0.207316,'l': 0.527969}
frac[5]['mu']["NNPDF30_nnlo_as_0118_8"] = {'bb': 0.141363,'cc': 0.146966,'c': 0.202655,'l': 0.509016}
# NNPDF30_nnlo_as_0118_9 
frac[2]['el']["NNPDF30_nnlo_as_0118_9"] = {'bb': 0.095538,'cc': 0.065530,'c': 0.209170,'l': 0.629762}
frac[3]['el']["NNPDF30_nnlo_as_0118_9"] = {'bb': 0.118686,'cc': 0.100400,'c': 0.219046,'l': 0.561868}
frac[4]['el']["NNPDF30_nnlo_as_0118_9"] = {'bb': 0.141468,'cc': 0.139095,'c': 0.215495,'l': 0.503941}
frac[5]['el']["NNPDF30_nnlo_as_0118_9"] = {'bb': 0.149698,'cc': 0.152315,'c': 0.210880,'l': 0.487106}
frac[2]['mu']["NNPDF30_nnlo_as_0118_9"] = {'bb': 0.084682,'cc': 0.063987,'c': 0.205339,'l': 0.645992}
frac[3]['mu']["NNPDF30_nnlo_as_0118_9"] = {'bb': 0.107741,'cc': 0.098200,'c': 0.214926,'l': 0.579133}
frac[4]['mu']["NNPDF30_nnlo_as_0118_9"] = {'bb': 0.131172,'cc': 0.134711,'c': 0.207255,'l': 0.526862}
frac[5]['mu']["NNPDF30_nnlo_as_0118_9"] = {'bb': 0.141244,'cc': 0.148264,'c': 0.202810,'l': 0.507682}
# NNPDF30_nnlo_as_0118_10 
frac[2]['el']["NNPDF30_nnlo_as_0118_10"] = {'bb': 0.095411,'cc': 0.065242,'c': 0.210225,'l': 0.629122}
frac[3]['el']["NNPDF30_nnlo_as_0118_10"] = {'bb': 0.118640,'cc': 0.100075,'c': 0.219719,'l': 0.561565}
frac[4]['el']["NNPDF30_nnlo_as_0118_10"] = {'bb': 0.141474,'cc': 0.138791,'c': 0.215559,'l': 0.504177}
frac[5]['el']["NNPDF30_nnlo_as_0118_10"] = {'bb': 0.149721,'cc': 0.152057,'c': 0.210546,'l': 0.487677}
frac[2]['mu']["NNPDF30_nnlo_as_0118_10"] = {'bb': 0.084567,'cc': 0.063565,'c': 0.206114,'l': 0.645754}
frac[3]['mu']["NNPDF30_nnlo_as_0118_10"] = {'bb': 0.107773,'cc': 0.097887,'c': 0.215245,'l': 0.579095}
frac[4]['mu']["NNPDF30_nnlo_as_0118_10"] = {'bb': 0.131172,'cc': 0.134214,'c': 0.207066,'l': 0.527548}
frac[5]['mu']["NNPDF30_nnlo_as_0118_10"] = {'bb': 0.141226,'cc': 0.147796,'c': 0.202482,'l': 0.508496}
# NNPDF30_nnlo_as_0118_11 
frac[2]['el']["NNPDF30_nnlo_as_0118_11"] = {'bb': 0.095320,'cc': 0.065588,'c': 0.208956,'l': 0.630136}
frac[3]['el']["NNPDF30_nnlo_as_0118_11"] = {'bb': 0.118547,'cc': 0.100746,'c': 0.218804,'l': 0.561903}
frac[4]['el']["NNPDF30_nnlo_as_0118_11"] = {'bb': 0.141245,'cc': 0.139722,'c': 0.214692,'l': 0.504341}
frac[5]['el']["NNPDF30_nnlo_as_0118_11"] = {'bb': 0.149567,'cc': 0.153028,'c': 0.209260,'l': 0.488146}
frac[2]['mu']["NNPDF30_nnlo_as_0118_11"] = {'bb': 0.083984,'cc': 0.063626,'c': 0.204017,'l': 0.648374}
frac[3]['mu']["NNPDF30_nnlo_as_0118_11"] = {'bb': 0.107617,'cc': 0.098678,'c': 0.214712,'l': 0.578993}
frac[4]['mu']["NNPDF30_nnlo_as_0118_11"] = {'bb': 0.131047,'cc': 0.135237,'c': 0.206598,'l': 0.527118}
frac[5]['mu']["NNPDF30_nnlo_as_0118_11"] = {'bb': 0.141049,'cc': 0.148799,'c': 0.202002,'l': 0.508150}
# NNPDF30_nnlo_as_0118_12 
frac[2]['el']["NNPDF30_nnlo_as_0118_12"] = {'bb': 0.095289,'cc': 0.064849,'c': 0.209829,'l': 0.630033}
frac[3]['el']["NNPDF30_nnlo_as_0118_12"] = {'bb': 0.118429,'cc': 0.099540,'c': 0.220249,'l': 0.561783}
frac[4]['el']["NNPDF30_nnlo_as_0118_12"] = {'bb': 0.141206,'cc': 0.138082,'c': 0.216693,'l': 0.504020}
frac[5]['el']["NNPDF30_nnlo_as_0118_12"] = {'bb': 0.149426,'cc': 0.151246,'c': 0.212170,'l': 0.487158}
frac[2]['mu']["NNPDF30_nnlo_as_0118_12"] = {'bb': 0.084192,'cc': 0.062890,'c': 0.204545,'l': 0.648372}
frac[3]['mu']["NNPDF30_nnlo_as_0118_12"] = {'bb': 0.107819,'cc': 0.097196,'c': 0.215431,'l': 0.579554}
frac[4]['mu']["NNPDF30_nnlo_as_0118_12"] = {'bb': 0.131520,'cc': 0.133505,'c': 0.208084,'l': 0.526891}
frac[5]['mu']["NNPDF30_nnlo_as_0118_12"] = {'bb': 0.141531,'cc': 0.146969,'c': 0.203690,'l': 0.507810}
# NNPDF30_nnlo_as_0118_13 
frac[2]['el']["NNPDF30_nnlo_as_0118_13"] = {'bb': 0.095430,'cc': 0.065566,'c': 0.211370,'l': 0.627634}
frac[3]['el']["NNPDF30_nnlo_as_0118_13"] = {'bb': 0.118557,'cc': 0.100631,'c': 0.220447,'l': 0.560365}
frac[4]['el']["NNPDF30_nnlo_as_0118_13"] = {'bb': 0.141241,'cc': 0.139510,'c': 0.215706,'l': 0.503543}
frac[5]['el']["NNPDF30_nnlo_as_0118_13"] = {'bb': 0.149463,'cc': 0.152757,'c': 0.210503,'l': 0.487277}
frac[2]['mu']["NNPDF30_nnlo_as_0118_13"] = {'bb': 0.083912,'cc': 0.063584,'c': 0.205560,'l': 0.646943}
frac[3]['mu']["NNPDF30_nnlo_as_0118_13"] = {'bb': 0.107656,'cc': 0.098526,'c': 0.216275,'l': 0.577543}
frac[4]['mu']["NNPDF30_nnlo_as_0118_13"] = {'bb': 0.131054,'cc': 0.135093,'c': 0.207301,'l': 0.526552}
frac[5]['mu']["NNPDF30_nnlo_as_0118_13"] = {'bb': 0.141090,'cc': 0.148654,'c': 0.202429,'l': 0.507827}
# NNPDF30_nnlo_as_0118_14 
frac[2]['el']["NNPDF30_nnlo_as_0118_14"] = {'bb': 0.095153,'cc': 0.066671,'c': 0.207290,'l': 0.630886}
frac[3]['el']["NNPDF30_nnlo_as_0118_14"] = {'bb': 0.118286,'cc': 0.102004,'c': 0.217210,'l': 0.562500}
frac[4]['el']["NNPDF30_nnlo_as_0118_14"] = {'bb': 0.140953,'cc': 0.141099,'c': 0.213090,'l': 0.504857}
frac[5]['el']["NNPDF30_nnlo_as_0118_14"] = {'bb': 0.149243,'cc': 0.154353,'c': 0.207874,'l': 0.488529}
frac[2]['mu']["NNPDF30_nnlo_as_0118_14"] = {'bb': 0.083469,'cc': 0.064636,'c': 0.201681,'l': 0.650214}
frac[3]['mu']["NNPDF30_nnlo_as_0118_14"] = {'bb': 0.107251,'cc': 0.100110,'c': 0.213398,'l': 0.579241}
frac[4]['mu']["NNPDF30_nnlo_as_0118_14"] = {'bb': 0.130651,'cc': 0.136783,'c': 0.205324,'l': 0.527242}
frac[5]['mu']["NNPDF30_nnlo_as_0118_14"] = {'bb': 0.140667,'cc': 0.150310,'c': 0.200733,'l': 0.508289}
# NNPDF30_nnlo_as_0118_15 
frac[2]['el']["NNPDF30_nnlo_as_0118_15"] = {'bb': 0.095291,'cc': 0.065310,'c': 0.209958,'l': 0.629441}
frac[3]['el']["NNPDF30_nnlo_as_0118_15"] = {'bb': 0.118602,'cc': 0.100442,'c': 0.219753,'l': 0.561203}
frac[4]['el']["NNPDF30_nnlo_as_0118_15"] = {'bb': 0.141310,'cc': 0.139338,'c': 0.215622,'l': 0.503731}
frac[5]['el']["NNPDF30_nnlo_as_0118_15"] = {'bb': 0.149467,'cc': 0.152580,'c': 0.210660,'l': 0.487293}
frac[2]['mu']["NNPDF30_nnlo_as_0118_15"] = {'bb': 0.083864,'cc': 0.063207,'c': 0.204421,'l': 0.648507}
frac[3]['mu']["NNPDF30_nnlo_as_0118_15"] = {'bb': 0.107694,'cc': 0.098285,'c': 0.215628,'l': 0.578393}
frac[4]['mu']["NNPDF30_nnlo_as_0118_15"] = {'bb': 0.131020,'cc': 0.134901,'c': 0.207212,'l': 0.526866}
frac[5]['mu']["NNPDF30_nnlo_as_0118_15"] = {'bb': 0.141084,'cc': 0.148474,'c': 0.202557,'l': 0.507885}
# NNPDF30_nnlo_as_0118_16 
frac[2]['el']["NNPDF30_nnlo_as_0118_16"] = {'bb': 0.095674,'cc': 0.065604,'c': 0.210579,'l': 0.628144}
frac[3]['el']["NNPDF30_nnlo_as_0118_16"] = {'bb': 0.118868,'cc': 0.100291,'c': 0.219627,'l': 0.561214}
frac[4]['el']["NNPDF30_nnlo_as_0118_16"] = {'bb': 0.141686,'cc': 0.138919,'c': 0.215846,'l': 0.503549}
frac[5]['el']["NNPDF30_nnlo_as_0118_16"] = {'bb': 0.150023,'cc': 0.152265,'c': 0.210590,'l': 0.487122}
frac[2]['mu']["NNPDF30_nnlo_as_0118_16"] = {'bb': 0.085240,'cc': 0.064393,'c': 0.208327,'l': 0.642040}
frac[3]['mu']["NNPDF30_nnlo_as_0118_16"] = {'bb': 0.107571,'cc': 0.097964,'c': 0.215451,'l': 0.579014}
frac[4]['mu']["NNPDF30_nnlo_as_0118_16"] = {'bb': 0.131226,'cc': 0.134248,'c': 0.207385,'l': 0.527141}
frac[5]['mu']["NNPDF30_nnlo_as_0118_16"] = {'bb': 0.141354,'cc': 0.147849,'c': 0.202792,'l': 0.508005}
# NNPDF30_nnlo_as_0118_17 
frac[2]['el']["NNPDF30_nnlo_as_0118_17"] = {'bb': 0.095208,'cc': 0.065556,'c': 0.208733,'l': 0.630503}
frac[3]['el']["NNPDF30_nnlo_as_0118_17"] = {'bb': 0.118300,'cc': 0.100454,'c': 0.218634,'l': 0.562612}
frac[4]['el']["NNPDF30_nnlo_as_0118_17"] = {'bb': 0.140953,'cc': 0.139174,'c': 0.214686,'l': 0.505187}
frac[5]['el']["NNPDF30_nnlo_as_0118_17"] = {'bb': 0.149149,'cc': 0.152401,'c': 0.209792,'l': 0.488658}
frac[2]['mu']["NNPDF30_nnlo_as_0118_17"] = {'bb': 0.083496,'cc': 0.063524,'c': 0.203087,'l': 0.649893}
frac[3]['mu']["NNPDF30_nnlo_as_0118_17"] = {'bb': 0.107242,'cc': 0.098637,'c': 0.214961,'l': 0.579160}
frac[4]['mu']["NNPDF30_nnlo_as_0118_17"] = {'bb': 0.130579,'cc': 0.135423,'c': 0.206764,'l': 0.527234}
frac[5]['mu']["NNPDF30_nnlo_as_0118_17"] = {'bb': 0.140602,'cc': 0.148841,'c': 0.202268,'l': 0.508289}
# NNPDF30_nnlo_as_0118_18 
frac[2]['el']["NNPDF30_nnlo_as_0118_18"] = {'bb': 0.095199,'cc': 0.065889,'c': 0.212482,'l': 0.626431}
frac[3]['el']["NNPDF30_nnlo_as_0118_18"] = {'bb': 0.118395,'cc': 0.100753,'c': 0.221422,'l': 0.559431}
frac[4]['el']["NNPDF30_nnlo_as_0118_18"] = {'bb': 0.141183,'cc': 0.139395,'c': 0.216213,'l': 0.503209}
frac[5]['el']["NNPDF30_nnlo_as_0118_18"] = {'bb': 0.149462,'cc': 0.152600,'c': 0.210580,'l': 0.487358}
frac[2]['mu']["NNPDF30_nnlo_as_0118_18"] = {'bb': 0.083442,'cc': 0.063104,'c': 0.204372,'l': 0.649081}
frac[3]['mu']["NNPDF30_nnlo_as_0118_18"] = {'bb': 0.107532,'cc': 0.098198,'c': 0.216080,'l': 0.578191}
frac[4]['mu']["NNPDF30_nnlo_as_0118_18"] = {'bb': 0.130990,'cc': 0.134596,'c': 0.207243,'l': 0.527172}
frac[5]['mu']["NNPDF30_nnlo_as_0118_18"] = {'bb': 0.140974,'cc': 0.148121,'c': 0.202463,'l': 0.508442}
# NNPDF30_nnlo_as_0118_19 
frac[2]['el']["NNPDF30_nnlo_as_0118_19"] = {'bb': 0.095340,'cc': 0.065568,'c': 0.209252,'l': 0.629841}
frac[3]['el']["NNPDF30_nnlo_as_0118_19"] = {'bb': 0.118560,'cc': 0.100388,'c': 0.219168,'l': 0.561883}
frac[4]['el']["NNPDF30_nnlo_as_0118_19"] = {'bb': 0.141172,'cc': 0.138960,'c': 0.215532,'l': 0.504336}
frac[5]['el']["NNPDF30_nnlo_as_0118_19"] = {'bb': 0.149527,'cc': 0.152220,'c': 0.210271,'l': 0.487982}
frac[2]['mu']["NNPDF30_nnlo_as_0118_19"] = {'bb': 0.084147,'cc': 0.063704,'c': 0.204804,'l': 0.647345}
frac[3]['mu']["NNPDF30_nnlo_as_0118_19"] = {'bb': 0.107460,'cc': 0.098311,'c': 0.215130,'l': 0.579099}
frac[4]['mu']["NNPDF30_nnlo_as_0118_19"] = {'bb': 0.130752,'cc': 0.134137,'c': 0.206783,'l': 0.528328}
frac[5]['mu']["NNPDF30_nnlo_as_0118_19"] = {'bb': 0.140838,'cc': 0.147618,'c': 0.202303,'l': 0.509241}
# NNPDF30_nnlo_as_0118_20 
frac[2]['el']["NNPDF30_nnlo_as_0118_20"] = {'bb': 0.095423,'cc': 0.065936,'c': 0.210109,'l': 0.628531}
frac[3]['el']["NNPDF30_nnlo_as_0118_20"] = {'bb': 0.118741,'cc': 0.101212,'c': 0.219903,'l': 0.560144}
frac[4]['el']["NNPDF30_nnlo_as_0118_20"] = {'bb': 0.141459,'cc': 0.140462,'c': 0.214912,'l': 0.503167}
frac[5]['el']["NNPDF30_nnlo_as_0118_20"] = {'bb': 0.149718,'cc': 0.153696,'c': 0.209039,'l': 0.487548}
frac[2]['mu']["NNPDF30_nnlo_as_0118_20"] = {'bb': 0.083660,'cc': 0.063104,'c': 0.202790,'l': 0.650447}
frac[3]['mu']["NNPDF30_nnlo_as_0118_20"] = {'bb': 0.109214,'cc': 0.098964,'c': 0.215083,'l': 0.576740}
frac[4]['mu']["NNPDF30_nnlo_as_0118_20"] = {'bb': 0.132880,'cc': 0.135565,'c': 0.205902,'l': 0.525653}
frac[5]['mu']["NNPDF30_nnlo_as_0118_20"] = {'bb': 0.142708,'cc': 0.149135,'c': 0.200983,'l': 0.507174}
# NNPDF30_nnlo_as_0118_21 
frac[2]['el']["NNPDF30_nnlo_as_0118_21"] = {'bb': 0.094818,'cc': 0.066044,'c': 0.210138,'l': 0.629000}
frac[3]['el']["NNPDF30_nnlo_as_0118_21"] = {'bb': 0.117229,'cc': 0.101166,'c': 0.219683,'l': 0.561922}
frac[4]['el']["NNPDF30_nnlo_as_0118_21"] = {'bb': 0.139655,'cc': 0.140055,'c': 0.215171,'l': 0.505119}
frac[5]['el']["NNPDF30_nnlo_as_0118_21"] = {'bb': 0.148101,'cc': 0.153333,'c': 0.209561,'l': 0.489004}
frac[2]['mu']["NNPDF30_nnlo_as_0118_21"] = {'bb': 0.083833,'cc': 0.063995,'c': 0.204645,'l': 0.647527}
frac[3]['mu']["NNPDF30_nnlo_as_0118_21"] = {'bb': 0.107471,'cc': 0.098943,'c': 0.215203,'l': 0.578382}
frac[4]['mu']["NNPDF30_nnlo_as_0118_21"] = {'bb': 0.130913,'cc': 0.135338,'c': 0.206542,'l': 0.527207}
frac[5]['mu']["NNPDF30_nnlo_as_0118_21"] = {'bb': 0.140923,'cc': 0.148874,'c': 0.201845,'l': 0.508358}
# NNPDF30_nnlo_as_0118_22 
frac[2]['el']["NNPDF30_nnlo_as_0118_22"] = {'bb': 0.094989,'cc': 0.065518,'c': 0.210762,'l': 0.628732}
frac[3]['el']["NNPDF30_nnlo_as_0118_22"] = {'bb': 0.118414,'cc': 0.100647,'c': 0.220184,'l': 0.560755}
frac[4]['el']["NNPDF30_nnlo_as_0118_22"] = {'bb': 0.141214,'cc': 0.139508,'c': 0.215226,'l': 0.504052}
frac[5]['el']["NNPDF30_nnlo_as_0118_22"] = {'bb': 0.149464,'cc': 0.152772,'c': 0.209885,'l': 0.487878}
frac[2]['mu']["NNPDF30_nnlo_as_0118_22"] = {'bb': 0.083954,'cc': 0.063482,'c': 0.205041,'l': 0.647523}
frac[3]['mu']["NNPDF30_nnlo_as_0118_22"] = {'bb': 0.107745,'cc': 0.098518,'c': 0.215876,'l': 0.577861}
frac[4]['mu']["NNPDF30_nnlo_as_0118_22"] = {'bb': 0.131093,'cc': 0.135158,'c': 0.207188,'l': 0.526561}
frac[5]['mu']["NNPDF30_nnlo_as_0118_22"] = {'bb': 0.141096,'cc': 0.148717,'c': 0.202373,'l': 0.507814}
# NNPDF30_nnlo_as_0118_23 
frac[2]['el']["NNPDF30_nnlo_as_0118_23"] = {'bb': 0.095628,'cc': 0.065073,'c': 0.212143,'l': 0.627156}
frac[3]['el']["NNPDF30_nnlo_as_0118_23"] = {'bb': 0.119028,'cc': 0.100336,'c': 0.220890,'l': 0.559747}
frac[4]['el']["NNPDF30_nnlo_as_0118_23"] = {'bb': 0.141753,'cc': 0.139506,'c': 0.215689,'l': 0.503052}
frac[5]['el']["NNPDF30_nnlo_as_0118_23"] = {'bb': 0.150029,'cc': 0.152898,'c': 0.209799,'l': 0.487274}
frac[2]['mu']["NNPDF30_nnlo_as_0118_23"] = {'bb': 0.084214,'cc': 0.063014,'c': 0.206163,'l': 0.646609}
frac[3]['mu']["NNPDF30_nnlo_as_0118_23"] = {'bb': 0.108049,'cc': 0.097919,'c': 0.215791,'l': 0.578241}
frac[4]['mu']["NNPDF30_nnlo_as_0118_23"] = {'bb': 0.131319,'cc': 0.134522,'c': 0.206635,'l': 0.527523}
frac[5]['mu']["NNPDF30_nnlo_as_0118_23"] = {'bb': 0.141213,'cc': 0.148179,'c': 0.201818,'l': 0.508790}
# NNPDF30_nnlo_as_0118_24 
frac[2]['el']["NNPDF30_nnlo_as_0118_24"] = {'bb': 0.095270,'cc': 0.065915,'c': 0.209231,'l': 0.629584}
frac[3]['el']["NNPDF30_nnlo_as_0118_24"] = {'bb': 0.118632,'cc': 0.101150,'c': 0.219197,'l': 0.561021}
frac[4]['el']["NNPDF30_nnlo_as_0118_24"] = {'bb': 0.141341,'cc': 0.140161,'c': 0.214855,'l': 0.503643}
frac[5]['el']["NNPDF30_nnlo_as_0118_24"] = {'bb': 0.149569,'cc': 0.153391,'c': 0.209630,'l': 0.487411}
frac[2]['mu']["NNPDF30_nnlo_as_0118_24"] = {'bb': 0.083681,'cc': 0.063933,'c': 0.203994,'l': 0.648392}
frac[3]['mu']["NNPDF30_nnlo_as_0118_24"] = {'bb': 0.107518,'cc': 0.099231,'c': 0.215493,'l': 0.577758}
frac[4]['mu']["NNPDF30_nnlo_as_0118_24"] = {'bb': 0.130933,'cc': 0.135886,'c': 0.207084,'l': 0.526097}
frac[5]['mu']["NNPDF30_nnlo_as_0118_24"] = {'bb': 0.140939,'cc': 0.149431,'c': 0.202307,'l': 0.507323}
# NNPDF30_nnlo_as_0118_25 
frac[2]['el']["NNPDF30_nnlo_as_0118_25"] = {'bb': 0.095345,'cc': 0.065727,'c': 0.209956,'l': 0.628972}
frac[3]['el']["NNPDF30_nnlo_as_0118_25"] = {'bb': 0.118489,'cc': 0.100778,'c': 0.219852,'l': 0.560881}
frac[4]['el']["NNPDF30_nnlo_as_0118_25"] = {'bb': 0.141303,'cc': 0.139696,'c': 0.215800,'l': 0.503200}
frac[5]['el']["NNPDF30_nnlo_as_0118_25"] = {'bb': 0.149553,'cc': 0.152962,'c': 0.210305,'l': 0.487180}
frac[2]['mu']["NNPDF30_nnlo_as_0118_25"] = {'bb': 0.084078,'cc': 0.063819,'c': 0.204798,'l': 0.647305}
frac[3]['mu']["NNPDF30_nnlo_as_0118_25"] = {'bb': 0.107521,'cc': 0.098657,'c': 0.215708,'l': 0.578114}
frac[4]['mu']["NNPDF30_nnlo_as_0118_25"] = {'bb': 0.130936,'cc': 0.135185,'c': 0.207425,'l': 0.526454}
frac[5]['mu']["NNPDF30_nnlo_as_0118_25"] = {'bb': 0.140942,'cc': 0.148715,'c': 0.202685,'l': 0.507658}
# NNPDF30_nnlo_as_0118_26 
frac[2]['el']["NNPDF30_nnlo_as_0118_26"] = {'bb': 0.095490,'cc': 0.065776,'c': 0.208857,'l': 0.629878}
frac[3]['el']["NNPDF30_nnlo_as_0118_26"] = {'bb': 0.118627,'cc': 0.100718,'c': 0.218448,'l': 0.562206}
frac[4]['el']["NNPDF30_nnlo_as_0118_26"] = {'bb': 0.141405,'cc': 0.139536,'c': 0.214361,'l': 0.504698}
frac[5]['el']["NNPDF30_nnlo_as_0118_26"] = {'bb': 0.149717,'cc': 0.152808,'c': 0.209110,'l': 0.488365}
frac[2]['mu']["NNPDF30_nnlo_as_0118_26"] = {'bb': 0.084461,'cc': 0.064177,'c': 0.205009,'l': 0.646353}
frac[3]['mu']["NNPDF30_nnlo_as_0118_26"] = {'bb': 0.107530,'cc': 0.098598,'c': 0.214328,'l': 0.579544}
frac[4]['mu']["NNPDF30_nnlo_as_0118_26"] = {'bb': 0.131044,'cc': 0.135032,'c': 0.206191,'l': 0.527733}
frac[5]['mu']["NNPDF30_nnlo_as_0118_26"] = {'bb': 0.141084,'cc': 0.148567,'c': 0.201690,'l': 0.508659}
# NNPDF30_nnlo_as_0118_27 
frac[2]['el']["NNPDF30_nnlo_as_0118_27"] = {'bb': 0.095284,'cc': 0.065890,'c': 0.210540,'l': 0.628287}
frac[3]['el']["NNPDF30_nnlo_as_0118_27"] = {'bb': 0.118457,'cc': 0.101083,'c': 0.219902,'l': 0.560557}
frac[4]['el']["NNPDF30_nnlo_as_0118_27"] = {'bb': 0.141126,'cc': 0.140110,'c': 0.215200,'l': 0.503564}
frac[5]['el']["NNPDF30_nnlo_as_0118_27"] = {'bb': 0.149433,'cc': 0.153424,'c': 0.209500,'l': 0.487643}
frac[2]['mu']["NNPDF30_nnlo_as_0118_27"] = {'bb': 0.084073,'cc': 0.063971,'c': 0.205059,'l': 0.646896}
frac[3]['mu']["NNPDF30_nnlo_as_0118_27"] = {'bb': 0.107508,'cc': 0.098830,'c': 0.215324,'l': 0.578338}
frac[4]['mu']["NNPDF30_nnlo_as_0118_27"] = {'bb': 0.130825,'cc': 0.135453,'c': 0.206602,'l': 0.527120}
frac[5]['mu']["NNPDF30_nnlo_as_0118_27"] = {'bb': 0.140806,'cc': 0.148974,'c': 0.202016,'l': 0.508203}
# NNPDF30_nnlo_as_0118_28 
frac[2]['el']["NNPDF30_nnlo_as_0118_28"] = {'bb': 0.095241,'cc': 0.066641,'c': 0.209087,'l': 0.629031}
frac[3]['el']["NNPDF30_nnlo_as_0118_28"] = {'bb': 0.118303,'cc': 0.102100,'c': 0.218998,'l': 0.560599}
frac[4]['el']["NNPDF30_nnlo_as_0118_28"] = {'bb': 0.140869,'cc': 0.141125,'c': 0.214504,'l': 0.503502}
frac[5]['el']["NNPDF30_nnlo_as_0118_28"] = {'bb': 0.149239,'cc': 0.154382,'c': 0.208763,'l': 0.487617}
frac[2]['mu']["NNPDF30_nnlo_as_0118_28"] = {'bb': 0.083452,'cc': 0.064912,'c': 0.204423,'l': 0.647213}
frac[3]['mu']["NNPDF30_nnlo_as_0118_28"] = {'bb': 0.107158,'cc': 0.100292,'c': 0.215917,'l': 0.576634}
frac[4]['mu']["NNPDF30_nnlo_as_0118_28"] = {'bb': 0.130635,'cc': 0.136910,'c': 0.206972,'l': 0.525483}
frac[5]['mu']["NNPDF30_nnlo_as_0118_28"] = {'bb': 0.140633,'cc': 0.150383,'c': 0.202044,'l': 0.506940}
# NNPDF30_nnlo_as_0118_29 
frac[2]['el']["NNPDF30_nnlo_as_0118_29"] = {'bb': 0.095625,'cc': 0.064949,'c': 0.210946,'l': 0.628480}
frac[3]['el']["NNPDF30_nnlo_as_0118_29"] = {'bb': 0.118759,'cc': 0.099822,'c': 0.219609,'l': 0.561811}
frac[4]['el']["NNPDF30_nnlo_as_0118_29"] = {'bb': 0.141550,'cc': 0.138642,'c': 0.214814,'l': 0.504994}
frac[5]['el']["NNPDF30_nnlo_as_0118_29"] = {'bb': 0.149875,'cc': 0.152065,'c': 0.209183,'l': 0.488876}
frac[2]['mu']["NNPDF30_nnlo_as_0118_29"] = {'bb': 0.084702,'cc': 0.063344,'c': 0.206572,'l': 0.645382}
frac[3]['mu']["NNPDF30_nnlo_as_0118_29"] = {'bb': 0.107909,'cc': 0.097625,'c': 0.214932,'l': 0.579533}
frac[4]['mu']["NNPDF30_nnlo_as_0118_29"] = {'bb': 0.131256,'cc': 0.134117,'c': 0.206319,'l': 0.528309}
frac[5]['mu']["NNPDF30_nnlo_as_0118_29"] = {'bb': 0.141306,'cc': 0.147749,'c': 0.201682,'l': 0.509263}
# NNPDF30_nnlo_as_0118_30 
frac[2]['el']["NNPDF30_nnlo_as_0118_30"] = {'bb': 0.095240,'cc': 0.065495,'c': 0.209943,'l': 0.629321}
frac[3]['el']["NNPDF30_nnlo_as_0118_30"] = {'bb': 0.118408,'cc': 0.100723,'c': 0.219371,'l': 0.561497}
frac[4]['el']["NNPDF30_nnlo_as_0118_30"] = {'bb': 0.141142,'cc': 0.139826,'c': 0.214858,'l': 0.504174}
frac[5]['el']["NNPDF30_nnlo_as_0118_30"] = {'bb': 0.149478,'cc': 0.153084,'c': 0.209632,'l': 0.487806}
frac[2]['mu']["NNPDF30_nnlo_as_0118_30"] = {'bb': 0.083346,'cc': 0.063350,'c': 0.204189,'l': 0.649116}
frac[3]['mu']["NNPDF30_nnlo_as_0118_30"] = {'bb': 0.107461,'cc': 0.098708,'c': 0.215363,'l': 0.578468}
frac[4]['mu']["NNPDF30_nnlo_as_0118_30"] = {'bb': 0.130786,'cc': 0.135514,'c': 0.206670,'l': 0.527031}
frac[5]['mu']["NNPDF30_nnlo_as_0118_30"] = {'bb': 0.140821,'cc': 0.149072,'c': 0.201901,'l': 0.508206}
# NNPDF30_nnlo_as_0118_31 
frac[2]['el']["NNPDF30_nnlo_as_0118_31"] = {'bb': 0.095226,'cc': 0.065165,'c': 0.211067,'l': 0.628541}
frac[3]['el']["NNPDF30_nnlo_as_0118_31"] = {'bb': 0.118655,'cc': 0.100319,'c': 0.221007,'l': 0.560019}
frac[4]['el']["NNPDF30_nnlo_as_0118_31"] = {'bb': 0.141456,'cc': 0.139207,'c': 0.216994,'l': 0.502344}
frac[5]['el']["NNPDF30_nnlo_as_0118_31"] = {'bb': 0.149660,'cc': 0.152414,'c': 0.211766,'l': 0.486159}
frac[2]['mu']["NNPDF30_nnlo_as_0118_31"] = {'bb': 0.083609,'cc': 0.062794,'c': 0.204884,'l': 0.648713}
frac[3]['mu']["NNPDF30_nnlo_as_0118_31"] = {'bb': 0.107615,'cc': 0.097949,'c': 0.216485,'l': 0.577952}
frac[4]['mu']["NNPDF30_nnlo_as_0118_31"] = {'bb': 0.130816,'cc': 0.134560,'c': 0.208478,'l': 0.526147}
frac[5]['mu']["NNPDF30_nnlo_as_0118_31"] = {'bb': 0.140835,'cc': 0.148144,'c': 0.203712,'l': 0.507309}
# NNPDF30_nnlo_as_0118_32 
frac[2]['el']["NNPDF30_nnlo_as_0118_32"] = {'bb': 0.095313,'cc': 0.065573,'c': 0.209667,'l': 0.629447}
frac[3]['el']["NNPDF30_nnlo_as_0118_32"] = {'bb': 0.118528,'cc': 0.100477,'c': 0.219065,'l': 0.561929}
frac[4]['el']["NNPDF30_nnlo_as_0118_32"] = {'bb': 0.141365,'cc': 0.139162,'c': 0.214832,'l': 0.504640}
frac[5]['el']["NNPDF30_nnlo_as_0118_32"] = {'bb': 0.149620,'cc': 0.152358,'c': 0.209353,'l': 0.488669}
frac[2]['mu']["NNPDF30_nnlo_as_0118_32"] = {'bb': 0.083891,'cc': 0.063661,'c': 0.204676,'l': 0.647772}
frac[3]['mu']["NNPDF30_nnlo_as_0118_32"] = {'bb': 0.107198,'cc': 0.098181,'c': 0.214490,'l': 0.580131}
frac[4]['mu']["NNPDF30_nnlo_as_0118_32"] = {'bb': 0.130875,'cc': 0.134798,'c': 0.206723,'l': 0.527603}
frac[5]['mu']["NNPDF30_nnlo_as_0118_32"] = {'bb': 0.140941,'cc': 0.148363,'c': 0.202099,'l': 0.508597}
# NNPDF30_nnlo_as_0118_33 
frac[2]['el']["NNPDF30_nnlo_as_0118_33"] = {'bb': 0.094937,'cc': 0.064940,'c': 0.209274,'l': 0.630849}
frac[3]['el']["NNPDF30_nnlo_as_0118_33"] = {'bb': 0.118471,'cc': 0.099763,'c': 0.219228,'l': 0.562539}
frac[4]['el']["NNPDF30_nnlo_as_0118_33"] = {'bb': 0.141313,'cc': 0.138485,'c': 0.215738,'l': 0.504463}
frac[5]['el']["NNPDF30_nnlo_as_0118_33"] = {'bb': 0.149513,'cc': 0.151792,'c': 0.210938,'l': 0.487757}
frac[2]['mu']["NNPDF30_nnlo_as_0118_33"] = {'bb': 0.083243,'cc': 0.062900,'c': 0.203832,'l': 0.650025}
frac[3]['mu']["NNPDF30_nnlo_as_0118_33"] = {'bb': 0.107507,'cc': 0.097877,'c': 0.215507,'l': 0.579108}
frac[4]['mu']["NNPDF30_nnlo_as_0118_33"] = {'bb': 0.130989,'cc': 0.134280,'c': 0.207801,'l': 0.526929}
frac[5]['mu']["NNPDF30_nnlo_as_0118_33"] = {'bb': 0.141323,'cc': 0.148129,'c': 0.201910,'l': 0.508639}
# NNPDF30_nnlo_as_0118_34 
frac[2]['el']["NNPDF30_nnlo_as_0118_34"] = {'bb': 0.095406,'cc': 0.065128,'c': 0.209783,'l': 0.629683}
frac[3]['el']["NNPDF30_nnlo_as_0118_34"] = {'bb': 0.118730,'cc': 0.099949,'c': 0.219911,'l': 0.561409}
frac[4]['el']["NNPDF30_nnlo_as_0118_34"] = {'bb': 0.141446,'cc': 0.138558,'c': 0.216296,'l': 0.503701}
frac[5]['el']["NNPDF30_nnlo_as_0118_34"] = {'bb': 0.149677,'cc': 0.151760,'c': 0.211501,'l': 0.487061}
frac[2]['mu']["NNPDF30_nnlo_as_0118_34"] = {'bb': 0.083366,'cc': 0.062906,'c': 0.204383,'l': 0.649345}
frac[3]['mu']["NNPDF30_nnlo_as_0118_34"] = {'bb': 0.107613,'cc': 0.097965,'c': 0.216342,'l': 0.578080}
frac[4]['mu']["NNPDF30_nnlo_as_0118_34"] = {'bb': 0.131101,'cc': 0.134278,'c': 0.208303,'l': 0.526319}
frac[5]['mu']["NNPDF30_nnlo_as_0118_34"] = {'bb': 0.141149,'cc': 0.147789,'c': 0.203709,'l': 0.507354}
# NNPDF30_nnlo_as_0118_35 
frac[2]['el']["NNPDF30_nnlo_as_0118_35"] = {'bb': 0.095439,'cc': 0.065561,'c': 0.209295,'l': 0.629705}
frac[3]['el']["NNPDF30_nnlo_as_0118_35"] = {'bb': 0.118623,'cc': 0.100387,'c': 0.219295,'l': 0.561695}
frac[4]['el']["NNPDF30_nnlo_as_0118_35"] = {'bb': 0.141322,'cc': 0.139051,'c': 0.216009,'l': 0.503618}
frac[5]['el']["NNPDF30_nnlo_as_0118_35"] = {'bb': 0.149642,'cc': 0.152307,'c': 0.210969,'l': 0.487082}
frac[2]['mu']["NNPDF30_nnlo_as_0118_35"] = {'bb': 0.084509,'cc': 0.064025,'c': 0.206211,'l': 0.645254}
frac[3]['mu']["NNPDF30_nnlo_as_0118_35"] = {'bb': 0.107426,'cc': 0.098280,'c': 0.215516,'l': 0.578778}
frac[4]['mu']["NNPDF30_nnlo_as_0118_35"] = {'bb': 0.131126,'cc': 0.134836,'c': 0.208050,'l': 0.525988}
frac[5]['mu']["NNPDF30_nnlo_as_0118_35"] = {'bb': 0.141157,'cc': 0.148337,'c': 0.203461,'l': 0.507045}
# NNPDF30_nnlo_as_0118_36 
frac[2]['el']["NNPDF30_nnlo_as_0118_36"] = {'bb': 0.095542,'cc': 0.065374,'c': 0.209752,'l': 0.629332}
frac[3]['el']["NNPDF30_nnlo_as_0118_36"] = {'bb': 0.118724,'cc': 0.100247,'c': 0.219330,'l': 0.561699}
frac[4]['el']["NNPDF30_nnlo_as_0118_36"] = {'bb': 0.141524,'cc': 0.139127,'c': 0.215696,'l': 0.503652}
frac[5]['el']["NNPDF30_nnlo_as_0118_36"] = {'bb': 0.149812,'cc': 0.152481,'c': 0.210255,'l': 0.487452}
frac[2]['mu']["NNPDF30_nnlo_as_0118_36"] = {'bb': 0.084951,'cc': 0.063708,'c': 0.205715,'l': 0.645626}
frac[3]['mu']["NNPDF30_nnlo_as_0118_36"] = {'bb': 0.107878,'cc': 0.097499,'c': 0.214093,'l': 0.580530}
frac[4]['mu']["NNPDF30_nnlo_as_0118_36"] = {'bb': 0.131427,'cc': 0.133864,'c': 0.206150,'l': 0.528559}
frac[5]['mu']["NNPDF30_nnlo_as_0118_36"] = {'bb': 0.141467,'cc': 0.147457,'c': 0.201745,'l': 0.509332}
# NNPDF30_nnlo_as_0118_37 
frac[2]['el']["NNPDF30_nnlo_as_0118_37"] = {'bb': 0.095707,'cc': 0.064154,'c': 0.211370,'l': 0.628769}
frac[3]['el']["NNPDF30_nnlo_as_0118_37"] = {'bb': 0.119023,'cc': 0.098490,'c': 0.221368,'l': 0.561119}
frac[4]['el']["NNPDF30_nnlo_as_0118_37"] = {'bb': 0.141830,'cc': 0.136706,'c': 0.218230,'l': 0.503233}
frac[5]['el']["NNPDF30_nnlo_as_0118_37"] = {'bb': 0.150067,'cc': 0.149898,'c': 0.213731,'l': 0.486304}
frac[2]['mu']["NNPDF30_nnlo_as_0118_37"] = {'bb': 0.085122,'cc': 0.062759,'c': 0.208045,'l': 0.644073}
frac[3]['mu']["NNPDF30_nnlo_as_0118_37"] = {'bb': 0.108083,'cc': 0.096201,'c': 0.217088,'l': 0.578628}
frac[4]['mu']["NNPDF30_nnlo_as_0118_37"] = {'bb': 0.131641,'cc': 0.132331,'c': 0.209703,'l': 0.526325}
frac[5]['mu']["NNPDF30_nnlo_as_0118_37"] = {'bb': 0.141741,'cc': 0.145866,'c': 0.205320,'l': 0.507074}
# NNPDF30_nnlo_as_0118_38 
frac[2]['el']["NNPDF30_nnlo_as_0118_38"] = {'bb': 0.095310,'cc': 0.066307,'c': 0.208880,'l': 0.629503}
frac[3]['el']["NNPDF30_nnlo_as_0118_38"] = {'bb': 0.118409,'cc': 0.101482,'c': 0.218574,'l': 0.561535}
frac[4]['el']["NNPDF30_nnlo_as_0118_38"] = {'bb': 0.141130,'cc': 0.140605,'c': 0.214591,'l': 0.503675}
frac[5]['el']["NNPDF30_nnlo_as_0118_38"] = {'bb': 0.149490,'cc': 0.153900,'c': 0.209122,'l': 0.487488}
frac[2]['mu']["NNPDF30_nnlo_as_0118_38"] = {'bb': 0.084178,'cc': 0.064575,'c': 0.204514,'l': 0.646732}
frac[3]['mu']["NNPDF30_nnlo_as_0118_38"] = {'bb': 0.107295,'cc': 0.099274,'c': 0.214477,'l': 0.578955}
frac[4]['mu']["NNPDF30_nnlo_as_0118_38"] = {'bb': 0.130706,'cc': 0.135823,'c': 0.206129,'l': 0.527342}
frac[5]['mu']["NNPDF30_nnlo_as_0118_38"] = {'bb': 0.140732,'cc': 0.149362,'c': 0.201401,'l': 0.508506}
# NNPDF30_nnlo_as_0118_39 
frac[2]['el']["NNPDF30_nnlo_as_0118_39"] = {'bb': 0.095453,'cc': 0.065739,'c': 0.209895,'l': 0.628913}
frac[3]['el']["NNPDF30_nnlo_as_0118_39"] = {'bb': 0.118595,'cc': 0.100834,'c': 0.219340,'l': 0.561230}
frac[4]['el']["NNPDF30_nnlo_as_0118_39"] = {'bb': 0.141300,'cc': 0.139841,'c': 0.215148,'l': 0.503710}
frac[5]['el']["NNPDF30_nnlo_as_0118_39"] = {'bb': 0.149683,'cc': 0.153221,'c': 0.209410,'l': 0.487686}
frac[2]['mu']["NNPDF30_nnlo_as_0118_39"] = {'bb': 0.084003,'cc': 0.063877,'c': 0.205134,'l': 0.646986}
frac[3]['mu']["NNPDF30_nnlo_as_0118_39"] = {'bb': 0.107727,'cc': 0.098734,'c': 0.215279,'l': 0.578259}
frac[4]['mu']["NNPDF30_nnlo_as_0118_39"] = {'bb': 0.131213,'cc': 0.135243,'c': 0.206878,'l': 0.526666}
frac[5]['mu']["NNPDF30_nnlo_as_0118_39"] = {'bb': 0.141278,'cc': 0.148851,'c': 0.202156,'l': 0.507715}
# NNPDF30_nnlo_as_0118_40 
frac[2]['el']["NNPDF30_nnlo_as_0118_40"] = {'bb': 0.095203,'cc': 0.065783,'c': 0.209137,'l': 0.629876}
frac[3]['el']["NNPDF30_nnlo_as_0118_40"] = {'bb': 0.118502,'cc': 0.100943,'c': 0.218892,'l': 0.561662}
frac[4]['el']["NNPDF30_nnlo_as_0118_40"] = {'bb': 0.141308,'cc': 0.139925,'c': 0.214356,'l': 0.504411}
frac[5]['el']["NNPDF30_nnlo_as_0118_40"] = {'bb': 0.149601,'cc': 0.153252,'c': 0.208512,'l': 0.488635}
frac[2]['mu']["NNPDF30_nnlo_as_0118_40"] = {'bb': 0.083580,'cc': 0.063848,'c': 0.204004,'l': 0.648568}
frac[3]['mu']["NNPDF30_nnlo_as_0118_40"] = {'bb': 0.107312,'cc': 0.099353,'c': 0.215835,'l': 0.577501}
frac[4]['mu']["NNPDF30_nnlo_as_0118_40"] = {'bb': 0.130501,'cc': 0.136024,'c': 0.207378,'l': 0.526096}
frac[5]['mu']["NNPDF30_nnlo_as_0118_40"] = {'bb': 0.140438,'cc': 0.149533,'c': 0.202526,'l': 0.507503}
# NNPDF30_nnlo_as_0118_41 
frac[2]['el']["NNPDF30_nnlo_as_0118_41"] = {'bb': 0.095293,'cc': 0.066062,'c': 0.208659,'l': 0.629987}
frac[3]['el']["NNPDF30_nnlo_as_0118_41"] = {'bb': 0.118439,'cc': 0.101218,'c': 0.218735,'l': 0.561608}
frac[4]['el']["NNPDF30_nnlo_as_0118_41"] = {'bb': 0.141084,'cc': 0.140186,'c': 0.214767,'l': 0.503963}
frac[5]['el']["NNPDF30_nnlo_as_0118_41"] = {'bb': 0.149451,'cc': 0.153495,'c': 0.209315,'l': 0.487738}
frac[2]['mu']["NNPDF30_nnlo_as_0118_41"] = {'bb': 0.083985,'cc': 0.064127,'c': 0.203690,'l': 0.648198}
frac[3]['mu']["NNPDF30_nnlo_as_0118_41"] = {'bb': 0.107449,'cc': 0.099145,'c': 0.214660,'l': 0.578746}
frac[4]['mu']["NNPDF30_nnlo_as_0118_41"] = {'bb': 0.130972,'cc': 0.135812,'c': 0.206684,'l': 0.526532}
frac[5]['mu']["NNPDF30_nnlo_as_0118_41"] = {'bb': 0.140986,'cc': 0.149333,'c': 0.202073,'l': 0.507608}
# NNPDF30_nnlo_as_0118_42 
frac[2]['el']["NNPDF30_nnlo_as_0118_42"] = {'bb': 0.095586,'cc': 0.065981,'c': 0.209265,'l': 0.629169}
frac[3]['el']["NNPDF30_nnlo_as_0118_42"] = {'bb': 0.118991,'cc': 0.101302,'c': 0.219238,'l': 0.560469}
frac[4]['el']["NNPDF30_nnlo_as_0118_42"] = {'bb': 0.142152,'cc': 0.140936,'c': 0.215988,'l': 0.500924}
frac[5]['el']["NNPDF30_nnlo_as_0118_42"] = {'bb': 0.150397,'cc': 0.154148,'c': 0.210074,'l': 0.485381}
frac[2]['mu']["NNPDF30_nnlo_as_0118_42"] = {'bb': 0.083808,'cc': 0.064007,'c': 0.204365,'l': 0.647820}
frac[3]['mu']["NNPDF30_nnlo_as_0118_42"] = {'bb': 0.107611,'cc': 0.099177,'c': 0.215216,'l': 0.577996}
frac[4]['mu']["NNPDF30_nnlo_as_0118_42"] = {'bb': 0.130949,'cc': 0.135717,'c': 0.206759,'l': 0.526575}
frac[5]['mu']["NNPDF30_nnlo_as_0118_42"] = {'bb': 0.140937,'cc': 0.149221,'c': 0.202000,'l': 0.507842}
# NNPDF30_nnlo_as_0118_43 
frac[2]['el']["NNPDF30_nnlo_as_0118_43"] = {'bb': 0.095567,'cc': 0.064985,'c': 0.209371,'l': 0.630076}
frac[3]['el']["NNPDF30_nnlo_as_0118_43"] = {'bb': 0.118899,'cc': 0.099460,'c': 0.218281,'l': 0.563361}
frac[4]['el']["NNPDF30_nnlo_as_0118_43"] = {'bb': 0.141838,'cc': 0.138039,'c': 0.214434,'l': 0.505688}
frac[5]['el']["NNPDF30_nnlo_as_0118_43"] = {'bb': 0.150173,'cc': 0.151412,'c': 0.209240,'l': 0.489175}
frac[2]['mu']["NNPDF30_nnlo_as_0118_43"] = {'bb': 0.084824,'cc': 0.063971,'c': 0.207927,'l': 0.643277}
frac[3]['mu']["NNPDF30_nnlo_as_0118_43"] = {'bb': 0.107626,'cc': 0.097747,'c': 0.215121,'l': 0.579505}
frac[4]['mu']["NNPDF30_nnlo_as_0118_43"] = {'bb': 0.131156,'cc': 0.133846,'c': 0.206924,'l': 0.528075}
frac[5]['mu']["NNPDF30_nnlo_as_0118_43"] = {'bb': 0.141199,'cc': 0.147620,'c': 0.202414,'l': 0.508767}
# NNPDF30_nnlo_as_0118_44 
frac[2]['el']["NNPDF30_nnlo_as_0118_44"] = {'bb': 0.095346,'cc': 0.066097,'c': 0.209057,'l': 0.629500}
frac[3]['el']["NNPDF30_nnlo_as_0118_44"] = {'bb': 0.118497,'cc': 0.101146,'c': 0.218556,'l': 0.561801}
frac[4]['el']["NNPDF30_nnlo_as_0118_44"] = {'bb': 0.141170,'cc': 0.139959,'c': 0.214570,'l': 0.504301}
frac[5]['el']["NNPDF30_nnlo_as_0118_44"] = {'bb': 0.149453,'cc': 0.153182,'c': 0.209344,'l': 0.488021}
frac[2]['mu']["NNPDF30_nnlo_as_0118_44"] = {'bb': 0.084006,'cc': 0.064216,'c': 0.204305,'l': 0.647474}
frac[3]['mu']["NNPDF30_nnlo_as_0118_44"] = {'bb': 0.107437,'cc': 0.098796,'c': 0.214682,'l': 0.579085}
frac[4]['mu']["NNPDF30_nnlo_as_0118_44"] = {'bb': 0.130797,'cc': 0.135398,'c': 0.206254,'l': 0.527551}
frac[5]['mu']["NNPDF30_nnlo_as_0118_44"] = {'bb': 0.140869,'cc': 0.148943,'c': 0.201634,'l': 0.508553}
# NNPDF30_nnlo_as_0118_45 
frac[2]['el']["NNPDF30_nnlo_as_0118_45"] = {'bb': 0.094612,'cc': 0.064914,'c': 0.207497,'l': 0.632977}
frac[3]['el']["NNPDF30_nnlo_as_0118_45"] = {'bb': 0.117918,'cc': 0.099607,'c': 0.217845,'l': 0.564630}
frac[4]['el']["NNPDF30_nnlo_as_0118_45"] = {'bb': 0.141082,'cc': 0.138384,'c': 0.215063,'l': 0.505471}
frac[5]['el']["NNPDF30_nnlo_as_0118_45"] = {'bb': 0.149387,'cc': 0.151624,'c': 0.210536,'l': 0.488453}
frac[2]['mu']["NNPDF30_nnlo_as_0118_45"] = {'bb': 0.084807,'cc': 0.064098,'c': 0.206472,'l': 0.644623}
frac[3]['mu']["NNPDF30_nnlo_as_0118_45"] = {'bb': 0.107564,'cc': 0.098015,'c': 0.215132,'l': 0.579289}
frac[4]['mu']["NNPDF30_nnlo_as_0118_45"] = {'bb': 0.131094,'cc': 0.134327,'c': 0.207506,'l': 0.527073}
frac[5]['mu']["NNPDF30_nnlo_as_0118_45"] = {'bb': 0.141169,'cc': 0.147959,'c': 0.203017,'l': 0.507855}
# NNPDF30_nnlo_as_0118_46 
frac[2]['el']["NNPDF30_nnlo_as_0118_46"] = {'bb': 0.095085,'cc': 0.066295,'c': 0.209172,'l': 0.629449}
frac[3]['el']["NNPDF30_nnlo_as_0118_46"] = {'bb': 0.118194,'cc': 0.101678,'c': 0.218982,'l': 0.561146}
frac[4]['el']["NNPDF30_nnlo_as_0118_46"] = {'bb': 0.140872,'cc': 0.140725,'c': 0.214642,'l': 0.503761}
frac[5]['el']["NNPDF30_nnlo_as_0118_46"] = {'bb': 0.149187,'cc': 0.153963,'c': 0.209164,'l': 0.487687}
frac[2]['mu']["NNPDF30_nnlo_as_0118_46"] = {'bb': 0.083573,'cc': 0.063871,'c': 0.202624,'l': 0.649931}
frac[3]['mu']["NNPDF30_nnlo_as_0118_46"] = {'bb': 0.107570,'cc': 0.099325,'c': 0.214371,'l': 0.578733}
frac[4]['mu']["NNPDF30_nnlo_as_0118_46"] = {'bb': 0.130933,'cc': 0.136022,'c': 0.205913,'l': 0.527132}
frac[5]['mu']["NNPDF30_nnlo_as_0118_46"] = {'bb': 0.140913,'cc': 0.149549,'c': 0.201252,'l': 0.508286}
# NNPDF30_nnlo_as_0118_47 
frac[2]['el']["NNPDF30_nnlo_as_0118_47"] = {'bb': 0.095805,'cc': 0.066226,'c': 0.210896,'l': 0.627073}
frac[3]['el']["NNPDF30_nnlo_as_0118_47"] = {'bb': 0.118811,'cc': 0.101388,'c': 0.219797,'l': 0.560005}
frac[4]['el']["NNPDF30_nnlo_as_0118_47"] = {'bb': 0.141428,'cc': 0.140441,'c': 0.214904,'l': 0.503228}
frac[5]['el']["NNPDF30_nnlo_as_0118_47"] = {'bb': 0.149637,'cc': 0.153697,'c': 0.209404,'l': 0.487262}
frac[2]['mu']["NNPDF30_nnlo_as_0118_47"] = {'bb': 0.084224,'cc': 0.063785,'c': 0.204087,'l': 0.647904}
frac[3]['mu']["NNPDF30_nnlo_as_0118_47"] = {'bb': 0.107996,'cc': 0.099035,'c': 0.215158,'l': 0.577811}
frac[4]['mu']["NNPDF30_nnlo_as_0118_47"] = {'bb': 0.131164,'cc': 0.135791,'c': 0.206422,'l': 0.526623}
frac[5]['mu']["NNPDF30_nnlo_as_0118_47"] = {'bb': 0.141113,'cc': 0.149351,'c': 0.201564,'l': 0.507971}
# NNPDF30_nnlo_as_0118_48 
frac[2]['el']["NNPDF30_nnlo_as_0118_48"] = {'bb': 0.095213,'cc': 0.065713,'c': 0.209024,'l': 0.630051}
frac[3]['el']["NNPDF30_nnlo_as_0118_48"] = {'bb': 0.118413,'cc': 0.100870,'c': 0.218218,'l': 0.562499}
frac[4]['el']["NNPDF30_nnlo_as_0118_48"] = {'bb': 0.141143,'cc': 0.139945,'c': 0.213987,'l': 0.504925}
frac[5]['el']["NNPDF30_nnlo_as_0118_48"] = {'bb': 0.149453,'cc': 0.153277,'c': 0.208512,'l': 0.488759}
frac[2]['mu']["NNPDF30_nnlo_as_0118_48"] = {'bb': 0.083810,'cc': 0.063743,'c': 0.203945,'l': 0.648502}
frac[3]['mu']["NNPDF30_nnlo_as_0118_48"] = {'bb': 0.107401,'cc': 0.098767,'c': 0.214165,'l': 0.579667}
frac[4]['mu']["NNPDF30_nnlo_as_0118_48"] = {'bb': 0.133227,'cc': 0.137837,'c': 0.209261,'l': 0.519675}
frac[5]['mu']["NNPDF30_nnlo_as_0118_48"] = {'bb': 0.142619,'cc': 0.150808,'c': 0.203407,'l': 0.503166}
# NNPDF30_nnlo_as_0118_49 
frac[2]['el']["NNPDF30_nnlo_as_0118_49"] = {'bb': -1.559287,'cc': 0.182561,'c': 0.590017,'l': 1.786709}
frac[3]['el']["NNPDF30_nnlo_as_0118_49"] = {'bb': 2.810581,'cc': -0.204193,'c': -0.450176,'l': -1.156212}
frac[4]['el']["NNPDF30_nnlo_as_0118_49"] = {'bb': 2.027711,'cc': -0.165945,'c': -0.258443,'l': -0.603323}
frac[5]['el']["NNPDF30_nnlo_as_0118_49"] = {'bb': 2.208094,'cc': -0.215938,'c': -0.298532,'l': -0.693624}
frac[2]['mu']["NNPDF30_nnlo_as_0118_49"] = {'bb': 0.083566,'cc': 0.062813,'c': 0.204251,'l': 0.649371}
frac[3]['mu']["NNPDF30_nnlo_as_0118_49"] = {'bb': 0.107626,'cc': 0.098009,'c': 0.216820,'l': 0.577546}
frac[4]['mu']["NNPDF30_nnlo_as_0118_49"] = {'bb': 0.131033,'cc': 0.134393,'c': 0.208255,'l': 0.526319}
frac[5]['mu']["NNPDF30_nnlo_as_0118_49"] = {'bb': 0.141028,'cc': 0.147957,'c': 0.203434,'l': 0.507581}
# NNPDF30_nnlo_as_0118_50 
frac[2]['el']["NNPDF30_nnlo_as_0118_50"] = {'bb': 0.095296,'cc': 0.066017,'c': 0.208305,'l': 0.630382}
frac[3]['el']["NNPDF30_nnlo_as_0118_50"] = {'bb': 0.118294,'cc': 0.101437,'c': 0.217793,'l': 0.562476}
frac[4]['el']["NNPDF30_nnlo_as_0118_50"] = {'bb': 0.140891,'cc': 0.140642,'c': 0.213382,'l': 0.505086}
frac[5]['el']["NNPDF30_nnlo_as_0118_50"] = {'bb': 0.149114,'cc': 0.153969,'c': 0.207895,'l': 0.489023}
frac[2]['mu']["NNPDF30_nnlo_as_0118_50"] = {'bb': 0.083429,'cc': 0.063718,'c': 0.201497,'l': 0.651356}
frac[3]['mu']["NNPDF30_nnlo_as_0118_50"] = {'bb': 0.107544,'cc': 0.099406,'c': 0.213629,'l': 0.579421}
frac[4]['mu']["NNPDF30_nnlo_as_0118_50"] = {'bb': 0.130871,'cc': 0.136274,'c': 0.205124,'l': 0.527731}
frac[5]['mu']["NNPDF30_nnlo_as_0118_50"] = {'bb': 0.140836,'cc': 0.149820,'c': 0.200514,'l': 0.508830}
# NNPDF30_nnlo_as_0118_51 
frac[2]['el']["NNPDF30_nnlo_as_0118_51"] = {'bb': 0.095254,'cc': 0.065474,'c': 0.210674,'l': 0.628598}
frac[3]['el']["NNPDF30_nnlo_as_0118_51"] = {'bb': 0.118428,'cc': 0.100717,'c': 0.220032,'l': 0.560824}
frac[4]['el']["NNPDF30_nnlo_as_0118_51"] = {'bb': 0.141093,'cc': 0.139771,'c': 0.215220,'l': 0.503916}
frac[5]['el']["NNPDF30_nnlo_as_0118_51"] = {'bb': 0.149513,'cc': 0.153162,'c': 0.208900,'l': 0.488425}
frac[2]['mu']["NNPDF30_nnlo_as_0118_51"] = {'bb': 0.083499,'cc': 0.063252,'c': 0.204500,'l': 0.648749}
frac[3]['mu']["NNPDF30_nnlo_as_0118_51"] = {'bb': 0.107629,'cc': 0.098744,'c': 0.216072,'l': 0.577555}
frac[4]['mu']["NNPDF30_nnlo_as_0118_51"] = {'bb': 0.130978,'cc': 0.135310,'c': 0.207122,'l': 0.526590}
frac[5]['mu']["NNPDF30_nnlo_as_0118_51"] = {'bb': 0.140952,'cc': 0.148880,'c': 0.202182,'l': 0.507986}
# NNPDF30_nnlo_as_0118_52 
frac[2]['el']["NNPDF30_nnlo_as_0118_52"] = {'bb': 0.095472,'cc': 0.065327,'c': 0.211553,'l': 0.627648}
frac[3]['el']["NNPDF30_nnlo_as_0118_52"] = {'bb': 0.118680,'cc': 0.100263,'c': 0.219988,'l': 0.561069}
frac[4]['el']["NNPDF30_nnlo_as_0118_52"] = {'bb': 0.141474,'cc': 0.139200,'c': 0.215121,'l': 0.504205}
frac[5]['el']["NNPDF30_nnlo_as_0118_52"] = {'bb': 0.149763,'cc': 0.152530,'c': 0.209147,'l': 0.488561}
frac[2]['mu']["NNPDF30_nnlo_as_0118_52"] = {'bb': 0.083942,'cc': 0.063349,'c': 0.206232,'l': 0.646477}
frac[3]['mu']["NNPDF30_nnlo_as_0118_52"] = {'bb': 0.107712,'cc': 0.098140,'c': 0.215799,'l': 0.578350}
frac[4]['mu']["NNPDF30_nnlo_as_0118_52"] = {'bb': 0.131114,'cc': 0.134551,'c': 0.206536,'l': 0.527798}
frac[5]['mu']["NNPDF30_nnlo_as_0118_52"] = {'bb': 0.141138,'cc': 0.148126,'c': 0.201726,'l': 0.509009}
# NNPDF30_nnlo_as_0118_53 
frac[2]['el']["NNPDF30_nnlo_as_0118_53"] = {'bb': 0.095485,'cc': 0.065338,'c': 0.209920,'l': 0.629258}
frac[3]['el']["NNPDF30_nnlo_as_0118_53"] = {'bb': 0.118706,'cc': 0.099998,'c': 0.219294,'l': 0.562002}
frac[4]['el']["NNPDF30_nnlo_as_0118_53"] = {'bb': 0.141625,'cc': 0.138641,'c': 0.215397,'l': 0.504337}
frac[5]['el']["NNPDF30_nnlo_as_0118_53"] = {'bb': 0.149887,'cc': 0.151921,'c': 0.210575,'l': 0.487618}
frac[2]['mu']["NNPDF30_nnlo_as_0118_53"] = {'bb': 0.084822,'cc': 0.063924,'c': 0.206599,'l': 0.644655}
frac[3]['mu']["NNPDF30_nnlo_as_0118_53"] = {'bb': 0.107630,'cc': 0.097908,'c': 0.214980,'l': 0.579482}
frac[4]['mu']["NNPDF30_nnlo_as_0118_53"] = {'bb': 0.131152,'cc': 0.134172,'c': 0.207129,'l': 0.527546}
frac[5]['mu']["NNPDF30_nnlo_as_0118_53"] = {'bb': 0.141222,'cc': 0.147745,'c': 0.202691,'l': 0.508342}
# NNPDF30_nnlo_as_0118_54 
frac[2]['el']["NNPDF30_nnlo_as_0118_54"] = {'bb': 0.095809,'cc': 0.064792,'c': 0.207094,'l': 0.632306}
frac[3]['el']["NNPDF30_nnlo_as_0118_54"] = {'bb': 0.118615,'cc': 0.100435,'c': 0.218708,'l': 0.562241}
frac[4]['el']["NNPDF30_nnlo_as_0118_54"] = {'bb': 0.141082,'cc': 0.140117,'c': 0.214453,'l': 0.504349}
frac[5]['el']["NNPDF30_nnlo_as_0118_54"] = {'bb': 0.149977,'cc': 0.154631,'c': 0.208092,'l': 0.487300}
frac[2]['mu']["NNPDF30_nnlo_as_0118_54"] = {'bb': 0.083124,'cc': 0.064699,'c': 0.207755,'l': 0.644422}
frac[3]['mu']["NNPDF30_nnlo_as_0118_54"] = {'bb': 0.105541,'cc': 0.101412,'c': 0.221799,'l': 0.571248}
frac[4]['mu']["NNPDF30_nnlo_as_0118_54"] = {'bb': 0.128622,'cc': 0.139043,'c': 0.214969,'l': 0.517367}
frac[5]['mu']["NNPDF30_nnlo_as_0118_54"] = {'bb': 0.138437,'cc': 0.151992,'c': 0.209773,'l': 0.499798}
# NNPDF30_nnlo_as_0118_55 
frac[2]['el']["NNPDF30_nnlo_as_0118_55"] = {'bb': 0.095336,'cc': 0.065604,'c': 0.210175,'l': 0.628885}
frac[3]['el']["NNPDF30_nnlo_as_0118_55"] = {'bb': 0.118554,'cc': 0.100716,'c': 0.219960,'l': 0.560771}
frac[4]['el']["NNPDF30_nnlo_as_0118_55"] = {'bb': 0.141099,'cc': 0.139551,'c': 0.215856,'l': 0.503494}
frac[5]['el']["NNPDF30_nnlo_as_0118_55"] = {'bb': 0.149357,'cc': 0.152811,'c': 0.210788,'l': 0.487044}
frac[2]['mu']["NNPDF30_nnlo_as_0118_55"] = {'bb': 0.083881,'cc': 0.063551,'c': 0.204688,'l': 0.647880}
frac[3]['mu']["NNPDF30_nnlo_as_0118_55"] = {'bb': 0.107652,'cc': 0.098580,'c': 0.216041,'l': 0.577727}
frac[4]['mu']["NNPDF30_nnlo_as_0118_55"] = {'bb': 0.131022,'cc': 0.135189,'c': 0.207633,'l': 0.526156}
frac[5]['mu']["NNPDF30_nnlo_as_0118_55"] = {'bb': 0.141074,'cc': 0.148755,'c': 0.202902,'l': 0.507270}
# NNPDF30_nnlo_as_0118_56 
frac[2]['el']["NNPDF30_nnlo_as_0118_56"] = {'bb': 0.091344,'cc': 0.063277,'c': 0.199953,'l': 0.645426}
frac[3]['el']["NNPDF30_nnlo_as_0118_56"] = {'bb': 0.114795,'cc': 0.098054,'c': 0.212539,'l': 0.574612}
frac[4]['el']["NNPDF30_nnlo_as_0118_56"] = {'bb': 0.138981,'cc': 0.137950,'c': 0.212344,'l': 0.510725}
frac[5]['el']["NNPDF30_nnlo_as_0118_56"] = {'bb': 0.147597,'cc': 0.151473,'c': 0.207189,'l': 0.493740}
frac[2]['mu']["NNPDF30_nnlo_as_0118_56"] = {'bb': 0.083403,'cc': 0.064133,'c': 0.203563,'l': 0.648901}
frac[3]['mu']["NNPDF30_nnlo_as_0118_56"] = {'bb': 0.106377,'cc': 0.098733,'c': 0.214195,'l': 0.580696}
frac[4]['mu']["NNPDF30_nnlo_as_0118_56"] = {'bb': 0.129979,'cc': 0.134989,'c': 0.206558,'l': 0.528474}
frac[5]['mu']["NNPDF30_nnlo_as_0118_56"] = {'bb': 0.140038,'cc': 0.148548,'c': 0.201966,'l': 0.509449}
# NNPDF30_nnlo_as_0118_57 
frac[2]['el']["NNPDF30_nnlo_as_0118_57"] = {'bb': 0.095543,'cc': 0.065537,'c': 0.210661,'l': 0.628259}
frac[3]['el']["NNPDF30_nnlo_as_0118_57"] = {'bb': 0.118914,'cc': 0.100519,'c': 0.220048,'l': 0.560520}
frac[4]['el']["NNPDF30_nnlo_as_0118_57"] = {'bb': 0.142009,'cc': 0.139652,'c': 0.216172,'l': 0.502167}
frac[5]['el']["NNPDF30_nnlo_as_0118_57"] = {'bb': 0.150101,'cc': 0.152838,'c': 0.210620,'l': 0.486441}
frac[2]['mu']["NNPDF30_nnlo_as_0118_57"] = {'bb': 0.084319,'cc': 0.063625,'c': 0.206064,'l': 0.645991}
frac[3]['mu']["NNPDF30_nnlo_as_0118_57"] = {'bb': 0.107760,'cc': 0.098182,'c': 0.215313,'l': 0.578746}
frac[4]['mu']["NNPDF30_nnlo_as_0118_57"] = {'bb': 0.131137,'cc': 0.134661,'c': 0.206709,'l': 0.527492}
frac[5]['mu']["NNPDF30_nnlo_as_0118_57"] = {'bb': 0.141205,'cc': 0.148270,'c': 0.201986,'l': 0.508540}
# NNPDF30_nnlo_as_0118_58 
frac[2]['el']["NNPDF30_nnlo_as_0118_58"] = {'bb': 0.096486,'cc': 0.066405,'c': 0.213090,'l': 0.624019}
frac[3]['el']["NNPDF30_nnlo_as_0118_58"] = {'bb': 0.119586,'cc': 0.101647,'c': 0.222352,'l': 0.556415}
frac[4]['el']["NNPDF30_nnlo_as_0118_58"] = {'bb': 0.141968,'cc': 0.140308,'c': 0.216917,'l': 0.500807}
frac[5]['el']["NNPDF30_nnlo_as_0118_58"] = {'bb': 0.150194,'cc': 0.153351,'c': 0.211540,'l': 0.484915}
frac[2]['mu']["NNPDF30_nnlo_as_0118_58"] = {'bb': 0.084119,'cc': 0.063739,'c': 0.205100,'l': 0.647042}
frac[3]['mu']["NNPDF30_nnlo_as_0118_58"] = {'bb': 0.107739,'cc': 0.098924,'c': 0.216240,'l': 0.577098}
frac[4]['mu']["NNPDF30_nnlo_as_0118_58"] = {'bb': 0.130971,'cc': 0.135700,'c': 0.207933,'l': 0.525396}
frac[5]['mu']["NNPDF30_nnlo_as_0118_58"] = {'bb': 0.141001,'cc': 0.149278,'c': 0.203079,'l': 0.506642}
# NNPDF30_nnlo_as_0118_59 
frac[2]['el']["NNPDF30_nnlo_as_0118_59"] = {'bb': 0.095215,'cc': 0.065645,'c': 0.209103,'l': 0.630038}
frac[3]['el']["NNPDF30_nnlo_as_0118_59"] = {'bb': 0.118416,'cc': 0.100714,'c': 0.219437,'l': 0.561433}
frac[4]['el']["NNPDF30_nnlo_as_0118_59"] = {'bb': 0.141037,'cc': 0.139577,'c': 0.215747,'l': 0.503639}
frac[5]['el']["NNPDF30_nnlo_as_0118_59"] = {'bb': 0.149339,'cc': 0.152818,'c': 0.210559,'l': 0.487285}
frac[2]['mu']["NNPDF30_nnlo_as_0118_59"] = {'bb': 0.083736,'cc': 0.063647,'c': 0.204297,'l': 0.648320}
frac[3]['mu']["NNPDF30_nnlo_as_0118_59"] = {'bb': 0.107487,'cc': 0.098686,'c': 0.215643,'l': 0.578184}
frac[4]['mu']["NNPDF30_nnlo_as_0118_59"] = {'bb': 0.130919,'cc': 0.135166,'c': 0.207627,'l': 0.526288}
frac[5]['mu']["NNPDF30_nnlo_as_0118_59"] = {'bb': 0.140968,'cc': 0.148604,'c': 0.203028,'l': 0.507400}
# NNPDF30_nnlo_as_0118_60 
frac[2]['el']["NNPDF30_nnlo_as_0118_60"] = {'bb': 0.095436,'cc': 0.065684,'c': 0.209640,'l': 0.629240}
frac[3]['el']["NNPDF30_nnlo_as_0118_60"] = {'bb': 0.118604,'cc': 0.100718,'c': 0.218761,'l': 0.561917}
frac[4]['el']["NNPDF30_nnlo_as_0118_60"] = {'bb': 0.141297,'cc': 0.139676,'c': 0.214480,'l': 0.504547}
frac[5]['el']["NNPDF30_nnlo_as_0118_60"] = {'bb': 0.149672,'cc': 0.152955,'c': 0.209222,'l': 0.488151}
frac[2]['mu']["NNPDF30_nnlo_as_0118_60"] = {'bb': 0.057475,'cc': 0.065353,'c': 0.209591,'l': 0.667580}
frac[3]['mu']["NNPDF30_nnlo_as_0118_60"] = {'bb': 0.082765,'cc': 0.101491,'c': 0.220645,'l': 0.595099}
frac[4]['mu']["NNPDF30_nnlo_as_0118_60"] = {'bb': 0.115762,'cc': 0.138031,'c': 0.209431,'l': 0.536776}
frac[5]['mu']["NNPDF30_nnlo_as_0118_60"] = {'bb': 0.128692,'cc': 0.151767,'c': 0.203879,'l': 0.515662}
# NNPDF30_nnlo_as_0118_61 
frac[2]['el']["NNPDF30_nnlo_as_0118_61"] = {'bb': 0.095647,'cc': 0.064999,'c': 0.209506,'l': 0.629848}
frac[3]['el']["NNPDF30_nnlo_as_0118_61"] = {'bb': 0.118854,'cc': 0.099486,'c': 0.219297,'l': 0.562364}
frac[4]['el']["NNPDF30_nnlo_as_0118_61"] = {'bb': 0.141606,'cc': 0.137759,'c': 0.215729,'l': 0.504905}
frac[5]['el']["NNPDF30_nnlo_as_0118_61"] = {'bb': 0.149887,'cc': 0.150972,'c': 0.211082,'l': 0.488060}
frac[2]['mu']["NNPDF30_nnlo_as_0118_61"] = {'bb': 0.084622,'cc': 0.063623,'c': 0.206602,'l': 0.645153}
frac[3]['mu']["NNPDF30_nnlo_as_0118_61"] = {'bb': 0.107735,'cc': 0.097405,'c': 0.215421,'l': 0.579439}
frac[4]['mu']["NNPDF30_nnlo_as_0118_61"] = {'bb': 0.131278,'cc': 0.133478,'c': 0.207555,'l': 0.527689}
frac[5]['mu']["NNPDF30_nnlo_as_0118_61"] = {'bb': 0.141360,'cc': 0.146988,'c': 0.203227,'l': 0.508425}
# NNPDF30_nnlo_as_0118_62 
frac[2]['el']["NNPDF30_nnlo_as_0118_62"] = {'bb': 0.096390,'cc': 0.064545,'c': 0.210333,'l': 0.628732}
frac[3]['el']["NNPDF30_nnlo_as_0118_62"] = {'bb': 0.119625,'cc': 0.099169,'c': 0.219430,'l': 0.561776}
frac[4]['el']["NNPDF30_nnlo_as_0118_62"] = {'bb': 0.142282,'cc': 0.137742,'c': 0.215678,'l': 0.504299}
frac[5]['el']["NNPDF30_nnlo_as_0118_62"] = {'bb': 0.150516,'cc': 0.151129,'c': 0.210479,'l': 0.487876}
frac[2]['mu']["NNPDF30_nnlo_as_0118_62"] = {'bb': 0.084478,'cc': 0.062365,'c': 0.204636,'l': 0.648521}
frac[3]['mu']["NNPDF30_nnlo_as_0118_62"] = {'bb': 0.106401,'cc': 0.095168,'c': 0.211241,'l': 0.587189}
frac[4]['mu']["NNPDF30_nnlo_as_0118_62"] = {'bb': 0.126598,'cc': 0.128264,'c': 0.199394,'l': 0.545743}
frac[5]['mu']["NNPDF30_nnlo_as_0118_62"] = {'bb': 0.135656,'cc': 0.140781,'c': 0.194400,'l': 0.529164}
# NNPDF30_nnlo_as_0118_63 
frac[2]['el']["NNPDF30_nnlo_as_0118_63"] = {'bb': 0.095250,'cc': 0.065055,'c': 0.208268,'l': 0.631427}
frac[3]['el']["NNPDF30_nnlo_as_0118_63"] = {'bb': 0.118559,'cc': 0.099982,'c': 0.218843,'l': 0.562616}
frac[4]['el']["NNPDF30_nnlo_as_0118_63"] = {'bb': 0.141304,'cc': 0.138666,'c': 0.215508,'l': 0.504522}
frac[5]['el']["NNPDF30_nnlo_as_0118_63"] = {'bb': 0.149609,'cc': 0.151929,'c': 0.210390,'l': 0.488071}
frac[2]['mu']["NNPDF30_nnlo_as_0118_63"] = {'bb': 0.083362,'cc': 0.062819,'c': 0.202966,'l': 0.650853}
frac[3]['mu']["NNPDF30_nnlo_as_0118_63"] = {'bb': 0.107615,'cc': 0.098047,'c': 0.215280,'l': 0.579058}
frac[4]['mu']["NNPDF30_nnlo_as_0118_63"] = {'bb': 0.131096,'cc': 0.134363,'c': 0.207582,'l': 0.526958}
frac[5]['mu']["NNPDF30_nnlo_as_0118_63"] = {'bb': 0.141114,'cc': 0.147882,'c': 0.203179,'l': 0.507825}
# NNPDF30_nnlo_as_0118_64 
frac[2]['el']["NNPDF30_nnlo_as_0118_64"] = {'bb': 0.095422,'cc': 0.065817,'c': 0.210993,'l': 0.627768}
frac[3]['el']["NNPDF30_nnlo_as_0118_64"] = {'bb': 0.118622,'cc': 0.100975,'c': 0.219989,'l': 0.560415}
frac[4]['el']["NNPDF30_nnlo_as_0118_64"] = {'bb': 0.141355,'cc': 0.140062,'c': 0.215454,'l': 0.503129}
frac[5]['el']["NNPDF30_nnlo_as_0118_64"] = {'bb': 0.149629,'cc': 0.153384,'c': 0.209472,'l': 0.487516}
frac[2]['mu']["NNPDF30_nnlo_as_0118_64"] = {'bb': 0.083535,'cc': 0.063424,'c': 0.204383,'l': 0.648658}
frac[3]['mu']["NNPDF30_nnlo_as_0118_64"] = {'bb': 0.107790,'cc': 0.098684,'c': 0.215636,'l': 0.577890}
frac[4]['mu']["NNPDF30_nnlo_as_0118_64"] = {'bb': 0.131207,'cc': 0.135124,'c': 0.206550,'l': 0.527119}
frac[5]['mu']["NNPDF30_nnlo_as_0118_64"] = {'bb': 0.141234,'cc': 0.148660,'c': 0.201675,'l': 0.508431}
# NNPDF30_nnlo_as_0118_65 
frac[2]['el']["NNPDF30_nnlo_as_0118_65"] = {'bb': 0.095391,'cc': 0.064843,'c': 0.211729,'l': 0.628037}
frac[3]['el']["NNPDF30_nnlo_as_0118_65"] = {'bb': 0.118636,'cc': 0.099746,'c': 0.220851,'l': 0.560767}
frac[4]['el']["NNPDF30_nnlo_as_0118_65"] = {'bb': 0.141402,'cc': 0.138697,'c': 0.216033,'l': 0.503868}
frac[5]['el']["NNPDF30_nnlo_as_0118_65"] = {'bb': 0.149654,'cc': 0.152000,'c': 0.210536,'l': 0.487810}
frac[2]['mu']["NNPDF30_nnlo_as_0118_65"] = {'bb': 0.084096,'cc': 0.062773,'c': 0.205631,'l': 0.647499}
frac[3]['mu']["NNPDF30_nnlo_as_0118_65"] = {'bb': 0.108273,'cc': 0.097807,'c': 0.216843,'l': 0.577077}
frac[4]['mu']["NNPDF30_nnlo_as_0118_65"] = {'bb': 0.131401,'cc': 0.134024,'c': 0.207244,'l': 0.527331}
frac[5]['mu']["NNPDF30_nnlo_as_0118_65"] = {'bb': 0.141416,'cc': 0.147814,'c': 0.202422,'l': 0.508349}
# NNPDF30_nnlo_as_0118_66 
frac[2]['el']["NNPDF30_nnlo_as_0118_66"] = {'bb': 0.095510,'cc': 0.065809,'c': 0.209639,'l': 0.629042}
frac[3]['el']["NNPDF30_nnlo_as_0118_66"] = {'bb': 0.118638,'cc': 0.100818,'c': 0.219587,'l': 0.560956}
frac[4]['el']["NNPDF30_nnlo_as_0118_66"] = {'bb': 0.141319,'cc': 0.139773,'c': 0.215796,'l': 0.503112}
frac[5]['el']["NNPDF30_nnlo_as_0118_66"] = {'bb': 0.149664,'cc': 0.152973,'c': 0.210556,'l': 0.486806}
frac[2]['mu']["NNPDF30_nnlo_as_0118_66"] = {'bb': 0.084646,'cc': 0.064236,'c': 0.205902,'l': 0.645216}
frac[3]['mu']["NNPDF30_nnlo_as_0118_66"] = {'bb': 0.107503,'cc': 0.098491,'c': 0.215252,'l': 0.578755}
frac[4]['mu']["NNPDF30_nnlo_as_0118_66"] = {'bb': 0.131037,'cc': 0.135052,'c': 0.207473,'l': 0.526438}
frac[5]['mu']["NNPDF30_nnlo_as_0118_66"] = {'bb': 0.141090,'cc': 0.148582,'c': 0.202858,'l': 0.507470}
# NNPDF30_nnlo_as_0118_67 
frac[2]['el']["NNPDF30_nnlo_as_0118_67"] = {'bb': 0.095540,'cc': 0.065312,'c': 0.208340,'l': 0.630807}
frac[3]['el']["NNPDF30_nnlo_as_0118_67"] = {'bb': 0.119162,'cc': 0.099856,'c': 0.216123,'l': 0.564859}
frac[4]['el']["NNPDF30_nnlo_as_0118_67"] = {'bb': 0.142023,'cc': 0.138689,'c': 0.211715,'l': 0.507573}
frac[5]['el']["NNPDF30_nnlo_as_0118_67"] = {'bb': 0.150321,'cc': 0.152235,'c': 0.205934,'l': 0.491509}
frac[2]['mu']["NNPDF30_nnlo_as_0118_67"] = {'bb': 0.083563,'cc': 0.063690,'c': 0.203806,'l': 0.648941}
frac[3]['mu']["NNPDF30_nnlo_as_0118_67"] = {'bb': 0.107585,'cc': 0.099172,'c': 0.214703,'l': 0.578540}
frac[4]['mu']["NNPDF30_nnlo_as_0118_67"] = {'bb': 0.130783,'cc': 0.135900,'c': 0.205857,'l': 0.527460}
frac[5]['mu']["NNPDF30_nnlo_as_0118_67"] = {'bb': 0.140870,'cc': 0.148707,'c': 0.201235,'l': 0.509189}
# NNPDF30_nnlo_as_0118_68 
frac[2]['el']["NNPDF30_nnlo_as_0118_68"] = {'bb': 0.095118,'cc': 0.065352,'c': 0.209705,'l': 0.629824}
frac[3]['el']["NNPDF30_nnlo_as_0118_68"] = {'bb': 0.118356,'cc': 0.100277,'c': 0.219317,'l': 0.562050}
frac[4]['el']["NNPDF30_nnlo_as_0118_68"] = {'bb': 0.141186,'cc': 0.139062,'c': 0.215089,'l': 0.504663}
frac[5]['el']["NNPDF30_nnlo_as_0118_68"] = {'bb': 0.149366,'cc': 0.152331,'c': 0.210142,'l': 0.488162}
frac[2]['mu']["NNPDF30_nnlo_as_0118_68"] = {'bb': 0.083884,'cc': 0.063464,'c': 0.204453,'l': 0.648199}
frac[3]['mu']["NNPDF30_nnlo_as_0118_68"] = {'bb': 0.107617,'cc': 0.098407,'c': 0.215616,'l': 0.578360}
frac[4]['mu']["NNPDF30_nnlo_as_0118_68"] = {'bb': 0.130996,'cc': 0.134911,'c': 0.207112,'l': 0.526981}
frac[5]['mu']["NNPDF30_nnlo_as_0118_68"] = {'bb': 0.141016,'cc': 0.148466,'c': 0.202400,'l': 0.508117}
# NNPDF30_nnlo_as_0118_69 
frac[2]['el']["NNPDF30_nnlo_as_0118_69"] = {'bb': 0.095401,'cc': 0.065572,'c': 0.210912,'l': 0.628115}
frac[3]['el']["NNPDF30_nnlo_as_0118_69"] = {'bb': 0.118547,'cc': 0.100568,'c': 0.220469,'l': 0.560416}
frac[4]['el']["NNPDF30_nnlo_as_0118_69"] = {'bb': 0.141213,'cc': 0.139440,'c': 0.216200,'l': 0.503147}
frac[5]['el']["NNPDF30_nnlo_as_0118_69"] = {'bb': 0.149574,'cc': 0.152709,'c': 0.210775,'l': 0.486941}
frac[2]['mu']["NNPDF30_nnlo_as_0118_69"] = {'bb': 0.084342,'cc': 0.063777,'c': 0.206219,'l': 0.645663}
frac[3]['mu']["NNPDF30_nnlo_as_0118_69"] = {'bb': 0.107744,'cc': 0.098210,'c': 0.216081,'l': 0.577965}
frac[4]['mu']["NNPDF30_nnlo_as_0118_69"] = {'bb': 0.131247,'cc': 0.134621,'c': 0.207456,'l': 0.526676}
frac[5]['mu']["NNPDF30_nnlo_as_0118_69"] = {'bb': 0.141333,'cc': 0.148152,'c': 0.202642,'l': 0.507872}
# NNPDF30_nnlo_as_0118_70 
frac[2]['el']["NNPDF30_nnlo_as_0118_70"] = {'bb': 0.095366,'cc': 0.066130,'c': 0.209364,'l': 0.629140}
frac[3]['el']["NNPDF30_nnlo_as_0118_70"] = {'bb': 0.118449,'cc': 0.101369,'c': 0.218692,'l': 0.561490}
frac[4]['el']["NNPDF30_nnlo_as_0118_70"] = {'bb': 0.141112,'cc': 0.140424,'c': 0.214233,'l': 0.504231}
frac[5]['el']["NNPDF30_nnlo_as_0118_70"] = {'bb': 0.149441,'cc': 0.153723,'c': 0.208682,'l': 0.488154}
frac[2]['mu']["NNPDF30_nnlo_as_0118_70"] = {'bb': 0.084148,'cc': 0.064334,'c': 0.204772,'l': 0.646745}
frac[3]['mu']["NNPDF30_nnlo_as_0118_70"] = {'bb': 0.107593,'cc': 0.099274,'c': 0.214599,'l': 0.578534}
frac[4]['mu']["NNPDF30_nnlo_as_0118_70"] = {'bb': 0.130967,'cc': 0.135996,'c': 0.206112,'l': 0.526926}
frac[5]['mu']["NNPDF30_nnlo_as_0118_70"] = {'bb': 0.140981,'cc': 0.149554,'c': 0.201379,'l': 0.508086}
# NNPDF30_nnlo_as_0118_71 
frac[2]['el']["NNPDF30_nnlo_as_0118_71"] = {'bb': 0.095309,'cc': 0.065109,'c': 0.209302,'l': 0.630279}
frac[3]['el']["NNPDF30_nnlo_as_0118_71"] = {'bb': 0.118642,'cc': 0.099699,'c': 0.218564,'l': 0.563095}
frac[4]['el']["NNPDF30_nnlo_as_0118_71"] = {'bb': 0.141448,'cc': 0.138128,'c': 0.214781,'l': 0.505643}
frac[5]['el']["NNPDF30_nnlo_as_0118_71"] = {'bb': 0.149811,'cc': 0.151444,'c': 0.209384,'l': 0.489361}
frac[2]['mu']["NNPDF30_nnlo_as_0118_71"] = {'bb': 0.083913,'cc': 0.063254,'c': 0.204867,'l': 0.647966}
frac[3]['mu']["NNPDF30_nnlo_as_0118_71"] = {'bb': 0.107585,'cc': 0.097813,'c': 0.214891,'l': 0.579711}
frac[4]['mu']["NNPDF30_nnlo_as_0118_71"] = {'bb': 0.131138,'cc': 0.133864,'c': 0.206649,'l': 0.528349}
frac[5]['mu']["NNPDF30_nnlo_as_0118_71"] = {'bb': 0.141213,'cc': 0.147350,'c': 0.202173,'l': 0.509264}
# NNPDF30_nnlo_as_0118_72 
frac[2]['el']["NNPDF30_nnlo_as_0118_72"] = {'bb': 0.095101,'cc': 0.065873,'c': 0.209244,'l': 0.629781}
frac[3]['el']["NNPDF30_nnlo_as_0118_72"] = {'bb': 0.118312,'cc': 0.101244,'c': 0.219030,'l': 0.561414}
frac[4]['el']["NNPDF30_nnlo_as_0118_72"] = {'bb': 0.141052,'cc': 0.140518,'c': 0.214789,'l': 0.503641}
frac[5]['el']["NNPDF30_nnlo_as_0118_72"] = {'bb': 0.149297,'cc': 0.153777,'c': 0.209244,'l': 0.487682}
frac[2]['mu']["NNPDF30_nnlo_as_0118_72"] = {'bb': 0.083326,'cc': 0.063278,'c': 0.202270,'l': 0.651126}
frac[3]['mu']["NNPDF30_nnlo_as_0118_72"] = {'bb': 0.107653,'cc': 0.099084,'c': 0.214959,'l': 0.578304}
frac[4]['mu']["NNPDF30_nnlo_as_0118_72"] = {'bb': 0.130864,'cc': 0.135876,'c': 0.206499,'l': 0.526761}
frac[5]['mu']["NNPDF30_nnlo_as_0118_72"] = {'bb': 0.140833,'cc': 0.149463,'c': 0.201668,'l': 0.508036}
# NNPDF30_nnlo_as_0118_73 
frac[2]['el']["NNPDF30_nnlo_as_0118_73"] = {'bb': 0.095107,'cc': 0.065563,'c': 0.209628,'l': 0.629702}
frac[3]['el']["NNPDF30_nnlo_as_0118_73"] = {'bb': 0.118251,'cc': 0.100482,'c': 0.218435,'l': 0.562832}
frac[4]['el']["NNPDF30_nnlo_as_0118_73"] = {'bb': 0.140990,'cc': 0.139326,'c': 0.214091,'l': 0.505593}
frac[5]['el']["NNPDF30_nnlo_as_0118_73"] = {'bb': 0.149315,'cc': 0.152670,'c': 0.208798,'l': 0.489216}
frac[2]['mu']["NNPDF30_nnlo_as_0118_73"] = {'bb': 0.084131,'cc': 0.063863,'c': 0.205317,'l': 0.646688}
frac[3]['mu']["NNPDF30_nnlo_as_0118_73"] = {'bb': 0.107802,'cc': 0.098772,'c': 0.215191,'l': 0.578235}
frac[4]['mu']["NNPDF30_nnlo_as_0118_73"] = {'bb': 0.130827,'cc': 0.135108,'c': 0.206158,'l': 0.527907}
frac[5]['mu']["NNPDF30_nnlo_as_0118_73"] = {'bb': 0.140892,'cc': 0.148698,'c': 0.201553,'l': 0.508857}
# NNPDF30_nnlo_as_0118_74 
frac[2]['el']["NNPDF30_nnlo_as_0118_74"] = {'bb': 0.095127,'cc': 0.066265,'c': 0.212348,'l': 0.626260}
frac[3]['el']["NNPDF30_nnlo_as_0118_74"] = {'bb': 0.118256,'cc': 0.101527,'c': 0.221104,'l': 0.559113}
frac[4]['el']["NNPDF30_nnlo_as_0118_74"] = {'bb': 0.141081,'cc': 0.140085,'c': 0.216103,'l': 0.502731}
frac[5]['el']["NNPDF30_nnlo_as_0118_74"] = {'bb': 0.149429,'cc': 0.153343,'c': 0.210462,'l': 0.486765}
frac[2]['mu']["NNPDF30_nnlo_as_0118_74"] = {'bb': 0.084178,'cc': 0.063782,'c': 0.205293,'l': 0.646747}
frac[3]['mu']["NNPDF30_nnlo_as_0118_74"] = {'bb': 0.107632,'cc': 0.098508,'c': 0.215338,'l': 0.578522}
frac[4]['mu']["NNPDF30_nnlo_as_0118_74"] = {'bb': 0.131081,'cc': 0.135087,'c': 0.206834,'l': 0.526998}
frac[5]['mu']["NNPDF30_nnlo_as_0118_74"] = {'bb': 0.141127,'cc': 0.148653,'c': 0.202126,'l': 0.508094}
# NNPDF30_nnlo_as_0118_75 
frac[2]['el']["NNPDF30_nnlo_as_0118_75"] = {'bb': 0.095414,'cc': 0.065257,'c': 0.209640,'l': 0.629689}
frac[3]['el']["NNPDF30_nnlo_as_0118_75"] = {'bb': 0.118610,'cc': 0.099929,'c': 0.219724,'l': 0.561737}
frac[4]['el']["NNPDF30_nnlo_as_0118_75"] = {'bb': 0.141403,'cc': 0.138475,'c': 0.216262,'l': 0.503860}
frac[5]['el']["NNPDF30_nnlo_as_0118_75"] = {'bb': 0.149716,'cc': 0.151871,'c': 0.211132,'l': 0.487281}
frac[2]['mu']["NNPDF30_nnlo_as_0118_75"] = {'bb': 0.084169,'cc': 0.063377,'c': 0.205244,'l': 0.647209}
frac[3]['mu']["NNPDF30_nnlo_as_0118_75"] = {'bb': 0.107519,'cc': 0.098057,'c': 0.215541,'l': 0.578883}
frac[4]['mu']["NNPDF30_nnlo_as_0118_75"] = {'bb': 0.131153,'cc': 0.133821,'c': 0.207846,'l': 0.527180}
frac[5]['mu']["NNPDF30_nnlo_as_0118_75"] = {'bb': 0.141262,'cc': 0.147320,'c': 0.203350,'l': 0.508068}
# NNPDF30_nnlo_as_0118_76 
frac[2]['el']["NNPDF30_nnlo_as_0118_76"] = {'bb': 0.095756,'cc': 0.065480,'c': 0.210155,'l': 0.628608}
frac[3]['el']["NNPDF30_nnlo_as_0118_76"] = {'bb': 0.119227,'cc': 0.100368,'c': 0.219300,'l': 0.561105}
frac[4]['el']["NNPDF30_nnlo_as_0118_76"] = {'bb': 0.142083,'cc': 0.139133,'c': 0.214912,'l': 0.503871}
frac[5]['el']["NNPDF30_nnlo_as_0118_76"] = {'bb': 0.150259,'cc': 0.152378,'c': 0.209734,'l': 0.487628}
frac[2]['mu']["NNPDF30_nnlo_as_0118_76"] = {'bb': 0.084295,'cc': 0.063647,'c': 0.205548,'l': 0.646510}
frac[3]['mu']["NNPDF30_nnlo_as_0118_76"] = {'bb': 0.107774,'cc': 0.098309,'c': 0.215316,'l': 0.578601}
frac[4]['mu']["NNPDF30_nnlo_as_0118_76"] = {'bb': 0.131121,'cc': 0.134884,'c': 0.206966,'l': 0.527029}
frac[5]['mu']["NNPDF30_nnlo_as_0118_76"] = {'bb': 0.141160,'cc': 0.148470,'c': 0.202315,'l': 0.508054}
# NNPDF30_nnlo_as_0118_77 
frac[2]['el']["NNPDF30_nnlo_as_0118_77"] = {'bb': 0.095551,'cc': 0.065755,'c': 0.210132,'l': 0.628561}
frac[3]['el']["NNPDF30_nnlo_as_0118_77"] = {'bb': 0.118595,'cc': 0.100658,'c': 0.219676,'l': 0.561071}
frac[4]['el']["NNPDF30_nnlo_as_0118_77"] = {'bb': 0.141273,'cc': 0.139059,'c': 0.215498,'l': 0.504170}
frac[5]['el']["NNPDF30_nnlo_as_0118_77"] = {'bb': 0.149567,'cc': 0.152308,'c': 0.210251,'l': 0.487874}
frac[2]['mu']["NNPDF30_nnlo_as_0118_77"] = {'bb': 0.083994,'cc': 0.064336,'c': 0.205879,'l': 0.645791}
frac[3]['mu']["NNPDF30_nnlo_as_0118_77"] = {'bb': 0.107026,'cc': 0.099043,'c': 0.216762,'l': 0.577169}
frac[4]['mu']["NNPDF30_nnlo_as_0118_77"] = {'bb': 0.130396,'cc': 0.135347,'c': 0.208627,'l': 0.525629}
frac[5]['mu']["NNPDF30_nnlo_as_0118_77"] = {'bb': 0.140434,'cc': 0.148779,'c': 0.203907,'l': 0.506880}
# NNPDF30_nnlo_as_0118_78 
frac[2]['el']["NNPDF30_nnlo_as_0118_78"] = {'bb': 0.095230,'cc': 0.066449,'c': 0.209506,'l': 0.628816}
frac[3]['el']["NNPDF30_nnlo_as_0118_78"] = {'bb': 0.118474,'cc': 0.101761,'c': 0.218460,'l': 0.561305}
frac[4]['el']["NNPDF30_nnlo_as_0118_78"] = {'bb': 0.141084,'cc': 0.140884,'c': 0.213837,'l': 0.504195}
frac[5]['el']["NNPDF30_nnlo_as_0118_78"] = {'bb': 0.149426,'cc': 0.154246,'c': 0.207989,'l': 0.488338}
frac[2]['mu']["NNPDF30_nnlo_as_0118_78"] = {'bb': 0.083445,'cc': 0.064298,'c': 0.203379,'l': 0.648878}
frac[3]['mu']["NNPDF30_nnlo_as_0118_78"] = {'bb': 0.107122,'cc': 0.099888,'c': 0.214770,'l': 0.578220}
frac[4]['mu']["NNPDF30_nnlo_as_0118_78"] = {'bb': 0.130516,'cc': 0.136612,'c': 0.205994,'l': 0.526878}
frac[5]['mu']["NNPDF30_nnlo_as_0118_78"] = {'bb': 0.140627,'cc': 0.149667,'c': 0.201292,'l': 0.508415}
# NNPDF30_nnlo_as_0118_79 
frac[2]['el']["NNPDF30_nnlo_as_0118_79"] = {'bb': 0.095468,'cc': 0.065554,'c': 0.209821,'l': 0.629156}
frac[3]['el']["NNPDF30_nnlo_as_0118_79"] = {'bb': 0.118903,'cc': 0.100832,'c': 0.218725,'l': 0.561540}
frac[4]['el']["NNPDF30_nnlo_as_0118_79"] = {'bb': 0.141409,'cc': 0.140029,'c': 0.214169,'l': 0.504392}
frac[5]['el']["NNPDF30_nnlo_as_0118_79"] = {'bb': 0.149709,'cc': 0.153422,'c': 0.208267,'l': 0.488602}
frac[2]['mu']["NNPDF30_nnlo_as_0118_79"] = {'bb': 0.083762,'cc': 0.063334,'c': 0.203640,'l': 0.649264}
frac[3]['mu']["NNPDF30_nnlo_as_0118_79"] = {'bb': 0.107926,'cc': 0.098702,'c': 0.214482,'l': 0.578889}
frac[4]['mu']["NNPDF30_nnlo_as_0118_79"] = {'bb': 0.131171,'cc': 0.135392,'c': 0.205628,'l': 0.527809}
frac[5]['mu']["NNPDF30_nnlo_as_0118_79"] = {'bb': 0.141149,'cc': 0.148997,'c': 0.200960,'l': 0.508895}
# NNPDF30_nnlo_as_0118_80 
frac[2]['el']["NNPDF30_nnlo_as_0118_80"] = {'bb': 0.095458,'cc': 0.065466,'c': 0.210191,'l': 0.628886}
frac[3]['el']["NNPDF30_nnlo_as_0118_80"] = {'bb': 0.118604,'cc': 0.100590,'c': 0.219115,'l': 0.561691}
frac[4]['el']["NNPDF30_nnlo_as_0118_80"] = {'bb': 0.141361,'cc': 0.139571,'c': 0.214766,'l': 0.504301}
frac[5]['el']["NNPDF30_nnlo_as_0118_80"] = {'bb': 0.149666,'cc': 0.152931,'c': 0.209522,'l': 0.487882}
frac[2]['mu']["NNPDF30_nnlo_as_0118_80"] = {'bb': 0.085748,'cc': 0.063524,'c': 0.204856,'l': 0.645872}
frac[3]['mu']["NNPDF30_nnlo_as_0118_80"] = {'bb': 0.108625,'cc': 0.098333,'c': 0.214612,'l': 0.578430}
frac[4]['mu']["NNPDF30_nnlo_as_0118_80"] = {'bb': 0.131561,'cc': 0.135000,'c': 0.206371,'l': 0.527068}
frac[5]['mu']["NNPDF30_nnlo_as_0118_80"] = {'bb': 0.141552,'cc': 0.148638,'c': 0.201775,'l': 0.508035}
# NNPDF30_nnlo_as_0118_81 
frac[2]['el']["NNPDF30_nnlo_as_0118_81"] = {'bb': 0.095350,'cc': 0.065613,'c': 0.210238,'l': 0.628799}
frac[3]['el']["NNPDF30_nnlo_as_0118_81"] = {'bb': 0.118581,'cc': 0.100716,'c': 0.220081,'l': 0.560622}
frac[4]['el']["NNPDF30_nnlo_as_0118_81"] = {'bb': 0.141273,'cc': 0.139698,'c': 0.215808,'l': 0.503222}
frac[5]['el']["NNPDF30_nnlo_as_0118_81"] = {'bb': 0.149572,'cc': 0.152988,'c': 0.210037,'l': 0.487403}
frac[2]['mu']["NNPDF30_nnlo_as_0118_81"] = {'bb': 0.083979,'cc': 0.063917,'c': 0.205939,'l': 0.646165}
frac[3]['mu']["NNPDF30_nnlo_as_0118_81"] = {'bb': 0.107346,'cc': 0.099023,'c': 0.216814,'l': 0.576817}
frac[4]['mu']["NNPDF30_nnlo_as_0118_81"] = {'bb': 0.130619,'cc': 0.135673,'c': 0.208442,'l': 0.525265}
frac[5]['mu']["NNPDF30_nnlo_as_0118_81"] = {'bb': 0.140618,'cc': 0.149148,'c': 0.203527,'l': 0.506707}
# NNPDF30_nnlo_as_0118_82 
frac[2]['el']["NNPDF30_nnlo_as_0118_82"] = {'bb': 0.095366,'cc': 0.066047,'c': 0.209585,'l': 0.629003}
frac[3]['el']["NNPDF30_nnlo_as_0118_82"] = {'bb': 0.118463,'cc': 0.101333,'c': 0.220059,'l': 0.560145}
frac[4]['el']["NNPDF30_nnlo_as_0118_82"] = {'bb': 0.141051,'cc': 0.140205,'c': 0.216196,'l': 0.502548}
frac[5]['el']["NNPDF30_nnlo_as_0118_82"] = {'bb': 0.149398,'cc': 0.153458,'c': 0.210695,'l': 0.486449}
frac[2]['mu']["NNPDF30_nnlo_as_0118_82"] = {'bb': 0.083967,'cc': 0.064008,'c': 0.204264,'l': 0.647762}
frac[3]['mu']["NNPDF30_nnlo_as_0118_82"] = {'bb': 0.107483,'cc': 0.098958,'c': 0.215700,'l': 0.577860}
frac[4]['mu']["NNPDF30_nnlo_as_0118_82"] = {'bb': 0.131033,'cc': 0.135479,'c': 0.207633,'l': 0.525854}
frac[5]['mu']["NNPDF30_nnlo_as_0118_82"] = {'bb': 0.141074,'cc': 0.149025,'c': 0.202894,'l': 0.507007}
# NNPDF30_nnlo_as_0118_83 
frac[2]['el']["NNPDF30_nnlo_as_0118_83"] = {'bb': 0.095473,'cc': 0.065549,'c': 0.209658,'l': 0.629320}
frac[3]['el']["NNPDF30_nnlo_as_0118_83"] = {'bb': 0.118675,'cc': 0.100410,'c': 0.219848,'l': 0.561067}
frac[4]['el']["NNPDF30_nnlo_as_0118_83"] = {'bb': 0.141414,'cc': 0.139072,'c': 0.216361,'l': 0.503153}
frac[5]['el']["NNPDF30_nnlo_as_0118_83"] = {'bb': 0.149735,'cc': 0.152314,'c': 0.211257,'l': 0.486694}
frac[2]['mu']["NNPDF30_nnlo_as_0118_83"] = {'bb': 0.080776,'cc': 0.061199,'c': 0.197044,'l': 0.660981}
frac[3]['mu']["NNPDF30_nnlo_as_0118_83"] = {'bb': 0.110169,'cc': 0.100658,'c': 0.221150,'l': 0.568023}
frac[4]['mu']["NNPDF30_nnlo_as_0118_83"] = {'bb': 0.137876,'cc': 0.141553,'c': 0.218845,'l': 0.501725}
frac[5]['mu']["NNPDF30_nnlo_as_0118_83"] = {'bb': 0.149285,'cc': 0.156631,'c': 0.215215,'l': 0.478869}
# NNPDF30_nnlo_as_0118_84 
frac[2]['el']["NNPDF30_nnlo_as_0118_84"] = {'bb': 0.095294,'cc': 0.065787,'c': 0.209009,'l': 0.629910}
frac[3]['el']["NNPDF30_nnlo_as_0118_84"] = {'bb': 0.118468,'cc': 0.100999,'c': 0.219190,'l': 0.561344}
frac[4]['el']["NNPDF30_nnlo_as_0118_84"] = {'bb': 0.141239,'cc': 0.139999,'c': 0.215111,'l': 0.503650}
frac[5]['el']["NNPDF30_nnlo_as_0118_84"] = {'bb': 0.149476,'cc': 0.153259,'c': 0.209623,'l': 0.487642}
frac[2]['mu']["NNPDF30_nnlo_as_0118_84"] = {'bb': 0.083366,'cc': 0.063451,'c': 0.202352,'l': 0.650831}
frac[3]['mu']["NNPDF30_nnlo_as_0118_84"] = {'bb': 0.107607,'cc': 0.098939,'c': 0.215283,'l': 0.578171}
frac[4]['mu']["NNPDF30_nnlo_as_0118_84"] = {'bb': 0.130970,'cc': 0.135590,'c': 0.206998,'l': 0.526442}
frac[5]['mu']["NNPDF30_nnlo_as_0118_84"] = {'bb': 0.140935,'cc': 0.149117,'c': 0.202268,'l': 0.507680}
# NNPDF30_nnlo_as_0118_85 
frac[2]['el']["NNPDF30_nnlo_as_0118_85"] = {'bb': 0.095384,'cc': 0.065459,'c': 0.209182,'l': 0.629975}
frac[3]['el']["NNPDF30_nnlo_as_0118_85"] = {'bb': 0.118603,'cc': 0.100281,'c': 0.218981,'l': 0.562136}
frac[4]['el']["NNPDF30_nnlo_as_0118_85"] = {'bb': 0.141401,'cc': 0.138991,'c': 0.215347,'l': 0.504261}
frac[5]['el']["NNPDF30_nnlo_as_0118_85"] = {'bb': 0.149756,'cc': 0.152288,'c': 0.209907,'l': 0.488049}
frac[2]['mu']["NNPDF30_nnlo_as_0118_85"] = {'bb': 0.084552,'cc': 0.063902,'c': 0.205629,'l': 0.645917}
frac[3]['mu']["NNPDF30_nnlo_as_0118_85"] = {'bb': 0.107563,'cc': 0.098141,'c': 0.214898,'l': 0.579398}
frac[4]['mu']["NNPDF30_nnlo_as_0118_85"] = {'bb': 0.131080,'cc': 0.134424,'c': 0.206918,'l': 0.527578}
frac[5]['mu']["NNPDF30_nnlo_as_0118_85"] = {'bb': 0.141132,'cc': 0.147949,'c': 0.202440,'l': 0.508479}
# NNPDF30_nnlo_as_0118_86 
frac[2]['el']["NNPDF30_nnlo_as_0118_86"] = {'bb': 0.095541,'cc': 0.065625,'c': 0.211309,'l': 0.627525}
frac[3]['el']["NNPDF30_nnlo_as_0118_86"] = {'bb': 0.118702,'cc': 0.100542,'c': 0.219829,'l': 0.560927}
frac[4]['el']["NNPDF30_nnlo_as_0118_86"] = {'bb': 0.141514,'cc': 0.139201,'c': 0.214668,'l': 0.504617}
frac[5]['el']["NNPDF30_nnlo_as_0118_86"] = {'bb': 0.149894,'cc': 0.152535,'c': 0.208926,'l': 0.488644}
frac[2]['mu']["NNPDF30_nnlo_as_0118_86"] = {'bb': 0.084136,'cc': 0.063706,'c': 0.205940,'l': 0.646218}
frac[3]['mu']["NNPDF30_nnlo_as_0118_86"] = {'bb': 0.107861,'cc': 0.098545,'c': 0.215573,'l': 0.578021}
frac[4]['mu']["NNPDF30_nnlo_as_0118_86"] = {'bb': 0.131242,'cc': 0.135099,'c': 0.206974,'l': 0.526686}
frac[5]['mu']["NNPDF30_nnlo_as_0118_86"] = {'bb': 0.141317,'cc': 0.148754,'c': 0.202135,'l': 0.507794}
# NNPDF30_nnlo_as_0118_87 
frac[2]['el']["NNPDF30_nnlo_as_0118_87"] = {'bb': 0.095300,'cc': 0.065849,'c': 0.209555,'l': 0.629296}
frac[3]['el']["NNPDF30_nnlo_as_0118_87"] = {'bb': 0.118526,'cc': 0.101191,'c': 0.219255,'l': 0.561028}
frac[4]['el']["NNPDF30_nnlo_as_0118_87"] = {'bb': 0.141144,'cc': 0.140314,'c': 0.214633,'l': 0.503909}
frac[5]['el']["NNPDF30_nnlo_as_0118_87"] = {'bb': 0.149483,'cc': 0.153685,'c': 0.208640,'l': 0.488192}
frac[2]['mu']["NNPDF30_nnlo_as_0118_87"] = {'bb': 0.083600,'cc': 0.063627,'c': 0.203638,'l': 0.649135}
frac[3]['mu']["NNPDF30_nnlo_as_0118_87"] = {'bb': 0.107610,'cc': 0.099054,'c': 0.214999,'l': 0.578337}
frac[4]['mu']["NNPDF30_nnlo_as_0118_87"] = {'bb': 0.130973,'cc': 0.135731,'c': 0.206330,'l': 0.526966}
frac[5]['mu']["NNPDF30_nnlo_as_0118_87"] = {'bb': 0.140959,'cc': 0.149305,'c': 0.201568,'l': 0.508169}
# NNPDF30_nnlo_as_0118_88 
frac[2]['el']["NNPDF30_nnlo_as_0118_88"] = {'bb': 0.095326,'cc': 0.066000,'c': 0.208558,'l': 0.630116}
frac[3]['el']["NNPDF30_nnlo_as_0118_88"] = {'bb': 0.118530,'cc': 0.101136,'c': 0.218375,'l': 0.561959}
frac[4]['el']["NNPDF30_nnlo_as_0118_88"] = {'bb': 0.141180,'cc': 0.140071,'c': 0.214550,'l': 0.504198}
frac[5]['el']["NNPDF30_nnlo_as_0118_88"] = {'bb': 0.148788,'cc': 0.153432,'c': 0.209715,'l': 0.488065}
frac[2]['mu']["NNPDF30_nnlo_as_0118_88"] = {'bb': 0.083612,'cc': 0.063873,'c': 0.202929,'l': 0.649585}
frac[3]['mu']["NNPDF30_nnlo_as_0118_88"] = {'bb': 0.107453,'cc': 0.099112,'c': 0.214718,'l': 0.578717}
frac[4]['mu']["NNPDF30_nnlo_as_0118_88"] = {'bb': 0.130973,'cc': 0.135720,'c': 0.206604,'l': 0.526703}
frac[5]['mu']["NNPDF30_nnlo_as_0118_88"] = {'bb': 0.141021,'cc': 0.149255,'c': 0.201989,'l': 0.507735}
# NNPDF30_nnlo_as_0118_89 
frac[2]['el']["NNPDF30_nnlo_as_0118_89"] = {'bb': 0.095682,'cc': 0.065281,'c': 0.210396,'l': 0.628641}
frac[3]['el']["NNPDF30_nnlo_as_0118_89"] = {'bb': 0.118817,'cc': 0.099987,'c': 0.219850,'l': 0.561346}
frac[4]['el']["NNPDF30_nnlo_as_0118_89"] = {'bb': 0.141578,'cc': 0.138551,'c': 0.215853,'l': 0.504018}
frac[5]['el']["NNPDF30_nnlo_as_0118_89"] = {'bb': 0.149911,'cc': 0.151883,'c': 0.210445,'l': 0.487761}
frac[2]['mu']["NNPDF30_nnlo_as_0118_89"] = {'bb': 0.084666,'cc': 0.063800,'c': 0.206391,'l': 0.645143}
frac[3]['mu']["NNPDF30_nnlo_as_0118_89"] = {'bb': 0.107811,'cc': 0.097892,'c': 0.215606,'l': 0.578691}
frac[4]['mu']["NNPDF30_nnlo_as_0118_89"] = {'bb': 0.131308,'cc': 0.134098,'c': 0.207675,'l': 0.526920}
frac[5]['mu']["NNPDF30_nnlo_as_0118_89"] = {'bb': 0.141369,'cc': 0.147641,'c': 0.203079,'l': 0.507911}
# NNPDF30_nnlo_as_0118_90 
frac[2]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.095534,'cc': 0.065632,'c': 0.209458,'l': 0.629377}
frac[3]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.118638,'cc': 0.100452,'c': 0.219178,'l': 0.561732}
frac[4]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.141436,'cc': 0.139177,'c': 0.215622,'l': 0.503765}
frac[5]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.149601,'cc': 0.152367,'c': 0.211240,'l': 0.486792}
frac[2]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.085222,'cc': 0.064679,'c': 0.207393,'l': 0.642706}
frac[3]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.107651,'cc': 0.098268,'c': 0.214974,'l': 0.579107}
frac[4]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.131049,'cc': 0.134843,'c': 0.207364,'l': 0.526743}
frac[5]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.141129,'cc': 0.148437,'c': 0.202912,'l': 0.507523}
# NNPDF30_nnlo_as_0118_91 
frac[2]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.095457,'cc': 0.065391,'c': 0.210532,'l': 0.628620}
frac[3]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.118576,'cc': 0.100375,'c': 0.220149,'l': 0.560901}
frac[4]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.141302,'cc': 0.139205,'c': 0.215836,'l': 0.503658}
frac[5]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.149642,'cc': 0.152515,'c': 0.210407,'l': 0.487435}
frac[2]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.083804,'cc': 0.063222,'c': 0.204668,'l': 0.648306}
frac[3]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.107750,'cc': 0.098304,'c': 0.216018,'l': 0.577927}
frac[4]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.131253,'cc': 0.134743,'c': 0.207520,'l': 0.526484}
frac[5]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.141283,'cc': 0.148335,'c': 0.202801,'l': 0.507581}
# NNPDF30_nnlo_as_0118_92 
frac[2]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.095294,'cc': 0.065997,'c': 0.209364,'l': 0.629345}
frac[3]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.118500,'cc': 0.101033,'c': 0.219270,'l': 0.561197}
frac[4]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.141240,'cc': 0.139808,'c': 0.215160,'l': 0.503792}
frac[5]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.149520,'cc': 0.153045,'c': 0.210021,'l': 0.487413}
frac[2]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.083883,'cc': 0.064064,'c': 0.204298,'l': 0.647755}
frac[3]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.107399,'cc': 0.098993,'c': 0.215325,'l': 0.578283}
frac[4]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.130914,'cc': 0.135399,'c': 0.207077,'l': 0.526609}
frac[5]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.140954,'cc': 0.148932,'c': 0.202385,'l': 0.507728}
# NNPDF30_nnlo_as_0118_93 
frac[2]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.095449,'cc': 0.065215,'c': 0.209767,'l': 0.629569}
frac[3]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.118695,'cc': 0.099966,'c': 0.219768,'l': 0.561572}
frac[4]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.141527,'cc': 0.138559,'c': 0.216158,'l': 0.503756}
frac[5]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.149802,'cc': 0.151793,'c': 0.211185,'l': 0.487219}
frac[2]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.084198,'cc': 0.063482,'c': 0.205695,'l': 0.646625}
frac[3]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.107666,'cc': 0.097917,'c': 0.215824,'l': 0.578592}
frac[4]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.131196,'cc': 0.134134,'c': 0.207925,'l': 0.526745}
frac[5]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.141246,'cc': 0.147643,'c': 0.203429,'l': 0.507683}
# NNPDF30_nnlo_as_0118_94 
frac[2]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.095238,'cc': 0.065882,'c': 0.208223,'l': 0.630657}
frac[3]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.118390,'cc': 0.101291,'c': 0.217894,'l': 0.562426}
frac[4]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.140971,'cc': 0.140285,'c': 0.213297,'l': 0.505446}
frac[5]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.149252,'cc': 0.153580,'c': 0.207938,'l': 0.489230}
frac[2]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.083068,'cc': 0.063323,'c': 0.200618,'l': 0.652990}
frac[3]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.107602,'cc': 0.099157,'c': 0.213568,'l': 0.579673}
frac[4]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.130776,'cc': 0.135692,'c': 0.204944,'l': 0.528588}
frac[5]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.140685,'cc': 0.149202,'c': 0.200313,'l': 0.509800}
# NNPDF30_nnlo_as_0118_95 
frac[2]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.094870,'cc': 0.064872,'c': 0.209703,'l': 0.630555}
frac[3]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.117223,'cc': 0.098642,'c': 0.215004,'l': 0.569131}
frac[4]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.138053,'cc': 0.134857,'c': 0.207814,'l': 0.519276}
frac[5]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.146006,'cc': 0.147428,'c': 0.202006,'l': 0.504560}
frac[2]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.083789,'cc': 0.063198,'c': 0.203914,'l': 0.649099}
frac[3]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.107654,'cc': 0.098135,'c': 0.214044,'l': 0.580167}
frac[4]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.131000,'cc': 0.134384,'c': 0.205681,'l': 0.528934}
frac[5]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.141043,'cc': 0.147969,'c': 0.201212,'l': 0.509775}
# NNPDF30_nnlo_as_0118_96 
frac[2]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.095415,'cc': 0.065606,'c': 0.210924,'l': 0.628055}
frac[3]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.118672,'cc': 0.100742,'c': 0.219769,'l': 0.560818}
frac[4]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.141521,'cc': 0.139724,'c': 0.214636,'l': 0.504119}
frac[5]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.149872,'cc': 0.153070,'c': 0.208683,'l': 0.488376}
frac[2]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.084539,'cc': 0.062286,'c': 0.201530,'l': 0.651645}
frac[3]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.108389,'cc': 0.097285,'c': 0.211974,'l': 0.582351}
frac[4]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.131563,'cc': 0.134164,'c': 0.204334,'l': 0.529939}
frac[5]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.141521,'cc': 0.147901,'c': 0.199747,'l': 0.510831}
# NNPDF30_nnlo_as_0118_97 
frac[2]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.095184,'cc': 0.065359,'c': 0.211302,'l': 0.628155}
frac[3]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.118337,'cc': 0.100268,'c': 0.220637,'l': 0.560758}
frac[4]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.141001,'cc': 0.139322,'c': 0.215716,'l': 0.503961}
frac[5]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.149244,'cc': 0.152588,'c': 0.209983,'l': 0.488185}
frac[2]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.083459,'cc': 0.062934,'c': 0.204496,'l': 0.649112}
frac[3]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.107748,'cc': 0.098359,'c': 0.216536,'l': 0.577358}
frac[4]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.130430,'cc': 0.134971,'c': 0.207505,'l': 0.527094}
frac[5]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.140271,'cc': 0.148545,'c': 0.202573,'l': 0.508611}
# NNPDF30_nnlo_as_0118_98 
frac[2]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.095403,'cc': 0.065887,'c': 0.210066,'l': 0.628645}
frac[3]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.118489,'cc': 0.101697,'c': 0.219335,'l': 0.560479}
frac[4]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.141188,'cc': 0.140100,'c': 0.214766,'l': 0.503946}
frac[5]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.149401,'cc': 0.153354,'c': 0.209378,'l': 0.487867}
frac[2]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.083690,'cc': 0.063767,'c': 0.204311,'l': 0.648232}
frac[3]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.107630,'cc': 0.099043,'c': 0.215302,'l': 0.578026}
frac[4]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.130937,'cc': 0.135688,'c': 0.206530,'l': 0.526845}
frac[5]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.140924,'cc': 0.149254,'c': 0.201699,'l': 0.508123}
# NNPDF30_nnlo_as_0118_99 
frac[2]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.095400,'cc': 0.065937,'c': 0.208751,'l': 0.629912}
frac[3]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.118485,'cc': 0.100965,'c': 0.218724,'l': 0.561827}
frac[4]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.141191,'cc': 0.139869,'c': 0.214764,'l': 0.504176}
frac[5]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.149513,'cc': 0.153123,'c': 0.209237,'l': 0.488127}
frac[2]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.084629,'cc': 0.064507,'c': 0.205546,'l': 0.645319}
frac[3]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.107358,'cc': 0.098816,'c': 0.214651,'l': 0.579174}
frac[4]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.130908,'cc': 0.135315,'c': 0.206574,'l': 0.527203}
frac[5]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.140931,'cc': 0.148857,'c': 0.201944,'l': 0.508268}
# NNPDF30_nnlo_as_0118_90 
frac[2]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.095534,'cc': 0.065632,'c': 0.209458,'l': 0.629377}
frac[3]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.118638,'cc': 0.100452,'c': 0.219178,'l': 0.561732}
frac[4]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.141436,'cc': 0.139177,'c': 0.215622,'l': 0.503765}
frac[5]['el']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.149601,'cc': 0.152367,'c': 0.211240,'l': 0.486792}
frac[2]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.085222,'cc': 0.064679,'c': 0.207393,'l': 0.642706}
frac[3]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.107651,'cc': 0.098268,'c': 0.214974,'l': 0.579107}
frac[4]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.131049,'cc': 0.134843,'c': 0.207364,'l': 0.526743}
frac[5]['mu']["NNPDF30_nnlo_as_0118_90"] = {'bb': 0.141129,'cc': 0.148437,'c': 0.202912,'l': 0.507523}
# NNPDF30_nnlo_as_0118_91 
frac[2]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.095457,'cc': 0.065391,'c': 0.210532,'l': 0.628620}
frac[3]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.118576,'cc': 0.100375,'c': 0.220149,'l': 0.560901}
frac[4]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.141302,'cc': 0.139205,'c': 0.215836,'l': 0.503658}
frac[5]['el']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.149642,'cc': 0.152515,'c': 0.210407,'l': 0.487435}
frac[2]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.083804,'cc': 0.063222,'c': 0.204668,'l': 0.648306}
frac[3]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.107750,'cc': 0.098304,'c': 0.216018,'l': 0.577927}
frac[4]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.131253,'cc': 0.134743,'c': 0.207520,'l': 0.526484}
frac[5]['mu']["NNPDF30_nnlo_as_0118_91"] = {'bb': 0.141283,'cc': 0.148335,'c': 0.202801,'l': 0.507581}
# NNPDF30_nnlo_as_0118_92 
frac[2]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.095294,'cc': 0.065997,'c': 0.209364,'l': 0.629345}
frac[3]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.118500,'cc': 0.101033,'c': 0.219270,'l': 0.561197}
frac[4]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.141240,'cc': 0.139808,'c': 0.215160,'l': 0.503792}
frac[5]['el']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.149520,'cc': 0.153045,'c': 0.210021,'l': 0.487413}
frac[2]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.083883,'cc': 0.064064,'c': 0.204298,'l': 0.647755}
frac[3]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.107399,'cc': 0.098993,'c': 0.215325,'l': 0.578283}
frac[4]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.130914,'cc': 0.135399,'c': 0.207077,'l': 0.526609}
frac[5]['mu']["NNPDF30_nnlo_as_0118_92"] = {'bb': 0.140954,'cc': 0.148932,'c': 0.202385,'l': 0.507728}
# NNPDF30_nnlo_as_0118_93 
frac[2]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.095449,'cc': 0.065215,'c': 0.209767,'l': 0.629569}
frac[3]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.118695,'cc': 0.099966,'c': 0.219768,'l': 0.561572}
frac[4]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.141527,'cc': 0.138559,'c': 0.216158,'l': 0.503756}
frac[5]['el']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.149802,'cc': 0.151793,'c': 0.211185,'l': 0.487219}
frac[2]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.084198,'cc': 0.063482,'c': 0.205695,'l': 0.646625}
frac[3]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.107666,'cc': 0.097917,'c': 0.215824,'l': 0.578592}
frac[4]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.131196,'cc': 0.134134,'c': 0.207925,'l': 0.526745}
frac[5]['mu']["NNPDF30_nnlo_as_0118_93"] = {'bb': 0.141246,'cc': 0.147643,'c': 0.203429,'l': 0.507683}
# NNPDF30_nnlo_as_0118_94 
frac[2]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.095238,'cc': 0.065882,'c': 0.208223,'l': 0.630657}
frac[3]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.118390,'cc': 0.101291,'c': 0.217894,'l': 0.562426}
frac[4]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.140971,'cc': 0.140285,'c': 0.213297,'l': 0.505446}
frac[5]['el']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.149252,'cc': 0.153580,'c': 0.207938,'l': 0.489230}
frac[2]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.083068,'cc': 0.063323,'c': 0.200618,'l': 0.652990}
frac[3]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.107602,'cc': 0.099157,'c': 0.213568,'l': 0.579673}
frac[4]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.130776,'cc': 0.135692,'c': 0.204944,'l': 0.528588}
frac[5]['mu']["NNPDF30_nnlo_as_0118_94"] = {'bb': 0.140685,'cc': 0.149202,'c': 0.200313,'l': 0.509800}
# NNPDF30_nnlo_as_0118_95 
frac[2]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.094870,'cc': 0.064872,'c': 0.209703,'l': 0.630555}
frac[3]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.117223,'cc': 0.098642,'c': 0.215004,'l': 0.569131}
frac[4]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.138053,'cc': 0.134857,'c': 0.207814,'l': 0.519276}
frac[5]['el']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.146006,'cc': 0.147428,'c': 0.202006,'l': 0.504560}
frac[2]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.083789,'cc': 0.063198,'c': 0.203914,'l': 0.649099}
frac[3]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.107654,'cc': 0.098135,'c': 0.214044,'l': 0.580167}
frac[4]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.131000,'cc': 0.134384,'c': 0.205681,'l': 0.528934}
frac[5]['mu']["NNPDF30_nnlo_as_0118_95"] = {'bb': 0.141043,'cc': 0.147969,'c': 0.201212,'l': 0.509775}
# NNPDF30_nnlo_as_0118_96 
frac[2]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.095415,'cc': 0.065606,'c': 0.210924,'l': 0.628055}
frac[3]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.118672,'cc': 0.100742,'c': 0.219769,'l': 0.560818}
frac[4]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.141521,'cc': 0.139724,'c': 0.214636,'l': 0.504119}
frac[5]['el']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.149872,'cc': 0.153070,'c': 0.208683,'l': 0.488376}
frac[2]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.084539,'cc': 0.062286,'c': 0.201530,'l': 0.651645}
frac[3]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.108389,'cc': 0.097285,'c': 0.211974,'l': 0.582351}
frac[4]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.131563,'cc': 0.134164,'c': 0.204334,'l': 0.529939}
frac[5]['mu']["NNPDF30_nnlo_as_0118_96"] = {'bb': 0.141521,'cc': 0.147901,'c': 0.199747,'l': 0.510831}
# NNPDF30_nnlo_as_0118_97 
frac[2]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.095184,'cc': 0.065359,'c': 0.211302,'l': 0.628155}
frac[3]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.118337,'cc': 0.100268,'c': 0.220637,'l': 0.560758}
frac[4]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.141001,'cc': 0.139322,'c': 0.215716,'l': 0.503961}
frac[5]['el']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.149244,'cc': 0.152588,'c': 0.209983,'l': 0.488185}
frac[2]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.083459,'cc': 0.062934,'c': 0.204496,'l': 0.649112}
frac[3]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.107748,'cc': 0.098359,'c': 0.216536,'l': 0.577358}
frac[4]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.130430,'cc': 0.134971,'c': 0.207505,'l': 0.527094}
frac[5]['mu']["NNPDF30_nnlo_as_0118_97"] = {'bb': 0.140271,'cc': 0.148545,'c': 0.202573,'l': 0.508611}
# NNPDF30_nnlo_as_0118_98 
frac[2]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.095403,'cc': 0.065887,'c': 0.210066,'l': 0.628645}
frac[3]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.118489,'cc': 0.101697,'c': 0.219335,'l': 0.560479}
frac[4]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.141188,'cc': 0.140100,'c': 0.214766,'l': 0.503946}
frac[5]['el']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.149401,'cc': 0.153354,'c': 0.209378,'l': 0.487867}
frac[2]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.083690,'cc': 0.063767,'c': 0.204311,'l': 0.648232}
frac[3]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.107630,'cc': 0.099043,'c': 0.215302,'l': 0.578026}
frac[4]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.130937,'cc': 0.135688,'c': 0.206530,'l': 0.526845}
frac[5]['mu']["NNPDF30_nnlo_as_0118_98"] = {'bb': 0.140924,'cc': 0.149254,'c': 0.201699,'l': 0.508123}
# NNPDF30_nnlo_as_0118_99 
frac[2]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.095400,'cc': 0.065937,'c': 0.208751,'l': 0.629912}
frac[3]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.118485,'cc': 0.100965,'c': 0.218724,'l': 0.561827}
frac[4]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.141191,'cc': 0.139869,'c': 0.214764,'l': 0.504176}
frac[5]['el']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.149513,'cc': 0.153123,'c': 0.209237,'l': 0.488127}
frac[2]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.084629,'cc': 0.064507,'c': 0.205546,'l': 0.645319}
frac[3]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.107358,'cc': 0.098816,'c': 0.214651,'l': 0.579174}
frac[4]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.130908,'cc': 0.135315,'c': 0.206574,'l': 0.527203}
frac[5]['mu']["NNPDF30_nnlo_as_0118_99"] = {'bb': 0.140931,'cc': 0.148857,'c': 0.201944,'l': 0.508268}
# NNPDF30_nnlo_as_0118_100 
frac[2]['el']["NNPDF30_nnlo_as_0118_100"] = {'bb': 0.095510,'cc': 0.065613,'c': 0.209885,'l': 0.628993}
frac[3]['el']["NNPDF30_nnlo_as_0118_100"] = {'bb': 0.118549,'cc': 0.100716,'c': 0.218995,'l': 0.561740}
frac[4]['el']["NNPDF30_nnlo_as_0118_100"] = {'bb': 0.141213,'cc': 0.139673,'c': 0.214452,'l': 0.504661}
frac[5]['el']["NNPDF30_nnlo_as_0118_100"] = {'bb': 0.149533,'cc': 0.153039,'c': 0.208728,'l': 0.488700}
frac[2]['mu']["NNPDF30_nnlo_as_0118_100"] = {'bb': 0.083810,'cc': 0.063515,'c': 0.204005,'l': 0.648670}
frac[3]['mu']["NNPDF30_nnlo_as_0118_100"] = {'bb': 0.108784,'cc': 0.099546,'c': 0.216853,'l': 0.574818}
frac[4]['mu']["NNPDF30_nnlo_as_0118_100"] = {'bb': 0.130922,'cc': 0.134980,'c': 0.205870,'l': 0.528228}
frac[5]['mu']["NNPDF30_nnlo_as_0118_100"] = {'bb': 0.140946,'cc': 0.148566,'c': 0.201234,'l': 0.509253}

