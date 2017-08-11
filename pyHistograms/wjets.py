
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

f_ca_map[2]['el'][""] =  1.175471
f_ca_map[3]['el'][""] =  1.275507
f_ca_map[4]['el'][""] =  1.356616
f_ca_map[5]['el'][""] =  1.149216
f_ca_map[2]['mu'][""] =  1.192968
f_ca_map[3]['mu'][""] =  1.190832
f_ca_map[4]['mu'][""] =  1.174213
f_ca_map[5]['mu'][""] =  1.097517

frac[2]['el'][""] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el'][""] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el'][""] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el'][""] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu'][""] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu'][""] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu'][""] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu'][""] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

flav_map[2]['el'][""] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el'][""] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el'][""] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el'][""] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu'][""] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu'][""] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu'][""] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu'][""] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}

# CA variation
f_ca_map[2]['el']["wnorm__1up"] =  1.175471*(1+(0.005**2+0.052**2)**0.5)
f_ca_map[3]['el']["wnorm__1up"] =  1.275507*(1+(0.009**2+0.036**2)**0.5)
f_ca_map[4]['el']["wnorm__1up"] =  1.356616*(1+(0.019**2+0.047**2)**0.5)
f_ca_map[5]['el']["wnorm__1up"] =  1.149216*(1+(0.036**2+0.031**2)**0.5)
f_ca_map[2]['mu']["wnorm__1up"] =  1.192968*(1+(0.003**2+0.046**2)**0.5)
f_ca_map[3]['mu']["wnorm__1up"] =  1.190832*(1+(0.007**2+0.030**2)**0.5)
f_ca_map[4]['mu']["wnorm__1up"] =  1.174213*(1+(0.014**2+0.031**2)**0.5)
f_ca_map[5]['mu']["wnorm__1up"] =  1.097517*(1+(0.025**2+0.023**2)**0.5)

frac[2]['el']["wnorm__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["wnorm__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["wnorm__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["wnorm__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["wnorm__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["wnorm__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["wnorm__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["wnorm__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

flav_map[2]['el']["wnorm__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["wnorm__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["wnorm__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["wnorm__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["wnorm__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["wnorm__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["wnorm__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["wnorm__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}

# CA variation
f_ca_map[2]['el']["wnorm__1down"] =  1.175471*(1-(0.005**2+0.052**2)**0.5)
f_ca_map[3]['el']["wnorm__1down"] =  1.275507*(1-(0.009**2+0.036**2)**0.5)
f_ca_map[4]['el']["wnorm__1down"] =  1.356616*(1-(0.019**2+0.047**2)**0.5)
f_ca_map[5]['el']["wnorm__1down"] =  1.149216*(1-(0.036**2+0.031**2)**0.5)
f_ca_map[2]['mu']["wnorm__1down"] =  1.192968*(1-(0.003**2+0.046**2)**0.5)
f_ca_map[3]['mu']["wnorm__1down"] =  1.190832*(1-(0.007**2+0.030**2)**0.5)
f_ca_map[4]['mu']["wnorm__1down"] =  1.174213*(1-(0.014**2+0.031**2)**0.5)
f_ca_map[5]['mu']["wnorm__1down"] =  1.097517*(1-(0.025**2+0.023**2)**0.5)

frac[2]['el']["wnorm__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["wnorm__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["wnorm__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["wnorm__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["wnorm__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["wnorm__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["wnorm__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["wnorm__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

flav_map[2]['el']["wnorm__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["wnorm__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["wnorm__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["wnorm__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["wnorm__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["wnorm__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["wnorm__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["wnorm__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}

# fc variation

f_ca_map[2]['el']["wc__1up"] =  1.175471
f_ca_map[3]['el']["wc__1up"] =  1.275507
f_ca_map[4]['el']["wc__1up"] =  1.356616
f_ca_map[5]['el']["wc__1up"] =  1.149216
f_ca_map[2]['mu']["wc__1up"] =  1.192968
f_ca_map[3]['mu']["wc__1up"] =  1.190832
f_ca_map[4]['mu']["wc__1up"] =  1.174213
f_ca_map[5]['mu']["wc__1up"] =  1.097517

frac[2]['el']["wc__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["wc__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["wc__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["wc__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["wc__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["wc__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["wc__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["wc__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

flav_map[2]['el']["wc__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000*1.3, 'l': 0.919451}
flav_map[3]['el']["wc__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623*1.3, 'l': 0.897957}
flav_map[4]['el']["wc__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920*1.3, 'l': 0.877083}
flav_map[5]['el']["wc__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604*1.3, 'l': 0.854725}
flav_map[2]['mu']["wc__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000*1.3, 'l': 0.877818}
flav_map[3]['mu']["wc__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415*1.3, 'l': 0.844826}
flav_map[4]['mu']["wc__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390*1.3, 'l': 0.814958}
flav_map[5]['mu']["wc__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237*1.3, 'l': 0.778833}

f_ca_map[2]['el']["wc__1down"] =  1.175471
f_ca_map[3]['el']["wc__1down"] =  1.275507
f_ca_map[4]['el']["wc__1down"] =  1.356616
f_ca_map[5]['el']["wc__1down"] =  1.149216
f_ca_map[2]['mu']["wc__1down"] =  1.192968
f_ca_map[3]['mu']["wc__1down"] =  1.190832
f_ca_map[4]['mu']["wc__1down"] =  1.174213
f_ca_map[5]['mu']["wc__1down"] =  1.097517

frac[2]['el']["wc__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["wc__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["wc__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["wc__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["wc__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["wc__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["wc__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["wc__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

flav_map[2]['el']["wc__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000*0.7, 'l': 0.919451}
flav_map[3]['el']["wc__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623*0.7, 'l': 0.897957}
flav_map[4]['el']["wc__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920*0.7, 'l': 0.877083}
flav_map[5]['el']["wc__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604*0.7, 'l': 0.854725}
flav_map[2]['mu']["wc__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000*0.7, 'l': 0.877818}
flav_map[3]['mu']["wc__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415*0.7, 'l': 0.844826}
flav_map[4]['mu']["wc__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390*0.7, 'l': 0.814958}
flav_map[5]['mu']["wc__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237*0.7, 'l': 0.778833}

# fbb stat variation
f_ca_map[2]['el']["wbb__1up"] =  1.175471
f_ca_map[3]['el']["wbb__1up"] =  1.275507
f_ca_map[4]['el']["wbb__1up"] =  1.356616
f_ca_map[5]['el']["wbb__1up"] =  1.149216
f_ca_map[2]['mu']["wbb__1up"] =  1.192968
f_ca_map[3]['mu']["wbb__1up"] =  1.190832
f_ca_map[4]['mu']["wbb__1up"] =  1.174213
f_ca_map[5]['mu']["wbb__1up"] =  1.097517

frac[2]['el']["wbb__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["wbb__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["wbb__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["wbb__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["wbb__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["wbb__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["wbb__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["wbb__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

flav_map[2]['el']["wbb__1up"] = {'bb': 1.321579*(1+(0.044**2+0.071**2)**0.5), 'cc': 1.321579*(1+(0.044**2+0.071**2)**0.5), 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["wbb__1up"] = {'bb': 1.290685*(1+(0.044**2+0.071**2)**0.5), 'cc': 1.290685*(1+(0.044**2+0.071**2)**0.5), 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["wbb__1up"] = {'bb': 1.260681*(1+(0.044**2+0.071**2)**0.5), 'cc': 1.260681*(1+(0.044**2+0.071**2)**0.5), 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["wbb__1up"] = {'bb': 1.228545*(1+(0.044**2+0.071**2)**0.5), 'cc': 1.228545*(1+(0.044**2+0.071**2)**0.5), 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["wbb__1up"] = {'bb': 1.541862*(1+(0.029**2+0.061**2)**0.5), 'cc': 1.541862*(1+(0.029**2+0.061**2)**0.5), 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["wbb__1up"] = {'bb': 1.483912*(1+(0.029**2+0.061**2)**0.5), 'cc': 1.483912*(1+(0.029**2+0.061**2)**0.5), 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["wbb__1up"] = {'bb': 1.431450*(1+(0.029**2+0.061**2)**0.5), 'cc': 1.431450*(1+(0.029**2+0.061**2)**0.5), 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["wbb__1up"] = {'bb': 1.367997*(1+(0.029**2+0.061**2)**0.5), 'cc': 1.367997*(1+(0.029**2+0.061**2)**0.5), 'c': 0.887237, 'l': 0.778833}

# fbb stat variation
f_ca_map[2]['el']["wbb__1down"] =  1.175471
f_ca_map[3]['el']["wbb__1down"] =  1.275507
f_ca_map[4]['el']["wbb__1down"] =  1.356616
f_ca_map[5]['el']["wbb__1down"] =  1.149216
f_ca_map[2]['mu']["wbb__1down"] =  1.192968
f_ca_map[3]['mu']["wbb__1down"] =  1.190832
f_ca_map[4]['mu']["wbb__1down"] =  1.174213
f_ca_map[5]['mu']["wbb__1down"] =  1.097517

frac[2]['el']["wbb__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["wbb__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["wbb__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["wbb__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["wbb__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["wbb__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["wbb__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["wbb__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

flav_map[2]['el']["wbb__1down"] = {'bb': 1.321579*(1-(0.044**2+0.071**2)**0.5), 'cc': 1.321579*(1-(0.044**2+0.071**2)**0.5), 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["wbb__1down"] = {'bb': 1.290685*(1-(0.044**2+0.071**2)**0.5), 'cc': 1.290685*(1-(0.044**2+0.071**2)**0.5), 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["wbb__1down"] = {'bb': 1.260681*(1-(0.044**2+0.071**2)**0.5), 'cc': 1.260681*(1-(0.044**2+0.071**2)**0.5), 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["wbb__1down"] = {'bb': 1.228545*(1-(0.044**2+0.071**2)**0.5), 'cc': 1.228545*(1-(0.044**2+0.071**2)**0.5), 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["wbb__1down"] = {'bb': 1.541862*(1-(0.029**2+0.061**2)**0.5), 'cc': 1.541862*(1-(0.029**2+0.061**2)**0.5), 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["wbb__1down"] = {'bb': 1.483912*(1-(0.029**2+0.061**2)**0.5), 'cc': 1.483912*(1-(0.029**2+0.061**2)**0.5), 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["wbb__1down"] = {'bb': 1.431450*(1-(0.029**2+0.061**2)**0.5), 'cc': 1.431450*(1-(0.029**2+0.061**2)**0.5), 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["wbb__1down"] = {'bb': 1.367997*(1-(0.029**2+0.061**2)**0.5), 'cc': 1.367997*(1-(0.029**2+0.061**2)**0.5), 'c': 0.887237, 'l': 0.778833}

# fl stat variation

f_ca_map[2]['el']["wl__1up"] =  1.175471
f_ca_map[3]['el']["wl__1up"] =  1.275507
f_ca_map[4]['el']["wl__1up"] =  1.356616
f_ca_map[5]['el']["wl__1up"] =  1.149216
f_ca_map[2]['mu']["wl__1up"] =  1.192968
f_ca_map[3]['mu']["wl__1up"] =  1.190832
f_ca_map[4]['mu']["wl__1up"] =  1.174213
f_ca_map[5]['mu']["wl__1up"] =  1.097517

frac[2]['el']["wl__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["wl__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["wl__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["wl__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["wl__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["wl__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["wl__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["wl__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

flav_map[2]['el']["wl__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451*(1+(0.015**2+0.025**2)**0.5)}
flav_map[3]['el']["wl__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957*(1+(0.015**2+0.025**2)**0.5)}
flav_map[4]['el']["wl__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083*(1+(0.015**2+0.025**2)**0.5)}
flav_map[5]['el']["wl__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725*(1+(0.015**2+0.025**2)**0.5)}
flav_map[2]['mu']["wl__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818*(1+(0.011**2+0.024**2)**0.5)}
flav_map[3]['mu']["wl__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826*(1+(0.011**2+0.024**2)**0.5)}
flav_map[4]['mu']["wl__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958*(1+(0.011**2+0.024**2)**0.5)}
flav_map[5]['mu']["wl__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833*(1+(0.011**2+0.024**2)**0.5)}

# fl stat variation

f_ca_map[2]['el']["wl__1down"] =  1.175471
f_ca_map[3]['el']["wl__1down"] =  1.275507
f_ca_map[4]['el']["wl__1down"] =  1.356616
f_ca_map[5]['el']["wl__1down"] =  1.149216
f_ca_map[2]['mu']["wl__1down"] =  1.192968
f_ca_map[3]['mu']["wl__1down"] =  1.190832
f_ca_map[4]['mu']["wl__1down"] =  1.174213
f_ca_map[5]['mu']["wl__1down"] =  1.097517

frac[2]['el']["wl__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["wl__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["wl__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["wl__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["wl__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["wl__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["wl__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["wl__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

flav_map[2]['el']["wl__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451*(1-(0.015**2+0.025**2)**0.5)}
flav_map[3]['el']["wl__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957*(1-(0.015**2+0.025**2)**0.5)}
flav_map[4]['el']["wl__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083*(1-(0.015**2+0.025**2)**0.5)}
flav_map[5]['el']["wl__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725*(1-(0.015**2+0.025**2)**0.5)}
flav_map[2]['mu']["wl__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818*(1-(0.011**2+0.024**2)**0.5)}
flav_map[3]['mu']["wl__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826*(1-(0.011**2+0.024**2)**0.5)}
flav_map[4]['mu']["wl__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958*(1-(0.011**2+0.024**2)**0.5)}
flav_map[5]['mu']["wl__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833*(1-(0.011**2+0.024**2)**0.5)}

# TTree variation:

# ttxsecup 
f_ca_map[2]['el']["ttxsecup"] =  1.175483
f_ca_map[3]['el']["ttxsecup"] =  1.275504
f_ca_map[4]['el']["ttxsecup"] =  1.356630
f_ca_map[5]['el']["ttxsecup"] =  1.149205
f_ca_map[2]['mu']["ttxsecup"] =  1.192966
f_ca_map[3]['mu']["ttxsecup"] =  1.190852
f_ca_map[4]['mu']["ttxsecup"] =  1.174239
f_ca_map[5]['mu']["ttxsecup"] =  1.097506
# ttxsecdw 
f_ca_map[2]['el']["ttxsecdw"] =  1.175461
f_ca_map[3]['el']["ttxsecdw"] =  1.275510
f_ca_map[4]['el']["ttxsecdw"] =  1.356605
f_ca_map[5]['el']["ttxsecdw"] =  1.149224
f_ca_map[2]['mu']["ttxsecdw"] =  1.192969
f_ca_map[3]['mu']["ttxsecdw"] =  1.190815
f_ca_map[4]['mu']["ttxsecdw"] =  1.174191
f_ca_map[5]['mu']["ttxsecdw"] =  1.097527
# singletopup 
f_ca_map[2]['el']["singletopup"] =  1.173180
f_ca_map[3]['el']["singletopup"] =  1.272557
f_ca_map[4]['el']["singletopup"] =  1.352316
f_ca_map[5]['el']["singletopup"] =  1.145925
f_ca_map[2]['mu']["singletopup"] =  1.191555
f_ca_map[3]['mu']["singletopup"] =  1.188007
f_ca_map[4]['mu']["singletopup"] =  1.170910
f_ca_map[5]['mu']["singletopup"] =  1.095054
# singletopdw 
f_ca_map[2]['el']["singletopdw"] =  1.177476
f_ca_map[3]['el']["singletopdw"] =  1.278089
f_ca_map[4]['el']["singletopdw"] =  1.360376
f_ca_map[5]['el']["singletopdw"] =  1.152101
f_ca_map[2]['mu']["singletopdw"] =  1.194204
f_ca_map[3]['mu']["singletopdw"] =  1.193303
f_ca_map[4]['mu']["singletopdw"] =  1.177100
f_ca_map[5]['mu']["singletopdw"] =  1.099677
# wnorm__1up 
f_ca_map[2]['el']["wnorm__1up"] =  1.175478
f_ca_map[3]['el']["wnorm__1up"] =  1.275505
f_ca_map[4]['el']["wnorm__1up"] =  1.356624
f_ca_map[5]['el']["wnorm__1up"] =  1.149210
f_ca_map[2]['mu']["wnorm__1up"] =  1.192968
f_ca_map[3]['mu']["wnorm__1up"] =  1.190832
f_ca_map[4]['mu']["wnorm__1up"] =  1.174213
f_ca_map[5]['mu']["wnorm__1up"] =  1.097517
# wnorm__1down 
f_ca_map[2]['el']["wnorm__1down"] =  1.175465
f_ca_map[3]['el']["wnorm__1down"] =  1.275509
f_ca_map[4]['el']["wnorm__1down"] =  1.356608
f_ca_map[5]['el']["wnorm__1down"] =  1.149221
f_ca_map[2]['mu']["wnorm__1down"] =  1.192968
f_ca_map[3]['mu']["wnorm__1down"] =  1.190832
f_ca_map[4]['mu']["wnorm__1down"] =  1.174213
f_ca_map[5]['mu']["wnorm__1down"] =  1.097517
# elMisIDpos_up 
f_ca_map[2]['el']["elMisIDpos_up"] =  1.106356
f_ca_map[3]['el']["elMisIDpos_up"] =  1.200246
f_ca_map[4]['el']["elMisIDpos_up"] =  1.275138
f_ca_map[5]['el']["elMisIDpos_up"] =  1.080519
f_ca_map[2]['mu']["elMisIDpos_up"] =  1.192968
f_ca_map[3]['mu']["elMisIDpos_up"] =  1.190832
f_ca_map[4]['mu']["elMisIDpos_up"] =  1.174213
f_ca_map[5]['mu']["elMisIDpos_up"] =  1.097517
# elMisIDpos_down 
f_ca_map[2]['el']["elMisIDpos_down"] =  1.253429
f_ca_map[3]['el']["elMisIDpos_down"] =  1.360373
f_ca_map[4]['el']["elMisIDpos_down"] =  1.448508
f_ca_map[5]['el']["elMisIDpos_down"] =  1.226679
f_ca_map[2]['mu']["elMisIDpos_down"] =  1.192968
f_ca_map[3]['mu']["elMisIDpos_down"] =  1.190832
f_ca_map[4]['mu']["elMisIDpos_down"] =  1.174213
f_ca_map[5]['mu']["elMisIDpos_down"] =  1.097517
# MET_SoftTrk_ResoPara 
f_ca_map[2]['el']["MET_SoftTrk_ResoPara"] =  1.180017
f_ca_map[3]['el']["MET_SoftTrk_ResoPara"] =  1.280742
f_ca_map[4]['el']["MET_SoftTrk_ResoPara"] =  1.360284
f_ca_map[5]['el']["MET_SoftTrk_ResoPara"] =  1.137502
f_ca_map[2]['mu']["MET_SoftTrk_ResoPara"] =  1.197394
f_ca_map[3]['mu']["MET_SoftTrk_ResoPara"] =  1.187955
f_ca_map[4]['mu']["MET_SoftTrk_ResoPara"] =  1.173324
f_ca_map[5]['mu']["MET_SoftTrk_ResoPara"] =  1.094365
# MET_SoftTrk_ResoPerp 
f_ca_map[2]['el']["MET_SoftTrk_ResoPerp"] =  1.177784
f_ca_map[3]['el']["MET_SoftTrk_ResoPerp"] =  1.273719
f_ca_map[4]['el']["MET_SoftTrk_ResoPerp"] =  1.360552
f_ca_map[5]['el']["MET_SoftTrk_ResoPerp"] =  1.148284
f_ca_map[2]['mu']["MET_SoftTrk_ResoPerp"] =  1.194643
f_ca_map[3]['mu']["MET_SoftTrk_ResoPerp"] =  1.196205
f_ca_map[4]['mu']["MET_SoftTrk_ResoPerp"] =  1.169294
f_ca_map[5]['mu']["MET_SoftTrk_ResoPerp"] =  1.094787
# MET_SoftTrk_ScaleUp 
f_ca_map[2]['el']["MET_SoftTrk_ScaleUp"] =  1.171918
f_ca_map[3]['el']["MET_SoftTrk_ScaleUp"] =  1.278665
f_ca_map[4]['el']["MET_SoftTrk_ScaleUp"] =  1.362719
f_ca_map[5]['el']["MET_SoftTrk_ScaleUp"] =  1.144548
f_ca_map[2]['mu']["MET_SoftTrk_ScaleUp"] =  1.192017
f_ca_map[3]['mu']["MET_SoftTrk_ScaleUp"] =  1.190113
f_ca_map[4]['mu']["MET_SoftTrk_ScaleUp"] =  1.176172
f_ca_map[5]['mu']["MET_SoftTrk_ScaleUp"] =  1.097947
# MET_SoftTrk_ScaleDown 
f_ca_map[2]['el']["MET_SoftTrk_ScaleDown"] =  1.177299
f_ca_map[3]['el']["MET_SoftTrk_ScaleDown"] =  1.273287
f_ca_map[4]['el']["MET_SoftTrk_ScaleDown"] =  1.356760
f_ca_map[5]['el']["MET_SoftTrk_ScaleDown"] =  1.146025
f_ca_map[2]['mu']["MET_SoftTrk_ScaleDown"] =  1.194138
f_ca_map[3]['mu']["MET_SoftTrk_ScaleDown"] =  1.191306
f_ca_map[4]['mu']["MET_SoftTrk_ScaleDown"] =  1.175219
f_ca_map[5]['mu']["MET_SoftTrk_ScaleDown"] =  1.093871
# EG_RESOLUTION_ALL__1up 
f_ca_map[2]['el']["EG_RESOLUTION_ALL__1up"] =  1.176437
f_ca_map[3]['el']["EG_RESOLUTION_ALL__1up"] =  1.278023
f_ca_map[4]['el']["EG_RESOLUTION_ALL__1up"] =  1.363507
f_ca_map[5]['el']["EG_RESOLUTION_ALL__1up"] =  1.151072
f_ca_map[2]['mu']["EG_RESOLUTION_ALL__1up"] =  1.192969
f_ca_map[3]['mu']["EG_RESOLUTION_ALL__1up"] =  1.190812
f_ca_map[4]['mu']["EG_RESOLUTION_ALL__1up"] =  1.174205
f_ca_map[5]['mu']["EG_RESOLUTION_ALL__1up"] =  1.097556
# EG_RESOLUTION_ALL__1down 
f_ca_map[2]['el']["EG_RESOLUTION_ALL__1down"] =  1.179473
f_ca_map[3]['el']["EG_RESOLUTION_ALL__1down"] =  1.272833
f_ca_map[4]['el']["EG_RESOLUTION_ALL__1down"] =  1.355026
f_ca_map[5]['el']["EG_RESOLUTION_ALL__1down"] =  1.143856
f_ca_map[2]['mu']["EG_RESOLUTION_ALL__1down"] =  1.192966
f_ca_map[3]['mu']["EG_RESOLUTION_ALL__1down"] =  1.190835
f_ca_map[4]['mu']["EG_RESOLUTION_ALL__1down"] =  1.174213
f_ca_map[5]['mu']["EG_RESOLUTION_ALL__1down"] =  1.097592
# EG_SCALE_ALL__1up 
f_ca_map[2]['el']["EG_SCALE_ALL__1up"] =  1.173280
f_ca_map[3]['el']["EG_SCALE_ALL__1up"] =  1.271720
f_ca_map[4]['el']["EG_SCALE_ALL__1up"] =  1.356896
f_ca_map[5]['el']["EG_SCALE_ALL__1up"] =  1.147093
f_ca_map[2]['mu']["EG_SCALE_ALL__1up"] =  1.192967
f_ca_map[3]['mu']["EG_SCALE_ALL__1up"] =  1.190829
f_ca_map[4]['mu']["EG_SCALE_ALL__1up"] =  1.174209
f_ca_map[5]['mu']["EG_SCALE_ALL__1up"] =  1.097555
# EG_SCALE_ALL__1down 
f_ca_map[2]['el']["EG_SCALE_ALL__1down"] =  1.179598
f_ca_map[3]['el']["EG_SCALE_ALL__1down"] =  1.278658
f_ca_map[4]['el']["EG_SCALE_ALL__1down"] =  1.362487
f_ca_map[5]['el']["EG_SCALE_ALL__1down"] =  1.148924
f_ca_map[2]['mu']["EG_SCALE_ALL__1down"] =  1.192970
f_ca_map[3]['mu']["EG_SCALE_ALL__1down"] =  1.190825
f_ca_map[4]['mu']["EG_SCALE_ALL__1down"] =  1.174209
f_ca_map[5]['mu']["EG_SCALE_ALL__1down"] =  1.097592
# MUON_ID__1up 
f_ca_map[2]['el']["MUON_ID__1up"] =  1.175479
f_ca_map[3]['el']["MUON_ID__1up"] =  1.275504
f_ca_map[4]['el']["MUON_ID__1up"] =  1.356622
f_ca_map[5]['el']["MUON_ID__1up"] =  1.149213
f_ca_map[2]['mu']["MUON_ID__1up"] =  1.191606
f_ca_map[3]['mu']["MUON_ID__1up"] =  1.192923
f_ca_map[4]['mu']["MUON_ID__1up"] =  1.167840
f_ca_map[5]['mu']["MUON_ID__1up"] =  1.098810
# MUON_ID__1down 
f_ca_map[2]['el']["MUON_ID__1down"] =  1.175475
f_ca_map[3]['el']["MUON_ID__1down"] =  1.275506
f_ca_map[4]['el']["MUON_ID__1down"] =  1.356609
f_ca_map[5]['el']["MUON_ID__1down"] =  1.149221
f_ca_map[2]['mu']["MUON_ID__1down"] =  1.191118
f_ca_map[3]['mu']["MUON_ID__1down"] =  1.189172
f_ca_map[4]['mu']["MUON_ID__1down"] =  1.175123
f_ca_map[5]['mu']["MUON_ID__1down"] =  1.097351
# MUON_MS__1up 
f_ca_map[2]['el']["MUON_MS__1up"] =  1.175476
f_ca_map[3]['el']["MUON_MS__1up"] =  1.275503
f_ca_map[4]['el']["MUON_MS__1up"] =  1.356616
f_ca_map[5]['el']["MUON_MS__1up"] =  1.149214
f_ca_map[2]['mu']["MUON_MS__1up"] =  1.193032
f_ca_map[3]['mu']["MUON_MS__1up"] =  1.190782
f_ca_map[4]['mu']["MUON_MS__1up"] =  1.173047
f_ca_map[5]['mu']["MUON_MS__1up"] =  1.098292
# MUON_MS__1down 
f_ca_map[2]['el']["MUON_MS__1down"] =  1.175469
f_ca_map[3]['el']["MUON_MS__1down"] =  1.275508
f_ca_map[4]['el']["MUON_MS__1down"] =  1.356606
f_ca_map[5]['el']["MUON_MS__1down"] =  1.149238
f_ca_map[2]['mu']["MUON_MS__1down"] =  1.194482
f_ca_map[3]['mu']["MUON_MS__1down"] =  1.188922
f_ca_map[4]['mu']["MUON_MS__1down"] =  1.173755
f_ca_map[5]['mu']["MUON_MS__1down"] =  1.097877
# MUON_SCALE__1up 
f_ca_map[2]['el']["MUON_SCALE__1up"] =  1.175470
f_ca_map[3]['el']["MUON_SCALE__1up"] =  1.275507
f_ca_map[4]['el']["MUON_SCALE__1up"] =  1.356612
f_ca_map[5]['el']["MUON_SCALE__1up"] =  1.149216
f_ca_map[2]['mu']["MUON_SCALE__1up"] =  1.194158
f_ca_map[3]['mu']["MUON_SCALE__1up"] =  1.193831
f_ca_map[4]['mu']["MUON_SCALE__1up"] =  1.175496
f_ca_map[5]['mu']["MUON_SCALE__1up"] =  1.099715
# MUON_SCALE__1down 
f_ca_map[2]['el']["MUON_SCALE__1down"] =  1.175475
f_ca_map[3]['el']["MUON_SCALE__1down"] =  1.275507
f_ca_map[4]['el']["MUON_SCALE__1down"] =  1.356615
f_ca_map[5]['el']["MUON_SCALE__1down"] =  1.149214
f_ca_map[2]['mu']["MUON_SCALE__1down"] =  1.188865
f_ca_map[3]['mu']["MUON_SCALE__1down"] =  1.188089
f_ca_map[4]['mu']["MUON_SCALE__1down"] =  1.171762
f_ca_map[5]['mu']["MUON_SCALE__1down"] =  1.097214
# MUON_SAGITTA_RESBIAS__1up 
f_ca_map[2]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.175471
f_ca_map[3]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.275507
f_ca_map[4]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.356616
f_ca_map[5]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.149216
f_ca_map[2]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  1.192968
f_ca_map[3]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  1.190832
f_ca_map[4]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  1.174213
f_ca_map[5]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  1.097517
# MUON_SAGITTA_RESBIAS__1down 
f_ca_map[2]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.175471
f_ca_map[3]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.275507
f_ca_map[4]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.356616
f_ca_map[5]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.149216
f_ca_map[2]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  1.192968
f_ca_map[3]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  1.190832
f_ca_map[4]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  1.174213
f_ca_map[5]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  1.097517
# MUON_SAGITTA_RHO__1up 
f_ca_map[2]['el']["MUON_SAGITTA_RHO__1up"] =  1.175471
f_ca_map[3]['el']["MUON_SAGITTA_RHO__1up"] =  1.275507
f_ca_map[4]['el']["MUON_SAGITTA_RHO__1up"] =  1.356616
f_ca_map[5]['el']["MUON_SAGITTA_RHO__1up"] =  1.149216
f_ca_map[2]['mu']["MUON_SAGITTA_RHO__1up"] =  1.192968
f_ca_map[3]['mu']["MUON_SAGITTA_RHO__1up"] =  1.190832
f_ca_map[4]['mu']["MUON_SAGITTA_RHO__1up"] =  1.174213
f_ca_map[5]['mu']["MUON_SAGITTA_RHO__1up"] =  1.097517
# MUON_SAGITTA_RHO__1down 
f_ca_map[2]['el']["MUON_SAGITTA_RHO__1down"] =  1.175471
f_ca_map[3]['el']["MUON_SAGITTA_RHO__1down"] =  1.275507
f_ca_map[4]['el']["MUON_SAGITTA_RHO__1down"] =  1.356616
f_ca_map[5]['el']["MUON_SAGITTA_RHO__1down"] =  1.149216
f_ca_map[2]['mu']["MUON_SAGITTA_RHO__1down"] =  1.192968
f_ca_map[3]['mu']["MUON_SAGITTA_RHO__1down"] =  1.190832
f_ca_map[4]['mu']["MUON_SAGITTA_RHO__1down"] =  1.174213
f_ca_map[5]['mu']["MUON_SAGITTA_RHO__1down"] =  1.097517
# JET_JER_SINGLE_NP__1up 
f_ca_map[2]['el']["JET_JER_SINGLE_NP__1up"] =  1.148932
f_ca_map[3]['el']["JET_JER_SINGLE_NP__1up"] =  1.285346
f_ca_map[4]['el']["JET_JER_SINGLE_NP__1up"] =  1.237220
f_ca_map[5]['el']["JET_JER_SINGLE_NP__1up"] =  1.042928
f_ca_map[2]['mu']["JET_JER_SINGLE_NP__1up"] =  1.118392
f_ca_map[3]['mu']["JET_JER_SINGLE_NP__1up"] =  1.149940
f_ca_map[4]['mu']["JET_JER_SINGLE_NP__1up"] =  1.198692
f_ca_map[5]['mu']["JET_JER_SINGLE_NP__1up"] =  1.037426
# JET_21NP_JET_EtaIntercalibration_Modelling__1up 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.172659
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.241027
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.327608
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.113637
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.179560
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.157391
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.145089
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.078201
# JET_21NP_JET_EtaIntercalibration_Modelling__1down 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.215650
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.304065
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.360406
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.184707
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.210555
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.211971
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.193701
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.130950
# JET_21NP_JET_EtaIntercalibration_NonClosure__1up 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.177906
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.293254
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.360713
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.142516
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.197403
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.192483
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.194368
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.104379
# JET_21NP_JET_EtaIntercalibration_NonClosure__1down 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.179302
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.271847
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.343681
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.144413
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.187823
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.189638
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.166803
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.091167
# JET_21NP_JET_EtaIntercalibration_TotalStat__1up 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.162581
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.270630
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.329084
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.137075
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.181469
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.175905
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.176487
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.083293
# JET_21NP_JET_EtaIntercalibration_TotalStat__1down 
f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.184300
f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.300792
f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.370178
f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.156716
f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.198625
f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.201295
f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.198145
f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.114301
# JET_21NP_JET_Flavor_Composition__1up 
f_ca_map[2]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  1.080556
f_ca_map[3]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  1.127365
f_ca_map[4]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  1.187038
f_ca_map[5]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  0.992410
f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  1.072870
f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  1.087030
f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  1.046518
f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  0.930011
# JET_21NP_JET_Flavor_Composition__1down 
f_ca_map[2]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.329250
f_ca_map[3]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.390503
f_ca_map[4]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.463725
f_ca_map[5]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.320563
f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.302588
f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.345243
f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.340758
f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.274846
# JET_21NP_JET_Flavor_Response__1up 
f_ca_map[2]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.221841
f_ca_map[3]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.315557
f_ca_map[4]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.385081
f_ca_map[5]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.196258
f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  1.224680
f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  1.235403
f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  1.220181
f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  1.141674
# JET_21NP_JET_Flavor_Response__1down 
f_ca_map[2]['el']["JET_21NP_JET_Flavor_Response__1down"] =  1.151382
f_ca_map[3]['el']["JET_21NP_JET_Flavor_Response__1down"] =  1.241715
f_ca_map[4]['el']["JET_21NP_JET_Flavor_Response__1down"] =  1.315271
f_ca_map[5]['el']["JET_21NP_JET_Flavor_Response__1down"] =  1.105543
f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  1.157789
f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  1.155060
f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  1.132356
f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  1.054674
# JET_21NP_JET_Pileup_OffsetMu__1up 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.177370
f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.285998
f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.353869
f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.142637
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.191249
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.191639
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.175295
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.098333
# JET_21NP_JET_Pileup_OffsetMu__1down 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.172452
f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.275979
f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.354851
f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.140263
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.192083
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.180580
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.182419
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.094755
# JET_21NP_JET_Pileup_OffsetNPV__1up 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.165055
f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.265328
f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.320744
f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.126172
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.169588
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.174022
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.162318
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.065055
# JET_21NP_JET_Pileup_OffsetNPV__1down 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.194728
f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.285536
f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.345410
f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.173417
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.208325
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.214403
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.194186
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.112890
# JET_21NP_JET_Pileup_PtTerm__1up 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.174666
f_ca_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.280272
f_ca_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.357933
f_ca_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.149864
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.195082
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.190189
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.167720
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.102830
# JET_21NP_JET_Pileup_PtTerm__1down 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.183445
f_ca_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.281782
f_ca_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.357755
f_ca_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.147919
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.192659
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.191326
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.179214
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.095246
# JET_21NP_JET_Pileup_RhoTopology__1up 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.116558
f_ca_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.171434
f_ca_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.249400
f_ca_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.038748
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.117852
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.096239
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.094348
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  0.986620
# JET_21NP_JET_Pileup_RhoTopology__1down 
f_ca_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.288876
f_ca_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.361586
f_ca_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.445437
f_ca_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.267058
f_ca_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.266912
f_ca_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.291482
f_ca_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.274788
f_ca_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.216835
# JET_21NP_JET_PunchThrough_MC15__1up 
f_ca_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.175385
f_ca_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.275864
f_ca_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.356663
f_ca_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.149376
f_ca_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.192992
f_ca_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.190828
f_ca_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.174193
f_ca_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.097470
# JET_21NP_JET_PunchThrough_MC15__1down 
f_ca_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.175468
f_ca_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.275542
f_ca_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.356692
f_ca_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.149215
f_ca_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.193011
f_ca_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.190811
f_ca_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.174136
f_ca_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.097699
# JET_21NP_JET_SingleParticle_HighPt__1up 
f_ca_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.175472
f_ca_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.275507
f_ca_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.356618
f_ca_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.149215
f_ca_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.192968
f_ca_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.190832
f_ca_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.174212
f_ca_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.097533
# JET_21NP_JET_SingleParticle_HighPt__1down 
f_ca_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.175471
f_ca_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.275507
f_ca_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.356617
f_ca_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.149216
f_ca_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.192968
f_ca_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.190832
f_ca_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.174213
f_ca_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.097534
# JET_21NP_JET_BJES_Response__1up 
f_ca_map[2]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.174742
f_ca_map[3]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.274757
f_ca_map[4]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.357193
f_ca_map[5]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.147801
f_ca_map[2]['mu']["JET_21NP_JET_BJES_Response__1up"] =  1.193581
f_ca_map[3]['mu']["JET_21NP_JET_BJES_Response__1up"] =  1.190319
f_ca_map[4]['mu']["JET_21NP_JET_BJES_Response__1up"] =  1.173709
f_ca_map[5]['mu']["JET_21NP_JET_BJES_Response__1up"] =  1.096625
# JET_21NP_JET_BJES_Response__1down 
f_ca_map[2]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.176155
f_ca_map[3]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.277613
f_ca_map[4]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.359035
f_ca_map[5]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.150047
f_ca_map[2]['mu']["JET_21NP_JET_BJES_Response__1down"] =  1.193227
f_ca_map[3]['mu']["JET_21NP_JET_BJES_Response__1down"] =  1.192637
f_ca_map[4]['mu']["JET_21NP_JET_BJES_Response__1down"] =  1.175675
f_ca_map[5]['mu']["JET_21NP_JET_BJES_Response__1down"] =  1.098858
# JET_21NP_JET_EffectiveNP_1__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.136177
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.221328
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.279569
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.079141
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.143721
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.133217
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.115070
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.020846
# JET_21NP_JET_EffectiveNP_1__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.241546
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.331798
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.425347
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.226590
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.235638
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.260250
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.246697
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.178857
# JET_21NP_JET_EffectiveNP_2__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.192250
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.296132
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.372154
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.163724
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.202644
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.203247
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.200357
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.118673
# JET_21NP_JET_EffectiveNP_2__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.163119
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.263420
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.334648
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.126787
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.181203
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.172518
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.171745
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.078889
# JET_21NP_JET_EffectiveNP_3__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.172097
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.279257
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.351342
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.144654
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.190958
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.187247
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.174506
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.095348
# JET_21NP_JET_EffectiveNP_3__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.176141
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.285615
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.364259
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.149594
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.193880
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.195667
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.176222
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.098535
# JET_21NP_JET_EffectiveNP_4__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.174990
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.281925
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.362075
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.149000
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.194581
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.191208
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.174260
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.097509
# JET_21NP_JET_EffectiveNP_4__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.174366
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.278768
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.355180
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.145647
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.192270
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.187924
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.174799
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.096275
# JET_21NP_JET_EffectiveNP_5__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.176747
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.275355
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.359664
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.142621
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.193702
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.189167
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.177705
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.096966
# JET_21NP_JET_EffectiveNP_5__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.172189
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.280760
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.356879
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.150510
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.191671
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.191659
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.171968
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.098990
# JET_21NP_JET_EffectiveNP_6__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.169296
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.279885
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.346376
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.146730
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.189811
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.189275
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.173393
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.093703
# JET_21NP_JET_EffectiveNP_6__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.176881
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.281133
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.362416
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.152637
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.194496
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.193983
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.180875
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.099052
# JET_21NP_JET_EffectiveNP_7__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.176135
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.289826
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.364545
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.154040
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.194991
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.197795
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.180353
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.101058
# JET_21NP_JET_EffectiveNP_7__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.169528
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.275738
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.348170
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.143597
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.188059
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.186368
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.174220
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.090792
# JET_21NP_JET_EffectiveNP_8restTerm__1up 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.171771
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.278713
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.353342
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.149259
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.190704
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.191746
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.172540
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.096943
# JET_21NP_JET_EffectiveNP_8restTerm__1down 
f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.176516
f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.276718
f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.361729
f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.147467
f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.194049
f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.191209
f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.176453
f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.097936
# LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.097517
# LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down 
f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.097517
# LARGERJET_Medium_JET_Comb_Baseline_Kin__1up 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.097517
# LARGERJET_Medium_JET_Comb_Baseline_Kin__1down 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.097517
# LARGERJET_Medium_JET_Comb_Modelling_Kin__1up 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.097517
# LARGERJET_Medium_JET_Comb_Modelling_Kin__1down 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.097517
# LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.097517
# LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.097517
# LARGERJET_Medium_JET_Comb_Tracking_Kin__1up 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.097517
# LARGERJET_Medium_JET_Comb_Tracking_Kin__1down 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.097517
# LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.097517
# LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.097517
# LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.097517
# LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.097517
# LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.097517
# LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.097517
# LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.097517
# LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down 
f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.097517
# LARGERJET_Strong_JET_Comb_Baseline_All__1up 
f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.097517
# LARGERJET_Strong_JET_Comb_Baseline_All__1down 
f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.097517
# LARGERJET_Strong_JET_Comb_Modelling_All__1up 
f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.097517
# LARGERJET_Strong_JET_Comb_Modelling_All__1down 
f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.097517
# LARGERJET_Strong_JET_Comb_TotalStat_All__1up 
f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.097517
# LARGERJET_Strong_JET_Comb_TotalStat_All__1down 
f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.097517
# LARGERJET_Strong_JET_Comb_Tracking_All__1up 
f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.097517
# LARGERJET_Strong_JET_Comb_Tracking_All__1down 
f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.175471
f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.275507
f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.356616
f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.149216
f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.192968
f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.190832
f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.174213
f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.097517


# ttxsecup 
frac[2]['el']["ttxsecup"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["ttxsecup"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["ttxsecup"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["ttxsecup"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["ttxsecup"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["ttxsecup"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["ttxsecup"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["ttxsecup"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# ttxsecdw 
frac[2]['el']["ttxsecdw"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["ttxsecdw"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["ttxsecdw"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["ttxsecdw"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["ttxsecdw"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["ttxsecdw"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["ttxsecdw"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["ttxsecdw"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# singletopup 
frac[2]['el']["singletopup"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["singletopup"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["singletopup"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["singletopup"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["singletopup"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["singletopup"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["singletopup"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["singletopup"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# singletopdw 
frac[2]['el']["singletopdw"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["singletopdw"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["singletopdw"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["singletopdw"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["singletopdw"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["singletopdw"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["singletopdw"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["singletopdw"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# wnorm__1up 
frac[2]['el']["wnorm__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["wnorm__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["wnorm__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["wnorm__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["wnorm__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["wnorm__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["wnorm__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["wnorm__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# wnorm__1down 
frac[2]['el']["wnorm__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["wnorm__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["wnorm__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["wnorm__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["wnorm__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["wnorm__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["wnorm__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["wnorm__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# elMisIDpos_up 
frac[2]['el']["elMisIDpos_up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["elMisIDpos_up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["elMisIDpos_up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["elMisIDpos_up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["elMisIDpos_up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["elMisIDpos_up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["elMisIDpos_up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["elMisIDpos_up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# elMisIDpos_down 
frac[2]['el']["elMisIDpos_down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["elMisIDpos_down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["elMisIDpos_down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["elMisIDpos_down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["elMisIDpos_down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["elMisIDpos_down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["elMisIDpos_down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["elMisIDpos_down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# MET_SoftTrk_ResoPara 
frac[2]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.094122,'cc': 0.064271,'c': 0.209090,'l': 0.632517}
frac[3]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.117216,'cc': 0.098634,'c': 0.219076,'l': 0.565074}
frac[4]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.139834,'cc': 0.137539,'c': 0.215314,'l': 0.507313}
frac[5]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.147347,'cc': 0.149739,'c': 0.210533,'l': 0.492380}
frac[2]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.083193,'cc': 0.062878,'c': 0.205023,'l': 0.648905}
frac[3]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.106226,'cc': 0.097082,'c': 0.215610,'l': 0.581083}
frac[4]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.129407,'cc': 0.132989,'c': 0.207510,'l': 0.530095}
frac[5]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.138424,'cc': 0.145063,'c': 0.203416,'l': 0.513097}
# MET_SoftTrk_ResoPerp 
frac[2]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.094084,'cc': 0.064118,'c': 0.209046,'l': 0.632753}
frac[3]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.117264,'cc': 0.098638,'c': 0.218945,'l': 0.565153}
frac[4]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.139829,'cc': 0.137496,'c': 0.215244,'l': 0.507431}
frac[5]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.147388,'cc': 0.149661,'c': 0.210523,'l': 0.492429}
frac[2]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.083234,'cc': 0.063074,'c': 0.204805,'l': 0.648887}
frac[3]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.106247,'cc': 0.097130,'c': 0.215583,'l': 0.581041}
frac[4]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.129370,'cc': 0.132851,'c': 0.207240,'l': 0.530539}
frac[5]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.138404,'cc': 0.144959,'c': 0.203365,'l': 0.513271}
# MET_SoftTrk_ScaleUp 
frac[2]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.094132,'cc': 0.064242,'c': 0.209094,'l': 0.632532}
frac[3]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.117241,'cc': 0.098584,'c': 0.218863,'l': 0.565313}
frac[4]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.139859,'cc': 0.137449,'c': 0.215376,'l': 0.507316}
frac[5]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.147360,'cc': 0.149638,'c': 0.210578,'l': 0.492424}
frac[2]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.083232,'cc': 0.062929,'c': 0.204987,'l': 0.648851}
frac[3]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.106237,'cc': 0.096931,'c': 0.215640,'l': 0.581191}
frac[4]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.129387,'cc': 0.132775,'c': 0.207229,'l': 0.530610}
frac[5]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.138409,'cc': 0.144895,'c': 0.203196,'l': 0.513500}
# MET_SoftTrk_ScaleDown 
frac[2]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.094186,'cc': 0.064171,'c': 0.209228,'l': 0.632416}
frac[3]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.117284,'cc': 0.098719,'c': 0.218967,'l': 0.565030}
frac[4]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.139846,'cc': 0.137496,'c': 0.215530,'l': 0.507128}
frac[5]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.147328,'cc': 0.149639,'c': 0.210751,'l': 0.492283}
frac[2]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.083227,'cc': 0.063032,'c': 0.205057,'l': 0.648684}
frac[3]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.106161,'cc': 0.096846,'c': 0.215437,'l': 0.581556}
frac[4]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.129236,'cc': 0.132703,'c': 0.207546,'l': 0.530515}
frac[5]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.138313,'cc': 0.144867,'c': 0.203565,'l': 0.513255}
# EG_RESOLUTION_ALL__1up 
frac[2]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.094168,'cc': 0.064205,'c': 0.209062,'l': 0.632565}
frac[3]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.117295,'cc': 0.098676,'c': 0.218891,'l': 0.565139}
frac[4]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.139646,'cc': 0.137548,'c': 0.215299,'l': 0.507507}
frac[5]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.147221,'cc': 0.149664,'c': 0.210548,'l': 0.492567}
frac[2]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648701}
frac[3]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581235}
frac[4]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203288,'l': 0.513496}
# EG_RESOLUTION_ALL__1down 
frac[2]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.094198,'cc': 0.064240,'c': 0.209302,'l': 0.632260}
frac[3]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.117278,'cc': 0.098655,'c': 0.218762,'l': 0.565305}
frac[4]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.139791,'cc': 0.137458,'c': 0.215525,'l': 0.507227}
frac[5]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.147307,'cc': 0.149651,'c': 0.210694,'l': 0.492348}
frac[2]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530693}
frac[5]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.138330,'cc': 0.144888,'c': 0.203287,'l': 0.513495}
# EG_SCALE_ALL__1up 
frac[2]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.094154,'cc': 0.064162,'c': 0.209215,'l': 0.632470}
frac[3]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.117344,'cc': 0.098695,'c': 0.218900,'l': 0.565061}
frac[4]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.139675,'cc': 0.137465,'c': 0.215400,'l': 0.507460}
frac[5]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.147238,'cc': 0.149609,'c': 0.210640,'l': 0.492513}
frac[2]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648701}
frac[3]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203288,'l': 0.513496}
# EG_SCALE_ALL__1down 
frac[2]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.094174,'cc': 0.064213,'c': 0.209278,'l': 0.632335}
frac[3]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.117279,'cc': 0.098739,'c': 0.218973,'l': 0.565009}
frac[4]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.139764,'cc': 0.137491,'c': 0.215477,'l': 0.507268}
frac[5]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.147294,'cc': 0.149650,'c': 0.210684,'l': 0.492372}
frac[2]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215636,'l': 0.581234}
frac[4]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.129284,'cc': 0.132729,'c': 0.207294,'l': 0.530693}
frac[5]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.138330,'cc': 0.144888,'c': 0.203287,'l': 0.513495}
# MUON_ID__1up 
frac[2]['el']["MUON_ID__1up"] = {'bb': 0.094189,'cc': 0.064219,'c': 0.209175,'l': 0.632417}
frac[3]['el']["MUON_ID__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["MUON_ID__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["MUON_ID__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["MUON_ID__1up"] = {'bb': 0.083234,'cc': 0.063023,'c': 0.205066,'l': 0.648676}
frac[3]['mu']["MUON_ID__1up"] = {'bb': 0.106135,'cc': 0.096922,'c': 0.215631,'l': 0.581312}
frac[4]['mu']["MUON_ID__1up"] = {'bb': 0.129261,'cc': 0.132697,'c': 0.207418,'l': 0.530624}
frac[5]['mu']["MUON_ID__1up"] = {'bb': 0.138292,'cc': 0.144814,'c': 0.203390,'l': 0.513504}
# MUON_ID__1down 
frac[2]['el']["MUON_ID__1down"] = {'bb': 0.094189,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["MUON_ID__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["MUON_ID__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["MUON_ID__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["MUON_ID__1down"] = {'bb': 0.083264,'cc': 0.063009,'c': 0.204985,'l': 0.648742}
frac[3]['mu']["MUON_ID__1down"] = {'bb': 0.106162,'cc': 0.096899,'c': 0.215631,'l': 0.581308}
frac[4]['mu']["MUON_ID__1down"] = {'bb': 0.129237,'cc': 0.132727,'c': 0.207370,'l': 0.530665}
frac[5]['mu']["MUON_ID__1down"] = {'bb': 0.138277,'cc': 0.144866,'c': 0.203361,'l': 0.513495}
# MUON_MS__1up 
frac[2]['el']["MUON_MS__1up"] = {'bb': 0.094189,'cc': 0.064219,'c': 0.209175,'l': 0.632417}
frac[3]['el']["MUON_MS__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["MUON_MS__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["MUON_MS__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["MUON_MS__1up"] = {'bb': 0.083220,'cc': 0.063015,'c': 0.204957,'l': 0.648807}
frac[3]['mu']["MUON_MS__1up"] = {'bb': 0.106164,'cc': 0.096908,'c': 0.215621,'l': 0.581307}
frac[4]['mu']["MUON_MS__1up"] = {'bb': 0.129314,'cc': 0.132683,'c': 0.207294,'l': 0.530709}
frac[5]['mu']["MUON_MS__1up"] = {'bb': 0.138340,'cc': 0.144839,'c': 0.203337,'l': 0.513484}
# MUON_MS__1down 
frac[2]['el']["MUON_MS__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["MUON_MS__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["MUON_MS__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["MUON_MS__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["MUON_MS__1down"] = {'bb': 0.083239,'cc': 0.063038,'c': 0.205021,'l': 0.648702}
frac[3]['mu']["MUON_MS__1down"] = {'bb': 0.106179,'cc': 0.096879,'c': 0.215719,'l': 0.581223}
frac[4]['mu']["MUON_MS__1down"] = {'bb': 0.129250,'cc': 0.132705,'c': 0.207182,'l': 0.530863}
frac[5]['mu']["MUON_MS__1down"] = {'bb': 0.138314,'cc': 0.144839,'c': 0.203205,'l': 0.513641}
# MUON_SCALE__1up 
frac[2]['el']["MUON_SCALE__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["MUON_SCALE__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["MUON_SCALE__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["MUON_SCALE__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["MUON_SCALE__1up"] = {'bb': 0.083244,'cc': 0.063032,'c': 0.204984,'l': 0.648740}
frac[3]['mu']["MUON_SCALE__1up"] = {'bb': 0.106196,'cc': 0.096980,'c': 0.215635,'l': 0.581189}
frac[4]['mu']["MUON_SCALE__1up"] = {'bb': 0.129333,'cc': 0.132726,'c': 0.207296,'l': 0.530645}
frac[5]['mu']["MUON_SCALE__1up"] = {'bb': 0.138356,'cc': 0.144891,'c': 0.203288,'l': 0.513465}
# MUON_SCALE__1down 
frac[2]['el']["MUON_SCALE__1down"] = {'bb': 0.094189,'cc': 0.064219,'c': 0.209175,'l': 0.632417}
frac[3]['el']["MUON_SCALE__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["MUON_SCALE__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["MUON_SCALE__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["MUON_SCALE__1down"] = {'bb': 0.083225,'cc': 0.063025,'c': 0.205022,'l': 0.648728}
frac[3]['mu']["MUON_SCALE__1down"] = {'bb': 0.106217,'cc': 0.096885,'c': 0.215568,'l': 0.581330}
frac[4]['mu']["MUON_SCALE__1down"] = {'bb': 0.129302,'cc': 0.132689,'c': 0.207338,'l': 0.530671}
frac[5]['mu']["MUON_SCALE__1down"] = {'bb': 0.138334,'cc': 0.144855,'c': 0.203351,'l': 0.513460}
# MUON_SAGITTA_RESBIAS__1up 
frac[2]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# MUON_SAGITTA_RESBIAS__1down 
frac[2]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# MUON_SAGITTA_RHO__1up 
frac[2]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# MUON_SAGITTA_RHO__1down 
frac[2]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# JET_JER_SINGLE_NP__1up 
frac[2]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.093226,'cc': 0.063181,'c': 0.207512,'l': 0.636081}
frac[3]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.117276,'cc': 0.097364,'c': 0.218170,'l': 0.567190}
frac[4]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.137566,'cc': 0.134219,'c': 0.214706,'l': 0.513509}
frac[5]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.145870,'cc': 0.146636,'c': 0.210010,'l': 0.497483}
frac[2]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.082779,'cc': 0.062074,'c': 0.204043,'l': 0.651104}
frac[3]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.106255,'cc': 0.095344,'c': 0.215392,'l': 0.583009}
frac[4]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.128808,'cc': 0.131273,'c': 0.208569,'l': 0.531350}
frac[5]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.137718,'cc': 0.143169,'c': 0.204364,'l': 0.514748}
# JET_21NP_JET_EtaIntercalibration_Modelling__1up 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.093832,'cc': 0.063733,'c': 0.208928,'l': 0.633507}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.117021,'cc': 0.098245,'c': 0.218586,'l': 0.566149}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.139306,'cc': 0.136394,'c': 0.216132,'l': 0.508168}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.146874,'cc': 0.148624,'c': 0.211324,'l': 0.493178}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.083067,'cc': 0.062520,'c': 0.205039,'l': 0.649374}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.105962,'cc': 0.096404,'c': 0.215132,'l': 0.582502}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.128484,'cc': 0.131608,'c': 0.207505,'l': 0.532403}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.137650,'cc': 0.143925,'c': 0.203607,'l': 0.514819}
# JET_21NP_JET_EtaIntercalibration_Modelling__1down 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.094485,'cc': 0.064608,'c': 0.209143,'l': 0.631764}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.117733,'cc': 0.099602,'c': 0.219011,'l': 0.563655}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.139965,'cc': 0.137727,'c': 0.214801,'l': 0.507506}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.147496,'cc': 0.150084,'c': 0.210118,'l': 0.492302}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.083464,'cc': 0.063412,'c': 0.205022,'l': 0.648102}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.106703,'cc': 0.097702,'c': 0.215375,'l': 0.580221}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.129438,'cc': 0.133078,'c': 0.206282,'l': 0.531202}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.138486,'cc': 0.145353,'c': 0.202459,'l': 0.513702}
# JET_21NP_JET_EtaIntercalibration_NonClosure__1up 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.094206,'cc': 0.064150,'c': 0.209318,'l': 0.632326}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.117329,'cc': 0.098971,'c': 0.218809,'l': 0.564891}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.140066,'cc': 0.137433,'c': 0.215334,'l': 0.507166}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.147520,'cc': 0.149691,'c': 0.210503,'l': 0.492285}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.083223,'cc': 0.063023,'c': 0.205093,'l': 0.648661}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.106307,'cc': 0.097046,'c': 0.215318,'l': 0.581328}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.129508,'cc': 0.132926,'c': 0.208197,'l': 0.529370}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.138438,'cc': 0.145080,'c': 0.203847,'l': 0.512635}
# JET_21NP_JET_EtaIntercalibration_NonClosure__1down 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.094119,'cc': 0.064072,'c': 0.209004,'l': 0.632806}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.117313,'cc': 0.098442,'c': 0.219052,'l': 0.565193}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.139697,'cc': 0.137202,'c': 0.215647,'l': 0.507454}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.147290,'cc': 0.149577,'c': 0.210801,'l': 0.492332}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.083203,'cc': 0.062894,'c': 0.204951,'l': 0.648951}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.106130,'cc': 0.096671,'c': 0.215639,'l': 0.581560}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.129291,'cc': 0.132470,'c': 0.207172,'l': 0.531067}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.138316,'cc': 0.144703,'c': 0.203190,'l': 0.513791}
# JET_21NP_JET_EtaIntercalibration_TotalStat__1up 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.093982,'cc': 0.064029,'c': 0.208883,'l': 0.633106}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.117164,'cc': 0.098417,'c': 0.218933,'l': 0.565486}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.139843,'cc': 0.137156,'c': 0.215787,'l': 0.507214}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.147340,'cc': 0.149322,'c': 0.210885,'l': 0.492453}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.083190,'cc': 0.062826,'c': 0.204992,'l': 0.648992}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.106006,'cc': 0.096669,'c': 0.215477,'l': 0.581848}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.129196,'cc': 0.132493,'c': 0.207413,'l': 0.530898}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.138247,'cc': 0.144677,'c': 0.203436,'l': 0.513640}
# JET_21NP_JET_EtaIntercalibration_TotalStat__1down 
frac[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.094323,'cc': 0.064396,'c': 0.209183,'l': 0.632099}
frac[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.117377,'cc': 0.098951,'c': 0.219042,'l': 0.564630}
frac[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.140142,'cc': 0.137735,'c': 0.215163,'l': 0.506960}
frac[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.147670,'cc': 0.149993,'c': 0.210586,'l': 0.491751}
frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.083368,'cc': 0.063303,'c': 0.205007,'l': 0.648322}
frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.106394,'cc': 0.097185,'c': 0.215416,'l': 0.581005}
frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.129590,'cc': 0.133301,'c': 0.207281,'l': 0.529828}
frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.138550,'cc': 0.145390,'c': 0.203155,'l': 0.512905}
# JET_21NP_JET_Flavor_Composition__1up 
frac[2]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.091699,'cc': 0.062130,'c': 0.208266,'l': 0.637906}
frac[3]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.114519,'cc': 0.095910,'c': 0.217702,'l': 0.571868}
frac[4]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.136115,'cc': 0.132176,'c': 0.218667,'l': 0.513043}
frac[5]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.143612,'cc': 0.144898,'c': 0.213895,'l': 0.497595}
frac[2]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.081334,'cc': 0.060889,'c': 0.203328,'l': 0.654449}
frac[3]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.103708,'cc': 0.093975,'c': 0.215915,'l': 0.586403}
frac[4]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.125469,'cc': 0.128208,'c': 0.209647,'l': 0.536676}
frac[5]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.134260,'cc': 0.140826,'c': 0.206002,'l': 0.518913}
# JET_21NP_JET_Flavor_Composition__1down 
frac[2]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.096691,'cc': 0.066463,'c': 0.209918,'l': 0.626929}
frac[3]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.121163,'cc': 0.102631,'c': 0.218731,'l': 0.557475}
frac[4]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.143103,'cc': 0.139399,'c': 0.212828,'l': 0.504670}
frac[5]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.150904,'cc': 0.152085,'c': 0.207871,'l': 0.489141}
frac[2]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.085232,'cc': 0.065263,'c': 0.205797,'l': 0.643708}
frac[3]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.109601,'cc': 0.100397,'c': 0.215278,'l': 0.574724}
frac[4]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.133604,'cc': 0.136477,'c': 0.205295,'l': 0.524624}
frac[5]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.142953,'cc': 0.148491,'c': 0.200832,'l': 0.507725}
# JET_21NP_JET_Flavor_Response__1up 
frac[2]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.094888,'cc': 0.064868,'c': 0.209275,'l': 0.630968}
frac[3]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.118150,'cc': 0.099570,'c': 0.219159,'l': 0.563121}
frac[4]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.140899,'cc': 0.138369,'c': 0.214555,'l': 0.506176}
frac[5]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.148478,'cc': 0.150646,'c': 0.209848,'l': 0.491028}
frac[2]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.083810,'cc': 0.063627,'c': 0.205024,'l': 0.647540}
frac[3]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.107327,'cc': 0.097955,'c': 0.215507,'l': 0.579211}
frac[4]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.129851,'cc': 0.133410,'c': 0.205413,'l': 0.531326}
frac[5]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.139158,'cc': 0.145687,'c': 0.201841,'l': 0.513314}
# JET_21NP_JET_Flavor_Response__1down 
frac[2]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.093335,'cc': 0.063331,'c': 0.208944,'l': 0.634390}
frac[3]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.116476,'cc': 0.097980,'c': 0.218446,'l': 0.567098}
frac[4]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.138806,'cc': 0.135889,'c': 0.217356,'l': 0.507950}
frac[5]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.146273,'cc': 0.148169,'c': 0.212224,'l': 0.493333}
frac[2]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.082867,'cc': 0.062472,'c': 0.204823,'l': 0.649838}
frac[3]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.105218,'cc': 0.095996,'c': 0.215213,'l': 0.583574}
frac[4]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.128101,'cc': 0.131174,'c': 0.208248,'l': 0.532477}
frac[5]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.137107,'cc': 0.143488,'c': 0.204287,'l': 0.515118}
# JET_21NP_JET_Pileup_OffsetMu__1up 
frac[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.094256,'cc': 0.064304,'c': 0.208939,'l': 0.632501}
frac[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.117251,'cc': 0.098952,'c': 0.219221,'l': 0.564577}
frac[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.140034,'cc': 0.137456,'c': 0.215490,'l': 0.507020}
frac[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.147475,'cc': 0.149655,'c': 0.210622,'l': 0.492248}
frac[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.083294,'cc': 0.063059,'c': 0.204865,'l': 0.648782}
frac[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.106280,'cc': 0.096910,'c': 0.215404,'l': 0.581405}
frac[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.129224,'cc': 0.132674,'c': 0.207360,'l': 0.530742}
frac[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.138285,'cc': 0.144906,'c': 0.203305,'l': 0.513504}
# JET_21NP_JET_Pileup_OffsetMu__1down 
frac[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.094092,'cc': 0.064150,'c': 0.209264,'l': 0.632493}
frac[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.117362,'cc': 0.098495,'c': 0.218646,'l': 0.565498}
frac[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.139607,'cc': 0.137260,'c': 0.215469,'l': 0.507663}
frac[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.147277,'cc': 0.149506,'c': 0.210755,'l': 0.492462}
frac[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.083258,'cc': 0.063051,'c': 0.205174,'l': 0.648518}
frac[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.106069,'cc': 0.097005,'c': 0.215425,'l': 0.581500}
frac[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.129526,'cc': 0.132764,'c': 0.207226,'l': 0.530484}
frac[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.138473,'cc': 0.144948,'c': 0.203246,'l': 0.513333}
# JET_21NP_JET_Pileup_OffsetNPV__1up 
frac[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.093792,'cc': 0.063796,'c': 0.209200,'l': 0.633212}
frac[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.116980,'cc': 0.098334,'c': 0.218852,'l': 0.565834}
frac[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.140134,'cc': 0.136520,'c': 0.216638,'l': 0.506708}
frac[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.147357,'cc': 0.148737,'c': 0.211397,'l': 0.492509}
frac[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.083270,'cc': 0.062739,'c': 0.204781,'l': 0.649210}
frac[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.105957,'cc': 0.096162,'c': 0.215452,'l': 0.582429}
frac[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.128599,'cc': 0.131604,'c': 0.207469,'l': 0.532329}
frac[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.137613,'cc': 0.143570,'c': 0.203763,'l': 0.515054}
# JET_21NP_JET_Pileup_OffsetNPV__1down 
frac[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.094548,'cc': 0.064442,'c': 0.209529,'l': 0.631481}
frac[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.117376,'cc': 0.098950,'c': 0.218789,'l': 0.564885}
frac[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.140092,'cc': 0.137779,'c': 0.215552,'l': 0.506577}
frac[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.147631,'cc': 0.150104,'c': 0.210491,'l': 0.491774}
frac[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.083507,'cc': 0.063253,'c': 0.205295,'l': 0.647945}
frac[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.106587,'cc': 0.097659,'c': 0.215095,'l': 0.580659}
frac[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.129620,'cc': 0.133520,'c': 0.206563,'l': 0.530297}
frac[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.138768,'cc': 0.145737,'c': 0.202571,'l': 0.512924}
# JET_21NP_JET_Pileup_PtTerm__1up 
frac[2]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.094198,'cc': 0.064169,'c': 0.209089,'l': 0.632543}
frac[3]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.117258,'cc': 0.098656,'c': 0.219031,'l': 0.565055}
frac[4]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.139850,'cc': 0.137384,'c': 0.215261,'l': 0.507504}
frac[5]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.147362,'cc': 0.149626,'c': 0.210609,'l': 0.492403}
frac[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.083242,'cc': 0.063008,'c': 0.204822,'l': 0.648928}
frac[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.106158,'cc': 0.096853,'c': 0.215637,'l': 0.581353}
frac[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.129347,'cc': 0.132664,'c': 0.207181,'l': 0.530808}
frac[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.138376,'cc': 0.144820,'c': 0.203231,'l': 0.513572}
# JET_21NP_JET_Pileup_PtTerm__1down 
frac[2]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.094219,'cc': 0.064274,'c': 0.209390,'l': 0.632117}
frac[3]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.117272,'cc': 0.098703,'c': 0.218796,'l': 0.565229}
frac[4]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.139747,'cc': 0.137334,'c': 0.215747,'l': 0.507173}
frac[5]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.147296,'cc': 0.149559,'c': 0.210841,'l': 0.492303}
frac[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.083246,'cc': 0.063066,'c': 0.205070,'l': 0.648619}
frac[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.106230,'cc': 0.096970,'c': 0.215379,'l': 0.581421}
frac[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.129343,'cc': 0.132718,'c': 0.207416,'l': 0.530522}
frac[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.138366,'cc': 0.144939,'c': 0.203283,'l': 0.513413}
# JET_21NP_JET_Pileup_RhoTopology__1up 
frac[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.092981,'cc': 0.062434,'c': 0.208625,'l': 0.635960}
frac[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.116270,'cc': 0.096783,'c': 0.217406,'l': 0.569541}
frac[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.138692,'cc': 0.133484,'c': 0.217871,'l': 0.509953}
frac[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.146254,'cc': 0.145995,'c': 0.212796,'l': 0.494955}
frac[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.082539,'cc': 0.061567,'c': 0.203976,'l': 0.651918}
frac[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.105084,'cc': 0.094509,'c': 0.215085,'l': 0.585321}
frac[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.128317,'cc': 0.129268,'c': 0.209057,'l': 0.533358}
frac[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.137119,'cc': 0.141726,'c': 0.205244,'l': 0.515911}
# JET_21NP_JET_Pileup_RhoTopology__1down 
frac[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.095169,'cc': 0.065497,'c': 0.209992,'l': 0.629342}
frac[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.118531,'cc': 0.101137,'c': 0.218826,'l': 0.561507}
frac[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.140763,'cc': 0.139758,'c': 0.214715,'l': 0.504763}
frac[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.148209,'cc': 0.152076,'c': 0.209652,'l': 0.490063}
frac[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.083964,'cc': 0.064544,'c': 0.205459,'l': 0.646033}
frac[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.107647,'cc': 0.099209,'c': 0.215308,'l': 0.577837}
frac[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.130409,'cc': 0.135185,'c': 0.205985,'l': 0.528422}
frac[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.139640,'cc': 0.147263,'c': 0.201843,'l': 0.511254}
# JET_21NP_JET_PunchThrough_MC15__1up 
frac[2]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.094190,'cc': 0.064222,'c': 0.209175,'l': 0.632414}
frac[3]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.117296,'cc': 0.098664,'c': 0.218955,'l': 0.565084}
frac[4]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.139788,'cc': 0.137485,'c': 0.215465,'l': 0.507261}
frac[5]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.147320,'cc': 0.149635,'c': 0.210684,'l': 0.492361}
frac[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.083238,'cc': 0.063033,'c': 0.205029,'l': 0.648700}
frac[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.106214,'cc': 0.096920,'c': 0.215632,'l': 0.581234}
frac[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.129286,'cc': 0.132728,'c': 0.207292,'l': 0.530694}
frac[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.138333,'cc': 0.144888,'c': 0.203285,'l': 0.513494}
# JET_21NP_JET_PunchThrough_MC15__1down 
frac[2]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.094189,'cc': 0.064218,'c': 0.209174,'l': 0.632419}
frac[3]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.117292,'cc': 0.098679,'c': 0.218955,'l': 0.565073}
frac[4]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215467,'l': 0.507259}
frac[5]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.147320,'cc': 0.149638,'c': 0.210685,'l': 0.492357}
frac[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205029,'l': 0.648699}
frac[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.106209,'cc': 0.096922,'c': 0.215628,'l': 0.581241}
frac[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.129285,'cc': 0.132727,'c': 0.207296,'l': 0.530692}
frac[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.138330,'cc': 0.144889,'c': 0.203288,'l': 0.513493}
# JET_21NP_JET_SingleParticle_HighPt__1up 
frac[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530693}
frac[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203288,'l': 0.513496}
# JET_21NP_JET_SingleParticle_HighPt__1down 
frac[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203288,'l': 0.513496}
# JET_21NP_JET_BJES_Response__1up 
frac[2]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.094451,'cc': 0.064201,'c': 0.209114,'l': 0.632234}
frac[3]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.117753,'cc': 0.098629,'c': 0.218839,'l': 0.564779}
frac[4]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.140342,'cc': 0.137399,'c': 0.215327,'l': 0.506932}
frac[5]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.147909,'cc': 0.149534,'c': 0.210538,'l': 0.492018}
frac[2]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.083453,'cc': 0.063018,'c': 0.204979,'l': 0.648549}
frac[3]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.106591,'cc': 0.096879,'c': 0.215543,'l': 0.580987}
frac[4]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.129845,'cc': 0.132643,'c': 0.207161,'l': 0.530351}
frac[5]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.138927,'cc': 0.144787,'c': 0.203146,'l': 0.513139}
# JET_21NP_JET_BJES_Response__1down 
frac[2]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.093957,'cc': 0.064236,'c': 0.209228,'l': 0.632579}
frac[3]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.116844,'cc': 0.098731,'c': 0.219066,'l': 0.565359}
frac[4]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.139125,'cc': 0.137593,'c': 0.215632,'l': 0.507649}
frac[5]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.146624,'cc': 0.149760,'c': 0.210856,'l': 0.492759}
frac[2]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.083024,'cc': 0.063048,'c': 0.205076,'l': 0.648852}
frac[3]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.105836,'cc': 0.096961,'c': 0.215726,'l': 0.581478}
frac[4]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.128762,'cc': 0.132810,'c': 0.207418,'l': 0.531010}
frac[5]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.137755,'cc': 0.144986,'c': 0.203422,'l': 0.513837}
# JET_21NP_JET_EffectiveNP_1__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.093298,'cc': 0.062842,'c': 0.208664,'l': 0.635196}
frac[3]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.116667,'cc': 0.097460,'c': 0.218103,'l': 0.567770}
frac[4]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.139263,'cc': 0.134774,'c': 0.217193,'l': 0.508770}
frac[5]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.146719,'cc': 0.147335,'c': 0.212163,'l': 0.493783}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.082843,'cc': 0.062094,'c': 0.204220,'l': 0.650842}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.105494,'cc': 0.095133,'c': 0.215654,'l': 0.583720}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.128088,'cc': 0.130082,'c': 0.208009,'l': 0.533821}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.137133,'cc': 0.142532,'c': 0.204176,'l': 0.516159}
# JET_21NP_JET_EffectiveNP_1__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.094930,'cc': 0.065134,'c': 0.209515,'l': 0.630421}
frac[3]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.118089,'cc': 0.100590,'c': 0.219086,'l': 0.562235}
frac[4]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.140504,'cc': 0.138883,'c': 0.214784,'l': 0.505829}
frac[5]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.148060,'cc': 0.151276,'c': 0.209888,'l': 0.490775}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.083752,'cc': 0.064126,'c': 0.205287,'l': 0.646834}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.107262,'cc': 0.098372,'c': 0.215254,'l': 0.579112}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.129735,'cc': 0.134604,'c': 0.205705,'l': 0.529956}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.139016,'cc': 0.146605,'c': 0.201988,'l': 0.512391}
# JET_21NP_JET_EffectiveNP_2__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.094330,'cc': 0.064410,'c': 0.209166,'l': 0.632094}
frac[3]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.117452,'cc': 0.098872,'c': 0.219074,'l': 0.564603}
frac[4]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.140159,'cc': 0.137874,'c': 0.215191,'l': 0.506777}
frac[5]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.147663,'cc': 0.150058,'c': 0.210455,'l': 0.491824}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.083372,'cc': 0.063365,'c': 0.205073,'l': 0.648190}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.106442,'cc': 0.097294,'c': 0.215425,'l': 0.580840}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.129480,'cc': 0.133200,'c': 0.207178,'l': 0.530141}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.138520,'cc': 0.145355,'c': 0.203098,'l': 0.513026}
# JET_21NP_JET_EffectiveNP_2__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.093936,'cc': 0.063979,'c': 0.208877,'l': 0.633208}
frac[3]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.117161,'cc': 0.098369,'c': 0.219042,'l': 0.565427}
frac[4]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.139830,'cc': 0.136942,'c': 0.215737,'l': 0.507490}
frac[5]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.147310,'cc': 0.149221,'c': 0.210924,'l': 0.492545}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.083151,'cc': 0.062795,'c': 0.205063,'l': 0.648991}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.105935,'cc': 0.096502,'c': 0.215394,'l': 0.582169}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.129222,'cc': 0.132279,'c': 0.207677,'l': 0.530823}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.138245,'cc': 0.144503,'c': 0.203668,'l': 0.513584}
# JET_21NP_JET_EffectiveNP_3__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.094158,'cc': 0.064184,'c': 0.209199,'l': 0.632459}
frac[3]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.117261,'cc': 0.098698,'c': 0.218840,'l': 0.565201}
frac[4]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.139723,'cc': 0.137388,'c': 0.215658,'l': 0.507231}
frac[5]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.147328,'cc': 0.149580,'c': 0.210865,'l': 0.492227}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.083213,'cc': 0.062960,'c': 0.205034,'l': 0.648794}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.106117,'cc': 0.096843,'c': 0.215720,'l': 0.581320}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.129363,'cc': 0.132791,'c': 0.207246,'l': 0.530601}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.138370,'cc': 0.144930,'c': 0.203295,'l': 0.513405}
# JET_21NP_JET_EffectiveNP_3__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.094194,'cc': 0.064201,'c': 0.209240,'l': 0.632365}
frac[3]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.117401,'cc': 0.098663,'c': 0.218962,'l': 0.564974}
frac[4]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.139823,'cc': 0.137674,'c': 0.215454,'l': 0.507049}
frac[5]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.147319,'cc': 0.149803,'c': 0.210641,'l': 0.492237}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.083249,'cc': 0.063132,'c': 0.204916,'l': 0.648703}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.106285,'cc': 0.096947,'c': 0.215699,'l': 0.581069}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.129397,'cc': 0.132825,'c': 0.207323,'l': 0.530455}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.138413,'cc': 0.144994,'c': 0.203291,'l': 0.513303}
# JET_21NP_JET_EffectiveNP_4__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.094184,'cc': 0.064241,'c': 0.209176,'l': 0.632399}
frac[3]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.117375,'cc': 0.098582,'c': 0.219006,'l': 0.565036}
frac[4]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.139819,'cc': 0.137560,'c': 0.215399,'l': 0.507222}
frac[5]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.147331,'cc': 0.149718,'c': 0.210615,'l': 0.492336}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.083258,'cc': 0.063114,'c': 0.204971,'l': 0.648657}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.106226,'cc': 0.096946,'c': 0.215645,'l': 0.581182}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.129370,'cc': 0.132738,'c': 0.207287,'l': 0.530605}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.138382,'cc': 0.144900,'c': 0.203290,'l': 0.513428}
# JET_21NP_JET_EffectiveNP_4__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.094174,'cc': 0.064205,'c': 0.209214,'l': 0.632407}
frac[3]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.117254,'cc': 0.098663,'c': 0.219021,'l': 0.565062}
frac[4]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.139771,'cc': 0.137473,'c': 0.215454,'l': 0.507302}
frac[5]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.147349,'cc': 0.149647,'c': 0.210717,'l': 0.492287}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.083241,'cc': 0.062990,'c': 0.205002,'l': 0.648767}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.106156,'cc': 0.096874,'c': 0.215721,'l': 0.581250}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.129369,'cc': 0.132792,'c': 0.207225,'l': 0.530613}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.138385,'cc': 0.144944,'c': 0.203274,'l': 0.513397}
# JET_21NP_JET_EffectiveNP_5__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.094181,'cc': 0.064236,'c': 0.209255,'l': 0.632328}
frac[3]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.117342,'cc': 0.098668,'c': 0.218953,'l': 0.565037}
frac[4]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.139750,'cc': 0.137485,'c': 0.215473,'l': 0.507292}
frac[5]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.147310,'cc': 0.149688,'c': 0.210690,'l': 0.492312}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.083237,'cc': 0.063056,'c': 0.205007,'l': 0.648699}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.106217,'cc': 0.096936,'c': 0.215687,'l': 0.581159}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.129346,'cc': 0.132686,'c': 0.207255,'l': 0.530713}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.138366,'cc': 0.144873,'c': 0.203241,'l': 0.513520}
# JET_21NP_JET_EffectiveNP_5__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.094188,'cc': 0.064196,'c': 0.209150,'l': 0.632465}
frac[3]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.117259,'cc': 0.098589,'c': 0.219003,'l': 0.565149}
frac[4]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.139887,'cc': 0.137548,'c': 0.215573,'l': 0.506992}
frac[5]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.147380,'cc': 0.149666,'c': 0.210763,'l': 0.492192}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.083247,'cc': 0.063040,'c': 0.205000,'l': 0.648712}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.106152,'cc': 0.096867,'c': 0.215714,'l': 0.581268}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.129335,'cc': 0.132834,'c': 0.207220,'l': 0.530611}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.138359,'cc': 0.144950,'c': 0.203224,'l': 0.513466}
# JET_21NP_JET_EffectiveNP_6__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.094150,'cc': 0.064154,'c': 0.209152,'l': 0.632544}
frac[3]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.117229,'cc': 0.098655,'c': 0.218746,'l': 0.565371}
frac[4]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.139821,'cc': 0.137471,'c': 0.215740,'l': 0.506968}
frac[5]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.147341,'cc': 0.149620,'c': 0.210875,'l': 0.492164}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.083205,'cc': 0.062971,'c': 0.204978,'l': 0.648847}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.106118,'cc': 0.096850,'c': 0.215857,'l': 0.581175}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.129278,'cc': 0.132686,'c': 0.207072,'l': 0.530963}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.138310,'cc': 0.144851,'c': 0.203165,'l': 0.513673}
# JET_21NP_JET_EffectiveNP_6__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.094186,'cc': 0.064210,'c': 0.209303,'l': 0.632300}
frac[3]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.117428,'cc': 0.098708,'c': 0.218939,'l': 0.564924}
frac[4]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.139789,'cc': 0.137682,'c': 0.215573,'l': 0.506956}
frac[5]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.147313,'cc': 0.149817,'c': 0.210698,'l': 0.492172}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.083256,'cc': 0.063077,'c': 0.205000,'l': 0.648667}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.106285,'cc': 0.096953,'c': 0.215681,'l': 0.581080}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.129376,'cc': 0.132940,'c': 0.207336,'l': 0.530348}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.138386,'cc': 0.145066,'c': 0.203293,'l': 0.513255}
# JET_21NP_JET_EffectiveNP_7__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.094203,'cc': 0.064225,'c': 0.209203,'l': 0.632370}
frac[3]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.117427,'cc': 0.098713,'c': 0.218995,'l': 0.564865}
frac[4]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.139796,'cc': 0.137683,'c': 0.215485,'l': 0.507036}
frac[5]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.147310,'cc': 0.149805,'c': 0.210651,'l': 0.492235}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.083252,'cc': 0.063145,'c': 0.204942,'l': 0.648661}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.106280,'cc': 0.097008,'c': 0.215617,'l': 0.581094}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.129439,'cc': 0.132842,'c': 0.207472,'l': 0.530247}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.138439,'cc': 0.144995,'c': 0.203389,'l': 0.513177}
# JET_21NP_JET_EffectiveNP_7__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.094133,'cc': 0.064153,'c': 0.209181,'l': 0.632533}
frac[3]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.117209,'cc': 0.098612,'c': 0.218795,'l': 0.565385}
frac[4]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.139769,'cc': 0.137448,'c': 0.215760,'l': 0.507023}
frac[5]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.147322,'cc': 0.149608,'c': 0.210890,'l': 0.492180}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.083204,'cc': 0.062951,'c': 0.204995,'l': 0.648849}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.106076,'cc': 0.096795,'c': 0.215736,'l': 0.581392}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.129286,'cc': 0.132602,'c': 0.207077,'l': 0.531034}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.138326,'cc': 0.144788,'c': 0.203192,'l': 0.513694}
# JET_21NP_JET_EffectiveNP_8restTerm__1up 
frac[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.094181,'cc': 0.064197,'c': 0.209201,'l': 0.632421}
frac[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.117260,'cc': 0.098651,'c': 0.218982,'l': 0.565107}
frac[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.139875,'cc': 0.137553,'c': 0.215541,'l': 0.507030}
frac[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.147379,'cc': 0.149683,'c': 0.210733,'l': 0.492205}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.083259,'cc': 0.062999,'c': 0.205047,'l': 0.648695}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.106159,'cc': 0.096883,'c': 0.215731,'l': 0.581227}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.129298,'cc': 0.132846,'c': 0.207182,'l': 0.530674}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.138332,'cc': 0.144967,'c': 0.203203,'l': 0.513498}
# JET_21NP_JET_EffectiveNP_8restTerm__1down 
frac[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.094181,'cc': 0.064230,'c': 0.209223,'l': 0.632366}
frac[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.117369,'cc': 0.098689,'c': 0.218897,'l': 0.565045}
frac[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.139775,'cc': 0.137555,'c': 0.215459,'l': 0.507211}
frac[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.147291,'cc': 0.149682,'c': 0.210640,'l': 0.492387}
frac[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.083239,'cc': 0.063083,'c': 0.205006,'l': 0.648671}
frac[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.106226,'cc': 0.096949,'c': 0.215630,'l': 0.581194}
frac[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.129332,'cc': 0.132697,'c': 0.207288,'l': 0.530683}
frac[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.138363,'cc': 0.144874,'c': 0.203284,'l': 0.513478}
# LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down 
frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Comb_Baseline_Kin__1up 
frac[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Comb_Baseline_Kin__1down 
frac[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Comb_Modelling_Kin__1up 
frac[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Comb_Modelling_Kin__1down 
frac[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up 
frac[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down 
frac[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Comb_Tracking_Kin__1up 
frac[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Comb_Tracking_Kin__1down 
frac[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up 
frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down 
frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up 
frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down 
frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up 
frac[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down 
frac[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up 
frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down 
frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Strong_JET_Comb_Baseline_All__1up 
frac[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Strong_JET_Comb_Baseline_All__1down 
frac[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Strong_JET_Comb_Modelling_All__1up 
frac[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Strong_JET_Comb_Modelling_All__1down 
frac[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Strong_JET_Comb_TotalStat_All__1up 
frac[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Strong_JET_Comb_TotalStat_All__1down 
frac[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Strong_JET_Comb_Tracking_All__1up 
frac[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# LARGERJET_Strong_JET_Comb_Tracking_All__1down 
frac[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

# ttxsecup 
flav_map[2]['el']["ttxsecup"] = {'bb': 1.322590, 'cc': 1.322590, 'c': 1.000000, 'l': 0.919198}
flav_map[3]['el']["ttxsecup"] = {'bb': 1.291577, 'cc': 1.291577, 'c': 0.976551, 'l': 0.897644}
flav_map[4]['el']["ttxsecup"] = {'bb': 1.261462, 'cc': 1.261462, 'c': 0.953782, 'l': 0.876714}
flav_map[5]['el']["ttxsecup"] = {'bb': 1.229212, 'cc': 1.229212, 'c': 0.929398, 'l': 0.854300}
flav_map[2]['mu']["ttxsecup"] = {'bb': 1.543033, 'cc': 1.543033, 'c': 1.000000, 'l': 0.877554}
flav_map[3]['mu']["ttxsecup"] = {'bb': 1.484918, 'cc': 1.484918, 'c': 0.962337, 'l': 0.844503}
flav_map[4]['mu']["ttxsecup"] = {'bb': 1.432315, 'cc': 1.432315, 'c': 0.928246, 'l': 0.814587}
flav_map[5]['mu']["ttxsecup"] = {'bb': 1.368702, 'cc': 1.368702, 'c': 0.887021, 'l': 0.778409}
# ttxsecdw 
flav_map[2]['el']["ttxsecdw"] = {'bb': 1.320717, 'cc': 1.320717, 'c': 1.000000, 'l': 0.919666}
flav_map[3]['el']["ttxsecdw"] = {'bb': 1.289924, 'cc': 1.289924, 'c': 0.976685, 'l': 0.898224}
flav_map[4]['el']["ttxsecdw"] = {'bb': 1.260014, 'cc': 1.260014, 'c': 0.954038, 'l': 0.877397}
flav_map[5]['el']["ttxsecdw"] = {'bb': 1.227975, 'cc': 1.227975, 'c': 0.929779, 'l': 0.855087}
flav_map[2]['mu']["ttxsecdw"] = {'bb': 1.540869, 'cc': 1.540869, 'c': 1.000000, 'l': 0.878042}
flav_map[3]['mu']["ttxsecdw"] = {'bb': 1.483058, 'cc': 1.483058, 'c': 0.962482, 'l': 0.845100}
flav_map[4]['mu']["ttxsecdw"] = {'bb': 1.430715, 'cc': 1.430715, 'c': 0.928512, 'l': 0.815273}
flav_map[5]['mu']["ttxsecdw"] = {'bb': 1.367398, 'cc': 1.367398, 'c': 0.887420, 'l': 0.779193}
# singletopup 
flav_map[2]['el']["singletopup"] = {'bb': 1.280857, 'cc': 1.280857, 'c': 1.000000, 'l': 0.929651}
flav_map[3]['el']["singletopup"] = {'bb': 1.254629, 'cc': 1.254629, 'c': 0.979523, 'l': 0.910614}
flav_map[4]['el']["singletopup"] = {'bb': 1.229007, 'cc': 1.229007, 'c': 0.959519, 'l': 0.892018}
flav_map[5]['el']["singletopup"] = {'bb': 1.201399, 'cc': 1.201399, 'c': 0.937965, 'l': 0.871980}
flav_map[2]['mu']["singletopup"] = {'bb': 1.506547, 'cc': 1.506547, 'c': 1.000000, 'l': 0.885781}
flav_map[3]['mu']["singletopup"] = {'bb': 1.453484, 'cc': 1.453484, 'c': 0.964779, 'l': 0.854583}
flav_map[4]['mu']["singletopup"] = {'bb': 1.405222, 'cc': 1.405222, 'c': 0.932743, 'l': 0.826207}
flav_map[5]['mu']["singletopup"] = {'bb': 1.346560, 'cc': 1.346560, 'c': 0.893806, 'l': 0.791716}
# singletopdw 
flav_map[2]['el']["singletopdw"] = {'bb': 1.357088, 'cc': 1.357088, 'c': 1.000000, 'l': 0.910556}
flav_map[3]['el']["singletopdw"] = {'bb': 1.321951, 'cc': 1.321951, 'c': 0.974109, 'l': 0.886981}
flav_map[4]['el']["singletopdw"] = {'bb': 1.288000, 'cc': 1.288000, 'c': 0.949091, 'l': 0.864201}
flav_map[5]['el']["singletopdw"] = {'bb': 1.251823, 'cc': 1.251823, 'c': 0.922433, 'l': 0.839928}
flav_map[2]['mu']["singletopdw"] = {'bb': 1.572705, 'cc': 1.572705, 'c': 1.000000, 'l': 0.870864}
flav_map[3]['mu']["singletopdw"] = {'bb': 1.510365, 'cc': 1.510365, 'c': 0.960361, 'l': 0.836343}
flav_map[4]['mu']["singletopdw"] = {'bb': 1.454157, 'cc': 1.454157, 'c': 0.924621, 'l': 0.805219}
flav_map[5]['mu']["singletopdw"] = {'bb': 1.386463, 'cc': 1.386463, 'c': 0.881579, 'l': 0.767735}
# wnorm__1up 
flav_map[2]['el']["wnorm__1up"] = {'bb': 1.322159, 'cc': 1.322159, 'c': 1.000000, 'l': 0.919306}
flav_map[3]['el']["wnorm__1up"] = {'bb': 1.291196, 'cc': 1.291196, 'c': 0.976582, 'l': 0.897777}
flav_map[4]['el']["wnorm__1up"] = {'bb': 1.261129, 'cc': 1.261129, 'c': 0.953841, 'l': 0.876871}
flav_map[5]['el']["wnorm__1up"] = {'bb': 1.228928, 'cc': 1.228928, 'c': 0.929486, 'l': 0.854481}
flav_map[2]['mu']["wnorm__1up"] = {'bb': 1.541871, 'cc': 1.541871, 'c': 1.000000, 'l': 0.877816}
flav_map[3]['mu']["wnorm__1up"] = {'bb': 1.483920, 'cc': 1.483920, 'c': 0.962415, 'l': 0.844824}
flav_map[4]['mu']["wnorm__1up"] = {'bb': 1.431456, 'cc': 1.431456, 'c': 0.928389, 'l': 0.814955}
flav_map[5]['mu']["wnorm__1up"] = {'bb': 1.368002, 'cc': 1.368002, 'c': 0.887235, 'l': 0.778830}
# wnorm__1down 
flav_map[2]['el']["wnorm__1down"] = {'bb': 1.321003, 'cc': 1.321003, 'c': 1.000000, 'l': 0.919595}
flav_map[3]['el']["wnorm__1down"] = {'bb': 1.290176, 'cc': 1.290176, 'c': 0.976664, 'l': 0.898135}
flav_map[4]['el']["wnorm__1down"] = {'bb': 1.260235, 'cc': 1.260235, 'c': 0.953999, 'l': 0.877292}
flav_map[5]['el']["wnorm__1down"] = {'bb': 1.228164, 'cc': 1.228164, 'c': 0.929721, 'l': 0.854967}
flav_map[2]['mu']["wnorm__1down"] = {'bb': 1.541857, 'cc': 1.541857, 'c': 1.000000, 'l': 0.877820}
flav_map[3]['mu']["wnorm__1down"] = {'bb': 1.483907, 'cc': 1.483907, 'c': 0.962416, 'l': 0.844828}
flav_map[4]['mu']["wnorm__1down"] = {'bb': 1.431445, 'cc': 1.431445, 'c': 0.928391, 'l': 0.814960}
flav_map[5]['mu']["wnorm__1down"] = {'bb': 1.367994, 'cc': 1.367994, 'c': 0.887238, 'l': 0.778835}
# elMisIDpos_up 
flav_map[2]['el']["elMisIDpos_up"] = {'bb': 1.269077, 'cc': 1.269077, 'c': 1.000000, 'l': 0.932600}
flav_map[3]['el']["elMisIDpos_up"] = {'bb': 1.244159, 'cc': 1.244159, 'c': 0.980365, 'l': 0.914289}
flav_map[4]['el']["elMisIDpos_up"] = {'bb': 1.219775, 'cc': 1.219775, 'c': 0.961151, 'l': 0.896370}
flav_map[5]['el']["elMisIDpos_up"] = {'bb': 1.193456, 'cc': 1.193456, 'c': 0.940412, 'l': 0.877029}
flav_map[2]['mu']["elMisIDpos_up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["elMisIDpos_up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["elMisIDpos_up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["elMisIDpos_up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# elMisIDpos_down 
flav_map[2]['el']["elMisIDpos_down"] = {'bb': 1.375246, 'cc': 1.375246, 'c': 1.000000, 'l': 0.906008}
flav_map[3]['el']["elMisIDpos_down"] = {'bb': 1.337878, 'cc': 1.337878, 'c': 0.972828, 'l': 0.881390}
flav_map[4]['el']["elMisIDpos_down"] = {'bb': 1.301864, 'cc': 1.301864, 'c': 0.946641, 'l': 0.857664}
flav_map[5]['el']["elMisIDpos_down"] = {'bb': 1.263589, 'cc': 1.263589, 'c': 0.918810, 'l': 0.832449}
flav_map[2]['mu']["elMisIDpos_down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["elMisIDpos_down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["elMisIDpos_down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["elMisIDpos_down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# MET_SoftTrk_ResoPara 
flav_map[2]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.297653, 'cc': 1.297653, 'c': 1.000000, 'l': 0.925463}
flav_map[3]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.269558, 'cc': 1.269558, 'c': 0.978349, 'l': 0.905426}
flav_map[4]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.242074, 'cc': 1.242074, 'c': 0.957169, 'l': 0.885825}
flav_map[5]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.212590, 'cc': 1.212590, 'c': 0.934449, 'l': 0.864798}
flav_map[2]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.573814, 'cc': 1.573814, 'c': 1.000000, 'l': 0.870831}
flav_map[3]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.510954, 'cc': 1.510954, 'c': 0.960059, 'l': 0.836049}
flav_map[4]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.454415, 'cc': 1.454415, 'c': 0.924134, 'l': 0.804764}
flav_map[5]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.387047, 'cc': 1.387047, 'c': 0.881328, 'l': 0.767488}
# MET_SoftTrk_ResoPerp 
flav_map[2]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.333786, 'cc': 1.333786, 'c': 1.000000, 'l': 0.916546}
flav_map[3]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.301381, 'cc': 1.301381, 'c': 0.975704, 'l': 0.894278}
flav_map[4]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.270006, 'cc': 1.270006, 'c': 0.952181, 'l': 0.872718}
flav_map[5]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.236391, 'cc': 1.236391, 'c': 0.926978, 'l': 0.849618}
flav_map[2]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.572243, 'cc': 1.572243, 'c': 1.000000, 'l': 0.870972}
flav_map[3]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.509724, 'cc': 1.509724, 'c': 0.960236, 'l': 0.836339}
flav_map[4]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.453626, 'cc': 1.453626, 'c': 0.924556, 'l': 0.805263}
flav_map[5]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.386108, 'cc': 1.386108, 'c': 0.881612, 'l': 0.767860}
# MET_SoftTrk_ScaleUp 
flav_map[2]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.342957, 'cc': 1.342957, 'c': 1.000000, 'l': 0.914130}
flav_map[3]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.309595, 'cc': 1.309595, 'c': 0.975158, 'l': 0.891421}
flav_map[4]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.277132, 'cc': 1.277132, 'c': 0.950985, 'l': 0.869324}
flav_map[5]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.242575, 'cc': 1.242575, 'c': 0.925253, 'l': 0.845802}
flav_map[2]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.554980, 'cc': 1.554980, 'c': 1.000000, 'l': 0.874984}
flav_map[3]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.495035, 'cc': 1.495035, 'c': 0.961450, 'l': 0.841253}
flav_map[4]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.440917, 'cc': 1.440917, 'c': 0.926647, 'l': 0.810801}
flav_map[5]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.375910, 'cc': 1.375910, 'c': 0.884841, 'l': 0.774221}
# MET_SoftTrk_ScaleDown 
flav_map[2]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.293631, 'cc': 1.293631, 'c': 1.000000, 'l': 0.926476}
flav_map[3]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.265930, 'cc': 1.265930, 'c': 0.978587, 'l': 0.906637}
flav_map[4]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.238932, 'cc': 1.238932, 'c': 0.957717, 'l': 0.887301}
flav_map[5]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.210012, 'cc': 1.210012, 'c': 0.935361, 'l': 0.866589}
flav_map[2]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.542878, 'cc': 1.542878, 'c': 1.000000, 'l': 0.877597}
flav_map[3]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.484931, 'cc': 1.484931, 'c': 0.962442, 'l': 0.844636}
flav_map[4]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.432219, 'cc': 1.432219, 'c': 0.928278, 'l': 0.814653}
flav_map[5]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.368454, 'cc': 1.368454, 'c': 0.886949, 'l': 0.778384}
# EG_RESOLUTION_ALL__1up 
flav_map[2]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.322073, 'cc': 1.322073, 'c': 1.000000, 'l': 0.919364}
flav_map[3]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.291102, 'cc': 1.291102, 'c': 0.976574, 'l': 0.897827}
flav_map[4]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.261095, 'cc': 1.261095, 'c': 0.953877, 'l': 0.876960}
flav_map[5]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.228861, 'cc': 1.228861, 'c': 0.929495, 'l': 0.854545}
flav_map[2]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.541465, 'cc': 1.541465, 'c': 1.000000, 'l': 0.877908}
flav_map[3]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.483571, 'cc': 1.483571, 'c': 0.962442, 'l': 0.844935}
flav_map[4]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.431156, 'cc': 1.431156, 'c': 0.928439, 'l': 0.815084}
flav_map[5]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.367757, 'cc': 1.367757, 'c': 0.887310, 'l': 0.778976}
# EG_RESOLUTION_ALL__1down 
flav_map[2]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.306271, 'cc': 1.306271, 'c': 1.000000, 'l': 0.923252}
flav_map[3]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.277217, 'cc': 1.277217, 'c': 0.977758, 'l': 0.902717}
flav_map[4]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.248843, 'cc': 1.248843, 'c': 0.956037, 'l': 0.882663}
flav_map[5]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.218393, 'cc': 1.218393, 'c': 0.932726, 'l': 0.861141}
flav_map[2]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.542010, 'cc': 1.542010, 'c': 1.000000, 'l': 0.877785}
flav_map[3]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.484039, 'cc': 1.484039, 'c': 0.962406, 'l': 0.844785}
flav_map[4]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.431559, 'cc': 1.431559, 'c': 0.928372, 'l': 0.814911}
flav_map[5]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.368083, 'cc': 1.368083, 'c': 0.887207, 'l': 0.778777}
# EG_SCALE_ALL__1up 
flav_map[2]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.315620, 'cc': 1.315620, 'c': 1.000000, 'l': 0.920996}
flav_map[3]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.285358, 'cc': 1.285358, 'c': 0.976997, 'l': 0.899810}
flav_map[4]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.256107, 'cc': 1.256107, 'c': 0.954764, 'l': 0.879333}
flav_map[5]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.224569, 'cc': 1.224569, 'c': 0.930792, 'l': 0.857256}
flav_map[2]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.541663, 'cc': 1.541663, 'c': 1.000000, 'l': 0.877863}
flav_map[3]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.483741, 'cc': 1.483741, 'c': 0.962429, 'l': 0.844881}
flav_map[4]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.431303, 'cc': 1.431303, 'c': 0.928415, 'l': 0.815021}
flav_map[5]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.367877, 'cc': 1.367877, 'c': 0.887273, 'l': 0.778904}
# EG_SCALE_ALL__1down 
flav_map[2]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.302935, 'cc': 1.302935, 'c': 1.000000, 'l': 0.924121}
flav_map[3]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.274180, 'cc': 1.274180, 'c': 0.977931, 'l': 0.903727}
flav_map[4]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.246232, 'cc': 1.246232, 'c': 0.956481, 'l': 0.883904}
flav_map[5]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.216182, 'cc': 1.216182, 'c': 0.933418, 'l': 0.862591}
flav_map[2]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.541811, 'cc': 1.541811, 'c': 1.000000, 'l': 0.877830}
flav_map[3]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.483868, 'cc': 1.483868, 'c': 0.962419, 'l': 0.844840}
flav_map[4]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.431411, 'cc': 1.431411, 'c': 0.928396, 'l': 0.814974}
flav_map[5]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.367962, 'cc': 1.367962, 'c': 0.887244, 'l': 0.778849}
# MUON_ID__1up 
flav_map[2]['el']["MUON_ID__1up"] = {'bb': 1.321753, 'cc': 1.321753, 'c': 1.000000, 'l': 0.919407}
flav_map[3]['el']["MUON_ID__1up"] = {'bb': 1.290838, 'cc': 1.290838, 'c': 0.976611, 'l': 0.897903}
flav_map[4]['el']["MUON_ID__1up"] = {'bb': 1.260815, 'cc': 1.260815, 'c': 0.953897, 'l': 0.877019}
flav_map[5]['el']["MUON_ID__1up"] = {'bb': 1.228660, 'cc': 1.228660, 'c': 0.929569, 'l': 0.854652}
flav_map[2]['mu']["MUON_ID__1up"] = {'bb': 1.537807, 'cc': 1.537807, 'c': 1.000000, 'l': 0.878740}
flav_map[3]['mu']["MUON_ID__1up"] = {'bb': 1.480489, 'cc': 1.480489, 'c': 0.962727, 'l': 0.845987}
flav_map[4]['mu']["MUON_ID__1up"] = {'bb': 1.428473, 'cc': 1.428473, 'c': 0.928902, 'l': 0.816264}
flav_map[5]['mu']["MUON_ID__1up"] = {'bb': 1.365747, 'cc': 1.365747, 'c': 0.888113, 'l': 0.780421}
# MUON_ID__1down 
flav_map[2]['el']["MUON_ID__1down"] = {'bb': 1.321068, 'cc': 1.321068, 'c': 1.000000, 'l': 0.919578}
flav_map[3]['el']["MUON_ID__1down"] = {'bb': 1.290234, 'cc': 1.290234, 'c': 0.976660, 'l': 0.898115}
flav_map[4]['el']["MUON_ID__1down"] = {'bb': 1.260286, 'cc': 1.260286, 'c': 0.953990, 'l': 0.877269}
flav_map[5]['el']["MUON_ID__1down"] = {'bb': 1.228207, 'cc': 1.228207, 'c': 0.929708, 'l': 0.854939}
flav_map[2]['mu']["MUON_ID__1down"] = {'bb': 1.535503, 'cc': 1.535503, 'c': 1.000000, 'l': 0.879259}
flav_map[3]['mu']["MUON_ID__1down"] = {'bb': 1.478503, 'cc': 1.478503, 'c': 0.962879, 'l': 0.846620}
flav_map[4]['mu']["MUON_ID__1down"] = {'bb': 1.426769, 'cc': 1.426769, 'c': 0.929187, 'l': 0.816996}
flav_map[5]['mu']["MUON_ID__1down"] = {'bb': 1.364251, 'cc': 1.364251, 'c': 0.888471, 'l': 0.781197}
# MUON_MS__1up 
flav_map[2]['el']["MUON_MS__1up"] = {'bb': 1.321562, 'cc': 1.321562, 'c': 1.000000, 'l': 0.919456}
flav_map[3]['el']["MUON_MS__1up"] = {'bb': 1.290669, 'cc': 1.290669, 'c': 0.976624, 'l': 0.897962}
flav_map[4]['el']["MUON_MS__1up"] = {'bb': 1.260667, 'cc': 1.260667, 'c': 0.953922, 'l': 0.877089}
flav_map[5]['el']["MUON_MS__1up"] = {'bb': 1.228533, 'cc': 1.228533, 'c': 0.929607, 'l': 0.854732}
flav_map[2]['mu']["MUON_MS__1up"] = {'bb': 1.551833, 'cc': 1.551833, 'c': 1.000000, 'l': 0.875621}
flav_map[3]['mu']["MUON_MS__1up"] = {'bb': 1.492492, 'cc': 1.492492, 'c': 0.961761, 'l': 0.842138}
flav_map[4]['mu']["MUON_MS__1up"] = {'bb': 1.438788, 'cc': 1.438788, 'c': 0.927154, 'l': 0.811835}
flav_map[5]['mu']["MUON_MS__1up"] = {'bb': 1.374013, 'cc': 1.374013, 'c': 0.885413, 'l': 0.775286}
# MUON_MS__1down 
flav_map[2]['el']["MUON_MS__1down"] = {'bb': 1.321075, 'cc': 1.321075, 'c': 1.000000, 'l': 0.919577}
flav_map[3]['el']["MUON_MS__1down"] = {'bb': 1.290240, 'cc': 1.290240, 'c': 0.976659, 'l': 0.898113}
flav_map[4]['el']["MUON_MS__1down"] = {'bb': 1.260291, 'cc': 1.260291, 'c': 0.953989, 'l': 0.877266}
flav_map[5]['el']["MUON_MS__1down"] = {'bb': 1.228212, 'cc': 1.228212, 'c': 0.929706, 'l': 0.854936}
flav_map[2]['mu']["MUON_MS__1down"] = {'bb': 1.518090, 'cc': 1.518090, 'c': 1.000000, 'l': 0.883175}
flav_map[3]['mu']["MUON_MS__1down"] = {'bb': 1.463500, 'cc': 1.463500, 'c': 0.964040, 'l': 0.851417}
flav_map[4]['mu']["MUON_MS__1down"] = {'bb': 1.413889, 'cc': 1.413889, 'c': 0.931360, 'l': 0.822554}
flav_map[5]['mu']["MUON_MS__1down"] = {'bb': 1.353666, 'cc': 1.353666, 'c': 0.891690, 'l': 0.787519}
# MUON_SCALE__1up 
flav_map[2]['el']["MUON_SCALE__1up"] = {'bb': 1.321522, 'cc': 1.321522, 'c': 1.000000, 'l': 0.919465}
flav_map[3]['el']["MUON_SCALE__1up"] = {'bb': 1.290634, 'cc': 1.290634, 'c': 0.976627, 'l': 0.897974}
flav_map[4]['el']["MUON_SCALE__1up"] = {'bb': 1.260637, 'cc': 1.260637, 'c': 0.953928, 'l': 0.877103}
flav_map[5]['el']["MUON_SCALE__1up"] = {'bb': 1.228507, 'cc': 1.228507, 'c': 0.929616, 'l': 0.854749}
flav_map[2]['mu']["MUON_SCALE__1up"] = {'bb': 1.545944, 'cc': 1.545944, 'c': 1.000000, 'l': 0.876902}
flav_map[3]['mu']["MUON_SCALE__1up"] = {'bb': 1.487372, 'cc': 1.487372, 'c': 0.962113, 'l': 0.843678}
flav_map[4]['mu']["MUON_SCALE__1up"] = {'bb': 1.434421, 'cc': 1.434421, 'c': 0.927860, 'l': 0.813643}
flav_map[5]['mu']["MUON_SCALE__1up"] = {'bb': 1.370476, 'cc': 1.370476, 'c': 0.886498, 'l': 0.777371}
# MUON_SCALE__1down 
flav_map[2]['el']["MUON_SCALE__1down"] = {'bb': 1.321535, 'cc': 1.321535, 'c': 1.000000, 'l': 0.919462}
flav_map[3]['el']["MUON_SCALE__1down"] = {'bb': 1.290646, 'cc': 1.290646, 'c': 0.976626, 'l': 0.897970}
flav_map[4]['el']["MUON_SCALE__1down"] = {'bb': 1.260647, 'cc': 1.260647, 'c': 0.953926, 'l': 0.877099}
flav_map[5]['el']["MUON_SCALE__1down"] = {'bb': 1.228516, 'cc': 1.228516, 'c': 0.929613, 'l': 0.854743}
flav_map[2]['mu']["MUON_SCALE__1down"] = {'bb': 1.543219, 'cc': 1.543219, 'c': 1.000000, 'l': 0.877536}
flav_map[3]['mu']["MUON_SCALE__1down"] = {'bb': 1.485096, 'cc': 1.485096, 'c': 0.962337, 'l': 0.844485}
flav_map[4]['mu']["MUON_SCALE__1down"] = {'bb': 1.432448, 'cc': 1.432448, 'c': 0.928221, 'l': 0.814547}
flav_map[5]['mu']["MUON_SCALE__1down"] = {'bb': 1.368813, 'cc': 1.368813, 'c': 0.886986, 'l': 0.778362}
# MUON_SAGITTA_RESBIAS__1up 
flav_map[2]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# MUON_SAGITTA_RESBIAS__1down 
flav_map[2]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# MUON_SAGITTA_RHO__1up 
flav_map[2]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# MUON_SAGITTA_RHO__1down 
flav_map[2]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# JET_JER_SINGLE_NP__1up 
flav_map[2]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.335768, 'cc': 1.335768, 'c': 1.000000, 'l': 0.917438}
flav_map[3]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.302882, 'cc': 1.302882, 'c': 0.975381, 'l': 0.894851}
flav_map[4]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.273542, 'cc': 1.273542, 'c': 0.953416, 'l': 0.874700}
flav_map[5]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.237561, 'cc': 1.237561, 'c': 0.926479, 'l': 0.849987}
flav_map[2]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.639812, 'cc': 1.639812, 'c': 1.000000, 'l': 0.857659}
flav_map[3]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.567699, 'cc': 1.567699, 'c': 0.956024, 'l': 0.819942}
flav_map[4]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.503352, 'cc': 1.503352, 'c': 0.916783, 'l': 0.786288}
flav_map[5]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.427922, 'cc': 1.427922, 'c': 0.870784, 'l': 0.746836}
# JET_21NP_JET_EtaIntercalibration_Modelling__1up 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.356688, 'cc': 1.356688, 'c': 1.000000, 'l': 0.911286}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.321590, 'cc': 1.321590, 'c': 0.974130, 'l': 0.887711}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.288088, 'cc': 1.288088, 'c': 0.949436, 'l': 0.865208}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.251802, 'cc': 1.251802, 'c': 0.922690, 'l': 0.840835}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.584748, 'cc': 1.584748, 'c': 1.000000, 'l': 0.868902}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.520918, 'cc': 1.520918, 'c': 0.959722, 'l': 0.833904}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.464253, 'cc': 1.464253, 'c': 0.923965, 'l': 0.802836}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.393896, 'cc': 1.393896, 'c': 0.879569, 'l': 0.764260}
# JET_21NP_JET_EtaIntercalibration_Modelling__1down 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.238491, 'cc': 1.238491, 'c': 1.000000, 'l': 0.939942}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.216616, 'cc': 1.216616, 'c': 0.982337, 'l': 0.923340}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.195746, 'cc': 1.195746, 'c': 0.965486, 'l': 0.907501}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.172334, 'cc': 1.172334, 'c': 0.946582, 'l': 0.889733}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.510501, 'cc': 1.510501, 'c': 1.000000, 'l': 0.884308}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.456295, 'cc': 1.456295, 'c': 0.964114, 'l': 0.852574}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.408315, 'cc': 1.408315, 'c': 0.932350, 'l': 0.824484}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.348411, 'cc': 1.348411, 'c': 0.892691, 'l': 0.789414}
# JET_21NP_JET_EtaIntercalibration_NonClosure__1up 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.350704, 'cc': 1.350704, 'c': 1.000000, 'l': 0.912172}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.316162, 'cc': 1.316162, 'c': 0.974427, 'l': 0.888845}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.282992, 'cc': 1.282992, 'c': 0.949869, 'l': 0.866444}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.247458, 'cc': 1.247458, 'c': 0.923561, 'l': 0.842447}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.590386, 'cc': 1.590386, 'c': 1.000000, 'l': 0.866893}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.525290, 'cc': 1.525290, 'c': 0.959069, 'l': 0.831410}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.466505, 'cc': 1.466505, 'c': 0.922106, 'l': 0.799367}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.396994, 'cc': 1.396994, 'c': 0.878399, 'l': 0.761478}
# JET_21NP_JET_EtaIntercalibration_NonClosure__1down 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.272678, 'cc': 1.272678, 'c': 1.000000, 'l': 0.931835}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.247351, 'cc': 1.247351, 'c': 0.980099, 'l': 0.913290}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.222655, 'cc': 1.222655, 'c': 0.960694, 'l': 0.895208}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.195574, 'cc': 1.195574, 'c': 0.939415, 'l': 0.875380}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.549276, 'cc': 1.549276, 'c': 1.000000, 'l': 0.876343}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.490435, 'cc': 1.490435, 'c': 0.962020, 'l': 0.843059}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.437032, 'cc': 1.437032, 'c': 0.927550, 'l': 0.812852}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.372377, 'cc': 1.372377, 'c': 0.885818, 'l': 0.776280}
# JET_21NP_JET_EtaIntercalibration_TotalStat__1up 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.313641, 'cc': 1.313641, 'c': 1.000000, 'l': 0.921721}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.283667, 'cc': 1.283667, 'c': 0.977183, 'l': 0.900691}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.254462, 'cc': 1.254462, 'c': 0.954951, 'l': 0.880199}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.223346, 'cc': 1.223346, 'c': 0.931264, 'l': 0.858366}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.569549, 'cc': 1.569549, 'c': 1.000000, 'l': 0.871858}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.507914, 'cc': 1.507914, 'c': 0.960731, 'l': 0.837621}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.451922, 'cc': 1.451922, 'c': 0.925057, 'l': 0.806518}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.384678, 'cc': 1.384678, 'c': 0.882214, 'l': 0.769165}
# JET_21NP_JET_EtaIntercalibration_TotalStat__1down 
flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.291533, 'cc': 1.291533, 'c': 1.000000, 'l': 0.926796}
flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.264060, 'cc': 1.264060, 'c': 0.978729, 'l': 0.907082}
flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.237220, 'cc': 1.237220, 'c': 0.957947, 'l': 0.887822}
flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.208163, 'cc': 1.208163, 'c': 0.935449, 'l': 0.866971}
flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.540339, 'cc': 1.540339, 'c': 1.000000, 'l': 0.877758}
flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.482551, 'cc': 1.482551, 'c': 0.962483, 'l': 0.844828}
flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.429837, 'cc': 1.429837, 'c': 0.928261, 'l': 0.814789}
flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.367063, 'cc': 1.367063, 'c': 0.887507, 'l': 0.779017}
# JET_21NP_JET_Flavor_Composition__1up 
flav_map[2]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.606268, 'cc': 1.606268, 'c': 1.000000, 'l': 0.853800}
flav_map[3]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.538616, 'cc': 1.538616, 'c': 0.957883, 'l': 0.817840}
flav_map[4]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.476826, 'cc': 1.476826, 'c': 0.919414, 'l': 0.784996}
flav_map[5]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.409168, 'cc': 1.409168, 'c': 0.877293, 'l': 0.749033}
flav_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.752749, 'cc': 1.752749, 'c': 1.000000, 'l': 0.836416}
flav_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.664721, 'cc': 1.664721, 'c': 0.949777, 'l': 0.794408}
flav_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.588839, 'cc': 1.588839, 'c': 0.906484, 'l': 0.758197}
flav_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.495515, 'cc': 1.495515, 'c': 0.853239, 'l': 0.713663}
# JET_21NP_JET_Flavor_Composition__1down 
flav_map[2]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.037746, 'cc': 1.037746, 'c': 1.000000, 'l': 0.990177}
flav_map[3]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.034672, 'cc': 1.034672, 'c': 0.997038, 'l': 0.987243}
flav_map[4]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.031859, 'cc': 1.031859, 'c': 0.994326, 'l': 0.984559}
flav_map[5]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.028329, 'cc': 1.028329, 'c': 0.990925, 'l': 0.981191}
flav_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.380383, 'cc': 1.380383, 'c': 1.000000, 'l': 0.911070}
flav_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.341781, 'cc': 1.341781, 'c': 0.972035, 'l': 0.885592}
flav_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.307083, 'cc': 1.307083, 'c': 0.946899, 'l': 0.862691}
flav_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.263842, 'cc': 1.263842, 'c': 0.915574, 'l': 0.834152}
# JET_21NP_JET_Flavor_Response__1up 
flav_map[2]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.194809, 'cc': 1.194809, 'c': 1.000000, 'l': 0.950675}
flav_map[3]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.177571, 'cc': 1.177571, 'c': 0.985573, 'l': 0.936960}
flav_map[4]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.160643, 'cc': 1.160643, 'c': 0.971405, 'l': 0.923491}
flav_map[5]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.141879, 'cc': 1.141879, 'c': 0.955700, 'l': 0.908560}
flav_map[2]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.500766, 'cc': 1.500766, 'c': 1.000000, 'l': 0.885982}
flav_map[3]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.447557, 'cc': 1.447557, 'c': 0.964546, 'l': 0.854570}
flav_map[4]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.400946, 'cc': 1.400946, 'c': 0.933488, 'l': 0.827053}
flav_map[5]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.341246, 'cc': 1.341246, 'c': 0.893708, 'l': 0.791808}
# JET_21NP_JET_Flavor_Response__1down 
flav_map[2]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.358986, 'cc': 1.358986, 'c': 1.000000, 'l': 0.911347}
flav_map[3]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.323629, 'cc': 1.323629, 'c': 0.973983, 'l': 0.887637}
flav_map[4]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.289874, 'cc': 1.289874, 'c': 0.949144, 'l': 0.865000}
flav_map[5]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.253650, 'cc': 1.253650, 'c': 0.922489, 'l': 0.840708}
flav_map[2]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.616678, 'cc': 1.616678, 'c': 1.000000, 'l': 0.862077}
flav_map[3]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.549142, 'cc': 1.549142, 'c': 0.958225, 'l': 0.826064}
flav_map[4]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.488039, 'cc': 1.488039, 'c': 0.920430, 'l': 0.793481}
flav_map[5]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.414006, 'cc': 1.414006, 'c': 0.874637, 'l': 0.754004}
# JET_21NP_JET_Pileup_OffsetMu__1up 
flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.276421, 'cc': 1.276421, 'c': 1.000000, 'l': 0.930705}
flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.250608, 'cc': 1.250608, 'c': 0.979777, 'l': 0.911883}
flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.225478, 'cc': 1.225478, 'c': 0.960089, 'l': 0.893560}
flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.198429, 'cc': 1.198429, 'c': 0.938899, 'l': 0.873837}
flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.554250, 'cc': 1.554250, 'c': 1.000000, 'l': 0.874972}
flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.494577, 'cc': 1.494577, 'c': 0.961607, 'l': 0.841379}
flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.440722, 'cc': 1.440722, 'c': 0.926957, 'l': 0.811061}
flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.375253, 'cc': 1.375253, 'c': 0.884834, 'l': 0.774204}
# JET_21NP_JET_Pileup_OffsetMu__1down 
flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.309126, 'cc': 1.309126, 'c': 1.000000, 'l': 0.922660}
flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.279704, 'cc': 1.279704, 'c': 0.977525, 'l': 0.901924}
flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.251166, 'cc': 1.251166, 'c': 0.955727, 'l': 0.881811}
flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.219998, 'cc': 1.219998, 'c': 0.931918, 'l': 0.859844}
flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.555991, 'cc': 1.555991, 'c': 1.000000, 'l': 0.874566}
flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.496192, 'cc': 1.496192, 'c': 0.961568, 'l': 0.840955}
flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.441681, 'cc': 1.441681, 'c': 0.926535, 'l': 0.810316}
flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.376548, 'cc': 1.376548, 'c': 0.884676, 'l': 0.773707}
# JET_21NP_JET_Pileup_OffsetNPV__1up 
flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.324154, 'cc': 1.324154, 'c': 1.000000, 'l': 0.919328}
flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.292932, 'cc': 1.292932, 'c': 0.976421, 'l': 0.897652}
flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.262540, 'cc': 1.262540, 'c': 0.953469, 'l': 0.876551}
flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.230816, 'cc': 1.230816, 'c': 0.929511, 'l': 0.854526}
flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.678542, 'cc': 1.678542, 'c': 1.000000, 'l': 0.847394}
flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.601259, 'cc': 1.601259, 'c': 0.953958, 'l': 0.808378}
flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.532465, 'cc': 1.532465, 'c': 0.912974, 'l': 0.773648}
flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.450558, 'cc': 1.450558, 'c': 0.864177, 'l': 0.732298}
# JET_21NP_JET_Pileup_OffsetNPV__1down 
flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.262943, 'cc': 1.262943, 'c': 1.000000, 'l': 0.933798}
flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.238805, 'cc': 1.238805, 'c': 0.980887, 'l': 0.915951}
flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.214920, 'cc': 1.214920, 'c': 0.961975, 'l': 0.898290}
flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.188957, 'cc': 1.188957, 'c': 0.941418, 'l': 0.879094}
flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.524080, 'cc': 1.524080, 'c': 1.000000, 'l': 0.881295}
flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.468123, 'cc': 1.468123, 'c': 0.963285, 'l': 0.848938}
flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.417805, 'cc': 1.417805, 'c': 0.930269, 'l': 0.819842}
flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.356137, 'cc': 1.356137, 'c': 0.889807, 'l': 0.784182}
# JET_21NP_JET_Pileup_PtTerm__1up 
flav_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.301765, 'cc': 1.301765, 'c': 1.000000, 'l': 0.924448}
flav_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.273165, 'cc': 1.273165, 'c': 0.978029, 'l': 0.904137}
flav_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.245331, 'cc': 1.245331, 'c': 0.956648, 'l': 0.884371}
flav_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.215249, 'cc': 1.215249, 'c': 0.933539, 'l': 0.863008}
flav_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.534942, 'cc': 1.534942, 'c': 1.000000, 'l': 0.879440}
flav_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.478022, 'cc': 1.478022, 'c': 0.962918, 'l': 0.846828}
flav_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.426305, 'cc': 1.426305, 'c': 0.929224, 'l': 0.817197}
flav_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.363843, 'cc': 1.363843, 'c': 0.888531, 'l': 0.781409}
# JET_21NP_JET_Pileup_PtTerm__1down 
flav_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.313192, 'cc': 1.313192, 'c': 1.000000, 'l': 0.921472}
flav_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.283348, 'cc': 1.283348, 'c': 0.977273, 'l': 0.900529}
flav_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.254300, 'cc': 1.254300, 'c': 0.955153, 'l': 0.880147}
flav_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.222968, 'cc': 1.222968, 'c': 0.931294, 'l': 0.858161}
flav_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.550420, 'cc': 1.550420, 'c': 1.000000, 'l': 0.875839}
flav_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.491282, 'cc': 1.491282, 'c': 0.961857, 'l': 0.842432}
flav_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.437739, 'cc': 1.437739, 'c': 0.927322, 'l': 0.812185}
flav_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.373095, 'cc': 1.373095, 'c': 0.885628, 'l': 0.775668}
# JET_21NP_JET_Pileup_RhoTopology__1up 
flav_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.508520, 'cc': 1.508520, 'c': 1.000000, 'l': 0.875728}
flav_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.453906, 'cc': 1.453906, 'c': 0.963796, 'l': 0.844024}
flav_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.403230, 'cc': 1.403230, 'c': 0.930203, 'l': 0.814605}
flav_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.348519, 'cc': 1.348519, 'c': 0.893935, 'l': 0.782844}
flav_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.685722, 'cc': 1.685722, 'c': 1.000000, 'l': 0.848421}
flav_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.608294, 'cc': 1.608294, 'c': 0.954068, 'l': 0.809451}
flav_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.538368, 'cc': 1.538368, 'c': 0.912587, 'l': 0.774258}
flav_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.455465, 'cc': 1.455465, 'c': 0.863407, 'l': 0.732533}
# JET_21NP_JET_Pileup_RhoTopology__1down 
flav_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.099937, 'cc': 1.099937, 'c': 1.000000, 'l': 0.974486}
flav_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.091612, 'cc': 1.091612, 'c': 0.992431, 'l': 0.967110}
flav_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.083515, 'cc': 1.083515, 'c': 0.985070, 'l': 0.959937}
flav_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.074338, 'cc': 1.074338, 'c': 0.976727, 'l': 0.951807}
flav_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.412006, 'cc': 1.412006, 'c': 1.000000, 'l': 0.905289}
flav_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.370217, 'cc': 1.370217, 'c': 0.970404, 'l': 0.878496}
flav_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.332862, 'cc': 1.332862, 'c': 0.943949, 'l': 0.854547}
flav_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.285727, 'cc': 1.285727, 'c': 0.910567, 'l': 0.824327}
# JET_21NP_JET_PunchThrough_MC15__1up 
flav_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.321321, 'cc': 1.321321, 'c': 1.000000, 'l': 0.919513}
flav_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.290465, 'cc': 1.290465, 'c': 0.976647, 'l': 0.898040}
flav_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.260483, 'cc': 1.260483, 'c': 0.953956, 'l': 0.877175}
flav_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.228377, 'cc': 1.228377, 'c': 0.929658, 'l': 0.854833}
flav_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.541873, 'cc': 1.541873, 'c': 1.000000, 'l': 0.877817}
flav_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.483917, 'cc': 1.483917, 'c': 0.962412, 'l': 0.844822}
flav_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.431455, 'cc': 1.431455, 'c': 0.928387, 'l': 0.814954}
flav_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887231, 'l': 0.778826}
# JET_21NP_JET_PunchThrough_MC15__1down 
flav_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.322266, 'cc': 1.322266, 'c': 1.000000, 'l': 0.919280}
flav_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.291291, 'cc': 1.291291, 'c': 0.976575, 'l': 0.897745}
flav_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.261211, 'cc': 1.261211, 'c': 0.953826, 'l': 0.876833}
flav_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.228997, 'cc': 1.228997, 'c': 0.929463, 'l': 0.854436}
flav_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.541769, 'cc': 1.541769, 'c': 1.000000, 'l': 0.877839}
flav_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.483833, 'cc': 1.483833, 'c': 0.962422, 'l': 0.844852}
flav_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.431380, 'cc': 1.431380, 'c': 0.928401, 'l': 0.814987}
flav_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.367936, 'cc': 1.367936, 'c': 0.887251, 'l': 0.778864}
# JET_21NP_JET_SingleParticle_HighPt__1up 
flav_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919450}
flav_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976624, 'l': 0.897956}
flav_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953921, 'l': 0.877082}
flav_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854724}
flav_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.541863, 'cc': 1.541863, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.483913, 'cc': 1.483913, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814957}
flav_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887236, 'l': 0.778832}
# JET_21NP_JET_SingleParticle_HighPt__1down 
flav_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.321581, 'cc': 1.321581, 'c': 1.000000, 'l': 0.919450}
flav_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.290686, 'cc': 1.290686, 'c': 0.976623, 'l': 0.897956}
flav_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.260682, 'cc': 1.260682, 'c': 0.953920, 'l': 0.877082}
flav_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.228546, 'cc': 1.228546, 'c': 0.929603, 'l': 0.854724}
flav_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887236, 'l': 0.778832}
# JET_21NP_JET_BJES_Response__1up 
flav_map[2]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.319998, 'cc': 1.319998, 'c': 1.000000, 'l': 0.919700}
flav_map[3]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.289198, 'cc': 1.289198, 'c': 0.976667, 'l': 0.898241}
flav_map[4]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.259336, 'cc': 1.259336, 'c': 0.954044, 'l': 0.877434}
flav_map[5]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.227348, 'cc': 1.227348, 'c': 0.929811, 'l': 0.855147}
flav_map[2]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.542639, 'cc': 1.542639, 'c': 1.000000, 'l': 0.877448}
flav_map[3]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.484435, 'cc': 1.484435, 'c': 0.962270, 'l': 0.844342}
flav_map[4]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.431762, 'cc': 1.431762, 'c': 0.928125, 'l': 0.814382}
flav_map[5]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.368157, 'cc': 1.368157, 'c': 0.886894, 'l': 0.778203}
# JET_21NP_JET_BJES_Response__1down 
flav_map[2]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.322203, 'cc': 1.322203, 'c': 1.000000, 'l': 0.919425}
flav_map[3]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.291333, 'cc': 1.291333, 'c': 0.976653, 'l': 0.897959}
flav_map[4]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.261336, 'cc': 1.261336, 'c': 0.953966, 'l': 0.877100}
flav_map[5]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.229153, 'cc': 1.229153, 'c': 0.929625, 'l': 0.854721}
flav_map[2]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.542296, 'cc': 1.542296, 'c': 1.000000, 'l': 0.877916}
flav_map[3]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.484423, 'cc': 1.484423, 'c': 0.962476, 'l': 0.844973}
flav_map[4]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.432001, 'cc': 1.432001, 'c': 0.928486, 'l': 0.815133}
flav_map[5]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.368572, 'cc': 1.368572, 'c': 0.887360, 'l': 0.779028}
# JET_21NP_JET_EffectiveNP_1__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.459011, 'cc': 1.459011, 'c': 1.000000, 'l': 0.887168}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.410731, 'cc': 1.410731, 'c': 0.966909, 'l': 0.857810}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.365628, 'cc': 1.365628, 'c': 0.935996, 'l': 0.830386}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.317044, 'cc': 1.317044, 'c': 0.902697, 'l': 0.800844}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.665441, 'cc': 1.665441, 'c': 1.000000, 'l': 0.851811}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.590672, 'cc': 1.590672, 'c': 0.955106, 'l': 0.813570}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.524165, 'cc': 1.524165, 'c': 0.915172, 'l': 0.779554}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.442741, 'cc': 1.442741, 'c': 0.866282, 'l': 0.737909}
# JET_21NP_JET_EffectiveNP_1__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.154249, 'cc': 1.154249, 'c': 1.000000, 'l': 0.960836}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.140888, 'cc': 1.140888, 'c': 0.988424, 'l': 0.949713}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.127984, 'cc': 1.127984, 'c': 0.977245, 'l': 0.938972}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.113317, 'cc': 1.113317, 'c': 0.964538, 'l': 0.926763}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.497554, 'cc': 1.497554, 'c': 1.000000, 'l': 0.886250}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.444902, 'cc': 1.444902, 'c': 0.964841, 'l': 0.855090}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.397963, 'cc': 1.397963, 'c': 0.933497, 'l': 0.827312}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.339419, 'cc': 1.339419, 'c': 0.894405, 'l': 0.792666}
# JET_21NP_JET_EffectiveNP_2__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.276241, 'cc': 1.276241, 'c': 1.000000, 'l': 0.930627}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.250495, 'cc': 1.250495, 'c': 0.979826, 'l': 0.911853}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.225214, 'cc': 1.225214, 'c': 0.960018, 'l': 0.893418}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.198044, 'cc': 1.198044, 'c': 0.938728, 'l': 0.873606}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.539923, 'cc': 1.539923, 'c': 1.000000, 'l': 0.877773}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.482110, 'cc': 1.482110, 'c': 0.962458, 'l': 0.844819}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.429787, 'cc': 1.429787, 'c': 0.928480, 'l': 0.814994}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.366535, 'cc': 1.366535, 'c': 0.887405, 'l': 0.778940}
# JET_21NP_JET_EffectiveNP_2__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.327196, 'cc': 1.327196, 'c': 1.000000, 'l': 0.918400}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.295607, 'cc': 1.295607, 'c': 0.976198, 'l': 0.896541}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.265023, 'cc': 1.265023, 'c': 0.953155, 'l': 0.875378}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.232177, 'cc': 1.232177, 'c': 0.928406, 'l': 0.852649}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.564859, 'cc': 1.564859, 'c': 1.000000, 'l': 0.872974}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.504097, 'cc': 1.504097, 'c': 0.961171, 'l': 0.839077}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.448565, 'cc': 1.448565, 'c': 0.925684, 'l': 0.808098}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.381962, 'cc': 1.381962, 'c': 0.883122, 'l': 0.770942}
# JET_21NP_JET_EffectiveNP_3__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.331409, 'cc': 1.331409, 'c': 1.000000, 'l': 0.917029}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.299347, 'cc': 1.299347, 'c': 0.975919, 'l': 0.894946}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.268309, 'cc': 1.268309, 'c': 0.952606, 'l': 0.873567}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.234843, 'cc': 1.234843, 'c': 0.927470, 'l': 0.850517}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.549120, 'cc': 1.549120, 'c': 1.000000, 'l': 0.876284}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.490210, 'cc': 1.490210, 'c': 0.961972, 'l': 0.842961}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.436619, 'cc': 1.436619, 'c': 0.927377, 'l': 0.812646}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.372385, 'cc': 1.372385, 'c': 0.885913, 'l': 0.776311}
# JET_21NP_JET_EffectiveNP_3__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.305817, 'cc': 1.305817, 'c': 1.000000, 'l': 0.923399}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.276709, 'cc': 1.276709, 'c': 0.977710, 'l': 0.902816}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.248363, 'cc': 1.248363, 'c': 0.956002, 'l': 0.882772}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.218112, 'cc': 1.218112, 'c': 0.932835, 'l': 0.861379}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.539989, 'cc': 1.539989, 'c': 1.000000, 'l': 0.878151}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.482268, 'cc': 1.482268, 'c': 0.962519, 'l': 0.845237}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.429938, 'cc': 1.429938, 'c': 0.928538, 'l': 0.815397}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.366806, 'cc': 1.366806, 'c': 0.887543, 'l': 0.779397}
# JET_21NP_JET_EffectiveNP_4__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.298300, 'cc': 1.298300, 'c': 1.000000, 'l': 0.925272}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.270108, 'cc': 1.270108, 'c': 0.978286, 'l': 0.905180}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.242584, 'cc': 1.242584, 'c': 0.957086, 'l': 0.885565}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.213073, 'cc': 1.213073, 'c': 0.934355, 'l': 0.864533}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.539356, 'cc': 1.539356, 'c': 1.000000, 'l': 0.878292}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.481791, 'cc': 1.481791, 'c': 0.962604, 'l': 0.845448}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.429578, 'cc': 1.429578, 'c': 0.928686, 'l': 0.815658}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.366530, 'cc': 1.366530, 'c': 0.887728, 'l': 0.779685}
# JET_21NP_JET_EffectiveNP_4__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.324554, 'cc': 1.324554, 'c': 1.000000, 'l': 0.918719}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.293324, 'cc': 1.293324, 'c': 0.976422, 'l': 0.897057}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.262988, 'cc': 1.262988, 'c': 0.953519, 'l': 0.876016}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.230363, 'cc': 1.230363, 'c': 0.928888, 'l': 0.853387}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.547815, 'cc': 1.547815, 'c': 1.000000, 'l': 0.876523}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.489069, 'cc': 1.489069, 'c': 0.962046, 'l': 0.843255}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.435691, 'cc': 1.435691, 'c': 0.927560, 'l': 0.813027}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.371548, 'cc': 1.371548, 'c': 0.886119, 'l': 0.776704}
# JET_21NP_JET_EffectiveNP_5__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.322973, 'cc': 1.322973, 'c': 1.000000, 'l': 0.919086}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.291908, 'cc': 1.291908, 'c': 0.976519, 'l': 0.897505}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.261786, 'cc': 1.261786, 'c': 0.953750, 'l': 0.876578}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.229344, 'cc': 1.229344, 'c': 0.929228, 'l': 0.854041}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.543409, 'cc': 1.543409, 'c': 1.000000, 'l': 0.877451}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.485226, 'cc': 1.485226, 'c': 0.962302, 'l': 0.844373}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.432595, 'cc': 1.432595, 'c': 0.928202, 'l': 0.814451}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.368925, 'cc': 1.368925, 'c': 0.886949, 'l': 0.778254}
# JET_21NP_JET_EffectiveNP_5__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.310228, 'cc': 1.310228, 'c': 1.000000, 'l': 0.922311}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.280700, 'cc': 1.280700, 'c': 0.977463, 'l': 0.901525}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.251794, 'cc': 1.251794, 'c': 0.955401, 'l': 0.881177}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.221063, 'cc': 1.221063, 'c': 0.931947, 'l': 0.859545}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.547575, 'cc': 1.547575, 'c': 1.000000, 'l': 0.876520}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.488922, 'cc': 1.488922, 'c': 0.962100, 'l': 0.843300}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.435549, 'cc': 1.435549, 'c': 0.927612, 'l': 0.813070}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.371530, 'cc': 1.371530, 'c': 0.886245, 'l': 0.776811}
# JET_21NP_JET_EffectiveNP_6__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.313618, 'cc': 1.313618, 'c': 1.000000, 'l': 0.921512}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.283669, 'cc': 1.283669, 'c': 0.977202, 'l': 0.900503}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.254442, 'cc': 1.254442, 'c': 0.954952, 'l': 0.880000}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.223268, 'cc': 1.223268, 'c': 0.931221, 'l': 0.858131}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.551199, 'cc': 1.551199, 'c': 1.000000, 'l': 0.875823}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.491957, 'cc': 1.491957, 'c': 0.961809, 'l': 0.842375}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.438344, 'cc': 1.438344, 'c': 0.927247, 'l': 0.812105}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.373610, 'cc': 1.373610, 'c': 0.885515, 'l': 0.775555}
# JET_21NP_JET_EffectiveNP_6__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.312750, 'cc': 1.312750, 'c': 1.000000, 'l': 0.921654}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.282813, 'cc': 1.282813, 'c': 0.977195, 'l': 0.900636}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.253747, 'cc': 1.253747, 'c': 0.955054, 'l': 0.880229}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.222693, 'cc': 1.222693, 'c': 0.931398, 'l': 0.858427}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.543510, 'cc': 1.543510, 'c': 1.000000, 'l': 0.877389}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.485265, 'cc': 1.485265, 'c': 0.962264, 'l': 0.844280}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.432432, 'cc': 1.432432, 'c': 0.928035, 'l': 0.814248}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.368979, 'cc': 1.368979, 'c': 0.886926, 'l': 0.778179}
# JET_21NP_JET_EffectiveNP_7__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.310007, 'cc': 1.310007, 'c': 1.000000, 'l': 0.922334}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.280387, 'cc': 1.280387, 'c': 0.977389, 'l': 0.901479}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.251630, 'cc': 1.251630, 'c': 0.955437, 'l': 0.881233}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.220900, 'cc': 1.220900, 'c': 0.931979, 'l': 0.859596}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.544007, 'cc': 1.544007, 'c': 1.000000, 'l': 0.877222}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.485701, 'cc': 1.485701, 'c': 0.962237, 'l': 0.844096}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.432847, 'cc': 1.432847, 'c': 0.928005, 'l': 0.814067}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.369286, 'cc': 1.369286, 'c': 0.886839, 'l': 0.777955}
# JET_21NP_JET_EffectiveNP_7__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.323650, 'cc': 1.323650, 'c': 1.000000, 'l': 0.919009}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.292552, 'cc': 1.292552, 'c': 0.976506, 'l': 0.897418}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.262234, 'cc': 1.262234, 'c': 0.953600, 'l': 0.876368}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.229861, 'cc': 1.229861, 'c': 0.929143, 'l': 0.853891}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.550964, 'cc': 1.550964, 'c': 1.000000, 'l': 0.875893}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.491857, 'cc': 1.491857, 'c': 0.961890, 'l': 0.842513}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.438227, 'cc': 1.438227, 'c': 0.927312, 'l': 0.812226}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.373417, 'cc': 1.373417, 'c': 0.885524, 'l': 0.775625}
# JET_21NP_JET_EffectiveNP_8restTerm__1up 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.317080, 'cc': 1.317080, 'c': 1.000000, 'l': 0.920593}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.286729, 'cc': 1.286729, 'c': 0.976956, 'l': 0.899379}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.257109, 'cc': 1.257109, 'c': 0.954467, 'l': 0.878676}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.225574, 'cc': 1.225574, 'c': 0.930524, 'l': 0.856634}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.553841, 'cc': 1.553841, 'c': 1.000000, 'l': 0.875129}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.494258, 'cc': 1.494258, 'c': 0.961655, 'l': 0.841572}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.440181, 'cc': 1.440181, 'c': 0.926853, 'l': 0.811115}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.375256, 'cc': 1.375256, 'c': 0.885069, 'l': 0.774549}
# JET_21NP_JET_EffectiveNP_8restTerm__1down 
flav_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.317547, 'cc': 1.317547, 'c': 1.000000, 'l': 0.920452}
flav_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.287094, 'cc': 1.287094, 'c': 0.976887, 'l': 0.899177}
flav_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.257540, 'cc': 1.257540, 'c': 0.954455, 'l': 0.878531}
flav_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.225948, 'cc': 1.225948, 'c': 0.930478, 'l': 0.856460}
flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.541450, 'cc': 1.541450, 'c': 1.000000, 'l': 0.877864}
flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.483555, 'cc': 1.483555, 'c': 0.962441, 'l': 0.844892}
flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.431164, 'cc': 1.431164, 'c': 0.928454, 'l': 0.815056}
flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.367728, 'cc': 1.367728, 'c': 0.887300, 'l': 0.778928}
# LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down 
flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Comb_Baseline_Kin__1up 
flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Comb_Baseline_Kin__1down 
flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Comb_Modelling_Kin__1up 
flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Comb_Modelling_Kin__1down 
flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up 
flav_map[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down 
flav_map[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Comb_Tracking_Kin__1up 
flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Comb_Tracking_Kin__1down 
flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up 
flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down 
flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up 
flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down 
flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up 
flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down 
flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up 
flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down 
flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Strong_JET_Comb_Baseline_All__1up 
flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Strong_JET_Comb_Baseline_All__1down 
flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Strong_JET_Comb_Modelling_All__1up 
flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Strong_JET_Comb_Modelling_All__1down 
flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Strong_JET_Comb_TotalStat_All__1up 
flav_map[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Strong_JET_Comb_TotalStat_All__1down 
flav_map[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Strong_JET_Comb_Tracking_All__1up 
flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}
# LARGERJET_Strong_JET_Comb_Tracking_All__1down 
flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.321579, 'cc': 1.321579, 'c': 1.000000, 'l': 0.919451}
flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.290685, 'cc': 1.290685, 'c': 0.976623, 'l': 0.897957}
flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.260681, 'cc': 1.260681, 'c': 0.953920, 'l': 0.877083}
flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.228545, 'cc': 1.228545, 'c': 0.929604, 'l': 0.854725}
flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.541862, 'cc': 1.541862, 'c': 1.000000, 'l': 0.877818}
flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.483912, 'cc': 1.483912, 'c': 0.962415, 'l': 0.844826}
flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.431450, 'cc': 1.431450, 'c': 0.928390, 'l': 0.814958}
flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.367997, 'cc': 1.367997, 'c': 0.887237, 'l': 0.778833}

# PDF variations on ttbar

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

# ttgendw 
f_ca_map[2]['el']["ttgendw"] =  1.175582
f_ca_map[3]['el']["ttgendw"] =  1.275476
f_ca_map[4]['el']["ttgendw"] =  1.356745
f_ca_map[5]['el']["ttgendw"] =  1.149121
f_ca_map[2]['mu']["ttgendw"] =  1.192963
f_ca_map[3]['mu']["ttgendw"] =  1.190882
f_ca_map[4]['mu']["ttgendw"] =  1.174277
f_ca_map[5]['mu']["ttgendw"] =  1.097489
# ttgenup 
f_ca_map[2]['el']["ttgenup"] =  1.175797
f_ca_map[3]['el']["ttgenup"] =  1.275415
f_ca_map[4]['el']["ttgenup"] =  1.356994
f_ca_map[5]['el']["ttgenup"] =  1.148937
f_ca_map[2]['mu']["ttgenup"] =  1.192954
f_ca_map[3]['mu']["ttgenup"] =  1.190979
f_ca_map[4]['mu']["ttgenup"] =  1.174399
f_ca_map[5]['mu']["ttgenup"] =  1.097436
# ttisrfsrup 
f_ca_map[2]['el']["ttisrfsrup"] =  1.175715
f_ca_map[3]['el']["ttisrfsrup"] =  1.275438
f_ca_map[4]['el']["ttisrfsrup"] =  1.356899
f_ca_map[5]['el']["ttisrfsrup"] =  1.149007
f_ca_map[2]['mu']["ttisrfsrup"] =  1.193015
f_ca_map[3]['mu']["ttisrfsrup"] =  1.190316
f_ca_map[4]['mu']["ttisrfsrup"] =  1.173558
f_ca_map[5]['mu']["ttisrfsrup"] =  1.097804
# ttisrfsrdw 
f_ca_map[2]['el']["ttisrfsrdw"] =  1.175529
f_ca_map[3]['el']["ttisrfsrdw"] =  1.275491
f_ca_map[4]['el']["ttisrfsrdw"] =  1.356684
f_ca_map[5]['el']["ttisrfsrdw"] =  1.149166
f_ca_map[2]['mu']["ttisrfsrdw"] =  1.192930
f_ca_map[3]['mu']["ttisrfsrdw"] =  1.191247
f_ca_map[4]['mu']["ttisrfsrdw"] =  1.174738
f_ca_map[5]['mu']["ttisrfsrdw"] =  1.097289
# ttpsup 
f_ca_map[2]['el']["ttpsup"] =  1.175627
f_ca_map[3]['el']["ttpsup"] =  1.275463
f_ca_map[4]['el']["ttpsup"] =  1.356797
f_ca_map[5]['el']["ttpsup"] =  1.149082
f_ca_map[2]['mu']["ttpsup"] =  1.192956
f_ca_map[3]['mu']["ttpsup"] =  1.190954
f_ca_map[4]['mu']["ttpsup"] =  1.174368
f_ca_map[5]['mu']["ttpsup"] =  1.097450
# ttpsdw 
f_ca_map[2]['el']["ttpsdw"] =  1.190866
f_ca_map[3]['el']["ttpsdw"] =  1.271576
f_ca_map[4]['el']["ttpsdw"] =  1.371735
f_ca_map[5]['el']["ttpsdw"] =  1.139085
f_ca_map[2]['mu']["ttpsdw"] =  1.192943
f_ca_map[3]['mu']["ttpsdw"] =  1.191100
f_ca_map[4]['mu']["ttpsdw"] =  1.174553
f_ca_map[5]['mu']["ttpsdw"] =  1.097369

# ttgendw 
frac[2]['el']["ttgendw"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["ttgendw"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["ttgendw"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["ttgendw"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["ttgendw"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["ttgendw"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["ttgendw"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["ttgendw"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# ttgenup 
frac[2]['el']["ttgenup"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["ttgenup"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["ttgenup"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["ttgenup"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["ttgenup"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["ttgenup"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["ttgenup"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["ttgenup"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# ttisrfsrup 
frac[2]['el']["ttisrfsrup"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["ttisrfsrup"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["ttisrfsrup"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["ttisrfsrup"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["ttisrfsrup"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["ttisrfsrup"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["ttisrfsrup"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["ttisrfsrup"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# ttisrfsrdw 
frac[2]['el']["ttisrfsrdw"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["ttisrfsrdw"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["ttisrfsrdw"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["ttisrfsrdw"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["ttisrfsrdw"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["ttisrfsrdw"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["ttisrfsrdw"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["ttisrfsrdw"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# ttpsup 
frac[2]['el']["ttpsup"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["ttpsup"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["ttpsup"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["ttpsup"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["ttpsup"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["ttpsup"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["ttpsup"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["ttpsup"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}
# ttpsdw 
frac[2]['el']["ttpsdw"] = {'bb': 0.094190,'cc': 0.064219,'c': 0.209175,'l': 0.632416}
frac[3]['el']["ttpsdw"] = {'bb': 0.117293,'cc': 0.098681,'c': 0.218953,'l': 0.565073}
frac[4]['el']["ttpsdw"] = {'bb': 0.139786,'cc': 0.137488,'c': 0.215466,'l': 0.507260}
frac[5]['el']["ttpsdw"] = {'bb': 0.147319,'cc': 0.149638,'c': 0.210684,'l': 0.492359}
frac[2]['mu']["ttpsdw"] = {'bb': 0.083239,'cc': 0.063033,'c': 0.205028,'l': 0.648700}
frac[3]['mu']["ttpsdw"] = {'bb': 0.106210,'cc': 0.096920,'c': 0.215635,'l': 0.581234}
frac[4]['mu']["ttpsdw"] = {'bb': 0.129284,'cc': 0.132728,'c': 0.207294,'l': 0.530694}
frac[5]['mu']["ttpsdw"] = {'bb': 0.138329,'cc': 0.144888,'c': 0.203287,'l': 0.513496}

# ttgendw 
flav_map[2]['el']["ttgendw"] = {'bb': 1.330862, 'cc': 1.330862, 'c': 1.000000, 'l': 0.917125}
flav_map[3]['el']["ttgendw"] = {'bb': 1.298874, 'cc': 1.298874, 'c': 0.975965, 'l': 0.895082}
flav_map[4]['el']["ttgendw"] = {'bb': 1.267850, 'cc': 1.267850, 'c': 0.952653, 'l': 0.873702}
flav_map[5]['el']["ttgendw"] = {'bb': 1.234665, 'cc': 1.234665, 'c': 0.927719, 'l': 0.850834}
flav_map[2]['mu']["ttgendw"] = {'bb': 1.544760, 'cc': 1.544760, 'c': 1.000000, 'l': 0.877165}
flav_map[3]['mu']["ttgendw"] = {'bb': 1.486402, 'cc': 1.486402, 'c': 0.962222, 'l': 0.844028}
flav_map[4]['mu']["ttgendw"] = {'bb': 1.433591, 'cc': 1.433591, 'c': 0.928035, 'l': 0.814040}
flav_map[5]['mu']["ttgendw"] = {'bb': 1.369742, 'cc': 1.369742, 'c': 0.886702, 'l': 0.777784}
# ttgenup 
flav_map[2]['el']["ttgenup"] = {'bb': 1.348978, 'cc': 1.348978, 'c': 1.000000, 'l': 0.912587}
flav_map[3]['el']["ttgenup"] = {'bb': 1.314825, 'cc': 1.314825, 'c': 0.974682, 'l': 0.889482}
flav_map[4]['el']["ttgenup"] = {'bb': 1.281785, 'cc': 1.281785, 'c': 0.950190, 'l': 0.867131}
flav_map[5]['el']["ttgenup"] = {'bb': 1.246539, 'cc': 1.246539, 'c': 0.924062, 'l': 0.843287}
flav_map[2]['mu']["ttgenup"] = {'bb': 1.550346, 'cc': 1.550346, 'c': 1.000000, 'l': 0.875906}
flav_map[3]['mu']["ttgenup"] = {'bb': 1.491200, 'cc': 1.491200, 'c': 0.961849, 'l': 0.842489}
flav_map[4]['mu']["ttgenup"] = {'bb': 1.437714, 'cc': 1.437714, 'c': 0.927350, 'l': 0.812271}
flav_map[5]['mu']["ttgenup"] = {'bb': 1.373100, 'cc': 1.373100, 'c': 0.885673, 'l': 0.775766}
# ttisrfsrup 
flav_map[2]['el']["ttisrfsrup"] = {'bb': 1.342106, 'cc': 1.342106, 'c': 1.000000, 'l': 0.914309}
flav_map[3]['el']["ttisrfsrup"] = {'bb': 1.308779, 'cc': 1.308779, 'c': 0.975168, 'l': 0.891605}
flav_map[4]['el']["ttisrfsrup"] = {'bb': 1.276507, 'cc': 1.276507, 'c': 0.951123, 'l': 0.869620}
flav_map[5]['el']["ttisrfsrup"] = {'bb': 1.242045, 'cc': 1.242045, 'c': 0.925445, 'l': 0.846143}
flav_map[2]['mu']["ttisrfsrup"] = {'bb': 1.512214, 'cc': 1.512214, 'c': 1.000000, 'l': 0.884504}
flav_map[3]['mu']["ttisrfsrup"] = {'bb': 1.458377, 'cc': 1.458377, 'c': 0.964399, 'l': 0.853014}
flav_map[4]['mu']["ttisrfsrup"] = {'bb': 1.409447, 'cc': 1.409447, 'c': 0.932042, 'l': 0.824395}
flav_map[5]['mu']["ttisrfsrup"] = {'bb': 1.350021, 'cc': 1.350021, 'c': 0.892745, 'l': 0.789636}
# ttisrfsrdw 
flav_map[2]['el']["ttisrfsrdw"] = {'bb': 1.326471, 'cc': 1.326471, 'c': 1.000000, 'l': 0.918225}
flav_map[3]['el']["ttisrfsrdw"] = {'bb': 1.295002, 'cc': 1.295002, 'c': 0.976276, 'l': 0.896441}
flav_map[4]['el']["ttisrfsrdw"] = {'bb': 1.264461, 'cc': 1.264461, 'c': 0.953252, 'l': 0.875300}
flav_map[5]['el']["ttisrfsrdw"] = {'bb': 1.231773, 'cc': 1.231773, 'c': 0.928609, 'l': 0.852672}
flav_map[2]['mu']["ttisrfsrdw"] = {'bb': 1.565782, 'cc': 1.565782, 'c': 1.000000, 'l': 0.872425}
flav_map[3]['mu']["ttisrfsrdw"] = {'bb': 1.504437, 'cc': 1.504437, 'c': 0.960821, 'l': 0.838244}
flav_map[4]['mu']["ttisrfsrdw"] = {'bb': 1.449076, 'cc': 1.449076, 'c': 0.925465, 'l': 0.807398}
flav_map[5]['mu']["ttisrfsrdw"] = {'bb': 1.382339, 'cc': 1.382339, 'c': 0.882843, 'l': 0.770214}
# ttpsup 
flav_map[2]['el']["ttpsup"] = {'bb': 1.334675, 'cc': 1.334675, 'c': 1.000000, 'l': 0.916170}
flav_map[3]['el']["ttpsup"] = {'bb': 1.302235, 'cc': 1.302235, 'c': 0.975695, 'l': 0.893902}
flav_map[4]['el']["ttpsup"] = {'bb': 1.270789, 'cc': 1.270789, 'c': 0.952134, 'l': 0.872316}
flav_map[5]['el']["ttpsup"] = {'bb': 1.237172, 'cc': 1.237172, 'c': 0.926946, 'l': 0.849241}
flav_map[2]['mu']["ttpsup"] = {'bb': 1.548902, 'cc': 1.548902, 'c': 1.000000, 'l': 0.876231}
flav_map[3]['mu']["ttpsup"] = {'bb': 1.489959, 'cc': 1.489959, 'c': 0.961946, 'l': 0.842887}
flav_map[4]['mu']["ttpsup"] = {'bb': 1.436648, 'cc': 1.436648, 'c': 0.927527, 'l': 0.812728}
flav_map[5]['mu']["ttpsup"] = {'bb': 1.372232, 'cc': 1.372232, 'c': 0.885939, 'l': 0.776287}
# ttpsdw 
flav_map[2]['el']["ttpsdw"] = {'bb': 2.602219, 'cc': 2.602219, 'c': 1.000000, 'l': 0.598674}
flav_map[3]['el']["ttpsdw"] = {'bb': 2.324949, 'cc': 2.324949, 'c': 0.893449, 'l': 0.534884}
flav_map[4]['el']["ttpsdw"] = {'bb': 2.097421, 'cc': 2.097421, 'c': 0.806012, 'l': 0.482539}
flav_map[5]['el']["ttpsdw"] = {'bb': 1.889364, 'cc': 1.889364, 'c': 0.726059, 'l': 0.434672}
flav_map[2]['mu']["ttpsdw"] = {'bb': 1.557324, 'cc': 1.557324, 'c': 1.000000, 'l': 0.874332}
flav_map[3]['mu']["ttpsdw"] = {'bb': 1.497187, 'cc': 1.497187, 'c': 0.961384, 'l': 0.840569}
flav_map[4]['mu']["ttpsdw"] = {'bb': 1.442856, 'cc': 1.442856, 'c': 0.926497, 'l': 0.810066}
flav_map[5]['mu']["ttpsdw"] = {'bb': 1.377284, 'cc': 1.377284, 'c': 0.884391, 'l': 0.773251}

#############################################
################# OLD #######################
### Do not use anything below this line #####
#############################################
#############################################

# flavour map

#flav_map[2]['el'][""] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el'][""] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el'][""] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el'][""] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu'][""] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu'][""] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu'][""] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu'][""] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## ttxsecup 
#flav_map[2]['el']["ttxsecup"] = {'bb': 1.402477, 'cc': 1.402477, 'c': 1.000000, 'l': 0.899785}
#flav_map[3]['el']["ttxsecup"] = {'bb': 1.361655, 'cc': 1.361655, 'c': 0.970893, 'l': 0.873594}
#flav_map[4]['el']["ttxsecup"] = {'bb': 1.322592, 'cc': 1.322592, 'c': 0.943040, 'l': 0.848533}
#flav_map[5]['el']["ttxsecup"] = {'bb': 1.281123, 'cc': 1.281123, 'c': 0.913472, 'l': 0.821928}
#flav_map[2]['mu']["ttxsecup"] = {'bb': 1.556236, 'cc': 1.556236, 'c': 1.000000, 'l': 0.875139}
#flav_map[3]['mu']["ttxsecup"] = {'bb': 1.496556, 'cc': 1.496556, 'c': 0.961651, 'l': 0.841578}
#flav_map[4]['mu']["ttxsecup"] = {'bb': 1.442664, 'cc': 1.442664, 'c': 0.927021, 'l': 0.811272}
#flav_map[5]['mu']["ttxsecup"] = {'bb': 1.377054, 'cc': 1.377054, 'c': 0.884862, 'l': 0.774377}
## ttxsecdw 
#flav_map[2]['el']["ttxsecdw"] = {'bb': 1.404276, 'cc': 1.404276, 'c': 1.000000, 'l': 0.899336}
#flav_map[3]['el']["ttxsecdw"] = {'bb': 1.363224, 'cc': 1.363224, 'c': 0.970767, 'l': 0.873046}
#flav_map[4]['el']["ttxsecdw"] = {'bb': 1.323952, 'cc': 1.323952, 'c': 0.942800, 'l': 0.847895}
#flav_map[5]['el']["ttxsecdw"] = {'bb': 1.282270, 'cc': 1.282270, 'c': 0.913119, 'l': 0.821201}
#flav_map[2]['mu']["ttxsecdw"] = {'bb': 1.553332, 'cc': 1.553332, 'c': 1.000000, 'l': 0.875791}
#flav_map[3]['mu']["ttxsecdw"] = {'bb': 1.494063, 'cc': 1.494063, 'c': 0.961844, 'l': 0.842374}
#flav_map[4]['mu']["ttxsecdw"] = {'bb': 1.440521, 'cc': 1.440521, 'c': 0.927375, 'l': 0.812186}
#flav_map[5]['mu']["ttxsecdw"] = {'bb': 1.375311, 'cc': 1.375311, 'c': 0.885394, 'l': 0.775420}
## singletopup 
#flav_map[2]['el']["singletopup"] = {'bb': 1.363253, 'cc': 1.363253, 'c': 1.000000, 'l': 0.909551}
#flav_map[3]['el']["singletopup"] = {'bb': 1.327337, 'cc': 1.327337, 'c': 0.973655, 'l': 0.885589}
#flav_map[4]['el']["singletopup"] = {'bb': 1.292778, 'cc': 1.292778, 'c': 0.948304, 'l': 0.862531}
#flav_map[5]['el']["singletopup"] = {'bb': 1.255883, 'cc': 1.255883, 'c': 0.921240, 'l': 0.837915}
#flav_map[2]['mu']["singletopup"] = {'bb': 1.518687, 'cc': 1.518687, 'c': 1.000000, 'l': 0.883568}
#flav_map[3]['mu']["singletopup"] = {'bb': 1.464238, 'cc': 1.464238, 'c': 0.964147, 'l': 0.851889}
#flav_map[4]['mu']["singletopup"] = {'bb': 1.414826, 'cc': 1.414826, 'c': 0.931611, 'l': 0.823141}
#flav_map[5]['mu']["singletopup"] = {'bb': 1.354355, 'cc': 1.354355, 'c': 0.891793, 'l': 0.787959}
## singletopdw 
#flav_map[2]['el']["singletopdw"] = {'bb': 1.438501, 'cc': 1.438501, 'c': 1.000000, 'l': 0.890815}
#flav_map[3]['el']["singletopdw"] = {'bb': 1.393001, 'cc': 1.393001, 'c': 0.968370, 'l': 0.862638}
#flav_map[4]['el']["singletopdw"] = {'bb': 1.349683, 'cc': 1.349683, 'c': 0.938257, 'l': 0.835813}
#flav_map[5]['el']["singletopdw"] = {'bb': 1.303931, 'cc': 1.303931, 'c': 0.906451, 'l': 0.807480}
#flav_map[2]['mu']["singletopdw"] = {'bb': 1.586092, 'cc': 1.586092, 'c': 1.000000, 'l': 0.868437}
#flav_map[3]['mu']["singletopdw"] = {'bb': 1.522134, 'cc': 1.522134, 'c': 0.959676, 'l': 0.833418}
#flav_map[4]['mu']["singletopdw"] = {'bb': 1.464604, 'cc': 1.464604, 'c': 0.923404, 'l': 0.801918}
#flav_map[5]['mu']["singletopdw"] = {'bb': 1.394852, 'cc': 1.394852, 'c': 0.879427, 'l': 0.763727}
## wnorm__1up 
#flav_map[2]['el']["wnorm__1up"] = {'bb': 1.403603, 'cc': 1.403603, 'c': 1.000000, 'l': 0.899504}
#flav_map[3]['el']["wnorm__1up"] = {'bb': 1.362637, 'cc': 1.362637, 'c': 0.970814, 'l': 0.873251}
#flav_map[4]['el']["wnorm__1up"] = {'bb': 1.323443, 'cc': 1.323443, 'c': 0.942890, 'l': 0.848134}
#flav_map[5]['el']["wnorm__1up"] = {'bb': 1.281841, 'cc': 1.281841, 'c': 0.913251, 'l': 0.821473}
#flav_map[2]['mu']["wnorm__1up"] = {'bb': 1.554777, 'cc': 1.554777, 'c': 1.000000, 'l': 0.875466}
#flav_map[3]['mu']["wnorm__1up"] = {'bb': 1.495304, 'cc': 1.495304, 'c': 0.961748, 'l': 0.841978}
#flav_map[4]['mu']["wnorm__1up"] = {'bb': 1.441588, 'cc': 1.441588, 'c': 0.927199, 'l': 0.811731}
#flav_map[5]['mu']["wnorm__1up"] = {'bb': 1.376178, 'cc': 1.376178, 'c': 0.885129, 'l': 0.774900}
## wnorm__1down 
#flav_map[2]['el']["wnorm__1down"] = {'bb': 1.403296, 'cc': 1.403296, 'c': 1.000000, 'l': 0.899580}
#flav_map[3]['el']["wnorm__1down"] = {'bb': 1.362369, 'cc': 1.362369, 'c': 0.970835, 'l': 0.873344}
#flav_map[4]['el']["wnorm__1down"] = {'bb': 1.323211, 'cc': 1.323211, 'c': 0.942931, 'l': 0.848242}
#flav_map[5]['el']["wnorm__1down"] = {'bb': 1.281645, 'cc': 1.281645, 'c': 0.913311, 'l': 0.821597}
#flav_map[2]['mu']["wnorm__1down"] = {'bb': 1.554559, 'cc': 1.554559, 'c': 1.000000, 'l': 0.875515}
#flav_map[3]['mu']["wnorm__1down"] = {'bb': 1.495116, 'cc': 1.495116, 'c': 0.961763, 'l': 0.842038}
#flav_map[4]['mu']["wnorm__1down"] = {'bb': 1.441427, 'cc': 1.441427, 'c': 0.927226, 'l': 0.811800}
#flav_map[5]['mu']["wnorm__1down"] = {'bb': 1.376047, 'cc': 1.376047, 'c': 0.885169, 'l': 0.774979}
## MET_SoftTrk_ResoPara 
#flav_map[2]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.378557, 'cc': 1.378557, 'c': 1.000000, 'l': 0.905764}
#flav_map[3]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.340804, 'cc': 1.340804, 'c': 0.972614, 'l': 0.880958}
#flav_map[4]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.304412, 'cc': 1.304412, 'c': 0.946215, 'l': 0.857047}
#flav_map[5]['el']["MET_SoftTrk_ResoPara"] = {'bb': 1.265700, 'cc': 1.265700, 'c': 0.918134, 'l': 0.831612}
#flav_map[2]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.586539, 'cc': 1.586539, 'c': 1.000000, 'l': 0.868542}
#flav_map[3]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.522162, 'cc': 1.522162, 'c': 0.959423, 'l': 0.833299}
#flav_map[4]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.464356, 'cc': 1.464356, 'c': 0.922987, 'l': 0.801653}
#flav_map[5]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 1.395042, 'cc': 1.395042, 'c': 0.879299, 'l': 0.763708}
## MET_SoftTrk_ResoPerp 
#flav_map[2]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.414799, 'cc': 1.414799, 'c': 1.000000, 'l': 0.896907}
#flav_map[3]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.372313, 'cc': 1.372313, 'c': 0.969971, 'l': 0.869974}
#flav_map[4]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.331769, 'cc': 1.331769, 'c': 0.941313, 'l': 0.844271}
#flav_map[5]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 1.288720, 'cc': 1.288720, 'c': 0.910886, 'l': 0.816980}
#flav_map[2]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.584058, 'cc': 1.584058, 'c': 1.000000, 'l': 0.868891}
#flav_map[3]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.520143, 'cc': 1.520143, 'c': 0.959651, 'l': 0.833833}
#flav_map[4]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.462906, 'cc': 1.462906, 'c': 0.923518, 'l': 0.802437}
#flav_map[5]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 1.393572, 'cc': 1.393572, 'c': 0.879748, 'l': 0.764405}
## MET_SoftTrk_ScaleUp 
#flav_map[2]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.425289, 'cc': 1.425289, 'c': 1.000000, 'l': 0.894147}
#flav_map[3]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.381614, 'cc': 1.381614, 'c': 0.969357, 'l': 0.866748}
#flav_map[4]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.339741, 'cc': 1.339741, 'c': 0.939978, 'l': 0.840479}
#flav_map[5]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 1.295584, 'cc': 1.295584, 'c': 0.908997, 'l': 0.812778}
#flav_map[2]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.567485, 'cc': 1.567485, 'c': 1.000000, 'l': 0.872719}
#flav_map[3]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.506086, 'cc': 1.506086, 'c': 0.960830, 'l': 0.838534}
#flav_map[4]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.450740, 'cc': 1.450740, 'c': 0.925521, 'l': 0.807720}
#flav_map[5]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 1.383831, 'cc': 1.383831, 'c': 0.882835, 'l': 0.770467}
## MET_SoftTrk_ScaleDown 
#flav_map[2]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.375679, 'cc': 1.375679, 'c': 1.000000, 'l': 0.906490}
#flav_map[3]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.338190, 'cc': 1.338190, 'c': 0.972749, 'l': 0.881788}
#flav_map[4]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.302186, 'cc': 1.302186, 'c': 0.946577, 'l': 0.858063}
#flav_map[5]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 1.263982, 'cc': 1.263982, 'c': 0.918806, 'l': 0.832889}
#flav_map[2]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.558088, 'cc': 1.558088, 'c': 1.000000, 'l': 0.874728}
#flav_map[3]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.498301, 'cc': 1.498301, 'c': 0.961628, 'l': 0.841162}
#flav_map[4]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.444041, 'cc': 1.444041, 'c': 0.926803, 'l': 0.810700}
#flav_map[5]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 1.377990, 'cc': 1.377990, 'c': 0.884411, 'l': 0.773619}
## EG_RESOLUTION_ALL__1up 
#flav_map[2]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.404362, 'cc': 1.404362, 'c': 1.000000, 'l': 0.899359}
#flav_map[3]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.363278, 'cc': 1.363278, 'c': 0.970746, 'l': 0.873049}
#flav_map[4]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.324059, 'cc': 1.324059, 'c': 0.942819, 'l': 0.847932}
#flav_map[5]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.282319, 'cc': 1.282319, 'c': 0.913097, 'l': 0.821202}
#flav_map[2]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.554270, 'cc': 1.554270, 'c': 1.000000, 'l': 0.875581}
#flav_map[3]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.494868, 'cc': 1.494868, 'c': 0.961781, 'l': 0.842117}
#flav_map[4]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.441213, 'cc': 1.441213, 'c': 0.927260, 'l': 0.811891}
#flav_map[5]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 1.375872, 'cc': 1.375872, 'c': 0.885221, 'l': 0.775082}
## EG_RESOLUTION_ALL__1down 
#flav_map[2]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.387693, 'cc': 1.387693, 'c': 1.000000, 'l': 0.903425}
#flav_map[3]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.348827, 'cc': 1.348827, 'c': 0.971992, 'l': 0.878122}
#flav_map[4]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.311428, 'cc': 1.311428, 'c': 0.945042, 'l': 0.853775}
#flav_map[5]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.271660, 'cc': 1.271660, 'c': 0.916384, 'l': 0.827885}
#flav_map[2]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.554815, 'cc': 1.554815, 'c': 1.000000, 'l': 0.875458}
#flav_map[3]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.495336, 'cc': 1.495336, 'c': 0.961745, 'l': 0.841967}
#flav_map[4]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.441616, 'cc': 1.441616, 'c': 0.927194, 'l': 0.811719}
#flav_map[5]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 1.376197, 'cc': 1.376197, 'c': 0.885120, 'l': 0.774885}
## EG_SCALE_ALL__1up 
#flav_map[2]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.397360, 'cc': 1.397360, 'c': 1.000000, 'l': 0.901124}
#flav_map[3]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.357105, 'cc': 1.357105, 'c': 0.971192, 'l': 0.875165}
#flav_map[4]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.318764, 'cc': 1.318764, 'c': 0.943754, 'l': 0.850440}
#flav_map[5]['el']["EG_SCALE_ALL__1up"] = {'bb': 1.277810, 'cc': 1.277810, 'c': 0.914446, 'l': 0.824030}
#flav_map[2]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.554462, 'cc': 1.554462, 'c': 1.000000, 'l': 0.875537}
#flav_map[3]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.495034, 'cc': 1.495034, 'c': 0.961769, 'l': 0.842064}
#flav_map[4]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.441355, 'cc': 1.441355, 'c': 0.927237, 'l': 0.811830}
#flav_map[5]['mu']["EG_SCALE_ALL__1up"] = {'bb': 1.375989, 'cc': 1.375989, 'c': 0.885186, 'l': 0.775013}
## EG_SCALE_ALL__1down 
#flav_map[2]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.385216, 'cc': 1.385216, 'c': 1.000000, 'l': 0.904084}
#flav_map[3]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.346545, 'cc': 1.346545, 'c': 0.972083, 'l': 0.878845}
#flav_map[4]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.309521, 'cc': 1.309521, 'c': 0.945355, 'l': 0.854681}
#flav_map[5]['el']["EG_SCALE_ALL__1down"] = {'bb': 1.270080, 'cc': 1.270080, 'c': 0.916882, 'l': 0.828939}
#flav_map[2]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.554624, 'cc': 1.554624, 'c': 1.000000, 'l': 0.875501}
#flav_map[3]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.495172, 'cc': 1.495172, 'c': 0.961758, 'l': 0.842020}
#flav_map[4]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.441474, 'cc': 1.441474, 'c': 0.927217, 'l': 0.811780}
#flav_map[5]['mu']["EG_SCALE_ALL__1down"] = {'bb': 1.376082, 'cc': 1.376082, 'c': 0.885154, 'l': 0.774953}
## MUON_ID__1up 
#flav_map[2]['el']["MUON_ID__1up"] = {'bb': 1.403633, 'cc': 1.403633, 'c': 1.000000, 'l': 0.899497}
#flav_map[3]['el']["MUON_ID__1up"] = {'bb': 1.362663, 'cc': 1.362663, 'c': 0.970812, 'l': 0.873242}
#flav_map[4]['el']["MUON_ID__1up"] = {'bb': 1.323466, 'cc': 1.323466, 'c': 0.942886, 'l': 0.848123}
#flav_map[5]['el']["MUON_ID__1up"] = {'bb': 1.281861, 'cc': 1.281861, 'c': 0.913245, 'l': 0.821460}
#flav_map[2]['mu']["MUON_ID__1up"] = {'bb': 1.550067, 'cc': 1.550067, 'c': 1.000000, 'l': 0.876530}
#flav_map[3]['mu']["MUON_ID__1up"] = {'bb': 1.491322, 'cc': 1.491322, 'c': 0.962102, 'l': 0.843312}
#flav_map[4]['mu']["MUON_ID__1up"] = {'bb': 1.438138, 'cc': 1.438138, 'c': 0.927791, 'l': 0.813237}
#flav_map[5]['mu']["MUON_ID__1up"] = {'bb': 1.373557, 'cc': 1.373557, 'c': 0.886128, 'l': 0.776718}
## MUON_ID__1down 
#flav_map[2]['el']["MUON_ID__1down"] = {'bb': 1.402939, 'cc': 1.402939, 'c': 1.000000, 'l': 0.899669}
#flav_map[3]['el']["MUON_ID__1down"] = {'bb': 1.362058, 'cc': 1.362058, 'c': 0.970860, 'l': 0.873453}
#flav_map[4]['el']["MUON_ID__1down"] = {'bb': 1.322941, 'cc': 1.322941, 'c': 0.942979, 'l': 0.848369}
#flav_map[5]['el']["MUON_ID__1down"] = {'bb': 1.281418, 'cc': 1.281418, 'c': 0.913381, 'l': 0.821741}
#flav_map[2]['mu']["MUON_ID__1down"] = {'bb': 1.547541, 'cc': 1.547541, 'c': 1.000000, 'l': 0.877100}
#flav_map[3]['mu']["MUON_ID__1down"] = {'bb': 1.489145, 'cc': 1.489145, 'c': 0.962265, 'l': 0.844003}
#flav_map[4]['mu']["MUON_ID__1down"] = {'bb': 1.436272, 'cc': 1.436272, 'c': 0.928099, 'l': 0.814036}
#flav_map[5]['mu']["MUON_ID__1down"] = {'bb': 1.371919, 'cc': 1.371919, 'c': 0.886516, 'l': 0.777563}
## MUON_MS__1up 
#flav_map[2]['el']["MUON_MS__1up"] = {'bb': 1.403419, 'cc': 1.403419, 'c': 1.000000, 'l': 0.899549}
#flav_map[3]['el']["MUON_MS__1up"] = {'bb': 1.362477, 'cc': 1.362477, 'c': 0.970827, 'l': 0.873307}
#flav_map[4]['el']["MUON_MS__1up"] = {'bb': 1.323305, 'cc': 1.323305, 'c': 0.942915, 'l': 0.848198}
#flav_map[5]['el']["MUON_MS__1up"] = {'bb': 1.281724, 'cc': 1.281724, 'c': 0.913287, 'l': 0.821547}
#flav_map[2]['mu']["MUON_MS__1up"] = {'bb': 1.565065, 'cc': 1.565065, 'c': 1.000000, 'l': 0.873209}
#flav_map[3]['mu']["MUON_MS__1up"] = {'bb': 1.504150, 'cc': 1.504150, 'c': 0.961078, 'l': 0.839223}
#flav_map[4]['mu']["MUON_MS__1up"] = {'bb': 1.449149, 'cc': 1.449149, 'c': 0.925935, 'l': 0.808535}
#flav_map[5]['mu']["MUON_MS__1up"] = {'bb': 1.382365, 'cc': 1.382365, 'c': 0.883264, 'l': 0.771274}
## MUON_MS__1down 
#flav_map[2]['el']["MUON_MS__1down"] = {'bb': 1.402946, 'cc': 1.402946, 'c': 1.000000, 'l': 0.899667}
#flav_map[3]['el']["MUON_MS__1down"] = {'bb': 1.362064, 'cc': 1.362064, 'c': 0.970860, 'l': 0.873451}
#flav_map[4]['el']["MUON_MS__1down"] = {'bb': 1.322947, 'cc': 1.322947, 'c': 0.942978, 'l': 0.848366}
#flav_map[5]['el']["MUON_MS__1down"] = {'bb': 1.281423, 'cc': 1.281423, 'c': 0.913380, 'l': 0.821738}
#flav_map[2]['mu']["MUON_MS__1down"] = {'bb': 1.529224, 'cc': 1.529224, 'c': 1.000000, 'l': 0.881195}
#flav_map[3]['mu']["MUON_MS__1down"] = {'bb': 1.473382, 'cc': 1.473382, 'c': 0.963484, 'l': 0.849017}
#flav_map[4]['mu']["MUON_MS__1down"] = {'bb': 1.422739, 'cc': 1.422739, 'c': 0.930366, 'l': 0.819834}
#flav_map[5]['mu']["MUON_MS__1down"] = {'bb': 1.360835, 'cc': 1.360835, 'c': 0.889885, 'l': 0.784163}
## MUON_SCALE__1up 
#flav_map[2]['el']["MUON_SCALE__1up"] = {'bb': 1.403391, 'cc': 1.403391, 'c': 1.000000, 'l': 0.899557}
#flav_map[3]['el']["MUON_SCALE__1up"] = {'bb': 1.362452, 'cc': 1.362452, 'c': 0.970829, 'l': 0.873315}
#flav_map[4]['el']["MUON_SCALE__1up"] = {'bb': 1.323283, 'cc': 1.323283, 'c': 0.942918, 'l': 0.848208}
#flav_map[5]['el']["MUON_SCALE__1up"] = {'bb': 1.281706, 'cc': 1.281706, 'c': 0.913292, 'l': 0.821558}
#flav_map[2]['mu']["MUON_SCALE__1up"] = {'bb': 1.558597, 'cc': 1.558597, 'c': 1.000000, 'l': 0.874613}
#flav_map[3]['mu']["MUON_SCALE__1up"] = {'bb': 1.498533, 'cc': 1.498533, 'c': 0.961463, 'l': 0.840908}
#flav_map[4]['mu']["MUON_SCALE__1up"] = {'bb': 1.444356, 'cc': 1.444356, 'c': 0.926703, 'l': 0.810507}
#flav_map[5]['mu']["MUON_SCALE__1up"] = {'bb': 1.378492, 'cc': 1.378492, 'c': 0.884444, 'l': 0.773547}
## MUON_SCALE__1down 
#flav_map[2]['el']["MUON_SCALE__1down"] = {'bb': 1.403406, 'cc': 1.403406, 'c': 1.000000, 'l': 0.899553}
#flav_map[3]['el']["MUON_SCALE__1down"] = {'bb': 1.362465, 'cc': 1.362465, 'c': 0.970828, 'l': 0.873311}
#flav_map[4]['el']["MUON_SCALE__1down"] = {'bb': 1.323295, 'cc': 1.323295, 'c': 0.942916, 'l': 0.848203}
#flav_map[5]['el']["MUON_SCALE__1down"] = {'bb': 1.281716, 'cc': 1.281716, 'c': 0.913289, 'l': 0.821552}
#flav_map[2]['mu']["MUON_SCALE__1down"] = {'bb': 1.555768, 'cc': 1.555768, 'c': 1.000000, 'l': 0.875267}
#flav_map[3]['mu']["MUON_SCALE__1down"] = {'bb': 1.496176, 'cc': 1.496176, 'c': 0.961696, 'l': 0.841740}
#flav_map[4]['mu']["MUON_SCALE__1down"] = {'bb': 1.442316, 'cc': 1.442316, 'c': 0.927076, 'l': 0.811439}
#flav_map[5]['mu']["MUON_SCALE__1down"] = {'bb': 1.376773, 'cc': 1.376773, 'c': 0.884947, 'l': 0.774565}
## MUON_SAGITTA_RESBIAS__1up 
#flav_map[2]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## MUON_SAGITTA_RESBIAS__1down 
#flav_map[2]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## MUON_SAGITTA_RHO__1up 
#flav_map[2]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## MUON_SAGITTA_RHO__1down 
#flav_map[2]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## JET_JER_SINGLE_NP__1up 
#flav_map[2]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.415827, 'cc': 1.415827, 'c': 1.000000, 'l': 0.898358}
#flav_map[3]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.372974, 'cc': 1.372974, 'c': 0.969733, 'l': 0.871168}
#flav_map[4]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.335182, 'cc': 1.335182, 'c': 0.943040, 'l': 0.847188}
#flav_map[5]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.289254, 'cc': 1.289254, 'c': 0.910602, 'l': 0.818047}
#flav_map[2]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.657373, 'cc': 1.657373, 'c': 1.000000, 'l': 0.854466}
#flav_map[3]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.583013, 'cc': 1.583013, 'c': 0.955133, 'l': 0.816129}
#flav_map[4]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.516440, 'cc': 1.516440, 'c': 0.914966, 'l': 0.781807}
#flav_map[5]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 1.438651, 'cc': 1.438651, 'c': 0.868031, 'l': 0.741703}
## JET_21NP_JET_EtaIntercalibration_Modelling__1up 
#flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.441978, 'cc': 1.441978, 'c': 1.000000, 'l': 0.890744}
#flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.396002, 'cc': 1.396002, 'c': 0.968116, 'l': 0.862343}
#flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.352763, 'cc': 1.352763, 'c': 0.938130, 'l': 0.835633}
#flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.306446, 'cc': 1.306446, 'c': 0.906009, 'l': 0.807022}
#flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.596699, 'cc': 1.596699, 'c': 1.000000, 'l': 0.866825}
#flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.531487, 'cc': 1.531487, 'c': 0.959158, 'l': 0.831422}
#flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.473627, 'cc': 1.473627, 'c': 0.922921, 'l': 0.800011}
#flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 1.401361, 'cc': 1.401361, 'c': 0.877661, 'l': 0.760779}
## JET_21NP_JET_EtaIntercalibration_Modelling__1down 
#flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.320135, 'cc': 1.320135, 'c': 1.000000, 'l': 0.919841}
#flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.289015, 'cc': 1.289015, 'c': 0.976427, 'l': 0.898157}
#flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.259759, 'cc': 1.259759, 'c': 0.954265, 'l': 0.877772}
#flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.227234, 'cc': 1.227234, 'c': 0.929628, 'l': 0.855109}
#flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.524643, 'cc': 1.524643, 'c': 1.000000, 'l': 0.881638}
#flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.468756, 'cc': 1.468756, 'c': 0.963344, 'l': 0.849321}
#flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.419390, 'cc': 1.419390, 'c': 0.930965, 'l': 0.820774}
#flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 1.357367, 'cc': 1.357367, 'c': 0.890285, 'l': 0.784909}
## JET_21NP_JET_EtaIntercalibration_NonClosure__1up 
#flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.432083, 'cc': 1.432083, 'c': 1.000000, 'l': 0.892423}
#flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.387206, 'cc': 1.387206, 'c': 0.968663, 'l': 0.864457}
#flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.344706, 'cc': 1.344706, 'c': 0.938986, 'l': 0.837973}
#flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.299630, 'cc': 1.299630, 'c': 0.907510, 'l': 0.809883}
#flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.603108, 'cc': 1.603108, 'c': 1.000000, 'l': 0.864645}
#flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.536456, 'cc': 1.536456, 'c': 0.958423, 'l': 0.828695}
#flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.476438, 'cc': 1.476438, 'c': 0.920985, 'l': 0.796324}
#flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 1.404926, 'cc': 1.404926, 'c': 0.876376, 'l': 0.757754}
## JET_21NP_JET_EtaIntercalibration_NonClosure__1down 
#flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.355537, 'cc': 1.355537, 'c': 1.000000, 'l': 0.911644}
#flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.320565, 'cc': 1.320565, 'c': 0.974200, 'l': 0.888124}
#flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.286934, 'cc': 1.286934, 'c': 0.949391, 'l': 0.865506}
#flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.250439, 'cc': 1.250439, 'c': 0.922467, 'l': 0.840962}
#flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.563021, 'cc': 1.563021, 'c': 1.000000, 'l': 0.873818}
#flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.502541, 'cc': 1.502541, 'c': 0.961306, 'l': 0.840006}
#flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.447788, 'cc': 1.447788, 'c': 0.926275, 'l': 0.809396}
#flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 1.380977, 'cc': 1.380977, 'c': 0.883531, 'l': 0.772045}
## JET_21NP_JET_EtaIntercalibration_TotalStat__1up 
#flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.399048, 'cc': 1.399048, 'c': 1.000000, 'l': 0.900990}
#flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.358679, 'cc': 1.358679, 'c': 0.971145, 'l': 0.874993}
#flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.319883, 'cc': 1.319883, 'c': 0.943415, 'l': 0.850008}
#flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.279037, 'cc': 1.279037, 'c': 0.914219, 'l': 0.823703}
#flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.583333, 'cc': 1.583333, 'c': 1.000000, 'l': 0.869346}
#flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.520042, 'cc': 1.520042, 'c': 0.960027, 'l': 0.834595}
#flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.462712, 'cc': 1.462712, 'c': 0.923818, 'l': 0.803118}
#flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 1.393243, 'cc': 1.393243, 'c': 0.879943, 'l': 0.764975}
## JET_21NP_JET_EtaIntercalibration_TotalStat__1down 
#flav_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.368370, 'cc': 1.368370, 'c': 1.000000, 'l': 0.908042}
#flav_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.331779, 'cc': 1.331779, 'c': 0.973260, 'l': 0.883761}
#flav_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.296523, 'cc': 1.296523, 'c': 0.947494, 'l': 0.860365}
#flav_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.258647, 'cc': 1.258647, 'c': 0.919815, 'l': 0.835231}
#flav_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.551743, 'cc': 1.551743, 'c': 1.000000, 'l': 0.875751}
#flav_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.492623, 'cc': 1.492623, 'c': 0.961902, 'l': 0.842386}
#flav_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.438834, 'cc': 1.438834, 'c': 0.927237, 'l': 0.812029}
#flav_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 1.374343, 'cc': 1.374343, 'c': 0.885678, 'l': 0.775633}
## JET_21NP_JET_Flavor_Composition__1up 
#flav_map[2]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.695919, 'cc': 1.695919, 'c': 1.000000, 'l': 0.833367}
#flav_map[3]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.614422, 'cc': 1.614422, 'c': 0.951945, 'l': 0.793320}
#flav_map[4]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.540871, 'cc': 1.540871, 'c': 0.908576, 'l': 0.757177}
#flav_map[5]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.461449, 'cc': 1.461449, 'c': 0.861745, 'l': 0.718149}
#flav_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.762402, 'cc': 1.762402, 'c': 1.000000, 'l': 0.835118}
#flav_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.673322, 'cc': 1.673322, 'c': 0.949456, 'l': 0.792908}
#flav_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.596650, 'cc': 1.596650, 'c': 0.905951, 'l': 0.756577}
#flav_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 1.501278, 'cc': 1.501278, 'c': 0.851836, 'l': 0.711384}
## JET_21NP_JET_Flavor_Composition__1down 
#flav_map[2]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.102560, 'cc': 1.102560, 'c': 1.000000, 'l': 0.973451}
#flav_map[3]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.093726, 'cc': 1.093726, 'c': 0.991988, 'l': 0.965651}
#flav_map[4]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.085754, 'cc': 1.085754, 'c': 0.984757, 'l': 0.958613}
#flav_map[5]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.075799, 'cc': 1.075799, 'c': 0.975728, 'l': 0.949823}
#flav_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.404821, 'cc': 1.404821, 'c': 1.000000, 'l': 0.905746}
#flav_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.363261, 'cc': 1.363261, 'c': 0.970416, 'l': 0.878950}
#flav_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.325996, 'cc': 1.325996, 'c': 0.943889, 'l': 0.854924}
#flav_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 1.279534, 'cc': 1.279534, 'c': 0.910816, 'l': 0.824968}
## JET_21NP_JET_Flavor_Response__1up 
#flav_map[2]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.273182, 'cc': 1.273182, 'c': 1.000000, 'l': 0.931230}
#flav_map[3]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.247550, 'cc': 1.247550, 'c': 0.979868, 'l': 0.912482}
#flav_map[4]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.222740, 'cc': 1.222740, 'c': 0.960381, 'l': 0.894336}
#flav_map[5]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.195524, 'cc': 1.195524, 'c': 0.939005, 'l': 0.874430}
#flav_map[2]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.515404, 'cc': 1.515404, 'c': 1.000000, 'l': 0.883171}
#flav_map[3]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.460429, 'cc': 1.460429, 'c': 0.963723, 'l': 0.851131}
#flav_map[4]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.412289, 'cc': 1.412289, 'c': 0.931956, 'l': 0.823076}
#flav_map[5]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 1.350492, 'cc': 1.350492, 'c': 0.891177, 'l': 0.787061}
## JET_21NP_JET_Flavor_Response__1down 
#flav_map[2]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.448013, 'cc': 1.448013, 'c': 1.000000, 'l': 0.890032}
#flav_map[3]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.401288, 'cc': 1.401288, 'c': 0.967731, 'l': 0.861312}
#flav_map[4]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.357261, 'cc': 1.357261, 'c': 0.937326, 'l': 0.834251}
#flav_map[5]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.310747, 'cc': 1.310747, 'c': 0.905204, 'l': 0.805661}
#flav_map[2]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.626614, 'cc': 1.626614, 'c': 1.000000, 'l': 0.860502}
#flav_map[3]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.558000, 'cc': 1.558000, 'c': 0.957818, 'l': 0.824204}
#flav_map[4]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.496043, 'cc': 1.496043, 'c': 0.919728, 'l': 0.791428}
#flav_map[5]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 1.420169, 'cc': 1.420169, 'c': 0.873083, 'l': 0.751290}
## JET_21NP_JET_Pileup_OffsetMu__1up 
#flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.354462, 'cc': 1.354462, 'c': 1.000000, 'l': 0.911661}
#flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.319514, 'cc': 1.319514, 'c': 0.974198, 'l': 0.888138}
#flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.285974, 'cc': 1.285974, 'c': 0.949436, 'l': 0.865563}
#flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.250200, 'cc': 1.250200, 'c': 0.923024, 'l': 0.841484}
#flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.565636, 'cc': 1.565636, 'c': 1.000000, 'l': 0.872963}
#flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.504663, 'cc': 1.504663, 'c': 0.961056, 'l': 0.838966}
#flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.449748, 'cc': 1.449748, 'c': 0.925980, 'l': 0.808346}
#flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 1.382435, 'cc': 1.382435, 'c': 0.882986, 'l': 0.770814}
## JET_21NP_JET_Pileup_OffsetMu__1down 
#flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.393442, 'cc': 1.393442, 'c': 1.000000, 'l': 0.902153}
#flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.353809, 'cc': 1.353809, 'c': 0.971558, 'l': 0.876493}
#flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.315904, 'cc': 1.315904, 'c': 0.944355, 'l': 0.851952}
#flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.274975, 'cc': 1.274975, 'c': 0.914982, 'l': 0.825453}
#flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.569139, 'cc': 1.569139, 'c': 1.000000, 'l': 0.872185}
#flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.507743, 'cc': 1.507743, 'c': 0.960873, 'l': 0.838060}
#flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.451956, 'cc': 1.451956, 'c': 0.925320, 'l': 0.807051}
#flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 1.384832, 'cc': 1.384832, 'c': 0.882543, 'l': 0.769741}
## JET_21NP_JET_Pileup_OffsetNPV__1up 
#flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.407171, 'cc': 1.407171, 'c': 1.000000, 'l': 0.899295}
#flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.365689, 'cc': 1.365689, 'c': 0.970521, 'l': 0.872785}
#flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.325888, 'cc': 1.325888, 'c': 0.942236, 'l': 0.847349}
#flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.284885, 'cc': 1.284885, 'c': 0.913098, 'l': 0.821145}
#flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.688293, 'cc': 1.688293, 'c': 1.000000, 'l': 0.845917}
#flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.609897, 'cc': 1.609897, 'c': 0.953564, 'l': 0.806636}
#flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.540235, 'cc': 1.540235, 'c': 0.912303, 'l': 0.771733}
#flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 1.456598, 'cc': 1.456598, 'c': 0.862764, 'l': 0.729826}
## JET_21NP_JET_Pileup_OffsetNPV__1down 
#flav_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.347332, 'cc': 1.347332, 'c': 1.000000, 'l': 0.913066}
#flav_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.313511, 'cc': 1.313511, 'c': 0.974898, 'l': 0.890146}
#flav_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.280518, 'cc': 1.280518, 'c': 0.950410, 'l': 0.867787}
#flav_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.245081, 'cc': 1.245081, 'c': 0.924108, 'l': 0.843772}
#flav_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.543228, 'cc': 1.543228, 'c': 1.000000, 'l': 0.877507}
#flav_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.484879, 'cc': 1.484879, 'c': 0.962191, 'l': 0.844329}
#flav_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.432449, 'cc': 1.432449, 'c': 0.928216, 'l': 0.814516}
#flav_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 1.368043, 'cc': 1.368043, 'c': 0.886482, 'l': 0.777894}
## JET_21NP_JET_Pileup_PtTerm__1up 
#flav_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.384531, 'cc': 1.384531, 'c': 1.000000, 'l': 0.904297}
#flav_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.345972, 'cc': 1.345972, 'c': 0.972150, 'l': 0.879113}
#flav_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.309023, 'cc': 1.309023, 'c': 0.945463, 'l': 0.854980}
#flav_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.269430, 'cc': 1.269430, 'c': 0.916866, 'l': 0.829120}
#flav_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.548265, 'cc': 1.548265, 'c': 1.000000, 'l': 0.876979}
#flav_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.489776, 'cc': 1.489776, 'c': 0.962223, 'l': 0.843849}
#flav_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.436767, 'cc': 1.436767, 'c': 0.927985, 'l': 0.813823}
#flav_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 1.372266, 'cc': 1.372266, 'c': 0.886325, 'l': 0.777288}
## JET_21NP_JET_Pileup_PtTerm__1down 
#flav_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.394846, 'cc': 1.394846, 'c': 1.000000, 'l': 0.901587}
#flav_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.355084, 'cc': 1.355084, 'c': 0.971494, 'l': 0.875887}
#flav_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.316958, 'cc': 1.316958, 'c': 0.944160, 'l': 0.851243}
#flav_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.276216, 'cc': 1.276216, 'c': 0.914951, 'l': 0.824909}
#flav_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.564161, 'cc': 1.564161, 'c': 1.000000, 'l': 0.873315}
#flav_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.503382, 'cc': 1.503382, 'c': 0.961143, 'l': 0.839381}
#flav_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.448492, 'cc': 1.448492, 'c': 0.926051, 'l': 0.808734}
#flav_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 1.381742, 'cc': 1.381742, 'c': 0.883375, 'l': 0.771465}
## JET_21NP_JET_Pileup_RhoTopology__1up 
#flav_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.598503, 'cc': 1.598503, 'c': 1.000000, 'l': 0.854749}
#flav_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.530750, 'cc': 1.530750, 'c': 0.957615, 'l': 0.818521}
#flav_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.468895, 'cc': 1.468895, 'c': 0.918919, 'l': 0.785445}
#flav_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.402779, 'cc': 1.402779, 'c': 0.877558, 'l': 0.750092}
#flav_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.693815, 'cc': 1.693815, 'c': 1.000000, 'l': 0.847381}
#flav_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.615585, 'cc': 1.615585, 'c': 0.953814, 'l': 0.808244}
#flav_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.545003, 'cc': 1.545003, 'c': 0.912144, 'l': 0.772933}
#flav_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 1.460458, 'cc': 1.460458, 'c': 0.862230, 'l': 0.730638}
## JET_21NP_JET_Pileup_RhoTopology__1down 
#flav_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.169643, 'cc': 1.169643, 'c': 1.000000, 'l': 0.956930}
#flav_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.154686, 'cc': 1.154686, 'c': 0.987212, 'l': 0.944693}
#flav_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.140327, 'cc': 1.140327, 'c': 0.974935, 'l': 0.932945}
#flav_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.124207, 'cc': 1.124207, 'c': 0.961154, 'l': 0.919757}
#flav_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.430956, 'cc': 1.430956, 'c': 1.000000, 'l': 0.901338}
#flav_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.386898, 'cc': 1.386898, 'c': 0.969211, 'l': 0.873587}
#flav_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.347599, 'cc': 1.347599, 'c': 0.941747, 'l': 0.848832}
#flav_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 1.297907, 'cc': 1.297907, 'c': 0.907021, 'l': 0.817532}
## JET_21NP_JET_PunchThrough_MC15__1up 
#flav_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.403158, 'cc': 1.403158, 'c': 1.000000, 'l': 0.899613}
#flav_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.362259, 'cc': 1.362259, 'c': 0.970852, 'l': 0.873391}
#flav_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.323108, 'cc': 1.323108, 'c': 0.942950, 'l': 0.848290}
#flav_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.281561, 'cc': 1.281561, 'c': 0.913340, 'l': 0.821653}
#flav_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.554680, 'cc': 1.554680, 'c': 1.000000, 'l': 0.875489}
#flav_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.495217, 'cc': 1.495217, 'c': 0.961752, 'l': 0.842003}
#flav_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.441514, 'cc': 1.441514, 'c': 0.927210, 'l': 0.811761}
#flav_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 1.376114, 'cc': 1.376114, 'c': 0.885143, 'l': 0.774932}
## JET_21NP_JET_PunchThrough_MC15__1down 
#flav_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.404150, 'cc': 1.404150, 'c': 1.000000, 'l': 0.899370}
#flav_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.363114, 'cc': 1.363114, 'c': 0.970775, 'l': 0.873086}
#flav_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.323855, 'cc': 1.323855, 'c': 0.942816, 'l': 0.847940}
#flav_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.282187, 'cc': 1.282187, 'c': 0.913141, 'l': 0.821252}
#flav_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.554578, 'cc': 1.554578, 'c': 1.000000, 'l': 0.875510}
#flav_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.495134, 'cc': 1.495134, 'c': 0.961762, 'l': 0.842033}
#flav_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.441440, 'cc': 1.441440, 'c': 0.927223, 'l': 0.811794}
#flav_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 1.376054, 'cc': 1.376054, 'c': 0.885162, 'l': 0.774969}
## JET_21NP_JET_SingleParticle_HighPt__1up 
#flav_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.403452, 'cc': 1.403452, 'c': 1.000000, 'l': 0.899541}
#flav_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.362505, 'cc': 1.362505, 'c': 0.970824, 'l': 0.873297}
#flav_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.323329, 'cc': 1.323329, 'c': 0.942910, 'l': 0.848187}
#flav_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.281745, 'cc': 1.281745, 'c': 0.913280, 'l': 0.821534}
#flav_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 1.376112, 'cc': 1.376112, 'c': 0.885148, 'l': 0.774939}
## JET_21NP_JET_SingleParticle_HighPt__1down 
#flav_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.362504, 'cc': 1.362504, 'c': 0.970825, 'l': 0.873297}
#flav_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.323328, 'cc': 1.323328, 'c': 0.942911, 'l': 0.848187}
#flav_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821534}
#flav_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 1.376112, 'cc': 1.376112, 'c': 0.885148, 'l': 0.774939}
## JET_21NP_JET_BJES_Response__1up 
#flav_map[2]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.402147, 'cc': 1.402147, 'c': 1.000000, 'l': 0.899689}
#flav_map[3]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.361249, 'cc': 1.361249, 'c': 0.970832, 'l': 0.873446}
#flav_map[4]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.322187, 'cc': 1.322187, 'c': 0.942973, 'l': 0.848382}
#flav_map[5]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.280721, 'cc': 1.280721, 'c': 0.913400, 'l': 0.821776}
#flav_map[2]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.555690, 'cc': 1.555690, 'c': 1.000000, 'l': 0.875069}
#flav_map[3]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.495942, 'cc': 1.495942, 'c': 0.961594, 'l': 0.841461}
#flav_map[4]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.441995, 'cc': 1.441995, 'c': 0.926917, 'l': 0.811116}
#flav_map[5]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 1.376416, 'cc': 1.376416, 'c': 0.884762, 'l': 0.774228}
## JET_21NP_JET_BJES_Response__1down 
#flav_map[2]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.404293, 'cc': 1.404293, 'c': 1.000000, 'l': 0.899491}
#flav_map[3]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.363365, 'cc': 1.363365, 'c': 0.970855, 'l': 0.873276}
#flav_map[4]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.324189, 'cc': 1.324189, 'c': 0.942958, 'l': 0.848182}
#flav_map[5]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.282537, 'cc': 1.282537, 'c': 0.913297, 'l': 0.821503}
#flav_map[2]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.556061, 'cc': 1.556061, 'c': 1.000000, 'l': 0.875373}
#flav_map[3]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.496548, 'cc': 1.496548, 'c': 0.961755, 'l': 0.841894}
#flav_map[4]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.442772, 'cc': 1.442772, 'c': 0.927195, 'l': 0.811642}
#flav_map[5]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 1.377266, 'cc': 1.377266, 'c': 0.885098, 'l': 0.774791}
## JET_21NP_JET_EffectiveNP_1__1up 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.546568, 'cc': 1.546568, 'c': 1.000000, 'l': 0.866529}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.485950, 'cc': 1.485950, 'c': 0.960805, 'l': 0.832565}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.430100, 'cc': 1.430100, 'c': 0.924693, 'l': 0.801273}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.370784, 'cc': 1.370784, 'c': 0.886339, 'l': 0.768039}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.674701, 'cc': 1.674701, 'c': 1.000000, 'l': 0.850476}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.598916, 'cc': 1.598916, 'c': 0.954747, 'l': 0.811990}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.531666, 'cc': 1.531666, 'c': 0.914591, 'l': 0.777837}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 1.448442, 'cc': 1.448442, 'c': 0.864896, 'l': 0.735573}
## JET_21NP_JET_EffectiveNP_1__1down 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.232023, 'cc': 1.232023, 'c': 1.000000, 'l': 0.941422}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.210666, 'cc': 1.210666, 'c': 0.982665, 'l': 0.925103}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.190357, 'cc': 1.190357, 'c': 0.966181, 'l': 0.909584}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.167506, 'cc': 1.167506, 'c': 0.947633, 'l': 0.892122}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.516193, 'cc': 1.516193, 'c': 1.000000, 'l': 0.882492}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.461195, 'cc': 1.461195, 'c': 0.963726, 'l': 0.850481}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.412282, 'cc': 1.412282, 'c': 0.931466, 'l': 0.822011}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 1.351107, 'cc': 1.351107, 'c': 0.891118, 'l': 0.786404}
## JET_21NP_JET_EffectiveNP_2__1up 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.352629, 'cc': 1.352629, 'c': 1.000000, 'l': 0.911955}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.317964, 'cc': 1.317964, 'c': 0.974372, 'l': 0.888584}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.284402, 'cc': 1.284402, 'c': 0.949560, 'l': 0.865956}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.248641, 'cc': 1.248641, 'c': 0.923122, 'l': 0.841846}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.549993, 'cc': 1.549993, 'c': 1.000000, 'l': 0.876059}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.491035, 'cc': 1.491035, 'c': 0.961963, 'l': 0.842736}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.437796, 'cc': 1.437796, 'c': 0.927615, 'l': 0.812645}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 1.373002, 'cc': 1.373002, 'c': 0.885812, 'l': 0.776024}
## JET_21NP_JET_EffectiveNP_2__1down 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.416307, 'cc': 1.416307, 'c': 1.000000, 'l': 0.896788}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.373673, 'cc': 1.373673, 'c': 0.969897, 'l': 0.869792}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.332999, 'cc': 1.332999, 'c': 0.941179, 'l': 0.844038}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.289884, 'cc': 1.289884, 'c': 0.910737, 'l': 0.816738}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.578706, 'cc': 1.578706, 'c': 1.000000, 'l': 0.870456}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.516290, 'cc': 1.516290, 'c': 0.960464, 'l': 0.836042}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.459407, 'cc': 1.459407, 'c': 0.924433, 'l': 0.804678}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 1.390567, 'cc': 1.390567, 'c': 0.880827, 'l': 0.766721}
## JET_21NP_JET_EffectiveNP_3__1up 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.414686, 'cc': 1.414686, 'c': 1.000000, 'l': 0.896798}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.372283, 'cc': 1.372283, 'c': 0.970026, 'l': 0.869918}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.331843, 'cc': 1.331843, 'c': 0.941441, 'l': 0.844282}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.288653, 'cc': 1.288653, 'c': 0.910911, 'l': 0.816903}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.562650, 'cc': 1.562650, 'c': 1.000000, 'l': 0.873805}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.502130, 'cc': 1.502130, 'c': 0.961271, 'l': 0.839964}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.447206, 'cc': 1.447206, 'c': 0.926123, 'l': 0.809251}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 1.380886, 'cc': 1.380886, 'c': 0.883682, 'l': 0.772166}
## JET_21NP_JET_EffectiveNP_3__1down 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.387112, 'cc': 1.387112, 'c': 1.000000, 'l': 0.903610}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.348175, 'cc': 1.348175, 'c': 0.971930, 'l': 0.878245}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.310828, 'cc': 1.310828, 'c': 0.945006, 'l': 0.853916}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.271314, 'cc': 1.271314, 'c': 0.916519, 'l': 0.828175}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.550914, 'cc': 1.550914, 'c': 1.000000, 'l': 0.876240}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.491945, 'cc': 1.491945, 'c': 0.961978, 'l': 0.842924}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.438604, 'cc': 1.438604, 'c': 0.927585, 'l': 0.812787}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 1.373804, 'cc': 1.373804, 'c': 0.885803, 'l': 0.776176}
## JET_21NP_JET_EffectiveNP_4__1up 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.380632, 'cc': 1.380632, 'c': 1.000000, 'l': 0.905208}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.342581, 'cc': 1.342581, 'c': 0.972439, 'l': 0.880260}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.305986, 'cc': 1.305986, 'c': 0.945933, 'l': 0.856266}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.267113, 'cc': 1.267113, 'c': 0.917777, 'l': 0.830779}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.551259, 'cc': 1.551259, 'c': 1.000000, 'l': 0.876163}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.492310, 'cc': 1.492310, 'c': 0.961999, 'l': 0.842869}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.438964, 'cc': 1.438964, 'c': 0.927611, 'l': 0.812738}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 1.374115, 'cc': 1.374115, 'c': 0.885807, 'l': 0.776111}
## JET_21NP_JET_EffectiveNP_4__1down 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.406710, 'cc': 1.406710, 'c': 1.000000, 'l': 0.898749}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.365363, 'cc': 1.365363, 'c': 0.970607, 'l': 0.872332}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.325791, 'cc': 1.325791, 'c': 0.942477, 'l': 0.847050}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.283630, 'cc': 1.283630, 'c': 0.912505, 'l': 0.820113}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.560713, 'cc': 1.560713, 'c': 1.000000, 'l': 0.874184}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.500447, 'cc': 1.500447, 'c': 0.961386, 'l': 0.840428}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.445797, 'cc': 1.445797, 'c': 0.926370, 'l': 0.809818}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 1.379695, 'cc': 1.379695, 'c': 0.884016, 'l': 0.772792}
## JET_21NP_JET_EffectiveNP_5__1up 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.404257, 'cc': 1.404257, 'c': 1.000000, 'l': 0.899318}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.363200, 'cc': 1.363200, 'c': 0.970763, 'l': 0.873024}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.323976, 'cc': 1.323976, 'c': 0.942830, 'l': 0.847904}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.282109, 'cc': 1.282109, 'c': 0.913016, 'l': 0.821091}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.556298, 'cc': 1.556298, 'c': 1.000000, 'l': 0.875109}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.496595, 'cc': 1.496595, 'c': 0.961638, 'l': 0.841537}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.442710, 'cc': 1.442710, 'c': 0.927014, 'l': 0.811238}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 1.377094, 'cc': 1.377094, 'c': 0.884852, 'l': 0.774342}
## JET_21NP_JET_EffectiveNP_5__1down 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.393595, 'cc': 1.393595, 'c': 1.000000, 'l': 0.902022}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.353956, 'cc': 1.353956, 'c': 0.971556, 'l': 0.876365}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.315739, 'cc': 1.315739, 'c': 0.944133, 'l': 0.851629}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.275489, 'cc': 1.275489, 'c': 0.915251, 'l': 0.825576}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.559873, 'cc': 1.559873, 'c': 1.000000, 'l': 0.874312}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.499783, 'cc': 1.499783, 'c': 0.961478, 'l': 0.840631}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.445224, 'cc': 1.445224, 'c': 0.926501, 'l': 0.810051}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 1.379310, 'cc': 1.379310, 'c': 0.884245, 'l': 0.773106}
## JET_21NP_JET_EffectiveNP_6__1up 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.397738, 'cc': 1.397738, 'c': 1.000000, 'l': 0.901054}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.357542, 'cc': 1.357542, 'c': 0.971243, 'l': 0.875142}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.318897, 'cc': 1.318897, 'c': 0.943594, 'l': 0.850229}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.278090, 'cc': 1.278090, 'c': 0.914399, 'l': 0.823923}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.563629, 'cc': 1.563629, 'c': 1.000000, 'l': 0.873592}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.502924, 'cc': 1.502924, 'c': 0.961177, 'l': 0.839677}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.448137, 'cc': 1.448137, 'c': 0.926139, 'l': 0.809068}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 1.381443, 'cc': 1.381443, 'c': 0.883485, 'l': 0.771806}
## JET_21NP_JET_EffectiveNP_6__1down 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.393414, 'cc': 1.393414, 'c': 1.000000, 'l': 0.902031}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.353644, 'cc': 1.353644, 'c': 0.971459, 'l': 0.876286}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.315616, 'cc': 1.315616, 'c': 0.944167, 'l': 0.851668}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.275312, 'cc': 1.275312, 'c': 0.915243, 'l': 0.825577}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.553352, 'cc': 1.553352, 'c': 1.000000, 'l': 0.875731}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.494013, 'cc': 1.494013, 'c': 0.961799, 'l': 0.842277}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.440292, 'cc': 1.440292, 'c': 0.927215, 'l': 0.811991}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 1.375318, 'cc': 1.375318, 'c': 0.885387, 'l': 0.775360}
## JET_21NP_JET_EffectiveNP_7__1up 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.391273, 'cc': 1.391273, 'c': 1.000000, 'l': 0.902553}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.351775, 'cc': 1.351775, 'c': 0.971609, 'l': 0.876929}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.314007, 'cc': 1.314007, 'c': 0.944464, 'l': 0.852428}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.273969, 'cc': 1.273969, 'c': 0.915686, 'l': 0.826455}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.554115, 'cc': 1.554115, 'c': 1.000000, 'l': 0.875505}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.494669, 'cc': 1.494669, 'c': 0.961749, 'l': 0.842016}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.440892, 'cc': 1.440892, 'c': 0.927146, 'l': 0.811721}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 1.375780, 'cc': 1.375780, 'c': 0.885250, 'l': 0.775040}
## JET_21NP_JET_EffectiveNP_7__1down 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.407078, 'cc': 1.407078, 'c': 1.000000, 'l': 0.898737}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.365725, 'cc': 1.365725, 'c': 0.970611, 'l': 0.872324}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.325993, 'cc': 1.325993, 'c': 0.942373, 'l': 0.846946}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.283991, 'cc': 1.283991, 'c': 0.912523, 'l': 0.820118}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.563571, 'cc': 1.563571, 'c': 1.000000, 'l': 0.873625}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.502982, 'cc': 1.502982, 'c': 0.961250, 'l': 0.839771}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.448140, 'cc': 1.448140, 'c': 0.926175, 'l': 0.809129}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 1.381369, 'cc': 1.381369, 'c': 0.883470, 'l': 0.771822}
## JET_21NP_JET_EffectiveNP_8restTerm__1up 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.400455, 'cc': 1.400455, 'c': 1.000000, 'l': 0.900309}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.359912, 'cc': 1.359912, 'c': 0.971050, 'l': 0.874245}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.320934, 'cc': 1.320934, 'c': 0.943218, 'l': 0.849187}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.279840, 'cc': 1.279840, 'c': 0.913874, 'l': 0.822769}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.566561, 'cc': 1.566561, 'c': 1.000000, 'l': 0.872832}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.505482, 'cc': 1.505482, 'c': 0.961011, 'l': 0.838801}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.450164, 'cc': 1.450164, 'c': 0.925699, 'l': 0.807980}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 1.383271, 'cc': 1.383271, 'c': 0.882999, 'l': 0.770710}
## JET_21NP_JET_EffectiveNP_8restTerm__1down 
#flav_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.398516, 'cc': 1.398516, 'c': 1.000000, 'l': 0.900758}
#flav_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.358159, 'cc': 1.358159, 'c': 0.971143, 'l': 0.874765}
#flav_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.319570, 'cc': 1.319570, 'c': 0.943550, 'l': 0.849911}
#flav_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.278692, 'cc': 1.278692, 'c': 0.914321, 'l': 0.823582}
#flav_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.553513, 'cc': 1.553513, 'c': 1.000000, 'l': 0.875703}
#flav_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.494210, 'cc': 1.494210, 'c': 0.961827, 'l': 0.842275}
#flav_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.440672, 'cc': 1.440672, 'c': 0.927364, 'l': 0.812096}
#flav_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 1.375406, 'cc': 1.375406, 'c': 0.885352, 'l': 0.775306}
## LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down 
#flav_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Comb_Baseline_Kin__1up 
#flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Comb_Baseline_Kin__1down 
#flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Comb_Modelling_Kin__1up 
#flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Comb_Modelling_Kin__1down 
#flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up 
#flav_map[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down 
#flav_map[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Comb_Tracking_Kin__1up 
#flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Comb_Tracking_Kin__1down 
#flav_map[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up 
#flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down 
#flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up 
#flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down 
#flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up 
#flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down 
#flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up 
#flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down 
#flav_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Strong_JET_Comb_Baseline_All__1up 
#flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Strong_JET_Comb_Baseline_All__1down 
#flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Strong_JET_Comb_Modelling_All__1up 
#flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Strong_JET_Comb_Modelling_All__1down 
#flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Strong_JET_Comb_TotalStat_All__1up 
#flav_map[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Strong_JET_Comb_TotalStat_All__1down 
#flav_map[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Strong_JET_Comb_Tracking_All__1up 
#flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
## LARGERJET_Strong_JET_Comb_Tracking_All__1down 
#flav_map[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.403450, 'cc': 1.403450, 'c': 1.000000, 'l': 0.899542}
#flav_map[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.362503, 'cc': 1.362503, 'c': 0.970824, 'l': 0.873298}
#flav_map[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.323327, 'cc': 1.323327, 'c': 0.942910, 'l': 0.848188}
#flav_map[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.281744, 'cc': 1.281744, 'c': 0.913281, 'l': 0.821535}
#flav_map[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.554668, 'cc': 1.554668, 'c': 1.000000, 'l': 0.875491}
#flav_map[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.495210, 'cc': 1.495210, 'c': 0.961755, 'l': 0.842008}
#flav_map[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.441507, 'cc': 1.441507, 'c': 0.927212, 'l': 0.811766}
#flav_map[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 1.376113, 'cc': 1.376113, 'c': 0.885149, 'l': 0.774940}
#
#
#
## fractions
#frac[2]['el'][""] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el'][""] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el'][""] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el'][""] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu'][""] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu'][""] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu'][""] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu'][""] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## ttxsecup 
#frac[2]['el']["ttxsecup"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["ttxsecup"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["ttxsecup"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["ttxsecup"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["ttxsecup"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["ttxsecup"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["ttxsecup"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["ttxsecup"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## ttxsecdw 
#frac[2]['el']["ttxsecdw"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["ttxsecdw"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["ttxsecdw"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["ttxsecdw"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["ttxsecdw"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["ttxsecdw"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["ttxsecdw"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["ttxsecdw"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## singletopup 
#frac[2]['el']["singletopup"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["singletopup"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["singletopup"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["singletopup"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["singletopup"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["singletopup"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["singletopup"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["singletopup"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## singletopdw 
#frac[2]['el']["singletopdw"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["singletopdw"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["singletopdw"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["singletopdw"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["singletopdw"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["singletopdw"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["singletopdw"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["singletopdw"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## wnorm__1up 
#frac[2]['el']["wnorm__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["wnorm__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["wnorm__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["wnorm__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["wnorm__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["wnorm__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["wnorm__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["wnorm__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## wnorm__1down 
#frac[2]['el']["wnorm__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["wnorm__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["wnorm__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["wnorm__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["wnorm__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["wnorm__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["wnorm__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["wnorm__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## MET_SoftTrk_ResoPara 
#frac[2]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.093845,'cc': 0.063846,'c': 0.208855,'l': 0.633454}
#frac[3]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.117044,'cc': 0.098130,'c': 0.219249,'l': 0.565578}
#frac[4]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.139597,'cc': 0.136977,'c': 0.215582,'l': 0.507844}
#frac[5]['el']["MET_SoftTrk_ResoPara"] = {'bb': 0.147188,'cc': 0.149250,'c': 0.210775,'l': 0.492787}
#frac[2]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.083016,'cc': 0.062556,'c': 0.204916,'l': 0.649512}
#frac[3]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.106004,'cc': 0.096522,'c': 0.215571,'l': 0.581903}
#frac[4]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.129079,'cc': 0.132162,'c': 0.207868,'l': 0.530890}
#frac[5]['mu']["MET_SoftTrk_ResoPara"] = {'bb': 0.138150,'cc': 0.144360,'c': 0.203793,'l': 0.513696}
## MET_SoftTrk_ResoPerp 
#frac[2]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.093806,'cc': 0.063687,'c': 0.208830,'l': 0.633677}
#frac[3]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.117097,'cc': 0.098127,'c': 0.219116,'l': 0.565661}
#frac[4]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.139608,'cc': 0.136933,'c': 0.215535,'l': 0.507924}
#frac[5]['el']["MET_SoftTrk_ResoPerp"] = {'bb': 0.147244,'cc': 0.149165,'c': 0.210776,'l': 0.492814}
#frac[2]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.083055,'cc': 0.062743,'c': 0.204707,'l': 0.649494}
#frac[3]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.106020,'cc': 0.096583,'c': 0.215540,'l': 0.581857}
#frac[4]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.129050,'cc': 0.132023,'c': 0.207569,'l': 0.531358}
#frac[5]['mu']["MET_SoftTrk_ResoPerp"] = {'bb': 0.138135,'cc': 0.144254,'c': 0.203725,'l': 0.513886}
## MET_SoftTrk_ScaleUp 
#frac[2]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.093852,'cc': 0.063815,'c': 0.208864,'l': 0.633468}
#frac[3]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.117072,'cc': 0.098087,'c': 0.219026,'l': 0.565814}
#frac[4]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.139634,'cc': 0.136901,'c': 0.215654,'l': 0.507810}
#frac[5]['el']["MET_SoftTrk_ScaleUp"] = {'bb': 0.147208,'cc': 0.149155,'c': 0.210830,'l': 0.492807}
#frac[2]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.083053,'cc': 0.062614,'c': 0.204869,'l': 0.649463}
#frac[3]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.106006,'cc': 0.096374,'c': 0.215599,'l': 0.582021}
#frac[4]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.129059,'cc': 0.131940,'c': 0.207573,'l': 0.531427}
#frac[5]['mu']["MET_SoftTrk_ScaleUp"] = {'bb': 0.138134,'cc': 0.144186,'c': 0.203564,'l': 0.514116}
## MET_SoftTrk_ScaleDown 
#frac[2]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.093911,'cc': 0.063737,'c': 0.208996,'l': 0.633356}
#frac[3]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.117118,'cc': 0.098218,'c': 0.219131,'l': 0.565533}
#frac[4]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.139632,'cc': 0.136950,'c': 0.215789,'l': 0.507629}
#frac[5]['el']["MET_SoftTrk_ScaleDown"] = {'bb': 0.147187,'cc': 0.149160,'c': 0.210992,'l': 0.492662}
#frac[2]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.083046,'cc': 0.062702,'c': 0.204943,'l': 0.649309}
#frac[3]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.105936,'cc': 0.096291,'c': 0.215385,'l': 0.582388}
#frac[4]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.128904,'cc': 0.131873,'c': 0.207913,'l': 0.531311}
#frac[5]['mu']["MET_SoftTrk_ScaleDown"] = {'bb': 0.138036,'cc': 0.144167,'c': 0.203954,'l': 0.513843}
## EG_RESOLUTION_ALL__1up 
#frac[2]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.093897,'cc': 0.063774,'c': 0.208830,'l': 0.633499}
#frac[3]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.117128,'cc': 0.098180,'c': 0.219056,'l': 0.565636}
#frac[4]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.139424,'cc': 0.137001,'c': 0.215572,'l': 0.508004}
#frac[5]['el']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.147074,'cc': 0.149181,'c': 0.210796,'l': 0.492948}
#frac[2]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582060}
#frac[4]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["EG_RESOLUTION_ALL__1up"] = {'bb': 0.138053,'cc': 0.144177,'c': 0.203654,'l': 0.514116}
## EG_RESOLUTION_ALL__1down 
#frac[2]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.093922,'cc': 0.063806,'c': 0.209077,'l': 0.633195}
#frac[3]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.117111,'cc': 0.098156,'c': 0.218930,'l': 0.565803}
#frac[4]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.139573,'cc': 0.136905,'c': 0.215785,'l': 0.507737}
#frac[5]['el']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.147161,'cc': 0.149166,'c': 0.210929,'l': 0.492744}
#frac[2]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.128954,'cc': 0.131890,'c': 0.207636,'l': 0.531521}
#frac[5]['mu']["EG_RESOLUTION_ALL__1down"] = {'bb': 0.138054,'cc': 0.144177,'c': 0.203653,'l': 0.514116}
## EG_SCALE_ALL__1up 
#frac[2]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.093880,'cc': 0.063731,'c': 0.208984,'l': 0.633405}
#frac[3]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.117180,'cc': 0.098198,'c': 0.219065,'l': 0.565558}
#frac[4]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.139455,'cc': 0.136924,'c': 0.215672,'l': 0.507950}
#frac[5]['el']["EG_SCALE_ALL__1up"] = {'bb': 0.147094,'cc': 0.149132,'c': 0.210887,'l': 0.492887}
#frac[2]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["EG_SCALE_ALL__1up"] = {'bb': 0.138053,'cc': 0.144177,'c': 0.203654,'l': 0.514116}
## EG_SCALE_ALL__1down 
#frac[2]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.093900,'cc': 0.063780,'c': 0.209046,'l': 0.633274}
#frac[3]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.117112,'cc': 0.098244,'c': 0.219148,'l': 0.565496}
#frac[4]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.139545,'cc': 0.136942,'c': 0.215741,'l': 0.507773}
#frac[5]['el']["EG_SCALE_ALL__1down"] = {'bb': 0.147148,'cc': 0.149167,'c': 0.210927,'l': 0.492757}
#frac[2]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.128953,'cc': 0.131890,'c': 0.207636,'l': 0.531521}
#frac[5]['mu']["EG_SCALE_ALL__1down"] = {'bb': 0.138054,'cc': 0.144177,'c': 0.203653,'l': 0.514115}
## MUON_ID__1up 
#frac[2]['el']["MUON_ID__1up"] = {'bb': 0.093915,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["MUON_ID__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["MUON_ID__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["MUON_ID__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["MUON_ID__1up"] = {'bb': 0.083053,'cc': 0.062691,'c': 0.204956,'l': 0.649300}
#frac[3]['mu']["MUON_ID__1up"] = {'bb': 0.105906,'cc': 0.096374,'c': 0.215580,'l': 0.582140}
#frac[4]['mu']["MUON_ID__1up"] = {'bb': 0.128929,'cc': 0.131852,'c': 0.207767,'l': 0.531452}
#frac[5]['mu']["MUON_ID__1up"] = {'bb': 0.138014,'cc': 0.144095,'c': 0.203765,'l': 0.514125}
## MUON_ID__1down 
#frac[2]['el']["MUON_ID__1down"] = {'bb': 0.093915,'cc': 0.063787,'c': 0.208946,'l': 0.633352}
#frac[3]['el']["MUON_ID__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["MUON_ID__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["MUON_ID__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["MUON_ID__1down"] = {'bb': 0.083080,'cc': 0.062678,'c': 0.204867,'l': 0.649375}
#frac[3]['mu']["MUON_ID__1down"] = {'bb': 0.105934,'cc': 0.096349,'c': 0.215588,'l': 0.582129}
#frac[4]['mu']["MUON_ID__1down"] = {'bb': 0.128904,'cc': 0.131884,'c': 0.207716,'l': 0.531497}
#frac[5]['mu']["MUON_ID__1down"] = {'bb': 0.137998,'cc': 0.144153,'c': 0.203732,'l': 0.514117}
## MUON_MS__1up 
#frac[2]['el']["MUON_MS__1up"] = {'bb': 0.093915,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["MUON_MS__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["MUON_MS__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["MUON_MS__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["MUON_MS__1up"] = {'bb': 0.083038,'cc': 0.062684,'c': 0.204840,'l': 0.649438}
#frac[3]['mu']["MUON_MS__1up"] = {'bb': 0.105935,'cc': 0.096356,'c': 0.215572,'l': 0.582138}
#frac[4]['mu']["MUON_MS__1up"] = {'bb': 0.128981,'cc': 0.131844,'c': 0.207636,'l': 0.531539}
#frac[5]['mu']["MUON_MS__1up"] = {'bb': 0.138062,'cc': 0.144125,'c': 0.203706,'l': 0.514107}
## MUON_MS__1down 
#frac[2]['el']["MUON_MS__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["MUON_MS__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["MUON_MS__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["MUON_MS__1down"] = {'bb': 0.147173,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["MUON_MS__1down"] = {'bb': 0.083058,'cc': 0.062708,'c': 0.204907,'l': 0.649327}
#frac[3]['mu']["MUON_MS__1down"] = {'bb': 0.105951,'cc': 0.096326,'c': 0.215678,'l': 0.582044}
#frac[4]['mu']["MUON_MS__1down"] = {'bb': 0.128922,'cc': 0.131862,'c': 0.207522,'l': 0.531693}
#frac[5]['mu']["MUON_MS__1down"] = {'bb': 0.138039,'cc': 0.144124,'c': 0.203572,'l': 0.514265}
## MUON_SCALE__1up 
#frac[2]['el']["MUON_SCALE__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["MUON_SCALE__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["MUON_SCALE__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["MUON_SCALE__1up"] = {'bb': 0.147173,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["MUON_SCALE__1up"] = {'bb': 0.083063,'cc': 0.062700,'c': 0.204868,'l': 0.649370}
#frac[3]['mu']["MUON_SCALE__1up"] = {'bb': 0.105969,'cc': 0.096430,'c': 0.215585,'l': 0.582016}
#frac[4]['mu']["MUON_SCALE__1up"] = {'bb': 0.129004,'cc': 0.131889,'c': 0.207636,'l': 0.531471}
#frac[5]['mu']["MUON_SCALE__1up"] = {'bb': 0.138081,'cc': 0.144181,'c': 0.203654,'l': 0.514085}
## MUON_SCALE__1down 
#frac[2]['el']["MUON_SCALE__1down"] = {'bb': 0.093915,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["MUON_SCALE__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["MUON_SCALE__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["MUON_SCALE__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["MUON_SCALE__1down"] = {'bb': 0.083044,'cc': 0.062694,'c': 0.204906,'l': 0.649357}
#frac[3]['mu']["MUON_SCALE__1down"] = {'bb': 0.105990,'cc': 0.096332,'c': 0.215522,'l': 0.582156}
#frac[4]['mu']["MUON_SCALE__1down"] = {'bb': 0.128970,'cc': 0.131850,'c': 0.207683,'l': 0.531497}
#frac[5]['mu']["MUON_SCALE__1down"] = {'bb': 0.138056,'cc': 0.144144,'c': 0.203721,'l': 0.514078}
## MUON_SAGITTA_RESBIAS__1up 
#frac[2]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["MUON_SAGITTA_RESBIAS__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## MUON_SAGITTA_RESBIAS__1down 
#frac[2]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["MUON_SAGITTA_RESBIAS__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## MUON_SAGITTA_RHO__1up 
#frac[2]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["MUON_SAGITTA_RHO__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## MUON_SAGITTA_RHO__1down 
#frac[2]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["MUON_SAGITTA_RHO__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## JET_JER_SINGLE_NP__1up 
#frac[2]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.092933,'cc': 0.062783,'c': 0.207235,'l': 0.637049}
#frac[3]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.117068,'cc': 0.096800,'c': 0.218249,'l': 0.567883}
#frac[4]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.137404,'cc': 0.133522,'c': 0.214932,'l': 0.514142}
#frac[5]['el']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.145757,'cc': 0.146036,'c': 0.210232,'l': 0.497975}
#frac[2]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.082586,'cc': 0.061727,'c': 0.203829,'l': 0.651858}
#frac[3]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.105957,'cc': 0.094780,'c': 0.215309,'l': 0.583954}
#frac[4]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.128601,'cc': 0.130517,'c': 0.209047,'l': 0.531835}
#frac[5]['mu']["JET_JER_SINGLE_NP__1up"] = {'bb': 0.137552,'cc': 0.142479,'c': 0.204831,'l': 0.515137}
## JET_21NP_JET_EtaIntercalibration_Modelling__1up 
#frac[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.093541,'cc': 0.063296,'c': 0.208694,'l': 0.634469}
#frac[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.116851,'cc': 0.097742,'c': 0.218743,'l': 0.566664}
#frac[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.139088,'cc': 0.135857,'c': 0.216442,'l': 0.508612}
#frac[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.146719,'cc': 0.148146,'c': 0.211619,'l': 0.493516}
#frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.082879,'cc': 0.062201,'c': 0.204883,'l': 0.650037}
#frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.105721,'cc': 0.095841,'c': 0.215062,'l': 0.583375}
#frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.128159,'cc': 0.130796,'c': 0.207901,'l': 0.533144}
#frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] = {'bb': 0.137378,'cc': 0.143253,'c': 0.204013,'l': 0.515357}
## JET_21NP_JET_EtaIntercalibration_Modelling__1down 
#frac[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.094227,'cc': 0.064193,'c': 0.208894,'l': 0.632686}
#frac[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.117565,'cc': 0.099107,'c': 0.219174,'l': 0.564153}
#frac[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.139725,'cc': 0.137187,'c': 0.215068,'l': 0.508020}
#frac[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.147339,'cc': 0.149610,'c': 0.210356,'l': 0.492695}
#frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.083280,'cc': 0.063088,'c': 0.204856,'l': 0.648776}
#frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.106474,'cc': 0.097137,'c': 0.215357,'l': 0.581032}
#frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.129103,'cc': 0.132269,'c': 0.206591,'l': 0.532037}
#frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] = {'bb': 0.138212,'cc': 0.144667,'c': 0.202805,'l': 0.514315}
## JET_21NP_JET_EtaIntercalibration_NonClosure__1up 
#frac[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.093935,'cc': 0.063728,'c': 0.209081,'l': 0.633256}
#frac[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.117153,'cc': 0.098481,'c': 0.218997,'l': 0.565370}
#frac[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.139854,'cc': 0.136928,'c': 0.215544,'l': 0.507675}
#frac[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.147382,'cc': 0.149242,'c': 0.210717,'l': 0.492659}
#frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.083041,'cc': 0.062689,'c': 0.204939,'l': 0.649331}
#frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.106076,'cc': 0.096503,'c': 0.215273,'l': 0.582148}
#frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.129166,'cc': 0.132078,'c': 0.208565,'l': 0.530191}
#frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] = {'bb': 0.138159,'cc': 0.144361,'c': 0.204239,'l': 0.513241}
## JET_21NP_JET_EtaIntercalibration_NonClosure__1down 
#frac[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.093843,'cc': 0.063648,'c': 0.208776,'l': 0.633733}
#frac[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.117133,'cc': 0.097941,'c': 0.219218,'l': 0.565709}
#frac[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.139487,'cc': 0.136670,'c': 0.215937,'l': 0.507907}
#frac[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.147151,'cc': 0.149111,'c': 0.211092,'l': 0.492646}
#frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.083021,'cc': 0.062563,'c': 0.204827,'l': 0.649589}
#frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.105892,'cc': 0.096130,'c': 0.215563,'l': 0.582416}
#frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.128955,'cc': 0.131622,'c': 0.207512,'l': 0.531911}
#frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] = {'bb': 0.138046,'cc': 0.143992,'c': 0.203553,'l': 0.514409}
## JET_21NP_JET_EtaIntercalibration_TotalStat__1up 
#frac[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.093707,'cc': 0.063608,'c': 0.208646,'l': 0.634040}
#frac[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.116981,'cc': 0.097908,'c': 0.219116,'l': 0.565995}
#frac[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.139639,'cc': 0.136634,'c': 0.216024,'l': 0.507703}
#frac[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.147198,'cc': 0.148854,'c': 0.211128,'l': 0.492819}
#frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.083004,'cc': 0.062500,'c': 0.204862,'l': 0.649634}
#frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.105781,'cc': 0.096111,'c': 0.215402,'l': 0.582706}
#frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.128842,'cc': 0.131635,'c': 0.207728,'l': 0.531795}
#frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] = {'bb': 0.137962,'cc': 0.143961,'c': 0.203782,'l': 0.514295}
## JET_21NP_JET_EtaIntercalibration_TotalStat__1down 
#frac[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.094056,'cc': 0.063967,'c': 0.208955,'l': 0.633023}
#frac[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.117217,'cc': 0.098446,'c': 0.219195,'l': 0.565141}
#frac[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.139935,'cc': 0.137178,'c': 0.215430,'l': 0.507457}
#frac[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.147544,'cc': 0.149515,'c': 0.210832,'l': 0.492108}
#frac[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.083179,'cc': 0.062967,'c': 0.204871,'l': 0.648983}
#frac[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.106167,'cc': 0.096643,'c': 0.215366,'l': 0.581824}
#frac[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.129261,'cc': 0.132468,'c': 0.207607,'l': 0.530664}
#frac[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] = {'bb': 0.138275,'cc': 0.144676,'c': 0.203511,'l': 0.513537}
## JET_21NP_JET_Flavor_Composition__1up 
#frac[2]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.091385,'cc': 0.061635,'c': 0.207917,'l': 0.639064}
#frac[3]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.114286,'cc': 0.095344,'c': 0.217827,'l': 0.572543}
#frac[4]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.135966,'cc': 0.131610,'c': 0.218797,'l': 0.513628}
#frac[5]['el']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.143520,'cc': 0.144366,'c': 0.214058,'l': 0.498056}
#frac[2]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.081135,'cc': 0.060567,'c': 0.203077,'l': 0.655221}
#frac[3]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.103461,'cc': 0.093408,'c': 0.215692,'l': 0.587439}
#frac[4]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.125146,'cc': 0.127273,'c': 0.210027,'l': 0.537554}
#frac[5]['mu']["JET_21NP_JET_Flavor_Composition__1up"] = {'bb': 0.134015,'cc': 0.140067,'c': 0.206383,'l': 0.519534}
## JET_21NP_JET_Flavor_Composition__1down 
#frac[2]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.096448,'cc': 0.066058,'c': 0.209736,'l': 0.627758}
#frac[3]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.120989,'cc': 0.102205,'c': 0.218829,'l': 0.557977}
#frac[4]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.142908,'cc': 0.138806,'c': 0.213034,'l': 0.505252}
#frac[5]['el']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.150793,'cc': 0.151585,'c': 0.208086,'l': 0.489536}
#frac[2]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.085063,'cc': 0.064949,'c': 0.205689,'l': 0.644299}
#frac[3]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.109373,'cc': 0.099905,'c': 0.215312,'l': 0.575409}
#frac[4]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.133352,'cc': 0.135779,'c': 0.205651,'l': 0.525218}
#frac[5]['mu']["JET_21NP_JET_Flavor_Composition__1down"] = {'bb': 0.142745,'cc': 0.147906,'c': 0.201191,'l': 0.508158}
## JET_21NP_JET_Flavor_Response__1up 
#frac[2]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.094625,'cc': 0.064450,'c': 0.209021,'l': 0.631905}
#frac[3]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.117978,'cc': 0.099115,'c': 0.219293,'l': 0.563615}
#frac[4]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.140685,'cc': 0.137872,'c': 0.214772,'l': 0.506672}
#frac[5]['el']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.148337,'cc': 0.150202,'c': 0.210068,'l': 0.491393}
#frac[2]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.083625,'cc': 0.063308,'c': 0.204857,'l': 0.648210}
#frac[3]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.107106,'cc': 0.097405,'c': 0.215477,'l': 0.580013}
#frac[4]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.129554,'cc': 0.132690,'c': 0.205793,'l': 0.531964}
#frac[5]['mu']["JET_21NP_JET_Flavor_Response__1up"] = {'bb': 0.138914,'cc': 0.145070,'c': 0.202238,'l': 0.513777}
## JET_21NP_JET_Flavor_Response__1down 
#frac[2]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.093054,'cc': 0.062899,'c': 0.208685,'l': 0.635361}
#frac[3]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.116289,'cc': 0.097471,'c': 0.218597,'l': 0.567643}
#frac[4]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.138620,'cc': 0.135395,'c': 0.217670,'l': 0.508315}
#frac[5]['el']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.146149,'cc': 0.147682,'c': 0.212545,'l': 0.493624}
#frac[2]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.082685,'cc': 0.062134,'c': 0.204665,'l': 0.650516}
#frac[3]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.104959,'cc': 0.095448,'c': 0.215078,'l': 0.584514}
#frac[4]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.127734,'cc': 0.130289,'c': 0.208614,'l': 0.533363}
#frac[5]['mu']["JET_21NP_JET_Flavor_Response__1down"] = {'bb': 0.136820,'cc': 0.142764,'c': 0.204638,'l': 0.515778}
## JET_21NP_JET_Pileup_OffsetMu__1up 
#frac[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.093983,'cc': 0.063882,'c': 0.208703,'l': 0.633432}
#frac[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.117077,'cc': 0.098465,'c': 0.219409,'l': 0.565049}
#frac[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.139818,'cc': 0.136920,'c': 0.215722,'l': 0.507540}
#frac[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.147335,'cc': 0.149175,'c': 0.210857,'l': 0.492633}
#frac[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.083117,'cc': 0.062735,'c': 0.204736,'l': 0.649412}
#frac[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.106056,'cc': 0.096347,'c': 0.215373,'l': 0.582224}
#frac[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.128875,'cc': 0.131842,'c': 0.207674,'l': 0.531609}
#frac[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] = {'bb': 0.138003,'cc': 0.144209,'c': 0.203651,'l': 0.514136}
## JET_21NP_JET_Pileup_OffsetMu__1down 
#frac[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.093818,'cc': 0.063715,'c': 0.209032,'l': 0.633435}
#frac[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.117192,'cc': 0.097989,'c': 0.218772,'l': 0.566047}
#frac[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.139390,'cc': 0.136746,'c': 0.215730,'l': 0.508135}
#frac[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.147132,'cc': 0.149044,'c': 0.210998,'l': 0.492826}
#frac[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.083076,'cc': 0.062712,'c': 0.205042,'l': 0.649170}
#frac[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.105841,'cc': 0.096479,'c': 0.215366,'l': 0.582314}
#frac[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.129198,'cc': 0.131926,'c': 0.207570,'l': 0.531306}
#frac[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] = {'bb': 0.138200,'cc': 0.144235,'c': 0.203615,'l': 0.513950}
## JET_21NP_JET_Pileup_OffsetNPV__1up 
#frac[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.093509,'cc': 0.063341,'c': 0.208967,'l': 0.634183}
#frac[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.116793,'cc': 0.097877,'c': 0.218988,'l': 0.566341}
#frac[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.139968,'cc': 0.136019,'c': 0.216898,'l': 0.507115}
#frac[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.147253,'cc': 0.148260,'c': 0.211655,'l': 0.492832}
#frac[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.083079,'cc': 0.062400,'c': 0.204658,'l': 0.649863}
#frac[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.105705,'cc': 0.095630,'c': 0.215338,'l': 0.583327}
#frac[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.128244,'cc': 0.130777,'c': 0.207786,'l': 0.533193}
#frac[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] = {'bb': 0.137328,'cc': 0.142881,'c': 0.204069,'l': 0.515722}
## JET_21NP_JET_Pileup_OffsetNPV__1down 
#frac[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.094286,'cc': 0.064006,'c': 0.209284,'l': 0.632425}
#frac[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.117213,'cc': 0.098443,'c': 0.218903,'l': 0.565440}
#frac[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.139866,'cc': 0.137272,'c': 0.215792,'l': 0.507069}
#frac[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.147480,'cc': 0.149635,'c': 0.210730,'l': 0.492155}
#frac[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.083321,'cc': 0.062929,'c': 0.205162,'l': 0.648588}
#frac[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.106349,'cc': 0.097119,'c': 0.214992,'l': 0.581540}
#frac[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.129332,'cc': 0.132755,'c': 0.206964,'l': 0.530948}
#frac[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] = {'bb': 0.138530,'cc': 0.145090,'c': 0.202973,'l': 0.513406}
## JET_21NP_JET_Pileup_PtTerm__1up 
#frac[2]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.093923,'cc': 0.063738,'c': 0.208864,'l': 0.633476}
#frac[3]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.117090,'cc': 0.098164,'c': 0.219197,'l': 0.565548}
#frac[4]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.139626,'cc': 0.136815,'c': 0.215549,'l': 0.508010}
#frac[5]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.147212,'cc': 0.149132,'c': 0.210874,'l': 0.492782}
#frac[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.083066,'cc': 0.062680,'c': 0.204714,'l': 0.649540}
#frac[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.105933,'cc': 0.096305,'c': 0.215587,'l': 0.582175}
#frac[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.129006,'cc': 0.131829,'c': 0.207525,'l': 0.531640}
#frac[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] = {'bb': 0.138095,'cc': 0.144115,'c': 0.203605,'l': 0.514185}
## JET_21NP_JET_Pileup_PtTerm__1down 
#frac[2]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.093946,'cc': 0.063840,'c': 0.209158,'l': 0.633057}
#frac[3]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.117107,'cc': 0.098211,'c': 0.218954,'l': 0.565729}
#frac[4]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.139525,'cc': 0.136793,'c': 0.216014,'l': 0.507668}
#frac[5]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.147154,'cc': 0.149079,'c': 0.211081,'l': 0.492686}
#frac[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.083063,'cc': 0.062729,'c': 0.204951,'l': 0.649256}
#frac[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.105993,'cc': 0.096416,'c': 0.215339,'l': 0.582252}
#frac[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.129007,'cc': 0.131859,'c': 0.207767,'l': 0.531366}
#frac[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] = {'bb': 0.138086,'cc': 0.144214,'c': 0.203653,'l': 0.514047}
## JET_21NP_JET_Pileup_RhoTopology__1up 
#frac[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.092657,'cc': 0.061948,'c': 0.208356,'l': 0.637040}
#frac[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.116035,'cc': 0.096286,'c': 0.217532,'l': 0.570146}
#frac[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.138446,'cc': 0.132896,'c': 0.218065,'l': 0.510593}
#frac[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.146086,'cc': 0.145447,'c': 0.213013,'l': 0.495454}
#frac[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.082325,'cc': 0.061242,'c': 0.203767,'l': 0.652666}
#frac[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.104828,'cc': 0.093937,'c': 0.214909,'l': 0.586325}
#frac[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.127934,'cc': 0.128412,'c': 0.209393,'l': 0.534261}
#frac[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] = {'bb': 0.136818,'cc': 0.141033,'c': 0.205560,'l': 0.516589}
## JET_21NP_JET_Pileup_RhoTopology__1down 
#frac[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.094925,'cc': 0.065085,'c': 0.209761,'l': 0.630230}
#frac[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.118376,'cc': 0.100669,'c': 0.218935,'l': 0.562020}
#frac[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.140564,'cc': 0.139262,'c': 0.214910,'l': 0.505264}
#frac[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.148076,'cc': 0.151633,'c': 0.209859,'l': 0.490432}
#frac[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.083812,'cc': 0.064232,'c': 0.205304,'l': 0.646653}
#frac[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.107431,'cc': 0.098725,'c': 0.215336,'l': 0.578508}
#frac[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.130143,'cc': 0.134515,'c': 0.206268,'l': 0.529075}
#frac[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] = {'bb': 0.139434,'cc': 0.146689,'c': 0.202150,'l': 0.511727}
## JET_21NP_JET_PunchThrough_MC15__1up 
#frac[2]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.093915,'cc': 0.063790,'c': 0.208945,'l': 0.633349}
#frac[3]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.117131,'cc': 0.098168,'c': 0.219126,'l': 0.565575}
#frac[4]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.139567,'cc': 0.136936,'c': 0.215735,'l': 0.507762}
#frac[5]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.147174,'cc': 0.149152,'c': 0.210933,'l': 0.492741}
#frac[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.083057,'cc': 0.062701,'c': 0.204913,'l': 0.649329}
#frac[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.105986,'cc': 0.096368,'c': 0.215587,'l': 0.582059}
#frac[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.128956,'cc': 0.131889,'c': 0.207633,'l': 0.531523}
#frac[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] = {'bb': 0.138056,'cc': 0.144177,'c': 0.203651,'l': 0.514116}
## JET_21NP_JET_PunchThrough_MC15__1down 
#frac[2]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.093915,'cc': 0.063786,'c': 0.208945,'l': 0.633354}
#frac[3]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.117126,'cc': 0.098184,'c': 0.219126,'l': 0.565564}
#frac[4]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215737,'l': 0.507761}
#frac[5]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.147173,'cc': 0.149155,'c': 0.210934,'l': 0.492738}
#frac[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204913,'l': 0.649329}
#frac[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.105981,'cc': 0.096370,'c': 0.215582,'l': 0.582067}
#frac[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.128955,'cc': 0.131888,'c': 0.207637,'l': 0.531520}
#frac[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] = {'bb': 0.138053,'cc': 0.144178,'c': 0.203655,'l': 0.514114}
## JET_21NP_JET_SingleParticle_HighPt__1up 
#frac[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514116}
## JET_21NP_JET_SingleParticle_HighPt__1down 
#frac[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514116}
## JET_21NP_JET_BJES_Response__1up 
#frac[2]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.094169,'cc': 0.063769,'c': 0.208887,'l': 0.633175}
#frac[3]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.117577,'cc': 0.098135,'c': 0.219012,'l': 0.565276}
#frac[4]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.140106,'cc': 0.136852,'c': 0.215600,'l': 0.507442}
#frac[5]['el']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.147748,'cc': 0.149054,'c': 0.210791,'l': 0.492407}
#frac[2]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.083264,'cc': 0.062687,'c': 0.204865,'l': 0.649184}
#frac[3]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.106352,'cc': 0.096328,'c': 0.215501,'l': 0.581819}
#frac[4]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.129503,'cc': 0.131806,'c': 0.207505,'l': 0.531186}
#frac[5]['mu']["JET_21NP_JET_BJES_Response__1up"] = {'bb': 0.138638,'cc': 0.144079,'c': 0.203516,'l': 0.513767}
## JET_21NP_JET_BJES_Response__1down 
#frac[2]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.093689,'cc': 0.063803,'c': 0.208997,'l': 0.633510}
#frac[3]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.116689,'cc': 0.098234,'c': 0.219233,'l': 0.565844}
#frac[4]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.138911,'cc': 0.137042,'c': 0.215900,'l': 0.508147}
#frac[5]['el']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.146483,'cc': 0.149275,'c': 0.211104,'l': 0.493138}
#frac[2]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.082849,'cc': 0.062715,'c': 0.204958,'l': 0.649478}
#frac[3]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.105614,'cc': 0.096408,'c': 0.215679,'l': 0.582299}
#frac[4]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.128437,'cc': 0.131970,'c': 0.207758,'l': 0.531835}
#frac[5]['mu']["JET_21NP_JET_BJES_Response__1down"] = {'bb': 0.137486,'cc': 0.144274,'c': 0.203787,'l': 0.514453}
## JET_21NP_JET_EffectiveNP_1__1up 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.092997,'cc': 0.062373,'c': 0.208387,'l': 0.636243}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.116460,'cc': 0.096964,'c': 0.218241,'l': 0.568335}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.139068,'cc': 0.134278,'c': 0.217465,'l': 0.509189}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.146590,'cc': 0.146858,'c': 0.212452,'l': 0.494101}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.082640,'cc': 0.061755,'c': 0.204048,'l': 0.651557}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.105239,'cc': 0.094583,'c': 0.215509,'l': 0.584670}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.127704,'cc': 0.129212,'c': 0.208347,'l': 0.534737}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] = {'bb': 0.136833,'cc': 0.141819,'c': 0.204514,'l': 0.516834}
## JET_21NP_JET_EffectiveNP_1__1down 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.094682,'cc': 0.064713,'c': 0.209253,'l': 0.631352}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.117940,'cc': 0.100152,'c': 0.219208,'l': 0.562700}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.140288,'cc': 0.138400,'c': 0.214990,'l': 0.506322}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.147918,'cc': 0.150838,'c': 0.210105,'l': 0.491139}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.083590,'cc': 0.063804,'c': 0.205121,'l': 0.647485}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.107050,'cc': 0.097869,'c': 0.215216,'l': 0.579865}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.129438,'cc': 0.133895,'c': 0.206032,'l': 0.530635}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] = {'bb': 0.138775,'cc': 0.145994,'c': 0.202341,'l': 0.512890}
## JET_21NP_JET_EffectiveNP_2__1up 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.094070,'cc': 0.063982,'c': 0.208934,'l': 0.633014}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.117299,'cc': 0.098382,'c': 0.219224,'l': 0.565095}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.139956,'cc': 0.137337,'c': 0.215442,'l': 0.507265}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.147531,'cc': 0.149590,'c': 0.210704,'l': 0.492175}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.083188,'cc': 0.063033,'c': 0.204923,'l': 0.648857}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.106219,'cc': 0.096749,'c': 0.215387,'l': 0.581645}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.129149,'cc': 0.132383,'c': 0.207518,'l': 0.530951}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] = {'bb': 0.138245,'cc': 0.144654,'c': 0.203465,'l': 0.513636}
## JET_21NP_JET_EffectiveNP_2__1down 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.093663,'cc': 0.063554,'c': 0.208644,'l': 0.634139}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.116981,'cc': 0.097876,'c': 0.219227,'l': 0.565916}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.139625,'cc': 0.136432,'c': 0.215989,'l': 0.507955}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.147169,'cc': 0.148748,'c': 0.211180,'l': 0.492903}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.082963,'cc': 0.062460,'c': 0.204935,'l': 0.649642}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.105701,'cc': 0.095945,'c': 0.215307,'l': 0.583048}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.128879,'cc': 0.131401,'c': 0.208003,'l': 0.531717}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] = {'bb': 0.137967,'cc': 0.143777,'c': 0.204025,'l': 0.514231}
## JET_21NP_JET_EffectiveNP_3__1up 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.093883,'cc': 0.063750,'c': 0.208966,'l': 0.633401}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.117090,'cc': 0.098204,'c': 0.219020,'l': 0.565685}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.139520,'cc': 0.136834,'c': 0.215920,'l': 0.507726}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.147198,'cc': 0.149095,'c': 0.211106,'l': 0.492602}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.083033,'cc': 0.062624,'c': 0.204919,'l': 0.649424}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.105886,'cc': 0.096290,'c': 0.215667,'l': 0.582157}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.129025,'cc': 0.131949,'c': 0.207571,'l': 0.531456}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] = {'bb': 0.138091,'cc': 0.144220,'c': 0.203659,'l': 0.514030}
## JET_21NP_JET_EffectiveNP_3__1down 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.093923,'cc': 0.063767,'c': 0.209011,'l': 0.633299}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.117235,'cc': 0.098172,'c': 0.219126,'l': 0.565467}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.139594,'cc': 0.137118,'c': 0.215728,'l': 0.507559}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.147166,'cc': 0.149315,'c': 0.210890,'l': 0.492629}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.083066,'cc': 0.062801,'c': 0.204804,'l': 0.649328}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.106060,'cc': 0.096400,'c': 0.215660,'l': 0.581880}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.129066,'cc': 0.131992,'c': 0.207657,'l': 0.531285}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] = {'bb': 0.138136,'cc': 0.144283,'c': 0.203653,'l': 0.513928}
## JET_21NP_JET_EffectiveNP_4__1up 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.093912,'cc': 0.063811,'c': 0.208948,'l': 0.633330}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.117206,'cc': 0.098093,'c': 0.219175,'l': 0.565526}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.139596,'cc': 0.137009,'c': 0.215676,'l': 0.507719}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.147180,'cc': 0.149234,'c': 0.210867,'l': 0.492719}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.083076,'cc': 0.062782,'c': 0.204855,'l': 0.649287}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.106000,'cc': 0.096400,'c': 0.215601,'l': 0.581999}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.129043,'cc': 0.131903,'c': 0.207625,'l': 0.531429}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] = {'bb': 0.138109,'cc': 0.144189,'c': 0.203654,'l': 0.514047}
## JET_21NP_JET_EffectiveNP_4__1down 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.093900,'cc': 0.063772,'c': 0.208983,'l': 0.633344}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.117085,'cc': 0.098168,'c': 0.219193,'l': 0.565554}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.139562,'cc': 0.136921,'c': 0.215727,'l': 0.507790}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.147215,'cc': 0.149162,'c': 0.210968,'l': 0.492655}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.083061,'cc': 0.062654,'c': 0.204888,'l': 0.649397}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.105925,'cc': 0.096318,'c': 0.215671,'l': 0.582086}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.129037,'cc': 0.131963,'c': 0.207563,'l': 0.531438}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] = {'bb': 0.138108,'cc': 0.144241,'c': 0.203643,'l': 0.514008}
## JET_21NP_JET_EffectiveNP_5__1up 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.093909,'cc': 0.063807,'c': 0.209025,'l': 0.633259}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.117176,'cc': 0.098173,'c': 0.219121,'l': 0.565529}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.139525,'cc': 0.136937,'c': 0.215749,'l': 0.507789}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.147161,'cc': 0.149205,'c': 0.210943,'l': 0.492691}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.083055,'cc': 0.062722,'c': 0.204895,'l': 0.649328}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.105987,'cc': 0.096383,'c': 0.215642,'l': 0.581988}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.129018,'cc': 0.131844,'c': 0.207600,'l': 0.531538}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] = {'bb': 0.138092,'cc': 0.144156,'c': 0.203611,'l': 0.514141}
## JET_21NP_JET_EffectiveNP_5__1down 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.093913,'cc': 0.063762,'c': 0.208919,'l': 0.633406}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.117091,'cc': 0.098097,'c': 0.219170,'l': 0.565642}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.139678,'cc': 0.136991,'c': 0.215844,'l': 0.507487}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.147242,'cc': 0.149178,'c': 0.211015,'l': 0.492565}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.083067,'cc': 0.062706,'c': 0.204887,'l': 0.649340}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.105923,'cc': 0.096317,'c': 0.215661,'l': 0.582099}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.128999,'cc': 0.132003,'c': 0.207535,'l': 0.531463}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] = {'bb': 0.138082,'cc': 0.144247,'c': 0.203575,'l': 0.514096}
## JET_21NP_JET_EffectiveNP_6__1up 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.093874,'cc': 0.063720,'c': 0.208920,'l': 0.633486}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.117055,'cc': 0.098157,'c': 0.218938,'l': 0.565851}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.139617,'cc': 0.136920,'c': 0.216000,'l': 0.507463}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.147205,'cc': 0.149136,'c': 0.211117,'l': 0.492542}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.083026,'cc': 0.062636,'c': 0.204858,'l': 0.649480}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.105890,'cc': 0.096300,'c': 0.215817,'l': 0.581994}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.128938,'cc': 0.131839,'c': 0.207373,'l': 0.531849}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] = {'bb': 0.138031,'cc': 0.144138,'c': 0.203514,'l': 0.514318}
## JET_21NP_JET_EffectiveNP_6__1down 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.093914,'cc': 0.063775,'c': 0.209077,'l': 0.633233}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.117264,'cc': 0.098217,'c': 0.219101,'l': 0.565418}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.139555,'cc': 0.137127,'c': 0.215853,'l': 0.507466}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.147159,'cc': 0.149331,'c': 0.210952,'l': 0.492558}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.083072,'cc': 0.062745,'c': 0.204883,'l': 0.649300}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.106056,'cc': 0.096403,'c': 0.215639,'l': 0.581902}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.129042,'cc': 0.132107,'c': 0.207675,'l': 0.531177}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] = {'bb': 0.138107,'cc': 0.144354,'c': 0.203657,'l': 0.513881}
## JET_21NP_JET_EffectiveNP_7__1up 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.093934,'cc': 0.063791,'c': 0.208971,'l': 0.633304}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.117261,'cc': 0.098221,'c': 0.219161,'l': 0.565357}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.139558,'cc': 0.137129,'c': 0.215772,'l': 0.507540}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.147156,'cc': 0.149320,'c': 0.210909,'l': 0.492615}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.083068,'cc': 0.062813,'c': 0.204821,'l': 0.649299}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.106055,'cc': 0.096460,'c': 0.215576,'l': 0.581908}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.129107,'cc': 0.132019,'c': 0.207804,'l': 0.531069}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] = {'bb': 0.138162,'cc': 0.144292,'c': 0.203750,'l': 0.513796}
## JET_21NP_JET_EffectiveNP_7__1down 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.093857,'cc': 0.063723,'c': 0.208948,'l': 0.633472}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.117037,'cc': 0.098108,'c': 0.218985,'l': 0.565870}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.139565,'cc': 0.136901,'c': 0.216018,'l': 0.507516}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.147188,'cc': 0.149128,'c': 0.211127,'l': 0.492557}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.083025,'cc': 0.062616,'c': 0.204871,'l': 0.649488}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.105850,'cc': 0.096237,'c': 0.215694,'l': 0.582218}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.128945,'cc': 0.131763,'c': 0.207404,'l': 0.531888}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] = {'bb': 0.138044,'cc': 0.144079,'c': 0.203554,'l': 0.514323}
## JET_21NP_JET_EffectiveNP_8restTerm__1up 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.093907,'cc': 0.063764,'c': 0.208971,'l': 0.633359}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.117094,'cc': 0.098157,'c': 0.219147,'l': 0.565602}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.139671,'cc': 0.137002,'c': 0.215816,'l': 0.507511}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.147245,'cc': 0.149198,'c': 0.210988,'l': 0.492569}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.083079,'cc': 0.062665,'c': 0.204937,'l': 0.649320}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.105929,'cc': 0.096329,'c': 0.215678,'l': 0.582065}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.128961,'cc': 0.132012,'c': 0.207506,'l': 0.531521}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] = {'bb': 0.138054,'cc': 0.144261,'c': 0.203561,'l': 0.514124}
## JET_21NP_JET_EffectiveNP_8restTerm__1down 
#frac[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.093908,'cc': 0.063801,'c': 0.208993,'l': 0.633298}
#frac[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.117202,'cc': 0.098196,'c': 0.219066,'l': 0.565536}
#frac[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.139550,'cc': 0.137008,'c': 0.215731,'l': 0.507710}
#frac[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.147141,'cc': 0.149199,'c': 0.210889,'l': 0.492771}
#frac[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.083057,'cc': 0.062751,'c': 0.204891,'l': 0.649302}
#frac[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.105998,'cc': 0.096400,'c': 0.215590,'l': 0.582011}
#frac[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.129003,'cc': 0.131858,'c': 0.207630,'l': 0.531509}
#frac[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] = {'bb': 0.138089,'cc': 0.144158,'c': 0.203652,'l': 0.514101}
## LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down 
#frac[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Comb_Baseline_Kin__1up 
#frac[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Comb_Baseline_Kin__1down 
#frac[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Comb_Modelling_Kin__1up 
#frac[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Comb_Modelling_Kin__1down 
#frac[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up 
#frac[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down 
#frac[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Comb_Tracking_Kin__1up 
#frac[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Comb_Tracking_Kin__1down 
#frac[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up 
#frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down 
#frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up 
#frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down 
#frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up 
#frac[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down 
#frac[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up 
#frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down 
#frac[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Strong_JET_Comb_Baseline_All__1up 
#frac[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Strong_JET_Comb_Baseline_All__1down 
#frac[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Strong_JET_Comb_Modelling_All__1up 
#frac[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Strong_JET_Comb_Modelling_All__1down 
#frac[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Strong_JET_Comb_TotalStat_All__1up 
#frac[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Strong_JET_Comb_TotalStat_All__1down 
#frac[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Strong_JET_Comb_Tracking_All__1up 
#frac[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## LARGERJET_Strong_JET_Comb_Tracking_All__1down 
#frac[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
#
#
## CA factors
#
#f_ca_map[2]['el'][""] =  1.161069
#f_ca_map[3]['el'][""] =  1.246692
#f_ca_map[4]['el'][""] =  1.321595
#f_ca_map[5]['el'][""] =  1.105718
#f_ca_map[2]['mu'][""] =  1.178331
#f_ca_map[3]['mu'][""] =  1.161164
#f_ca_map[4]['mu'][""] =  1.142417
#f_ca_map[5]['mu'][""] =  1.062010
## ttxsecup 
#f_ca_map[2]['el']["ttxsecup"] =  1.161057
#f_ca_map[3]['el']["ttxsecup"] =  1.246696
#f_ca_map[4]['el']["ttxsecup"] =  1.321584
#f_ca_map[5]['el']["ttxsecup"] =  1.105726
#f_ca_map[2]['mu']["ttxsecup"] =  1.178328
#f_ca_map[3]['mu']["ttxsecup"] =  1.161188
#f_ca_map[4]['mu']["ttxsecup"] =  1.142448
#f_ca_map[5]['mu']["ttxsecup"] =  1.061996
## ttxsecdw 
#f_ca_map[2]['el']["ttxsecdw"] =  1.161079
#f_ca_map[3]['el']["ttxsecdw"] =  1.246689
#f_ca_map[4]['el']["ttxsecdw"] =  1.321605
#f_ca_map[5]['el']["ttxsecdw"] =  1.105710
#f_ca_map[2]['mu']["ttxsecdw"] =  1.178334
#f_ca_map[3]['mu']["ttxsecdw"] =  1.161143
#f_ca_map[4]['mu']["ttxsecdw"] =  1.142390
#f_ca_map[5]['mu']["ttxsecdw"] =  1.062021
## singletopup 
#f_ca_map[2]['el']["singletopup"] =  1.158796
#f_ca_map[3]['el']["singletopup"] =  1.243775
#f_ca_map[4]['el']["singletopup"] =  1.317420
#f_ca_map[5]['el']["singletopup"] =  1.102379
#f_ca_map[2]['mu']["singletopup"] =  1.176944
#f_ca_map[3]['mu']["singletopup"] =  1.158418
#f_ca_map[4]['mu']["singletopup"] =  1.139190
#f_ca_map[5]['mu']["singletopup"] =  1.059512
## singletopdw 
#f_ca_map[2]['el']["singletopdw"] =  1.163058
#f_ca_map[3]['el']["singletopdw"] =  1.249246
#f_ca_map[4]['el']["singletopdw"] =  1.325246
#f_ca_map[5]['el']["singletopdw"] =  1.108644
#f_ca_map[2]['mu']["singletopdw"] =  1.179545
#f_ca_map[3]['mu']["singletopdw"] =  1.163566
#f_ca_map[4]['mu']["singletopdw"] =  1.145237
#f_ca_map[5]['mu']["singletopdw"] =  1.064199
## wnorm__1up 
#f_ca_map[2]['el']["wnorm__1up"] =  1.161071
#f_ca_map[3]['el']["wnorm__1up"] =  1.246692
#f_ca_map[4]['el']["wnorm__1up"] =  1.321597
#f_ca_map[5]['el']["wnorm__1up"] =  1.105716
#f_ca_map[2]['mu']["wnorm__1up"] =  1.178331
#f_ca_map[3]['mu']["wnorm__1up"] =  1.161165
#f_ca_map[4]['mu']["wnorm__1up"] =  1.142419
#f_ca_map[5]['mu']["wnorm__1up"] =  1.062009
## wnorm__1down 
#f_ca_map[2]['el']["wnorm__1down"] =  1.161067
#f_ca_map[3]['el']["wnorm__1down"] =  1.246693
#f_ca_map[4]['el']["wnorm__1down"] =  1.321594
#f_ca_map[5]['el']["wnorm__1down"] =  1.105719
#f_ca_map[2]['mu']["wnorm__1down"] =  1.178331
#f_ca_map[3]['mu']["wnorm__1down"] =  1.161162
#f_ca_map[4]['mu']["wnorm__1down"] =  1.142414
#f_ca_map[5]['mu']["wnorm__1down"] =  1.062011
## MET_SoftTrk_ResoPara 
#f_ca_map[2]['el']["MET_SoftTrk_ResoPara"] =  1.165139
#f_ca_map[3]['el']["MET_SoftTrk_ResoPara"] =  1.252028
#f_ca_map[4]['el']["MET_SoftTrk_ResoPara"] =  1.323998
#f_ca_map[5]['el']["MET_SoftTrk_ResoPara"] =  1.094430
#f_ca_map[2]['mu']["MET_SoftTrk_ResoPara"] =  1.182690
#f_ca_map[3]['mu']["MET_SoftTrk_ResoPara"] =  1.158372
#f_ca_map[4]['mu']["MET_SoftTrk_ResoPara"] =  1.141267
#f_ca_map[5]['mu']["MET_SoftTrk_ResoPara"] =  1.059111
## MET_SoftTrk_ResoPerp 
#f_ca_map[2]['el']["MET_SoftTrk_ResoPerp"] =  1.163230
#f_ca_map[3]['el']["MET_SoftTrk_ResoPerp"] =  1.245768
#f_ca_map[4]['el']["MET_SoftTrk_ResoPerp"] =  1.325017
#f_ca_map[5]['el']["MET_SoftTrk_ResoPerp"] =  1.104585
#f_ca_map[2]['mu']["MET_SoftTrk_ResoPerp"] =  1.179752
#f_ca_map[3]['mu']["MET_SoftTrk_ResoPerp"] =  1.166323
#f_ca_map[4]['mu']["MET_SoftTrk_ResoPerp"] =  1.137747
#f_ca_map[5]['mu']["MET_SoftTrk_ResoPerp"] =  1.059103
## MET_SoftTrk_ScaleUp 
#f_ca_map[2]['el']["MET_SoftTrk_ScaleUp"] =  1.157480
#f_ca_map[3]['el']["MET_SoftTrk_ScaleUp"] =  1.249972
#f_ca_map[4]['el']["MET_SoftTrk_ScaleUp"] =  1.326986
#f_ca_map[5]['el']["MET_SoftTrk_ScaleUp"] =  1.101039
#f_ca_map[2]['mu']["MET_SoftTrk_ScaleUp"] =  1.177501
#f_ca_map[3]['mu']["MET_SoftTrk_ScaleUp"] =  1.160551
#f_ca_map[4]['mu']["MET_SoftTrk_ScaleUp"] =  1.144446
#f_ca_map[5]['mu']["MET_SoftTrk_ScaleUp"] =  1.062378
## MET_SoftTrk_ScaleDown 
#f_ca_map[2]['el']["MET_SoftTrk_ScaleDown"] =  1.162872
#f_ca_map[3]['el']["MET_SoftTrk_ScaleDown"] =  1.245010
#f_ca_map[4]['el']["MET_SoftTrk_ScaleDown"] =  1.321759
#f_ca_map[5]['el']["MET_SoftTrk_ScaleDown"] =  1.102634
#f_ca_map[2]['mu']["MET_SoftTrk_ScaleDown"] =  1.179316
#f_ca_map[3]['mu']["MET_SoftTrk_ScaleDown"] =  1.161400
#f_ca_map[4]['mu']["MET_SoftTrk_ScaleDown"] =  1.143314
#f_ca_map[5]['mu']["MET_SoftTrk_ScaleDown"] =  1.058590
## EG_RESOLUTION_ALL__1up 
#f_ca_map[2]['el']["EG_RESOLUTION_ALL__1up"] =  1.161998
#f_ca_map[3]['el']["EG_RESOLUTION_ALL__1up"] =  1.249150
#f_ca_map[4]['el']["EG_RESOLUTION_ALL__1up"] =  1.327970
#f_ca_map[5]['el']["EG_RESOLUTION_ALL__1up"] =  1.107554
#f_ca_map[2]['mu']["EG_RESOLUTION_ALL__1up"] =  1.178332
#f_ca_map[3]['mu']["EG_RESOLUTION_ALL__1up"] =  1.161144
#f_ca_map[4]['mu']["EG_RESOLUTION_ALL__1up"] =  1.142409
#f_ca_map[5]['mu']["EG_RESOLUTION_ALL__1up"] =  1.062048
## EG_RESOLUTION_ALL__1down 
#f_ca_map[2]['el']["EG_RESOLUTION_ALL__1down"] =  1.164984
#f_ca_map[3]['el']["EG_RESOLUTION_ALL__1down"] =  1.244040
#f_ca_map[4]['el']["EG_RESOLUTION_ALL__1down"] =  1.320241
#f_ca_map[5]['el']["EG_RESOLUTION_ALL__1down"] =  1.100187
#f_ca_map[2]['mu']["EG_RESOLUTION_ALL__1down"] =  1.178329
#f_ca_map[3]['mu']["EG_RESOLUTION_ALL__1down"] =  1.161166
#f_ca_map[4]['mu']["EG_RESOLUTION_ALL__1down"] =  1.142417
#f_ca_map[5]['mu']["EG_RESOLUTION_ALL__1down"] =  1.062087
## EG_SCALE_ALL__1up 
#f_ca_map[2]['el']["EG_SCALE_ALL__1up"] =  1.158815
#f_ca_map[3]['el']["EG_SCALE_ALL__1up"] =  1.243004
#f_ca_map[4]['el']["EG_SCALE_ALL__1up"] =  1.321705
#f_ca_map[5]['el']["EG_SCALE_ALL__1up"] =  1.103771
#f_ca_map[2]['mu']["EG_SCALE_ALL__1up"] =  1.178330
#f_ca_map[3]['mu']["EG_SCALE_ALL__1up"] =  1.161161
#f_ca_map[4]['mu']["EG_SCALE_ALL__1up"] =  1.142413
#f_ca_map[5]['mu']["EG_SCALE_ALL__1up"] =  1.062047
## EG_SCALE_ALL__1down 
#f_ca_map[2]['el']["EG_SCALE_ALL__1down"] =  1.165162
#f_ca_map[3]['el']["EG_SCALE_ALL__1down"] =  1.249940
#f_ca_map[4]['el']["EG_SCALE_ALL__1down"] =  1.327365
#f_ca_map[5]['el']["EG_SCALE_ALL__1down"] =  1.105257
#f_ca_map[2]['mu']["EG_SCALE_ALL__1down"] =  1.178334
#f_ca_map[3]['mu']["EG_SCALE_ALL__1down"] =  1.161157
#f_ca_map[4]['mu']["EG_SCALE_ALL__1down"] =  1.142413
#f_ca_map[5]['mu']["EG_SCALE_ALL__1down"] =  1.062087
## MUON_ID__1up 
#f_ca_map[2]['el']["MUON_ID__1up"] =  1.161077
#f_ca_map[3]['el']["MUON_ID__1up"] =  1.246688
#f_ca_map[4]['el']["MUON_ID__1up"] =  1.321600
#f_ca_map[5]['el']["MUON_ID__1up"] =  1.105715
#f_ca_map[2]['mu']["MUON_ID__1up"] =  1.176747
#f_ca_map[3]['mu']["MUON_ID__1up"] =  1.163365
#f_ca_map[4]['mu']["MUON_ID__1up"] =  1.136158
#f_ca_map[5]['mu']["MUON_ID__1up"] =  1.063287
## MUON_ID__1down 
#f_ca_map[2]['el']["MUON_ID__1down"] =  1.161074
#f_ca_map[3]['el']["MUON_ID__1down"] =  1.246691
#f_ca_map[4]['el']["MUON_ID__1down"] =  1.321590
#f_ca_map[5]['el']["MUON_ID__1down"] =  1.105722
#f_ca_map[2]['mu']["MUON_ID__1down"] =  1.176202
#f_ca_map[3]['mu']["MUON_ID__1down"] =  1.159592
#f_ca_map[4]['mu']["MUON_ID__1down"] =  1.143328
#f_ca_map[5]['mu']["MUON_ID__1down"] =  1.061789
## MUON_MS__1up 
#f_ca_map[2]['el']["MUON_MS__1up"] =  1.161075
#f_ca_map[3]['el']["MUON_MS__1up"] =  1.246688
#f_ca_map[4]['el']["MUON_MS__1up"] =  1.321595
#f_ca_map[5]['el']["MUON_MS__1up"] =  1.105716
#f_ca_map[2]['mu']["MUON_MS__1up"] =  1.178378
#f_ca_map[3]['mu']["MUON_MS__1up"] =  1.161161
#f_ca_map[4]['mu']["MUON_MS__1up"] =  1.141277
#f_ca_map[5]['mu']["MUON_MS__1up"] =  1.062713
## MUON_MS__1down 
#f_ca_map[2]['el']["MUON_MS__1down"] =  1.161067
#f_ca_map[3]['el']["MUON_MS__1down"] =  1.246693
#f_ca_map[4]['el']["MUON_MS__1down"] =  1.321586
#f_ca_map[5]['el']["MUON_MS__1down"] =  1.105740
#f_ca_map[2]['mu']["MUON_MS__1down"] =  1.179637
#f_ca_map[3]['mu']["MUON_MS__1down"] =  1.159506
#f_ca_map[4]['mu']["MUON_MS__1down"] =  1.141836
#f_ca_map[5]['mu']["MUON_MS__1down"] =  1.062235
## MUON_SCALE__1up 
#f_ca_map[2]['el']["MUON_SCALE__1up"] =  1.161067
#f_ca_map[3]['el']["MUON_SCALE__1up"] =  1.246693
#f_ca_map[4]['el']["MUON_SCALE__1up"] =  1.321591
#f_ca_map[5]['el']["MUON_SCALE__1up"] =  1.105718
#f_ca_map[2]['mu']["MUON_SCALE__1up"] =  1.179483
#f_ca_map[3]['mu']["MUON_SCALE__1up"] =  1.164134
#f_ca_map[4]['mu']["MUON_SCALE__1up"] =  1.143702
#f_ca_map[5]['mu']["MUON_SCALE__1up"] =  1.064143
## MUON_SCALE__1down 
#f_ca_map[2]['el']["MUON_SCALE__1down"] =  1.161074
#f_ca_map[3]['el']["MUON_SCALE__1down"] =  1.246693
#f_ca_map[4]['el']["MUON_SCALE__1down"] =  1.321595
#f_ca_map[5]['el']["MUON_SCALE__1down"] =  1.105716
#f_ca_map[2]['mu']["MUON_SCALE__1down"] =  1.174194
#f_ca_map[3]['mu']["MUON_SCALE__1down"] =  1.158466
#f_ca_map[4]['mu']["MUON_SCALE__1down"] =  1.139979
#f_ca_map[5]['mu']["MUON_SCALE__1down"] =  1.061695
## MUON_SAGITTA_RESBIAS__1up 
#f_ca_map[2]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.161069
#f_ca_map[3]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.246692
#f_ca_map[4]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.321595
#f_ca_map[5]['el']["MUON_SAGITTA_RESBIAS__1up"] =  1.105718
#f_ca_map[2]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  1.178331
#f_ca_map[3]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  1.161164
#f_ca_map[4]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  1.142417
#f_ca_map[5]['mu']["MUON_SAGITTA_RESBIAS__1up"] =  1.062010
## MUON_SAGITTA_RESBIAS__1down 
#f_ca_map[2]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.161069
#f_ca_map[3]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.246692
#f_ca_map[4]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.321595
#f_ca_map[5]['el']["MUON_SAGITTA_RESBIAS__1down"] =  1.105718
#f_ca_map[2]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  1.178331
#f_ca_map[3]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  1.161164
#f_ca_map[4]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  1.142417
#f_ca_map[5]['mu']["MUON_SAGITTA_RESBIAS__1down"] =  1.062010
## MUON_SAGITTA_RHO__1up 
#f_ca_map[2]['el']["MUON_SAGITTA_RHO__1up"] =  1.161069
#f_ca_map[3]['el']["MUON_SAGITTA_RHO__1up"] =  1.246692
#f_ca_map[4]['el']["MUON_SAGITTA_RHO__1up"] =  1.321595
#f_ca_map[5]['el']["MUON_SAGITTA_RHO__1up"] =  1.105718
#f_ca_map[2]['mu']["MUON_SAGITTA_RHO__1up"] =  1.178331
#f_ca_map[3]['mu']["MUON_SAGITTA_RHO__1up"] =  1.161164
#f_ca_map[4]['mu']["MUON_SAGITTA_RHO__1up"] =  1.142417
#f_ca_map[5]['mu']["MUON_SAGITTA_RHO__1up"] =  1.062010
## MUON_SAGITTA_RHO__1down 
#f_ca_map[2]['el']["MUON_SAGITTA_RHO__1down"] =  1.161069
#f_ca_map[3]['el']["MUON_SAGITTA_RHO__1down"] =  1.246692
#f_ca_map[4]['el']["MUON_SAGITTA_RHO__1down"] =  1.321595
#f_ca_map[5]['el']["MUON_SAGITTA_RHO__1down"] =  1.105718
#f_ca_map[2]['mu']["MUON_SAGITTA_RHO__1down"] =  1.178331
#f_ca_map[3]['mu']["MUON_SAGITTA_RHO__1down"] =  1.161164
#f_ca_map[4]['mu']["MUON_SAGITTA_RHO__1down"] =  1.142417
#f_ca_map[5]['mu']["MUON_SAGITTA_RHO__1down"] =  1.062010
## JET_JER_SINGLE_NP__1up 
#f_ca_map[2]['el']["JET_JER_SINGLE_NP__1up"] =  1.134675
#f_ca_map[3]['el']["JET_JER_SINGLE_NP__1up"] =  1.261534
#f_ca_map[4]['el']["JET_JER_SINGLE_NP__1up"] =  1.203325
#f_ca_map[5]['el']["JET_JER_SINGLE_NP__1up"] =  1.009480
#f_ca_map[2]['mu']["JET_JER_SINGLE_NP__1up"] =  1.106026
#f_ca_map[3]['mu']["JET_JER_SINGLE_NP__1up"] =  1.124754
#f_ca_map[4]['mu']["JET_JER_SINGLE_NP__1up"] =  1.167586
#f_ca_map[5]['mu']["JET_JER_SINGLE_NP__1up"] =  1.006819
## JET_21NP_JET_EtaIntercalibration_Modelling__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.159396
#f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.214052
#f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.293537
#f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.072783
#f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.165128
#f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.129411
#f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.113825
#f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1up"] =  1.044368
## JET_21NP_JET_EtaIntercalibration_Modelling__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.200187
#f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.273582
#f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.325761
#f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.138529
#f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.195131
#f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.181171
#f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.160346
#f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_Modelling__1down"] =  1.094926
## JET_21NP_JET_EtaIntercalibration_NonClosure__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.163055
#f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.263815
#f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.325448
#f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.099757
#f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.182204
#f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.162173
#f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.161528
#f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1up"] =  1.068537
## JET_21NP_JET_EtaIntercalibration_NonClosure__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.164420
#f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.243234
#f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.309622
#f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.101809
#f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.172755
#f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.159869
#f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.136067
#f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_NonClosure__1down"] =  1.056041
## JET_21NP_JET_EtaIntercalibration_TotalStat__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.148552
#f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.241985
#f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.295369
#f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.095486
#f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.166304
#f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.146998
#f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.145369
#f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1up"] =  1.048047
## JET_21NP_JET_EtaIntercalibration_TotalStat__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.169564
#f_ca_map[3]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.271821
#f_ca_map[4]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.335721
#f_ca_map[5]['el']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.111933
#f_ca_map[2]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.183340
#f_ca_map[3]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.171100
#f_ca_map[4]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.164472
#f_ca_map[5]['mu']["JET_21NP_JET_EtaIntercalibration_TotalStat__1down"] =  1.078925
## JET_21NP_JET_Flavor_Composition__1up 
#f_ca_map[2]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  1.068512
#f_ca_map[3]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  1.102384
#f_ca_map[4]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  1.157983
#f_ca_map[5]['el']["JET_21NP_JET_Flavor_Composition__1up"] =  0.955662
#f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  1.062918
#f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  1.064505
#f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  1.022950
#f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1up"] =  0.900911
## JET_21NP_JET_Flavor_Composition__1down 
#f_ca_map[2]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.309792
#f_ca_map[3]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.362154
#f_ca_map[4]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.419799
#f_ca_map[5]['el']["JET_21NP_JET_Flavor_Composition__1down"] =  1.270463
#f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.285138
#f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.309096
#f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.299627
#f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Composition__1down"] =  1.231899
## JET_21NP_JET_Flavor_Response__1up 
#f_ca_map[2]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.205944
#f_ca_map[3]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.285009
#f_ca_map[4]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.347299
#f_ca_map[5]['el']["JET_21NP_JET_Flavor_Response__1up"] =  1.150243
#f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  1.209064
#f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  1.204366
#f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  1.183375
#f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Response__1up"] =  1.104502
## JET_21NP_JET_Flavor_Response__1down 
#f_ca_map[2]['el']["JET_21NP_JET_Flavor_Response__1down"] =  1.138824
#f_ca_map[3]['el']["JET_21NP_JET_Flavor_Response__1down"] =  1.214119
#f_ca_map[4]['el']["JET_21NP_JET_Flavor_Response__1down"] =  1.283220
#f_ca_map[5]['el']["JET_21NP_JET_Flavor_Response__1down"] =  1.064249
#f_ca_map[2]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  1.143817
#f_ca_map[3]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  1.127129
#f_ca_map[4]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  1.102897
#f_ca_map[5]['mu']["JET_21NP_JET_Flavor_Response__1down"] =  1.020969
## JET_21NP_JET_Pileup_OffsetMu__1up 
#f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.162570
#f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.257667
#f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.318769
#f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.100415
#f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.176228
#f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.162382
#f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.143453
#f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1up"] =  1.062311
## JET_21NP_JET_Pileup_OffsetMu__1down 
#f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.158290
#f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.247172
#f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.322176
#f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.096166
#f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.176836
#f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.151115
#f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.150668
#f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetMu__1down"] =  1.059450
## JET_21NP_JET_Pileup_OffsetNPV__1up 
#f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.150585
#f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.237387
#f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.287804
#f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.084521
#f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.155470
#f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.145917
#f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.131868
#f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1up"] =  1.029182
## JET_21NP_JET_Pileup_OffsetNPV__1down 
#f_ca_map[2]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.179023
#f_ca_map[3]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.256141
#f_ca_map[4]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.310221
#f_ca_map[5]['el']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.128348
#f_ca_map[2]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.192498
#f_ca_map[3]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.184080
#f_ca_map[4]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.160213
#f_ca_map[5]['mu']["JET_21NP_JET_Pileup_OffsetNPV__1down"] =  1.076761
## JET_21NP_JET_Pileup_PtTerm__1up 
#f_ca_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.160565
#f_ca_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.251549
#f_ca_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.322986
#f_ca_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.106611
#f_ca_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.179780
#f_ca_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.160523
#f_ca_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.137184
#f_ca_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1up"] =  1.067077
## JET_21NP_JET_Pileup_PtTerm__1down 
#f_ca_map[2]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.168729
#f_ca_map[3]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.252828
#f_ca_map[4]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.322389
#f_ca_map[5]['el']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.104272
#f_ca_map[2]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.177569
#f_ca_map[3]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.161525
#f_ca_map[4]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.147051
#f_ca_map[5]['mu']["JET_21NP_JET_Pileup_PtTerm__1down"] =  1.059275
## JET_21NP_JET_Pileup_RhoTopology__1up 
#f_ca_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.105337
#f_ca_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.146028
#f_ca_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.217018
#f_ca_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  0.999734
#f_ca_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.106931
#f_ca_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.069415
#f_ca_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  1.065791
#f_ca_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1up"] =  0.954882
## JET_21NP_JET_Pileup_RhoTopology__1down 
#f_ca_map[2]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.269685
#f_ca_map[3]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.332399
#f_ca_map[4]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.405438
#f_ca_map[5]['el']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.218336
#f_ca_map[2]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.250241
#f_ca_map[3]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.260467
#f_ca_map[4]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.235378
#f_ca_map[5]['mu']["JET_21NP_JET_Pileup_RhoTopology__1down"] =  1.177829
## JET_21NP_JET_PunchThrough_MC15__1up 
#f_ca_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.160979
#f_ca_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.247063
#f_ca_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.321626
#f_ca_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.105869
#f_ca_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.178361
#f_ca_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.161147
#f_ca_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.142405
#f_ca_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1up"] =  1.061973
## JET_21NP_JET_PunchThrough_MC15__1down 
#f_ca_map[2]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.161066
#f_ca_map[3]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.246728
#f_ca_map[4]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.321671
#f_ca_map[5]['el']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.105707
#f_ca_map[2]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.178376
#f_ca_map[3]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.161135
#f_ca_map[4]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.142342
#f_ca_map[5]['mu']["JET_21NP_JET_PunchThrough_MC15__1down"] =  1.062198
## JET_21NP_JET_SingleParticle_HighPt__1up 
#f_ca_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.161069
#f_ca_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.246693
#f_ca_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.321596
#f_ca_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.105717
#f_ca_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.178331
#f_ca_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.161164
#f_ca_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.142416
#f_ca_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1up"] =  1.062026
## JET_21NP_JET_SingleParticle_HighPt__1down 
#f_ca_map[2]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.161069
#f_ca_map[3]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.246692
#f_ca_map[4]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.321595
#f_ca_map[5]['el']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.105718
#f_ca_map[2]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.178331
#f_ca_map[3]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.161164
#f_ca_map[4]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.142417
#f_ca_map[5]['mu']["JET_21NP_JET_SingleParticle_HighPt__1down"] =  1.062026
## JET_21NP_JET_BJES_Response__1up 
#f_ca_map[2]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.160316
#f_ca_map[3]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.245974
#f_ca_map[4]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.322339
#f_ca_map[5]['el']["JET_21NP_JET_BJES_Response__1up"] =  1.104393
#f_ca_map[2]['mu']["JET_21NP_JET_BJES_Response__1up"] =  1.179024
#f_ca_map[3]['mu']["JET_21NP_JET_BJES_Response__1up"] =  1.160703
#f_ca_map[4]['mu']["JET_21NP_JET_BJES_Response__1up"] =  1.142034
#f_ca_map[5]['mu']["JET_21NP_JET_BJES_Response__1up"] =  1.061160
## JET_21NP_JET_BJES_Response__1down 
#f_ca_map[2]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.161681
#f_ca_map[3]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.248866
#f_ca_map[4]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.323967
#f_ca_map[5]['el']["JET_21NP_JET_BJES_Response__1down"] =  1.106468
#f_ca_map[2]['mu']["JET_21NP_JET_BJES_Response__1down"] =  1.178600
#f_ca_map[3]['mu']["JET_21NP_JET_BJES_Response__1down"] =  1.162989
#f_ca_map[4]['mu']["JET_21NP_JET_BJES_Response__1down"] =  1.143851
#f_ca_map[5]['mu']["JET_21NP_JET_BJES_Response__1down"] =  1.063218
## JET_21NP_JET_EffectiveNP_1__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.123662
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.194025
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.250345
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.038630
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.131043
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.105134
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  1.085050
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1up"] =  0.988033
## JET_21NP_JET_EffectiveNP_1__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.223690
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.304274
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.386924
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.180729
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.218821
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.229004
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.208133
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_1__1down"] =  1.141101
## JET_21NP_JET_EffectiveNP_2__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.176998
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.267424
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.337350
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.119819
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.187928
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.173055
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.166960
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1up"] =  1.083174
## JET_21NP_JET_EffectiveNP_2__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.148631
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.234865
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.301526
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.084740
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.166131
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.143226
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.140836
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_2__1down"] =  1.043517
## JET_21NP_JET_EffectiveNP_3__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.157548
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.249946
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.316826
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.101521
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.176126
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.158013
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.142953
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1up"] =  1.059397
## JET_21NP_JET_EffectiveNP_3__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.161906
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.256764
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.329222
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.106104
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.179200
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.165276
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.144228
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_3__1down"] =  1.063056
## JET_21NP_JET_EffectiveNP_4__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.160671
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.253334
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.326950
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.105377
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.179899
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.161379
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.142632
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1up"] =  1.062027
## JET_21NP_JET_EffectiveNP_4__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.159964
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.249555
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.320551
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.102370
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.177407
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.158543
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.142585
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_4__1down"] =  1.060708
## JET_21NP_JET_EffectiveNP_5__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.162371
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.246672
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.324726
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.098926
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.178947
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.159699
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.145598
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1up"] =  1.061611
## JET_21NP_JET_EffectiveNP_5__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.157860
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.251698
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.321988
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.107343
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.176992
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.162080
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.140509
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_5__1down"] =  1.063035
## JET_21NP_JET_EffectiveNP_6__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.155000
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.250287
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.311914
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.103738
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.175196
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.159514
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.141975
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1up"] =  1.057674
## JET_21NP_JET_EffectiveNP_6__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.162625
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.252458
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.327716
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.108798
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.179798
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.163815
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.148756
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_6__1down"] =  1.063537
## JET_21NP_JET_EffectiveNP_7__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.161822
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.261078
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.329996
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.110038
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.180264
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.167360
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.148446
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1up"] =  1.065414
## JET_21NP_JET_EffectiveNP_7__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.155221
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.246331
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.313832
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.100468
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.173431
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.156764
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.142398
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_7__1down"] =  1.055166
## JET_21NP_JET_EffectiveNP_8restTerm__1up 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.157452
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.249529
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.318782
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.106149
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.176100
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.162379
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.141113
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1up"] =  1.061102
## JET_21NP_JET_EffectiveNP_8restTerm__1down 
#f_ca_map[2]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.162081
#f_ca_map[3]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.248045
#f_ca_map[4]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.326696
#f_ca_map[5]['el']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.103697
#f_ca_map[2]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.179417
#f_ca_map[3]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.161410
#f_ca_map[4]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.144579
#f_ca_map[5]['mu']["JET_21NP_JET_EffectiveNP_8restTerm__1down"] =  1.062455
## LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Split23__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_Tau32WTA__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Baseline_pT__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Split23__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_Tau32WTA__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Modelling_pT__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Split23__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_Tau32WTA__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_TotalStat_pT__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Split23__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_Tau32WTA__1down"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1up"] =  1.062010
## LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down 
#f_ca_map[2]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Weak_JET_Rtrk_Tracking_pT__1down"] =  1.062010
## LARGERJET_Medium_JET_Comb_Baseline_Kin__1up 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1up"] =  1.062010
## LARGERJET_Medium_JET_Comb_Baseline_Kin__1down 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Baseline_Kin__1down"] =  1.062010
## LARGERJET_Medium_JET_Comb_Modelling_Kin__1up 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1up"] =  1.062010
## LARGERJET_Medium_JET_Comb_Modelling_Kin__1down 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Modelling_Kin__1down"] =  1.062010
## LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up"] =  1.062010
## LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down"] =  1.062010
## LARGERJET_Medium_JET_Comb_Tracking_Kin__1up 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1up"] =  1.062010
## LARGERJET_Medium_JET_Comb_Tracking_Kin__1down 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Comb_Tracking_Kin__1down"] =  1.062010
## LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up"] =  1.062010
## LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down"] =  1.062010
## LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up"] =  1.062010
## LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down"] =  1.062010
## LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up"] =  1.062010
## LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down"] =  1.062010
## LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up"] =  1.062010
## LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down 
#f_ca_map[2]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down"] =  1.062010
## LARGERJET_Strong_JET_Comb_Baseline_All__1up 
#f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1up"] =  1.062010
## LARGERJET_Strong_JET_Comb_Baseline_All__1down 
#f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Baseline_All__1down"] =  1.062010
## LARGERJET_Strong_JET_Comb_Modelling_All__1up 
#f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1up"] =  1.062010
## LARGERJET_Strong_JET_Comb_Modelling_All__1down 
#f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Modelling_All__1down"] =  1.062010
## LARGERJET_Strong_JET_Comb_TotalStat_All__1up 
#f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1up"] =  1.062010
## LARGERJET_Strong_JET_Comb_TotalStat_All__1down 
#f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_TotalStat_All__1down"] =  1.062010
## LARGERJET_Strong_JET_Comb_Tracking_All__1up 
#f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1up"] =  1.062010
## LARGERJET_Strong_JET_Comb_Tracking_All__1down 
#f_ca_map[2]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.161069
#f_ca_map[3]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.246692
#f_ca_map[4]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.321595
#f_ca_map[5]['el']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.105718
#f_ca_map[2]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.178331
#f_ca_map[3]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.161164
#f_ca_map[4]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.142417
#f_ca_map[5]['mu']["LARGERJET_Strong_JET_Comb_Tracking_All__1down"] =  1.062010
#
#
## TTbarSyst_McHer 
#f_ca_map[2]['el']["ttgendw"] =  1.161221
#f_ca_map[3]['el']["ttgendw"] =  1.246647
#f_ca_map[4]['el']["ttgendw"] =  1.321738
#f_ca_map[5]['el']["ttgendw"] =  1.105607
#f_ca_map[2]['mu']["ttgendw"] =  1.178339
#f_ca_map[3]['mu']["ttgendw"] =  1.161106
#f_ca_map[4]['mu']["ttgendw"] =  1.142343
#f_ca_map[5]['mu']["ttgendw"] =  1.062042
## TTbarSyst_PowHer 
#f_ca_map[2]['el']["ttgenup"] =  1.161440
#f_ca_map[3]['el']["ttgenup"] =  1.246582
#f_ca_map[4]['el']["ttgenup"] =  1.321943
#f_ca_map[5]['el']["ttgenup"] =  1.105448
#f_ca_map[2]['mu']["ttgenup"] =  1.178317
#f_ca_map[3]['mu']["ttgenup"] =  1.161272
#f_ca_map[4]['mu']["ttgenup"] =  1.142555
#f_ca_map[5]['mu']["ttgenup"] =  1.061949
## TTbarSyst_radLo 
#f_ca_map[2]['el']["ttisrfsrup"] =  1.161319
#f_ca_map[3]['el']["ttisrfsrup"] =  1.246618
#f_ca_map[4]['el']["ttisrfsrup"] =  1.321830
#f_ca_map[5]['el']["ttisrfsrup"] =  1.105536
#f_ca_map[2]['mu']["ttisrfsrup"] =  1.178391
#f_ca_map[3]['mu']["ttisrfsrup"] =  1.160703
#f_ca_map[4]['mu']["ttisrfsrup"] =  1.141824
#f_ca_map[5]['mu']["ttisrfsrup"] =  1.062270
## TTBarSyst_radHi 
#f_ca_map[2]['el']["ttisrfsrdw"] =  1.161102
#f_ca_map[3]['el']["ttisrfsrdw"] =  1.246682
#f_ca_map[4]['el']["ttisrfsrdw"] =  1.321627
#f_ca_map[5]['el']["ttisrfsrdw"] =  1.105693
#f_ca_map[2]['mu']["ttisrfsrdw"] =  1.178289
#f_ca_map[3]['mu']["ttisrfsrdw"] =  1.161487
#f_ca_map[4]['mu']["ttisrfsrdw"] =  1.142831
#f_ca_map[5]['mu']["ttisrfsrdw"] =  1.061829
#
## TTbarSyst_McHer 
#frac[2]['el']["ttgendw"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["ttgendw"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["ttgendw"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["ttgendw"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["ttgendw"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["ttgendw"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["ttgendw"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["ttgendw"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## TTbarSyst_PowHer 
#frac[2]['el']["ttgenup"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["ttgenup"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["ttgenup"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["ttgenup"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["ttgenup"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["ttgenup"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["ttgenup"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["ttgenup"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## TTbarSyst_radLo 
#frac[2]['el']["ttisrfsrup"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["ttisrfsrup"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["ttisrfsrup"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["ttisrfsrup"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["ttisrfsrup"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["ttisrfsrup"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["ttisrfsrup"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["ttisrfsrup"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## TTBarSyst_radHi 
#frac[2]['el']["ttisrfsrdw"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["ttisrfsrdw"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["ttisrfsrdw"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["ttisrfsrdw"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["ttisrfsrdw"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["ttisrfsrdw"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["ttisrfsrdw"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["ttisrfsrdw"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
#
## TTbarSyst_McHer 
#flav_map[2]['el']["ttgendw"] = {'bb': 1.416203, 'cc': 1.416203, 'c': 1.000000, 'l': 0.896367}
#flav_map[3]['el']["ttgendw"] = {'bb': 1.373617, 'cc': 1.373617, 'c': 0.969930, 'l': 0.869413}
#flav_map[4]['el']["ttgendw"] = {'bb': 1.332947, 'cc': 1.332947, 'c': 0.941212, 'l': 0.843671}
#flav_map[5]['el']["ttgendw"] = {'bb': 1.289855, 'cc': 1.289855, 'c': 0.910784, 'l': 0.816397}
#flav_map[2]['mu']["ttgendw"] = {'bb': 1.550960, 'cc': 1.550960, 'c': 1.000000, 'l': 0.876323}
#flav_map[3]['mu']["ttgendw"] = {'bb': 1.492025, 'cc': 1.492025, 'c': 0.962001, 'l': 0.843024}
#flav_map[4]['mu']["ttgendw"] = {'bb': 1.438769, 'cc': 1.438769, 'c': 0.927664, 'l': 0.812933}
#flav_map[5]['mu']["ttgendw"] = {'bb': 1.373885, 'cc': 1.373885, 'c': 0.885829, 'l': 0.776273}
## TTbarSyst_PowHer 
#flav_map[2]['el']["ttgenup"] = {'bb': 1.434626, 'cc': 1.434626, 'c': 1.000000, 'l': 0.891780}
#flav_map[3]['el']["ttgenup"] = {'bb': 1.389636, 'cc': 1.389636, 'c': 0.968640, 'l': 0.863814}
#flav_map[4]['el']["ttgenup"] = {'bb': 1.346782, 'cc': 1.346782, 'c': 0.938769, 'l': 0.837175}
#flav_map[5]['el']["ttgenup"] = {'bb': 1.301494, 'cc': 1.301494, 'c': 0.907201, 'l': 0.809024}
#flav_map[2]['mu']["ttgenup"] = {'bb': 1.561602, 'cc': 1.561602, 'c': 1.000000, 'l': 0.873935}
#flav_map[3]['mu']["ttgenup"] = {'bb': 1.501161, 'cc': 1.501161, 'c': 0.961296, 'l': 0.840109}
#flav_map[4]['mu']["ttgenup"] = {'bb': 1.446620, 'cc': 1.446620, 'c': 0.926369, 'l': 0.809586}
#flav_map[5]['mu']["ttgenup"] = {'bb': 1.380268, 'cc': 1.380268, 'c': 0.883880, 'l': 0.772453}
## TTbarSyst_radLo 
#flav_map[2]['el']["ttisrfsrup"] = {'bb': 1.424419, 'cc': 1.424419, 'c': 1.000000, 'l': 0.894321}
#flav_map[3]['el']["ttisrfsrup"] = {'bb': 1.380767, 'cc': 1.380767, 'c': 0.969354, 'l': 0.866914}
#flav_map[4]['el']["ttisrfsrup"] = {'bb': 1.339126, 'cc': 1.339126, 'c': 0.940121, 'l': 0.840770}
#flav_map[5]['el']["ttisrfsrup"] = {'bb': 1.295057, 'cc': 1.295057, 'c': 0.909183, 'l': 0.813101}
#flav_map[2]['mu']["ttisrfsrup"] = {'bb': 1.525100, 'cc': 1.525100, 'c': 1.000000, 'l': 0.882128}
#flav_map[3]['mu']["ttisrfsrup"] = {'bb': 1.469769, 'cc': 1.469769, 'c': 0.963720, 'l': 0.850124}
#flav_map[4]['mu']["ttisrfsrup"] = {'bb': 1.419600, 'cc': 1.419600, 'c': 0.930824, 'l': 0.821106}
#flav_map[5]['mu']["ttisrfsrup"] = {'bb': 1.358257, 'cc': 1.358257, 'c': 0.890602, 'l': 0.785625}
## TTBarSyst_radHi 
#flav_map[2]['el']["ttisrfsrdw"] = {'bb': 1.406258, 'cc': 1.406258, 'c': 1.000000, 'l': 0.898843}
#flav_map[3]['el']["ttisrfsrdw"] = {'bb': 1.364952, 'cc': 1.364952, 'c': 0.970627, 'l': 0.872442}
#flav_map[4]['el']["ttisrfsrdw"] = {'bb': 1.325448, 'cc': 1.325448, 'c': 0.942536, 'l': 0.847192}
#flav_map[5]['el']["ttisrfsrdw"] = {'bb': 1.283533, 'cc': 1.283533, 'c': 0.912730, 'l': 0.820401}
#flav_map[2]['mu']["ttisrfsrdw"] = {'bb': 1.575480, 'cc': 1.575480, 'c': 1.000000, 'l': 0.870819}
#flav_map[3]['mu']["ttisrfsrdw"] = {'bb': 1.513055, 'cc': 1.513055, 'c': 0.960377, 'l': 0.836315}
#flav_map[4]['mu']["ttisrfsrdw"] = {'bb': 1.456825, 'cc': 1.456825, 'c': 0.924687, 'l': 0.805235}
#flav_map[5]['mu']["ttisrfsrdw"] = {'bb': 1.388551, 'cc': 1.388551, 'c': 0.881351, 'l': 0.767497}
#
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_0"] =  1.161203
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_0"] =  1.246653
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_0"] =  1.321721
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_0"] =  1.105620
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_0"] =  1.178333
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_0"] =  1.161149
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_0"] =  1.142397
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_0"] =  1.062018
## pdf_PDF4LHC15_nlo_30_1 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_1"] =  1.161194
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_1"] =  1.246655
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_1"] =  1.321713
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_1"] =  1.105626
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_1"] =  1.178333
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_1"] =  1.161148
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_1"] =  1.142396
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_1"] =  1.062019
## pdf_PDF4LHC15_nlo_30_2 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_2"] =  1.161182
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_2"] =  1.246659
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_2"] =  1.321701
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_2"] =  1.105635
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_2"] =  1.178336
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_2"] =  1.161122
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_2"] =  1.142364
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_2"] =  1.062033
## pdf_PDF4LHC15_nlo_30_3 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_3"] =  1.161202
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_3"] =  1.246653
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_3"] =  1.321720
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_3"] =  1.105620
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_3"] =  1.178328
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_3"] =  1.161183
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_3"] =  1.142441
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_3"] =  1.061999
## pdf_PDF4LHC15_nlo_30_4 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_4"] =  1.161196
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_4"] =  1.246655
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_4"] =  1.321715
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_4"] =  1.105624
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_4"] =  1.178339
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_4"] =  1.161108
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_4"] =  1.142345
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_4"] =  1.062041
## pdf_PDF4LHC15_nlo_30_5 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_5"] =  1.161198
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_5"] =  1.246654
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_5"] =  1.321716
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_5"] =  1.105623
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_5"] =  1.178335
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_5"] =  1.161134
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_5"] =  1.142379
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_5"] =  1.062026
## pdf_PDF4LHC15_nlo_30_6 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_6"] =  1.161204
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_6"] =  1.246653
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_6"] =  1.321722
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_6"] =  1.105619
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_6"] =  1.178335
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_6"] =  1.161134
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_6"] =  1.142379
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_6"] =  1.062026
## pdf_PDF4LHC15_nlo_30_7 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_7"] =  1.161194
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_7"] =  1.246655
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_7"] =  1.321713
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_7"] =  1.105626
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_7"] =  1.178333
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_7"] =  1.161143
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_7"] =  1.142391
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_7"] =  1.062021
## pdf_PDF4LHC15_nlo_30_8 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_8"] =  1.161209
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_8"] =  1.246651
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_8"] =  1.321727
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_8"] =  1.105615
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_8"] =  1.178329
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_8"] =  1.161174
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_8"] =  1.142430
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_8"] =  1.062004
## pdf_PDF4LHC15_nlo_30_9 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_9"] =  1.161207
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_9"] =  1.246652
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_9"] =  1.321725
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_9"] =  1.105617
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_9"] =  1.178333
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_9"] =  1.161145
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_9"] =  1.142392
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_9"] =  1.062020
## pdf_PDF4LHC15_nlo_30_10 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_10"] =  1.161241
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_10"] =  1.246642
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_10"] =  1.321757
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_10"] =  1.105592
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_10"] =  1.178331
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_10"] =  1.161162
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_10"] =  1.142414
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_10"] =  1.062011
## pdf_PDF4LHC15_nlo_30_11 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_11"] =  1.161207
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_11"] =  1.246651
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_11"] =  1.321725
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_11"] =  1.105617
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_11"] =  1.178333
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_11"] =  1.161150
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_11"] =  1.142399
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_11"] =  1.062017
## pdf_PDF4LHC15_nlo_30_12 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_12"] =  1.161209
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_12"] =  1.246651
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_12"] =  1.321727
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_12"] =  1.105615
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_12"] =  1.178331
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_12"] =  1.161161
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_12"] =  1.142414
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_12"] =  1.062011
## pdf_PDF4LHC15_nlo_30_13 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_13"] =  1.161202
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_13"] =  1.246653
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_13"] =  1.321721
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_13"] =  1.105620
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_13"] =  1.178340
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_13"] =  1.161090
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_13"] =  1.142323
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_13"] =  1.062051
## pdf_PDF4LHC15_nlo_30_14 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_14"] =  1.161200
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_14"] =  1.246653
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_14"] =  1.321719
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_14"] =  1.105622
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_14"] =  1.178334
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_14"] =  1.161138
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_14"] =  1.142383
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_14"] =  1.062024
## pdf_PDF4LHC15_nlo_30_15 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_15"] =  1.161205
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_15"] =  1.246652
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_15"] =  1.321723
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_15"] =  1.105618
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_15"] =  1.178333
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_15"] =  1.161148
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_15"] =  1.142396
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_15"] =  1.062019
## pdf_PDF4LHC15_nlo_30_16 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_16"] =  1.161212
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_16"] =  1.246650
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_16"] =  1.321729
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_16"] =  1.105613
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_16"] =  1.178336
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_16"] =  1.161124
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_16"] =  1.142366
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_16"] =  1.062032
## pdf_PDF4LHC15_nlo_30_17 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_17"] =  1.161197
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_17"] =  1.246655
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_17"] =  1.321715
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_17"] =  1.105624
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_17"] =  1.178333
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_17"] =  1.161150
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_17"] =  1.142399
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_17"] =  1.062018
## pdf_PDF4LHC15_nlo_30_18 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_18"] =  1.161200
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_18"] =  1.246653
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_18"] =  1.321719
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_18"] =  1.105622
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_18"] =  1.178332
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_18"] =  1.161162
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_18"] =  1.142414
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_18"] =  1.062011
## pdf_PDF4LHC15_nlo_30_19 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_19"] =  1.161208
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_19"] =  1.246651
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_19"] =  1.321726
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_19"] =  1.105616
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_19"] =  1.178331
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_19"] =  1.161164
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_19"] =  1.142416
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_19"] =  1.062010
## pdf_PDF4LHC15_nlo_30_20 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_20"] =  1.161216
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_20"] =  1.246649
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_20"] =  1.321733
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_20"] =  1.105611
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_20"] =  1.178332
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_20"] =  1.161155
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_20"] =  1.142405
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_20"] =  1.062015
## pdf_PDF4LHC15_nlo_30_21 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_21"] =  1.161199
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_21"] =  1.246654
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_21"] =  1.321718
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_21"] =  1.105622
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_21"] =  1.178333
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_21"] =  1.161145
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_21"] =  1.142392
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_21"] =  1.062020
## pdf_PDF4LHC15_nlo_30_22 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_22"] =  1.161207
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_22"] =  1.246652
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_22"] =  1.321724
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_22"] =  1.105617
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_22"] =  1.178331
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_22"] =  1.161164
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_22"] =  1.142417
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_22"] =  1.062010
## pdf_PDF4LHC15_nlo_30_23 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_23"] =  1.161173
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_23"] =  1.246662
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_23"] =  1.321693
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_23"] =  1.105642
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_23"] =  1.178331
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_23"] =  1.161162
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_23"] =  1.142414
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_23"] =  1.062011
## pdf_PDF4LHC15_nlo_30_24 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_24"] =  1.161192
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_24"] =  1.246656
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_24"] =  1.321710
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_24"] =  1.105628
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_24"] =  1.178332
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_24"] =  1.161155
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_24"] =  1.142405
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_24"] =  1.062015
## pdf_PDF4LHC15_nlo_30_25 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_25"] =  1.161202
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_25"] =  1.246653
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_25"] =  1.321720
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_25"] =  1.105621
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_25"] =  1.178334
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_25"] =  1.161146
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_25"] =  1.142394
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_25"] =  1.062019
## pdf_PDF4LHC15_nlo_30_26 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_26"] =  1.161200
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_26"] =  1.246653
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_26"] =  1.321719
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_26"] =  1.105622
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_26"] =  1.178333
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_26"] =  1.161150
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_26"] =  1.142399
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_26"] =  1.062018
## pdf_PDF4LHC15_nlo_30_27 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_27"] =  1.161203
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_27"] =  1.246653
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_27"] =  1.321721
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_27"] =  1.105620
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_27"] =  1.178332
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_27"] =  1.161153
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_27"] =  1.142402
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_27"] =  1.062016
## pdf_PDF4LHC15_nlo_30_28 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_28"] =  1.161194
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_28"] =  1.246655
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_28"] =  1.321713
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_28"] =  1.105626
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_28"] =  1.178333
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_28"] =  1.161142
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_28"] =  1.142389
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_28"] =  1.062022
## pdf_PDF4LHC15_nlo_30_29 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_29"] =  1.161204
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_29"] =  1.246652
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_29"] =  1.321722
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_29"] =  1.105619
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_29"] =  1.178332
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_29"] =  1.161156
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_29"] =  1.142407
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_29"] =  1.062014
## pdf_PDF4LHC15_nlo_30_30 
#f_ca_map[2]['el']["pdf_PDF4LHC15_nlo_30_30"] =  1.161202
#f_ca_map[3]['el']["pdf_PDF4LHC15_nlo_30_30"] =  1.246653
#f_ca_map[4]['el']["pdf_PDF4LHC15_nlo_30_30"] =  1.321721
#f_ca_map[5]['el']["pdf_PDF4LHC15_nlo_30_30"] =  1.105620
#f_ca_map[2]['mu']["pdf_PDF4LHC15_nlo_30_30"] =  1.178334
#f_ca_map[3]['mu']["pdf_PDF4LHC15_nlo_30_30"] =  1.161140
#f_ca_map[4]['mu']["pdf_PDF4LHC15_nlo_30_30"] =  1.142386
#f_ca_map[5]['mu']["pdf_PDF4LHC15_nlo_30_30"] =  1.062023
#
## pdf_PDF4LHC15_nlo_30_0 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_1 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_2 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_3 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_4 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_5 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_6 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_7 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_8 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_9 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_10 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_11 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_12 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_13 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_14 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_15 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_16 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_17 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_18 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_19 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_20 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_21 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_22 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_23 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_24 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_25 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_26 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_27 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_28 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_29 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
## pdf_PDF4LHC15_nlo_30_30 
#frac[2]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.093916,'cc': 0.063787,'c': 0.208945,'l': 0.633352}
#frac[3]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.117127,'cc': 0.098185,'c': 0.219124,'l': 0.565564}
#frac[4]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.139564,'cc': 0.136938,'c': 0.215736,'l': 0.507762}
#frac[5]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.147172,'cc': 0.149155,'c': 0.210933,'l': 0.492740}
#frac[2]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.083058,'cc': 0.062701,'c': 0.204911,'l': 0.649330}
#frac[3]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.105982,'cc': 0.096368,'c': 0.215590,'l': 0.582059}
#frac[4]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.128953,'cc': 0.131889,'c': 0.207636,'l': 0.531522}
#frac[5]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 0.138052,'cc': 0.144177,'c': 0.203654,'l': 0.514117}
#
## pdf_PDF4LHC15_nlo_30_0 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.414658, 'cc': 1.414658, 'c': 1.000000, 'l': 0.896751}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.372272, 'cc': 1.372272, 'c': 0.970038, 'l': 0.869883}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.331783, 'cc': 1.331783, 'c': 0.941417, 'l': 0.844217}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.288875, 'cc': 1.288875, 'c': 0.911086, 'l': 0.817018}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.553709, 'cc': 1.553709, 'c': 1.000000, 'l': 0.875705}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.494387, 'cc': 1.494387, 'c': 0.961819, 'l': 0.842270}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.440800, 'cc': 1.440800, 'c': 0.927329, 'l': 0.812067}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_0"] = {'bb': 1.375537, 'cc': 1.375537, 'c': 0.885325, 'l': 0.775284}
## pdf_PDF4LHC15_nlo_30_1 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.413967, 'cc': 1.413967, 'c': 1.000000, 'l': 0.896924}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.371670, 'cc': 1.371670, 'c': 0.970087, 'l': 0.870093}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.331263, 'cc': 1.331263, 'c': 0.941509, 'l': 0.844462}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.288436, 'cc': 1.288436, 'c': 0.911221, 'l': 0.817295}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.553646, 'cc': 1.553646, 'c': 1.000000, 'l': 0.875720}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.494332, 'cc': 1.494332, 'c': 0.961823, 'l': 0.842288}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.440753, 'cc': 1.440753, 'c': 0.927336, 'l': 0.812087}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_1"] = {'bb': 1.375499, 'cc': 1.375499, 'c': 0.885336, 'l': 0.775307}
## pdf_PDF4LHC15_nlo_30_2 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.412922, 'cc': 1.412922, 'c': 1.000000, 'l': 0.897184}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.370760, 'cc': 1.370760, 'c': 0.970160, 'l': 0.870412}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.330475, 'cc': 1.330475, 'c': 0.941648, 'l': 0.844832}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.287772, 'cc': 1.287772, 'c': 0.911425, 'l': 0.817716}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.552015, 'cc': 1.552015, 'c': 1.000000, 'l': 0.876086}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.492932, 'cc': 1.492932, 'c': 0.961931, 'l': 0.842735}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.439549, 'cc': 1.439549, 'c': 0.927535, 'l': 0.812601}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_2"] = {'bb': 1.374520, 'cc': 1.374520, 'c': 0.885635, 'l': 0.775893}
## pdf_PDF4LHC15_nlo_30_3 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.414619, 'cc': 1.414619, 'c': 1.000000, 'l': 0.896761}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.372239, 'cc': 1.372239, 'c': 0.970041, 'l': 0.869895}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.331755, 'cc': 1.331755, 'c': 0.941422, 'l': 0.844231}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.288850, 'cc': 1.288850, 'c': 0.911093, 'l': 0.817033}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.555917, 'cc': 1.555917, 'c': 1.000000, 'l': 0.875211}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.496282, 'cc': 1.496282, 'c': 0.961672, 'l': 0.841666}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.442429, 'cc': 1.442429, 'c': 0.927060, 'l': 0.811373}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_3"] = {'bb': 1.376862, 'cc': 1.376862, 'c': 0.884920, 'l': 0.774491}
## pdf_PDF4LHC15_nlo_30_4 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.414148, 'cc': 1.414148, 'c': 1.000000, 'l': 0.896879}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.371828, 'cc': 1.371828, 'c': 0.970074, 'l': 0.870038}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.331399, 'cc': 1.331399, 'c': 0.941485, 'l': 0.844398}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.288551, 'cc': 1.288551, 'c': 0.911185, 'l': 0.817223}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.551065, 'cc': 1.551065, 'c': 1.000000, 'l': 0.876299}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.492116, 'cc': 1.492116, 'c': 0.961994, 'l': 0.842995}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.438847, 'cc': 1.438847, 'c': 0.927651, 'l': 0.812900}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_4"] = {'bb': 1.373949, 'cc': 1.373949, 'c': 0.885810, 'l': 0.776234}
## pdf_PDF4LHC15_nlo_30_5 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.414274, 'cc': 1.414274, 'c': 1.000000, 'l': 0.896847}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.371938, 'cc': 1.371938, 'c': 0.970065, 'l': 0.870000}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.331495, 'cc': 1.331495, 'c': 0.941468, 'l': 0.844353}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.288631, 'cc': 1.288631, 'c': 0.911161, 'l': 0.817172}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.552774, 'cc': 1.552774, 'c': 1.000000, 'l': 0.875916}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.493584, 'cc': 1.493584, 'c': 0.961881, 'l': 0.842526}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.440109, 'cc': 1.440109, 'c': 0.927443, 'l': 0.812362}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_5"] = {'bb': 1.374976, 'cc': 1.374976, 'c': 0.885496, 'l': 0.775620}
## pdf_PDF4LHC15_nlo_30_6 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.414745, 'cc': 1.414745, 'c': 1.000000, 'l': 0.896729}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.372348, 'cc': 1.372348, 'c': 0.970032, 'l': 0.869856}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.331849, 'cc': 1.331849, 'c': 0.941406, 'l': 0.844186}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.288930, 'cc': 1.288930, 'c': 0.911069, 'l': 0.816982}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.552781, 'cc': 1.552781, 'c': 1.000000, 'l': 0.875914}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.493590, 'cc': 1.493590, 'c': 0.961880, 'l': 0.842525}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.440114, 'cc': 1.440114, 'c': 0.927442, 'l': 0.812359}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_6"] = {'bb': 1.374980, 'cc': 1.374980, 'c': 0.885495, 'l': 0.775618}
## pdf_PDF4LHC15_nlo_30_7 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.414013, 'cc': 1.414013, 'c': 1.000000, 'l': 0.896913}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.371710, 'cc': 1.371710, 'c': 0.970083, 'l': 0.870080}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.331297, 'cc': 1.331297, 'c': 0.941503, 'l': 0.844446}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.288465, 'cc': 1.288465, 'c': 0.911212, 'l': 0.817277}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.553367, 'cc': 1.553367, 'c': 1.000000, 'l': 0.875783}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.494092, 'cc': 1.494092, 'c': 0.961841, 'l': 0.842364}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.440546, 'cc': 1.440546, 'c': 0.927370, 'l': 0.812175}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_7"] = {'bb': 1.375331, 'cc': 1.375331, 'c': 0.885387, 'l': 0.775407}
## pdf_PDF4LHC15_nlo_30_8 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.415241, 'cc': 1.415241, 'c': 1.000000, 'l': 0.896606}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.372780, 'cc': 1.372780, 'c': 0.969997, 'l': 0.869706}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.332223, 'cc': 1.332223, 'c': 0.941340, 'l': 0.844011}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.289245, 'cc': 1.289245, 'c': 0.910972, 'l': 0.816783}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.555341, 'cc': 1.555341, 'c': 1.000000, 'l': 0.875340}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.495788, 'cc': 1.495788, 'c': 0.961711, 'l': 0.841824}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.442004, 'cc': 1.442004, 'c': 0.927130, 'l': 0.811554}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_8"] = {'bb': 1.376516, 'cc': 1.376516, 'c': 0.885026, 'l': 0.774698}
## pdf_PDF4LHC15_nlo_30_9 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.415003, 'cc': 1.415003, 'c': 1.000000, 'l': 0.896666}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.372573, 'cc': 1.372573, 'c': 0.970014, 'l': 0.869778}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.332043, 'cc': 1.332043, 'c': 0.941371, 'l': 0.844095}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.289094, 'cc': 1.289094, 'c': 0.911018, 'l': 0.816879}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.553455, 'cc': 1.553455, 'c': 1.000000, 'l': 0.875763}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.494169, 'cc': 1.494169, 'c': 0.961836, 'l': 0.842340}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.440612, 'cc': 1.440612, 'c': 0.927360, 'l': 0.812147}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_9"] = {'bb': 1.375385, 'cc': 1.375385, 'c': 0.885371, 'l': 0.775375}
## pdf_PDF4LHC15_nlo_30_10 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.417860, 'cc': 1.417860, 'c': 1.000000, 'l': 0.895954}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.375060, 'cc': 1.375060, 'c': 0.969814, 'l': 0.868909}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.334194, 'cc': 1.334194, 'c': 0.940992, 'l': 0.843085}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.290906, 'cc': 1.290906, 'c': 0.910461, 'l': 0.815731}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.554552, 'cc': 1.554552, 'c': 1.000000, 'l': 0.875517}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.495111, 'cc': 1.495111, 'c': 0.961763, 'l': 0.842039}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.441422, 'cc': 1.441422, 'c': 0.927226, 'l': 0.811802}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_10"] = {'bb': 1.376043, 'cc': 1.376043, 'c': 0.885170, 'l': 0.774981}
## pdf_PDF4LHC15_nlo_30_11 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.415031, 'cc': 1.415031, 'c': 1.000000, 'l': 0.896658}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.372597, 'cc': 1.372597, 'c': 0.970012, 'l': 0.869769}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.332065, 'cc': 1.332065, 'c': 0.941368, 'l': 0.844085}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.289112, 'cc': 1.289112, 'c': 0.911013, 'l': 0.816867}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.553774, 'cc': 1.553774, 'c': 1.000000, 'l': 0.875691}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.494442, 'cc': 1.494442, 'c': 0.961815, 'l': 0.842253}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.440847, 'cc': 1.440847, 'c': 0.927321, 'l': 0.812047}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_11"] = {'bb': 1.375576, 'cc': 1.375576, 'c': 0.885313, 'l': 0.775261}
## pdf_PDF4LHC15_nlo_30_12 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.415220, 'cc': 1.415220, 'c': 1.000000, 'l': 0.896612}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.372762, 'cc': 1.372762, 'c': 0.969999, 'l': 0.869712}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.332207, 'cc': 1.332207, 'c': 0.941342, 'l': 0.844019}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.289231, 'cc': 1.289231, 'c': 0.910976, 'l': 0.816792}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.554523, 'cc': 1.554523, 'c': 1.000000, 'l': 0.875524}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.495085, 'cc': 1.495085, 'c': 0.961765, 'l': 0.842048}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.441400, 'cc': 1.441400, 'c': 0.927230, 'l': 0.811812}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_12"] = {'bb': 1.376025, 'cc': 1.376025, 'c': 0.885176, 'l': 0.774992}
## pdf_PDF4LHC15_nlo_30_13 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.414648, 'cc': 1.414648, 'c': 1.000000, 'l': 0.896754}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.372263, 'cc': 1.372263, 'c': 0.970039, 'l': 0.869886}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.331776, 'cc': 1.331776, 'c': 0.941418, 'l': 0.844221}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.288868, 'cc': 1.288868, 'c': 0.911088, 'l': 0.817022}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.549958, 'cc': 1.549958, 'c': 1.000000, 'l': 0.876548}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.491165, 'cc': 1.491165, 'c': 0.962068, 'l': 0.843298}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.438029, 'cc': 1.438029, 'c': 0.927786, 'l': 0.813249}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_13"] = {'bb': 1.373283, 'cc': 1.373283, 'c': 0.886013, 'l': 0.776633}
## pdf_PDF4LHC15_nlo_30_14 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.414474, 'cc': 1.414474, 'c': 1.000000, 'l': 0.896797}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.372112, 'cc': 1.372112, 'c': 0.970051, 'l': 0.869939}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.331645, 'cc': 1.331645, 'c': 0.941442, 'l': 0.844282}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.288758, 'cc': 1.288758, 'c': 0.911122, 'l': 0.817091}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.552998, 'cc': 1.552998, 'c': 1.000000, 'l': 0.875866}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.493776, 'cc': 1.493776, 'c': 0.961866, 'l': 0.842465}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.440274, 'cc': 1.440274, 'c': 0.927415, 'l': 0.812291}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_14"] = {'bb': 1.375110, 'cc': 1.375110, 'c': 0.885455, 'l': 0.775540}
## pdf_PDF4LHC15_nlo_30_15 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.414864, 'cc': 1.414864, 'c': 1.000000, 'l': 0.896700}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.372452, 'cc': 1.372452, 'c': 0.970024, 'l': 0.869820}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.331939, 'cc': 1.331939, 'c': 0.941390, 'l': 0.844144}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.289005, 'cc': 1.289005, 'c': 0.911046, 'l': 0.816935}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.553646, 'cc': 1.553646, 'c': 1.000000, 'l': 0.875720}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.494333, 'cc': 1.494333, 'c': 0.961823, 'l': 0.842288}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.440753, 'cc': 1.440753, 'c': 0.927337, 'l': 0.812087}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_15"] = {'bb': 1.375499, 'cc': 1.375499, 'c': 0.885336, 'l': 0.775307}
## pdf_PDF4LHC15_nlo_30_16 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.415434, 'cc': 1.415434, 'c': 1.000000, 'l': 0.896558}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.372948, 'cc': 1.372948, 'c': 0.969984, 'l': 0.869647}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.332368, 'cc': 1.332368, 'c': 0.941314, 'l': 0.843943}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.289367, 'cc': 1.289367, 'c': 0.910934, 'l': 0.816706}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.552126, 'cc': 1.552126, 'c': 1.000000, 'l': 0.876061}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.493027, 'cc': 1.493027, 'c': 0.961924, 'l': 0.842704}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.439630, 'cc': 1.439630, 'c': 0.927522, 'l': 0.812566}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_16"] = {'bb': 1.374586, 'cc': 1.374586, 'c': 0.885615, 'l': 0.775853}
## pdf_PDF4LHC15_nlo_30_17 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.414171, 'cc': 1.414171, 'c': 1.000000, 'l': 0.896873}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.371848, 'cc': 1.371848, 'c': 0.970072, 'l': 0.870031}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.331417, 'cc': 1.331417, 'c': 0.941482, 'l': 0.844389}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.288566, 'cc': 1.288566, 'c': 0.911181, 'l': 0.817213}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.553764, 'cc': 1.553764, 'c': 1.000000, 'l': 0.875693}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.494434, 'cc': 1.494434, 'c': 0.961815, 'l': 0.842255}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.440840, 'cc': 1.440840, 'c': 0.927322, 'l': 0.812050}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_17"] = {'bb': 1.375570, 'cc': 1.375570, 'c': 0.885315, 'l': 0.775264}
## pdf_PDF4LHC15_nlo_30_18 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.414474, 'cc': 1.414474, 'c': 1.000000, 'l': 0.896797}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.372112, 'cc': 1.372112, 'c': 0.970051, 'l': 0.869939}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.331645, 'cc': 1.331645, 'c': 0.941442, 'l': 0.844282}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.288758, 'cc': 1.288758, 'c': 0.911122, 'l': 0.817091}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.554543, 'cc': 1.554543, 'c': 1.000000, 'l': 0.875518}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.495104, 'cc': 1.495104, 'c': 0.961764, 'l': 0.842042}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.441416, 'cc': 1.441416, 'c': 0.927228, 'l': 0.811805}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_18"] = {'bb': 1.376038, 'cc': 1.376038, 'c': 0.885172, 'l': 0.774984}
## pdf_PDF4LHC15_nlo_30_19 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.415089, 'cc': 1.415089, 'c': 1.000000, 'l': 0.896644}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.372647, 'cc': 1.372647, 'c': 0.970008, 'l': 0.869752}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.332108, 'cc': 1.332108, 'c': 0.941360, 'l': 0.844065}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.289148, 'cc': 1.289148, 'c': 0.911002, 'l': 0.816844}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.554652, 'cc': 1.554652, 'c': 1.000000, 'l': 0.875494}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.495197, 'cc': 1.495197, 'c': 0.961756, 'l': 0.842012}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.441496, 'cc': 1.441496, 'c': 0.927214, 'l': 0.811771}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_19"] = {'bb': 1.376103, 'cc': 1.376103, 'c': 0.885152, 'l': 0.774945}
## pdf_PDF4LHC15_nlo_30_20 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.415764, 'cc': 1.415764, 'c': 1.000000, 'l': 0.896475}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.373236, 'cc': 1.373236, 'c': 0.969961, 'l': 0.869546}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.332617, 'cc': 1.332617, 'c': 0.941271, 'l': 0.843826}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.289577, 'cc': 1.289577, 'c': 0.910870, 'l': 0.816573}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.554078, 'cc': 1.554078, 'c': 1.000000, 'l': 0.875623}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.494704, 'cc': 1.494704, 'c': 0.961795, 'l': 0.842169}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.441072, 'cc': 1.441072, 'c': 0.927284, 'l': 0.811951}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_20"] = {'bb': 1.375759, 'cc': 1.375759, 'c': 0.885257, 'l': 0.775151}
## pdf_PDF4LHC15_nlo_30_21 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.414377, 'cc': 1.414377, 'c': 1.000000, 'l': 0.896821}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.372028, 'cc': 1.372028, 'c': 0.970058, 'l': 0.869969}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.331572, 'cc': 1.331572, 'c': 0.941455, 'l': 0.844317}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.288696, 'cc': 1.288696, 'c': 0.911141, 'l': 0.817130}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.553442, 'cc': 1.553442, 'c': 1.000000, 'l': 0.875766}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.494157, 'cc': 1.494157, 'c': 0.961837, 'l': 0.842344}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.440602, 'cc': 1.440602, 'c': 0.927361, 'l': 0.812151}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_21"] = {'bb': 1.375377, 'cc': 1.375377, 'c': 0.885374, 'l': 0.775380}
## pdf_PDF4LHC15_nlo_30_22 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.414991, 'cc': 1.414991, 'c': 1.000000, 'l': 0.896668}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.372563, 'cc': 1.372563, 'c': 0.970015, 'l': 0.869782}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.332035, 'cc': 1.332035, 'c': 0.941373, 'l': 0.844099}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.289086, 'cc': 1.289086, 'c': 0.911021, 'l': 0.816883}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.554679, 'cc': 1.554679, 'c': 1.000000, 'l': 0.875489}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.495219, 'cc': 1.495219, 'c': 0.961754, 'l': 0.842005}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.441515, 'cc': 1.441515, 'c': 0.927211, 'l': 0.811762}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_22"] = {'bb': 1.376119, 'cc': 1.376119, 'c': 0.885147, 'l': 0.774936}
## pdf_PDF4LHC15_nlo_30_23 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.412180, 'cc': 1.412180, 'c': 1.000000, 'l': 0.897368}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.370114, 'cc': 1.370114, 'c': 0.970212, 'l': 0.870638}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.329916, 'cc': 1.329916, 'c': 0.941747, 'l': 0.845094}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.287301, 'cc': 1.287301, 'c': 0.911570, 'l': 0.818014}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.554549, 'cc': 1.554549, 'c': 1.000000, 'l': 0.875518}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.495108, 'cc': 1.495108, 'c': 0.961763, 'l': 0.842040}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.441419, 'cc': 1.441419, 'c': 0.927227, 'l': 0.811803}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_23"] = {'bb': 1.376041, 'cc': 1.376041, 'c': 0.885171, 'l': 0.774982}
## pdf_PDF4LHC15_nlo_30_24 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.413738, 'cc': 1.413738, 'c': 1.000000, 'l': 0.896980}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.371471, 'cc': 1.371471, 'c': 0.970103, 'l': 0.870163}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.331091, 'cc': 1.331091, 'c': 0.941540, 'l': 0.844543}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.288291, 'cc': 1.288291, 'c': 0.911266, 'l': 0.817387}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.554103, 'cc': 1.554103, 'c': 1.000000, 'l': 0.875618}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.494725, 'cc': 1.494725, 'c': 0.961793, 'l': 0.842163}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.441090, 'cc': 1.441090, 'c': 0.927281, 'l': 0.811943}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_24"] = {'bb': 1.375774, 'cc': 1.375774, 'c': 0.885253, 'l': 0.775143}
## pdf_PDF4LHC15_nlo_30_25 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.414598, 'cc': 1.414598, 'c': 1.000000, 'l': 0.896767}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.372220, 'cc': 1.372220, 'c': 0.970042, 'l': 0.869901}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.331738, 'cc': 1.331738, 'c': 0.941425, 'l': 0.844239}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.288837, 'cc': 1.288837, 'c': 0.911097, 'l': 0.817042}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.553550, 'cc': 1.553550, 'c': 1.000000, 'l': 0.875741}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.494250, 'cc': 1.494250, 'c': 0.961830, 'l': 0.842314}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.440682, 'cc': 1.440682, 'c': 0.927349, 'l': 0.812117}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_25"] = {'bb': 1.375442, 'cc': 1.375442, 'c': 0.885354, 'l': 0.775341}
## pdf_PDF4LHC15_nlo_30_26 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.414480, 'cc': 1.414480, 'c': 1.000000, 'l': 0.896796}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.372117, 'cc': 1.372117, 'c': 0.970051, 'l': 0.869937}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.331650, 'cc': 1.331650, 'c': 0.941441, 'l': 0.844280}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.288762, 'cc': 1.288762, 'c': 0.911120, 'l': 0.817089}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.553770, 'cc': 1.553770, 'c': 1.000000, 'l': 0.875691}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.494440, 'cc': 1.494440, 'c': 0.961815, 'l': 0.842253}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.440845, 'cc': 1.440845, 'c': 0.927322, 'l': 0.812048}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_26"] = {'bb': 1.375574, 'cc': 1.375574, 'c': 0.885314, 'l': 0.775262}
## pdf_PDF4LHC15_nlo_30_27 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.414669, 'cc': 1.414669, 'c': 1.000000, 'l': 0.896749}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.372282, 'cc': 1.372282, 'c': 0.970037, 'l': 0.869880}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.331792, 'cc': 1.331792, 'c': 0.941416, 'l': 0.844213}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.288882, 'cc': 1.288882, 'c': 0.911084, 'l': 0.817013}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.553963, 'cc': 1.553963, 'c': 1.000000, 'l': 0.875649}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.494604, 'cc': 1.494604, 'c': 0.961802, 'l': 0.842201}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.440987, 'cc': 1.440987, 'c': 0.927298, 'l': 0.811988}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_27"] = {'bb': 1.375689, 'cc': 1.375689, 'c': 0.885278, 'l': 0.775193}
## pdf_PDF4LHC15_nlo_30_28 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.413950, 'cc': 1.413950, 'c': 1.000000, 'l': 0.896927}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.371656, 'cc': 1.371656, 'c': 0.970088, 'l': 0.870098}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.331250, 'cc': 1.331250, 'c': 0.941512, 'l': 0.844468}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.288425, 'cc': 1.288425, 'c': 0.911224, 'l': 0.817302}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.553293, 'cc': 1.553293, 'c': 1.000000, 'l': 0.875800}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.494029, 'cc': 1.494029, 'c': 0.961846, 'l': 0.842385}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.440492, 'cc': 1.440492, 'c': 0.927379, 'l': 0.812199}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_28"] = {'bb': 1.375287, 'cc': 1.375287, 'c': 0.885401, 'l': 0.775434}
## pdf_PDF4LHC15_nlo_30_29 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.414785, 'cc': 1.414785, 'c': 1.000000, 'l': 0.896720}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.372383, 'cc': 1.372383, 'c': 0.970029, 'l': 0.869844}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.331879, 'cc': 1.331879, 'c': 0.941400, 'l': 0.844172}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.288955, 'cc': 1.288955, 'c': 0.911061, 'l': 0.816966}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.554165, 'cc': 1.554165, 'c': 1.000000, 'l': 0.875603}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.494778, 'cc': 1.494778, 'c': 0.961789, 'l': 0.842145}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.441136, 'cc': 1.441136, 'c': 0.927274, 'l': 0.811924}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_29"] = {'bb': 1.375811, 'cc': 1.375811, 'c': 0.885241, 'l': 0.775120}
## pdf_PDF4LHC15_nlo_30_30 
#flav_map[2]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.414639, 'cc': 1.414639, 'c': 1.000000, 'l': 0.896756}
#flav_map[3]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.372255, 'cc': 1.372255, 'c': 0.970040, 'l': 0.869889}
#flav_map[4]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.331769, 'cc': 1.331769, 'c': 0.941420, 'l': 0.844224}
#flav_map[5]['el']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.288862, 'cc': 1.288862, 'c': 0.911090, 'l': 0.817025}
#flav_map[2]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.553114, 'cc': 1.553114, 'c': 1.000000, 'l': 0.875840}
#flav_map[3]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.493875, 'cc': 1.493875, 'c': 0.961858, 'l': 0.842434}
#flav_map[4]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.440360, 'cc': 1.440360, 'c': 0.927401, 'l': 0.812255}
#flav_map[5]['mu']["pdf_PDF4LHC15_nlo_30_30"] = {'bb': 1.375180, 'cc': 1.375180, 'c': 0.885434, 'l': 0.775498}

