
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

