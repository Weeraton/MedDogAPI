from flask import Flask, jsonify, request
import pickle
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import numpy as np
app = Flask(__name__)

def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
def rsilabel(j):
    if j == 'S' or j == '*S':
        j = 1
    elif j == 'I' or j == '*I':
        j = 2
    elif j == 'R' or j == '*R' or j == 'R*':
        j = 3
    elif j == '-' or j == '*-':
        j = 4
    elif j == '+' or j == '*+':
        j = 5
    else:
        j = 6
    return j

@app.route('/GP', methods=['POST'])
def get_data():
    le = LabelEncoder()

    value =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    request_json = request.get_json()
    temp = request_json.get('species')
    if temp == 'DOG' or temp == 'dog' or temp == 'Dog ':
        temp = "1"  # dog
    elif temp == 'Cat' or temp == 'cat' or temp == 'Feline' or temp == 'C' or temp == 'Domestic Shorthair (DSH)':
        temp = "2"  # cat
    else:
        temp = "3"  # unknow NaN
    value[0] = temp
    temp = request_json.get('bact_species_1')
    bact = ['Hafnia alvei','Klebsiella pneumonia ssp pneumoniae','Klebsiella pneumoniae ssp pneumoniae ','Antimicrobials','Klebsiella pneumoniae subsp. pneumoniae','Aeromonas hydrophila','Escherichia coli ','Pseudomonas aeruginosa','Escherichia coli  ','Proteus mirabilis','Escherichia coli','Proteus hauseri','Serratia marcescens','Acinetobacter baumannii complex','Klebsiella pneumonia ssp pneumoniae  ','Enterobacter cloacae complex','Pseudomonas alcaligenes','Klebsiella pneumoniae ssp pneumoniae','Proteus mirabilis  ','Pseudomonas aeruginosa ','Klebsiella pneumoniae ssp. pneumoniae','Klebsiella pneumonia ssp ozaenae','','Citrobacter freundii  ','Proteus mirabilis ','Acinetobacter baumannii','Acinetobacter lwoffii','Moraxella group','Burkholderia cepacian','Klebsiella pneumoniae ssp  pneumoniae ','Salmonella group','Citrobacter koseri','Klebsiella pneumonia ssp pneumoniae ','Pasteurella canis','Unidentified gram-negative bacilli','Aeromonas salmonicida','Pseudomonas putida','Methylobacterium spp','Pantoea spp ','Burkholderia cepacia','Providencia stuartii','Achromobacter denitrificans','Chromobacterium violaceum ','Enterobacter clocae complex','Burkholderia cepacia group','Aeromonas sobria','Pantoea spp','Pseudomonas aeruginosa  ','Pseudomonas oryzihabitans','Burkholderia cepacia group ','Acinetobacter lwoffii ','Acinetobacter sp.','Klebsiella pneumoniae ssp pneumoniae  ','Low discrimination between Moraxella group and  Acinetobacter lwoffii','Aeromonas sobria ','Pasteurella multocida','Acinetobacter baumannii complex  ','Enterobacter cloacae complex ','Pseudomonas stutzeri','Pasteurella canis or P. multocida','Acinetobacter ursingii','Klebsiella pneumoniae subsp. pneumoniae ','Pantoea spp.','Stenotrophomonas maltophilia ','Achromobacter xylosoxidans','Enterobacter aerogenes','Pseudomonas fluorescens','Neisseria animaloris  ','Serratia marcecens','Acinetobacter haemolyticus','Morganella morganoo ssp morganii','Salmonella sp.','Sphingomonas paucimobilis','Stenotrophomonas maltophilia','Pseudomonas oleovorans','Klebsiella pneumoniae ssp pneumonia ','Escherichia fergusonii','Pseudomonas luteola','Bordetella bronchiseptica','Klebsiella pnuemoniae ssp. pneumoniae','Enterobacter amnigenus 2','Pantoea agglomerans or Kluyvera intermedia ','Burkholderia cepacia ','Pseudomonas putida  2x103 CFU','Morganella morganii ssp morganii','Pasteurella canis ','Roseomonas gilardii','Citrobacter youngae','Pseudomonas oryzihabitans  ','Proteus sp. ','Providencia rettgeri','Pseudomonas aeruginosa or Pseudomonas putida','Klebsiella pneumoniae ssp pneuminoae','Myroides spp','Acinetobacter radioresistens','Serratia ficaria','Shewanella algae','Enterobacter aerogenes ','Serratia marcescens ','Acinetobacter baumannii complex ','Pasteurella canis or Pasteurella multocida','Stenotrophomonas maltophillia','Pasteurella multocida or Pasteurella canis','nan','Escherichia coli 5.2x104 CFU','R','S','Staphylococcus schleiferi','Staphylococcus pseudintermedius','Enterococcus faecalis','Staphylococcus lugdunensis','Lactococcus garvieae','Staphylococcus haemolyticus','Staphylococcus hominis ssp hominis','Enterococcus faecium ','Staphylococcus aureus ','Staphylococcus pseudintermedius or S. aureus or S. haemolyticus','Streptococcus canis','Enterococcus faecium','Enterococcus gallinarum','Staphylococcus epidermidis','Streptococcus agalactiae','Staphylococcus pseudintermedius ','Staphylococcus sciuri','Gemella haemolyticus','Micrococcus luteus','Staphylococcus aureus','Streptococcus thoraltensis','Streptococcus pyogenes','Streptococcus dysgalactiae ssp dysgalactiae or Streptococcus sanguinis','Erysipelothrix rhusiopathiae','Staphylococcus caprae or Staphylococcus chromogenes','Streptococcus dysgalactiae ssp equisimilis','Staphylococcus xylosus or Staphylococcus simulans or Staphylococcus chromogenes','Staphylococcus vitulinus or Staphylococcus capitis','Staphylococcus scuiri','Staphylococcus caprae','Staphylococcus chromogenes','Staphylococcus lugdunensis ','Staphylococcus simulans','Staphylococcus saprophyticus','Staphylococcus cohnii ssp urealyticus ','Kocuria rosea ','Streptococcus sanguinis','Streptococcus infantarius ssp coli','Enterococcus faecalis ','Unidentified gram positive bacteria ','Staphylococcus warneri','Staphylococcus cohnii ssp urealyticus','Staphylococcus hominis ssp hominis ','Kocuria rhizophila','Low discrimination among Staphylococcus aureus, Staphylococcus chromogenes, Staphylococcus pseudintermedius ','Dermacoccus nishinomiyaensis ','Streptococcus agalactiae, Streptococcus constellatus ssp constellatus, or Streptococcus dysgalactiae ssp equisimilis','Streptococcus gallolyticus ssp pasteurianus ','Staphylococcus capitis','Staphylococcus chromogenes ','Streptococcus iniae','Streptococcus pseudoporcinus','Enterococcus gallinarum ','Staphylococcus caprae ','Lactococcus garvieae ','Staphylococcus warneri ','Bacillus spp.','Staphylococcus aureus or Staphylococcus pseudintermedius','Staphylococcus capitis ','Staphylococcus aureus, Staphylococcus chromogenes or Staphylococcus hyicus','Streptococcus parasanguinis','Streptococcus pseudoporcinus ','Unidentified Gram positive cocci, +Catalase, -Oxidase, -motility','Non or low reactive biopattern ','Streptococcus agalactiae ','Staphylococcus equorum','Staphylococcus hyicus','Streptococcus oralis ','Staphylococcus simulans ','Streptococcus pneumoniae','Enterococcus casseliflavus ','Staphylococcus epidermidis ','Streptococcus mitis ','Staphylococcus auricularis','Non or Low reactive biopattern ','Staphylococcus hominis ssp hominis or Staphylococcus hominis ssp novobiosepticus','Streptococcus anginosus','Kocuria virians ','Enterococcus hirae','Granulicatella adiacens ','Streptococcus canis ','Kocuria rhizophila ','Streptococcus pluranimalium','Staphylococcus simulans, Staphylococcus chromogenes or Staphylococcus xylosus','Enterococcus cecorum','Globicatella sanguinis ','Staphylococcus lentus','Enterococcus durans ','Low discrimination ','Streptococcus agalactiae, Streptococcus anginosus, Streptococcus gordonii','Achromobacter denitrificans ', 'Acinetobacter baumanniii complex ', 'Acinetobacter lwoffii or Moraxella group', 'Aeromonas hydrophila ', 'Alcaligenes faecalis ssp faecalis or Pseudomonas aeruginosa ', 'Chryseobacterium indologenes', 'Citrobacter freundii', 'Citrobacter freundii ', 'Citrobacter youngae ', 'Escherichia hermannii', 'Klebsiela pneumoniae ssp ozaenae ', 'Klebsiella oxytoca', 'Klebsiella oxytoca ', 'Klebsiella pneumoniae ', 'Klebsiella pneumoniae ssp ozaenae', 'Klebsiella pneumoniae ssp ozaenae ', 'Low discrimination between Pasteurella multocida or Acinetobacter lwoffii)', 'Neisseria animaloris ', 'Ochrobactrum anthropi', 'Ochrobactrum anthropi ', 'Ochrobactrum anthropic', 'Pasteurella dagmatis', 'Pasteurella multocida ', 'Proteus miribilis ', 'Proteus penneri ', 'Proteus penneri or Proteus hauseri ', 'Pseudomonas fluorescens ', 'Pseudomonas putida ', 'Raoultella planticola', 'Rhizobium radiobacter', 'Shigella sonnei ', 'Steotrophomonas maltophilia', 'Yersinia enterocolitica ']
    if temp not in bact:
        temp = "nan"
    le.fit('Hafnia alvei','Klebsiella pneumonia ssp pneumoniae','Klebsiella pneumoniae ssp pneumoniae ','Antimicrobials','Klebsiella pneumoniae subsp. pneumoniae','Aeromonas hydrophila','Escherichia coli ','Pseudomonas aeruginosa','Escherichia coli  ','Proteus mirabilis','Escherichia coli','Proteus hauseri','Serratia marcescens','Acinetobacter baumannii complex','Klebsiella pneumonia ssp pneumoniae  ','Enterobacter cloacae complex','Pseudomonas alcaligenes','Klebsiella pneumoniae ssp pneumoniae','Proteus mirabilis  ','Pseudomonas aeruginosa ','Klebsiella pneumoniae ssp. pneumoniae','Klebsiella pneumonia ssp ozaenae','','Citrobacter freundii  ','Proteus mirabilis ','Acinetobacter baumannii','Acinetobacter lwoffii','Moraxella group','Burkholderia cepacian','Klebsiella pneumoniae ssp  pneumoniae ','Salmonella group','Citrobacter koseri','Klebsiella pneumonia ssp pneumoniae ','Pasteurella canis','Unidentified gram-negative bacilli','Aeromonas salmonicida','Pseudomonas putida','Methylobacterium spp','Pantoea spp ','Burkholderia cepacia','Providencia stuartii','Achromobacter denitrificans','Chromobacterium violaceum ','Enterobacter clocae complex','Burkholderia cepacia group','Aeromonas sobria','Pantoea spp','Pseudomonas aeruginosa  ','Pseudomonas oryzihabitans','Burkholderia cepacia group ','Acinetobacter lwoffii ','Acinetobacter sp.','Klebsiella pneumoniae ssp pneumoniae  ','Low discrimination between Moraxella group and  Acinetobacter lwoffii','Aeromonas sobria ','Pasteurella multocida','Acinetobacter baumannii complex  ','Enterobacter cloacae complex ','Pseudomonas stutzeri','Pasteurella canis or P. multocida','Acinetobacter ursingii','Klebsiella pneumoniae subsp. pneumoniae ','Pantoea spp.','Stenotrophomonas maltophilia ','Achromobacter xylosoxidans','Enterobacter aerogenes','Pseudomonas fluorescens','Neisseria animaloris  ','Serratia marcecens','Acinetobacter haemolyticus','Morganella morganoo ssp morganii','Salmonella sp.','Sphingomonas paucimobilis','Stenotrophomonas maltophilia','Pseudomonas oleovorans','Klebsiella pneumoniae ssp pneumonia ','Escherichia fergusonii','Pseudomonas luteola','Bordetella bronchiseptica','Klebsiella pnuemoniae ssp. pneumoniae','Enterobacter amnigenus 2','Pantoea agglomerans or Kluyvera intermedia ','Burkholderia cepacia ','Pseudomonas putida  2x103 CFU','Morganella morganii ssp morganii','Pasteurella canis ','Roseomonas gilardii','Citrobacter youngae','Pseudomonas oryzihabitans  ','Proteus sp. ','Providencia rettgeri','Pseudomonas aeruginosa or Pseudomonas putida','Klebsiella pneumoniae ssp pneuminoae','Myroides spp','Acinetobacter radioresistens','Serratia ficaria','Shewanella algae','Enterobacter aerogenes ','Serratia marcescens ','Acinetobacter baumannii complex ','Pasteurella canis or Pasteurella multocida','Stenotrophomonas maltophillia','Pasteurella multocida or Pasteurella canis','nan','Escherichia coli 5.2x104 CFU','R','S','Staphylococcus schleiferi','Staphylococcus pseudintermedius','Enterococcus faecalis','Staphylococcus lugdunensis','Lactococcus garvieae','Staphylococcus haemolyticus','Staphylococcus hominis ssp hominis','Enterococcus faecium ','Staphylococcus aureus ','Staphylococcus pseudintermedius or S. aureus or S. haemolyticus','Streptococcus canis','Enterococcus faecium','Enterococcus gallinarum','Staphylococcus epidermidis','Streptococcus agalactiae','Staphylococcus pseudintermedius ','Staphylococcus sciuri','Gemella haemolyticus','Micrococcus luteus','Staphylococcus aureus','Streptococcus thoraltensis','Streptococcus pyogenes','Streptococcus dysgalactiae ssp dysgalactiae or Streptococcus sanguinis','Erysipelothrix rhusiopathiae','Staphylococcus caprae or Staphylococcus chromogenes','Streptococcus dysgalactiae ssp equisimilis','Staphylococcus xylosus or Staphylococcus simulans or Staphylococcus chromogenes','Staphylococcus vitulinus or Staphylococcus capitis','Staphylococcus scuiri','Staphylococcus caprae','Staphylococcus chromogenes','Staphylococcus lugdunensis ','Staphylococcus simulans','Staphylococcus saprophyticus','Staphylococcus cohnii ssp urealyticus ','Kocuria rosea ','Streptococcus sanguinis','Streptococcus infantarius ssp coli','Enterococcus faecalis ','Unidentified gram positive bacteria ','Staphylococcus warneri','Staphylococcus cohnii ssp urealyticus','Staphylococcus hominis ssp hominis ','Kocuria rhizophila','Low discrimination among Staphylococcus aureus, Staphylococcus chromogenes, Staphylococcus pseudintermedius ','Dermacoccus nishinomiyaensis ','Streptococcus agalactiae, Streptococcus constellatus ssp constellatus, or Streptococcus dysgalactiae ssp equisimilis','Streptococcus gallolyticus ssp pasteurianus ','Staphylococcus capitis','Staphylococcus chromogenes ','Streptococcus iniae','Streptococcus pseudoporcinus','Enterococcus gallinarum ','Staphylococcus caprae ','Lactococcus garvieae ','Staphylococcus warneri ','Bacillus spp.','Staphylococcus aureus or Staphylococcus pseudintermedius','Staphylococcus capitis ','Staphylococcus aureus, Staphylococcus chromogenes or Staphylococcus hyicus','Streptococcus parasanguinis','Streptococcus pseudoporcinus ','Unidentified Gram positive cocci, +Catalase, -Oxidase, -motility','Non or low reactive biopattern ','Streptococcus agalactiae ','Staphylococcus equorum','Staphylococcus hyicus','Streptococcus oralis ','Staphylococcus simulans ','Streptococcus pneumoniae','Enterococcus casseliflavus ','Staphylococcus epidermidis ','Streptococcus mitis ','Staphylococcus auricularis','Non or Low reactive biopattern ','Staphylococcus hominis ssp hominis or Staphylococcus hominis ssp novobiosepticus','Streptococcus anginosus','Kocuria virians ','Enterococcus hirae','Granulicatella adiacens ','Streptococcus canis ','Kocuria rhizophila ','Streptococcus pluranimalium','Staphylococcus simulans, Staphylococcus chromogenes or Staphylococcus xylosus','Enterococcus cecorum','Globicatella sanguinis ','Staphylococcus lentus','Enterococcus durans ','Low discrimination ','Streptococcus agalactiae, Streptococcus anginosus, Streptococcus gordonii','Achromobacter denitrificans ', 'Acinetobacter baumanniii complex ', 'Acinetobacter lwoffii or Moraxella group', 'Aeromonas hydrophila ', 'Alcaligenes faecalis ssp faecalis or Pseudomonas aeruginosa ', 'Chryseobacterium indologenes', 'Citrobacter freundii', 'Citrobacter freundii ', 'Citrobacter youngae ', 'Escherichia hermannii', 'Klebsiela pneumoniae ssp ozaenae ', 'Klebsiella oxytoca', 'Klebsiella oxytoca ', 'Klebsiella pneumoniae ', 'Klebsiella pneumoniae ssp ozaenae', 'Klebsiella pneumoniae ssp ozaenae ', 'Low discrimination between Pasteurella multocida or Acinetobacter lwoffii)', 'Neisseria animaloris ', 'Ochrobactrum anthropi', 'Ochrobactrum anthropi ', 'Ochrobactrum anthropic', 'Pasteurella dagmatis', 'Pasteurella multocida ', 'Proteus miribilis ', 'Proteus penneri ', 'Proteus penneri or Proteus hauseri ', 'Pseudomonas fluorescens ', 'Pseudomonas putida ', 'Raoultella planticola', 'Rhizobium radiobacter', 'Shigella sonnei ', 'Steotrophomonas maltophilia', 'Yersinia enterocolitica ',nan)
    value[1] = le.transform(temp)
    value[2] = rsilabel(request_json.get('Amikacin'))
    value[3] = rsilabel(request_json.get('Ampicillin'))
    value[4] = rsilabel(request_json.get('Amoxicillin/clavulanic acid'))
    value[5] = rsilabel(request_json.get('Cefixime'))
    value[6] = rsilabel(request_json.get('Cefovecin'))
    value[7] = rsilabel(request_json.get('Cefpodoxime'))
    value[8] = rsilabel(request_json.get('Ceftiofur'))
    value[9] = rsilabel(request_json.get('Ceftriaxone'))
    value[10] = rsilabel(request_json.get('Cephalexin'))
    value[11] = rsilabel(request_json.get('Chloramphenicol'))
    value[12] = rsilabel(request_json.get('Colistin (polymyxin E)'))
    value[14] = rsilabel(request_json.get('ESBL'))
    value[15] = rsilabel(request_json.get('Enrofloxacin'))
    value[16] = rsilabel(request_json.get('Fosfomycin'))
    value[17] = rsilabel(request_json.get('Gentamicin'))
    value[18] = rsilabel(request_json.get('Imipenem'))
    value[19] = rsilabel(request_json.get('Marbofloxacin'))
    value[20] = rsilabel(request_json.get('Nitrofurantoin'))
    value[21] = rsilabel(request_json.get('Piperacillin-tazobactam'))
    value[22] = rsilabel(request_json.get('Polymyxin B'))
    value[23] = rsilabel(request_json.get('Rifampin'))
    value[24] = rsilabel(request_json.get('Sulfamethoxazole/trimethoprim'))
    value[25] = rsilabel(request_json.get('Tetracycline'))
    value[26] = rsilabel(request_json.get('Tobramycin'))
    value[27] = rsilabel(request_json.get('Benzyl penicillin'))
    value[28] = rsilabel(request_json.get('Cefotaxime'))
    value[29] = rsilabel(request_json.get('Cefoxitin'))
    value[30] = rsilabel(request_json.get('Cephalothin'))
    value[31] = rsilabel(request_json.get('Clindamycin'))
    value[32] = rsilabel(request_json.get('Erythromycin'))
    value[33] = rsilabel(request_json.get('Fusidic acid'))
    value[34] = rsilabel(request_json.get('Inducible clindamycin'))
    value[35] = rsilabel(request_json.get('Levofloxacin'))
    value[36] = rsilabel(request_json.get('Linezolid'))
    value[37] = rsilabel(request_json.get('Mupirocin'))
    value[38] = rsilabel(request_json.get('Oxacillin'))
    value[39] = rsilabel(request_json.get('Rifampicin'))
    value[40] = rsilabel(request_json.get('Vancomycin'))

    pathlist = ["Amikacin_decisionTree.sav","Amoxicillin_decisionTree.sav","Azithromycin_decisionTree.sav","Cefazolin_decisionTree.sav","Cefixime_decisionTree.sav","Cefovecin_decisionTree.sav","Ceftriaxone_decisionTree.sav","Cephalexin_decisionTree.sav","Clavulanic acid_decisionTree.sav","Clindamycin_decisionTree.sav","Doxycycline_decisionTree.sav","Enrofloxacin_decisionTree.sav","Gentamicin_decisionTree.sav","Marbofloxacin_decisionTree.sav","Nitrofurantoin_decisionTree.sav","Pradofloxacin_decisionTree.sav","Rifampicin_decisionTree.sav","Sulfamethoxazole_decisionTree.sav","Vancomycin_decisionTree.sav"]
    ans =[]
    for i in pathlist:
        print(i)
        Med_Name = []
        for j in i:
            if j is not "_":
                Med_Name.append(j)
            else:
                break
        infile = open("GP_model/"+i, 'rb')
        model = pickle.load(infile)
        my_array = np.array(value)
        my_array =my_array.reshape(1,-1)
        x = model.predict(my_array)
        print(type(x))
        for j in x:
            print(type(j))
            if j is np.bool_(True):
                print("Do")
                ans.append(listToString(Med_Name))
    response_content ={
            "Med" : str(ans)
    }
    return jsonify(response_content)

@app.route('/GN', methods=['POST'])
def get_data2():
    le = LabelEncoder()

    value =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    request_json = request.get_json()
    temp = request_json.get('species')
    if temp == 'DOG' or temp == 'dog' or temp == 'Dog ':
        temp = "1"  # dog
    elif temp == 'Cat' or temp == 'cat' or temp == 'Feline' or temp == 'C' or temp == 'Domestic Shorthair (DSH)':
        temp = "2"  # cat
    else:
        temp = "3"  # unknow NaN
    value[0] = temp
    temp = request_json.get('bact_species_1')
    bact = ['Staphylococcus pseudintermedius','Antimicrobials','Staphylococcus schleiferi','Staphylococcus chromogenes','Enterococcus faecium','Enterococcus faecalis 2.1 x 105 CFU','Leuconostoc mesenteroides ssp cremoris','unidentified gram-positive bacteria','Staphylococcus auricularis','Staphylococcus aureus','Streptococcus sp. ','Staphylococcus hominis ssp hominis','Alloiococcus otitis','Staphylococcus cohnii ssp. urealyticus','Granulicatella adiacens','Micrococcus luteus','Unidentified gram-positive cocci','Staphylococcus lentus','Streptococcus agalactiae','Streptococcus pluranimalium','Streptococcus spp.','Streptococcus infantarius ssp coli','Enterococcus faecalis ','Enterococcus faecalis','Staphylococcus pseudintermedius ','Kocuria varians','Staphylococcus warneri','Corynebacterium spp. ','Aerococcus viridans','Staphylococcus haemolyticus','Streptococcus sp.','Staphylococcus hyicus','Streptococcus equinus','Kocuria rosea','Corynebacterium spp.','Corynebacterium spp ','Staphylococcus cohnii ssp unrealyticus ','Kocuria kristinae','Streptococcus dysgalactiae ssp equisimilis','Streptococcus canis','Staphylococcus pseudinternedius','Enterococcus faecium ','Methicillin-resistant Staphylococcus schleiferi','Staphylococcus sciuri','Methicillin-susceptible Staphylococcus chromogenes','Staphylococcus hominis ssp hominis or Staphylococcus saprohyticus','Streptococcus gallolyticus ssp pasteurianus','Enterococcus avium','Unidentified Gram positive cocci ','Staphylococcus auricularis ','Staphylococcus saprophyticus ','Streptococcus anginosus','Enterococcus raffinosus','Unidentified gram positive cocci','Staphylococcus xylosus','Staphylococcus cohnii ssp unrealyticus','Staphylococcus pseudintermedius or lugdunensis ','Staphylococcus hominis ssp hominis ','Streptococcus pseudoporcinus','Staphylococcus chromogenes ','Staphylococcus cohnii ssp urealyticus','Staphylococcus pseuedintermedius','Low discrimination between Staphylococcus aureus','Staphylococcus pseudintermedius or Staphylococcus aureus','Streptococcus agalactiae ','Methicillin-resistant Staphylococcus aureus','Lactococcus garvieae','Staphylococcus aureus ','Staphylococcus kloosii','Corynebacterium spp','Streptococcus dysagalactiae ssp equisimilis','Non or low reactive biopattern ','Unidentified gram-positive cocci ','Staphylococcus epidermidis','Staphylococcus caprae','Kocuria varians ','Staphylococcus capitis','Streptococcus mitis','Enterococcus columbae','Streptococcus pneumoniae','Enterococcus casseliflavus','Kocuria kristinae ','Streptococcus canis ','Coagulase-negative staphylococci','Streptococcus constellatus ssp pharynges','Streptococcus constellatus ssp constellatus','Unidentified gram-positive bacteria','Staphylococcus cohnii ssp cohnii','Coagulase-negative Staphylococcus sp.','Staphylococcus hominis','Staphylococcus lugdunensis ','Streptococcus constellatus ssp pharyngis','Streptococcus dysgalactiae ssp dysgalactiae','Staphylococcus epidermidis กับ Staphylococcus hominis ssp hominis','Erysipelothrix rhusiopathiae','Enterococcus casseliflavus ','Gram positive cocci bacteria ','Staphylococcus saprophyticus','Low discrimination','Pasteurella canis','Streptococcus suis','Streptococcus dysgalactiae','Enterococcus durans','Staphylococcus schleiferi or Staphylococcus aureus','Streptococcus ovis ','Staphylococcus caprae or chromogenes) ','Staphylococcus epidermidis ','Streptococcus constellatus','Staphylococcus simulans','Granulicatella elegans','Streptococcus dysgalactiae ssp equisimilis ','Streptococcus thoraltensis','Methicillin-susceptible Staphylococcus pseudintermedius','Staphylococcus lugdunensis','Kocuria rosea ','Enterococcus durans ','Streptococcus gallolyticus ssp gallolyticus ','Streptococcus parasanguinis','Staphylococcus chormogenes','Staphylococcus warneri or Staphylococcus lugdunensis','Staphylococcus warneri or Staphylococcus hominis ssp hominis)','Streptococcus sanguinis or Streptococcus thoraltensis','Streptococcus agalactiae or Streptococcus canis','Staphylococcus chromoenes','Streptococcus infantarius ssp coli ','Low discrimination ','Staphylococcus pseudintermedius or S. aureus or S. haemolyticus','Enterococcus gallinarum','Gemella haemolyticus','Streptococcus pyogenes','Streptococcus dysgalactiae ssp dysgalactiae or Streptococcus sanguinis','Staphylococcus caprae or Staphylococcus chromogenes','Staphylococcus xylosus or Staphylococcus simulans or Staphylococcus chromogenes','Staphylococcus vitulinus or Staphylococcus capitis','Staphylococcus scuiri','Staphylococcus cohnii ssp urealyticus ','Streptococcus sanguinis','Unidentified gram positive bacteria ','Kocuria rhizophila','Low discrimination among Staphylococcus aureus, Staphylococcus chromogenes, Staphylococcus pseudintermedius ','Dermacoccus nishinomiyaensis ','Streptococcus agalactiae, Streptococcus constellatus ssp constellatus, or Streptococcus dysgalactiae ssp equisimilis','Streptococcus gallolyticus ssp pasteurianus ','Streptococcus iniae','Enterococcus gallinarum ','Staphylococcus caprae ','Lactococcus garvieae ','Staphylococcus warneri ','Bacillus spp.','Staphylococcus aureus or Staphylococcus pseudintermedius','Staphylococcus capitis ','Staphylococcus aureus, Staphylococcus chromogenes or Staphylococcus hyicus','Streptococcus pseudoporcinus ','Unidentified Gram positive cocci, +Catalase, -Oxidase, -motility','Staphylococcus equorum','Streptococcus oralis ','Staphylococcus simulans ','Streptococcus mitis ','Non or Low reactive biopattern ','Staphylococcus hominis ssp hominis or Staphylococcus hominis ssp novobiosepticus','Kocuria virians ','Enterococcus hirae','Granulicatella adiacens ','Kocuria rhizophila ','Staphylococcus simulans, Staphylococcus chromogenes or Staphylococcus xylosus','Enterococcus cecorum','Globicatella sanguinis ','Streptococcus agalactiae, Streptococcus anginosus, Streptococcus gordonii']
    if temp not in bact:
        temp = "nan"
    le.fit('Staphylococcus pseudintermedius','Antimicrobials','Staphylococcus schleiferi','Staphylococcus chromogenes','Enterococcus faecium','Enterococcus faecalis 2.1 x 105 CFU','Leuconostoc mesenteroides ssp cremoris','unidentified gram-positive bacteria','Staphylococcus auricularis','Staphylococcus aureus','Streptococcus sp. ','Staphylococcus hominis ssp hominis','Alloiococcus otitis','Staphylococcus cohnii ssp. urealyticus','Granulicatella adiacens','Micrococcus luteus','Unidentified gram-positive cocci','Staphylococcus lentus','Streptococcus agalactiae','Streptococcus pluranimalium','Streptococcus spp.','Streptococcus infantarius ssp coli','Enterococcus faecalis ','Enterococcus faecalis','Staphylococcus pseudintermedius ','Kocuria varians','Staphylococcus warneri','Corynebacterium spp. ','Aerococcus viridans','Staphylococcus haemolyticus','Streptococcus sp.','Staphylococcus hyicus','Streptococcus equinus','Kocuria rosea','Corynebacterium spp.','Corynebacterium spp ','Staphylococcus cohnii ssp unrealyticus ','Kocuria kristinae','Streptococcus dysgalactiae ssp equisimilis','Streptococcus canis','Staphylococcus pseudinternedius','Enterococcus faecium ','Methicillin-resistant Staphylococcus schleiferi','Staphylococcus sciuri','Methicillin-susceptible Staphylococcus chromogenes','Staphylococcus hominis ssp hominis or Staphylococcus saprohyticus','Streptococcus gallolyticus ssp pasteurianus','Enterococcus avium','Unidentified Gram positive cocci ','Staphylococcus auricularis ','Staphylococcus saprophyticus ','Streptococcus anginosus','Enterococcus raffinosus','Unidentified gram positive cocci','Staphylococcus xylosus','Staphylococcus cohnii ssp unrealyticus','Staphylococcus pseudintermedius or lugdunensis ','Staphylococcus hominis ssp hominis ','Streptococcus pseudoporcinus','Staphylococcus chromogenes ','Staphylococcus cohnii ssp urealyticus','Staphylococcus pseuedintermedius','Low discrimination between Staphylococcus aureus','Staphylococcus pseudintermedius or Staphylococcus aureus','Streptococcus agalactiae ','Methicillin-resistant Staphylococcus aureus','Lactococcus garvieae','Staphylococcus aureus ','Staphylococcus kloosii','Corynebacterium spp','Streptococcus dysagalactiae ssp equisimilis','Non or low reactive biopattern ','Unidentified gram-positive cocci ','Staphylococcus epidermidis','Staphylococcus caprae','Kocuria varians ','Staphylococcus capitis','Streptococcus mitis','Enterococcus columbae','Streptococcus pneumoniae','Enterococcus casseliflavus','Kocuria kristinae ','Streptococcus canis ','Coagulase-negative staphylococci','Streptococcus constellatus ssp pharynges','Streptococcus constellatus ssp constellatus','Unidentified gram-positive bacteria','Staphylococcus cohnii ssp cohnii','Coagulase-negative Staphylococcus sp.','Staphylococcus hominis','Staphylococcus lugdunensis ','Streptococcus constellatus ssp pharyngis','Streptococcus dysgalactiae ssp dysgalactiae','Staphylococcus epidermidis กับ Staphylococcus hominis ssp hominis','Erysipelothrix rhusiopathiae','Enterococcus casseliflavus ','Gram positive cocci bacteria ','Staphylococcus saprophyticus','Low discrimination','Pasteurella canis','Streptococcus suis','Streptococcus dysgalactiae','Enterococcus durans','Staphylococcus schleiferi or Staphylococcus aureus','Streptococcus ovis ','Staphylococcus caprae or chromogenes) ','Staphylococcus epidermidis ','Streptococcus constellatus','Staphylococcus simulans','Granulicatella elegans','Streptococcus dysgalactiae ssp equisimilis ','Streptococcus thoraltensis','Methicillin-susceptible Staphylococcus pseudintermedius','Staphylococcus lugdunensis','Kocuria rosea ','Enterococcus durans ','Streptococcus gallolyticus ssp gallolyticus ','Streptococcus parasanguinis','Staphylococcus chormogenes','Staphylococcus warneri or Staphylococcus lugdunensis','Staphylococcus warneri or Staphylococcus hominis ssp hominis)','Streptococcus sanguinis or Streptococcus thoraltensis','Streptococcus agalactiae or Streptococcus canis','Staphylococcus chromoenes','Streptococcus infantarius ssp coli ','Low discrimination ','Staphylococcus pseudintermedius or S. aureus or S. haemolyticus','Enterococcus gallinarum','Gemella haemolyticus','Streptococcus pyogenes','Streptococcus dysgalactiae ssp dysgalactiae or Streptococcus sanguinis','Staphylococcus caprae or Staphylococcus chromogenes','Staphylococcus xylosus or Staphylococcus simulans or Staphylococcus chromogenes','Staphylococcus vitulinus or Staphylococcus capitis','Staphylococcus scuiri','Staphylococcus cohnii ssp urealyticus ','Streptococcus sanguinis','Unidentified gram positive bacteria ','Kocuria rhizophila','Low discrimination among Staphylococcus aureus, Staphylococcus chromogenes, Staphylococcus pseudintermedius ','Dermacoccus nishinomiyaensis ','Streptococcus agalactiae, Streptococcus constellatus ssp constellatus, or Streptococcus dysgalactiae ssp equisimilis','Streptococcus gallolyticus ssp pasteurianus ','Streptococcus iniae','Enterococcus gallinarum ','Staphylococcus caprae ','Lactococcus garvieae ','Staphylococcus warneri ','Bacillus spp.','Staphylococcus aureus or Staphylococcus pseudintermedius','Staphylococcus capitis ','Staphylococcus aureus, Staphylococcus chromogenes or Staphylococcus hyicus','Streptococcus pseudoporcinus ','Unidentified Gram positive cocci, +Catalase, -Oxidase, -motility','Staphylococcus equorum','Streptococcus oralis ','Staphylococcus simulans ','Streptococcus mitis ','Non or Low reactive biopattern ','Staphylococcus hominis ssp hominis or Staphylococcus hominis ssp novobiosepticus','Kocuria virians ','Enterococcus hirae','Granulicatella adiacens ','Kocuria rhizophila ','Staphylococcus simulans, Staphylococcus chromogenes or Staphylococcus xylosus','Enterococcus cecorum','Globicatella sanguinis ','Streptococcus agalactiae, Streptococcus anginosus, Streptococcus gordonii','nan')
    value[1] = le.transform(temp)
    value[2] = rsilabel(request_json.get('Amikacin'))
    value[3] = rsilabel(request_json.get('Ampicillin'))
    value[4] = rsilabel(request_json.get('Amoxicillin/clavulanic acid'))
    value[5] = rsilabel(request_json.get('Cefixime'))
    value[6] = rsilabel(request_json.get('Cefovecin'))
    value[7] = rsilabel(request_json.get('Cefpodoxime'))
    value[8] = rsilabel(request_json.get('Ceftiofur'))
    value[9] = rsilabel(request_json.get('Ceftriaxone'))
    value[10] = rsilabel(request_json.get('Cephalexin'))
    value[11] = rsilabel(request_json.get('Chloramphenicol'))
    value[12] = rsilabel(request_json.get('Colistin (polymyxin E)'))
    value[13] = rsilabel(request_json.get('Doxycycline'))
    value[14] = rsilabel(request_json.get('ESBL'))
    value[15] = rsilabel(request_json.get('Enrofloxacin'))
    value[16] = rsilabel(request_json.get('Fosfomycin'))
    value[17] = rsilabel(request_json.get('Gentamicin'))
    value[18] = rsilabel(request_json.get('Imipenem'))
    value[19] = rsilabel(request_json.get('Marbofloxacin'))
    value[20] = rsilabel(request_json.get('Nitrofurantoin'))
    value[21] = rsilabel(request_json.get('Piperacillin-tazobactam'))
    value[22] = rsilabel(request_json.get('Polymyxin B'))
    value[23] = rsilabel(request_json.get('Rifampin'))
    value[24] = rsilabel(request_json.get('Sulfamethoxazole/trimethoprim'))
    value[25] = rsilabel(request_json.get('Tetracycline'))
    value[26] = rsilabel(request_json.get('Tobramycin'))
    value[27] = rsilabel(request_json.get('Benzyl penicillin'))
    value[28] = rsilabel(request_json.get('Cefotaxime'))
    value[29] = rsilabel(request_json.get('Cefoxitin'))
    value[30] = rsilabel(request_json.get('Cephalothin'))
    value[31] = rsilabel(request_json.get('Clindamycin'))
    value[32] = rsilabel(request_json.get('Erythromycin'))
    value[33] = rsilabel(request_json.get('Fusidic acid'))
    value[34] = rsilabel(request_json.get('Inducible clindamycin'))
    value[35] = rsilabel(request_json.get('Levofloxacin'))
    value[36] = rsilabel(request_json.get('Linezolid'))
    value[37] = rsilabel(request_json.get('Mupirocin'))
    value[38] = rsilabel(request_json.get('Oxacillin'))
    value[39] = rsilabel(request_json.get('Rifampicin'))
    value[40] = rsilabel(request_json.get('Vancomycin'))

    pathlist = ["Amikacin_decisionTree.sav","Amoxicillin_decisionTree.sav","Cefalexin_decisionTree.sav","Cefixime_decisionTree.sav","Cefovecin_decisionTree.sav","Ceftriaxone_decisionTree.sav","Ceftriazone_decisionTree.sav","Cephalexin_decisionTree.sav","Cephazolin_decisionTree.sav","Clindamycin_decisionTree.sav","Colistin (polymyxin E)_decisionTree.sav","Doxycycline_decisionTree.sav","Empirically_decisionTree.sav","Endofloxacin_decisionTree.sav","Fosfomycin_decisionTree.sav","Gentamicin_decisionTree.sav","Imipenem_decisionTree.sav","Marboflocacin_decisionTree.sav","Metronidazole_decisionTree.sav","Nitrofurantoin_decisionTree.sav","Piperacillin-tazobactam_decisionTree.sav","Sulfamethoxazole_trimethoprim_decisionTree.sav","Tetracycline_decisionTree.sav"]
    ans =[]
    for i in pathlist:
        print(i)
        Med_Name = []
        for j in i:
            if j is not "_":
                Med_Name.append(j)
            else:
                break
        infile = open("GP_model/"+i, 'rb')
        model = pickle.load(infile)
        my_array = np.array(value)
        my_array =my_array.reshape(1,-1)
        x = model.predict(my_array)
        print(type(x))
        for j in x:
            print(type(j))
            if j is np.bool_(True):
                print("Do")
                ans.append(listToString(Med_Name))
    response_content ={
            "Med" : str(ans)
    }
    return jsonify(response_content)

if __name__ == "__main__":
    app.run(debug=True)