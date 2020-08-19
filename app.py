from flask import Flask, jsonify, request
import pickle
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import numpy as np

app = Flask(__name__)
def SumitEncode(case):
    AppenData = "aound"
    if case == "wound":
        AppenData = "Wound"
    elif case == "Granulomatous formation @ Lt Stifle (Sx site)":
        AppenData = "ETC"
    elif case == "Right proximal ureter (calculi)":  # Not Sure
        AppenData = "Ub mucosa"
    elif case == "Pustule":
        AppenData = "pustule"
    elif case == "Fistular tract":
        AppenData = "ETC..."
    elif case == "Chin Acne":  # Not Sure
        AppenData = "Abscess"
    elif case == "Peritoneal fluid":
        AppenData = "Abdominal effusion"
    elif case == "UB mucosa":
        AppenData = "Ub mucosa"
    elif case == "Lt. ear exudate":
        AppenData = "Ear exudate"
    elif case == "urine":
        AppenData = "Urine"
    elif case == "Wound @ Lt thorax":
        AppenData = "Wound"
    elif case == "Exudate from surgical wound":
        AppenData = "Surgical Site"
    elif case == "Deep pyoderma":
        AppenData = "ETC..."
    elif case == "Gall bladder":
        AppenData = "Ub mucosa"
    elif case == "pustule":
        AppenData = "pustule"
    elif case == "Purulent exudate (pododermatitis)":  # not SURE
        AppenData = "pustule"
    elif case == "GB":  # Not Sure
        AppenData = "Ub mucosa"
    elif case == "Purulent from mass":
        AppenData = "pustule"
    elif case == "Rt stifle":
        AppenData = "ETC..."
    elif case == "Nasal discharge":  # not Sure
        AppenData = "Pleural effusion"
    elif case == "Crust from skin":
        AppenData = "ETC..."
    elif case == "Left thoracic wound":
        AppenData = "Wound"
    elif case == "Oral mass":
        AppenData = "ETC..."
    elif case == "Chronic wound":
        AppenData = "Wound"
    elif case == "Exudate from PG cyst":  # not Sure
        AppenData = "ETC..."
    elif case == "Wound @ lt lumbar":
        AppenData = "Wound"
    elif case == "Pus from renal pelvis":
        AppenData = "ETC..."
    elif case == "Wound @ Lt flank":
        AppenData = "Wound"
    elif case == "Abdominal effusion":
        AppenData = "Abdominal effusion"
    elif case == "Exudate from wound (bed sore)":
        AppenData = "Wound"
    elif case == "Urine":
        AppenData = "Urine"
    elif case == "Abscess @ right ear":
        AppenData = "Abscess"
    elif case == "Left kidney":
        AppenData = "ETC..."
    elif case == "Epidermal collarette":
        AppenData = "ETC..."
    elif case == "Purulent exudate from wound at Rt.lumbar area":
        AppenData = "Wound"
    elif case == "Wound @ rt perineal area":
        AppenData = "Wound"
    elif case == "แผลโดนเหล็กเสียบ":
        AppenData = "Wound"
    elif case == "Exudate from wound":
        AppenData = "Wound"
    elif case == "Wound at LHL":
        AppenData = "Wound"
    elif case == "Abdominal fluid":
        AppenData = "Abdominal effusion"
    elif case == "Abdo fluid":
        AppenData = "Abdominal effusion"
    elif case == "Bite wound":
        AppenData = "Bite wound"
    elif case == "Crust from skin//Mucocutaneous":
        AppenData = "ETC..."
    elif case == "Exudate from pin protrusion":
        AppenData = "ETC..."
    elif case == "หูขวา":
        AppenData = "Ear exudate"
    elif case == "abscess":
        AppenData = "Abscess"
    elif case == "Rt.stifle hematoma (post MPL surgery)":
        AppenData = "Surgical Site"
    elif case == "furunculosis":
        AppenData = "ETC..."
    elif case == "Deep exudate from celluslitis / deep mycoses / deep pyoderma":
        AppenData = "ETC..."
    elif case == "Pus from rt temporal fistular tract":
        AppenData = "ETC..."
    elif case == "ปัสสาวะ":
        AppenData = "Urine"
    elif case == "Skin swab":
        AppenData = "ETC..."
    elif case == "Purulent exudate from wound":
        AppenData = "Wound"
    elif case == "Exudate from Rt ear":
        AppenData = "Ear exudate"
    elif case == "Exudate from mass":
        AppenData = "ETC..."
    elif case == "Swab from rostral nasal mucosa":
        AppenData = "Pleural effusion"
    elif case == "Skin (post op skin flap)":
        AppenData = "ETC..."
    elif case == "PG abscess":
        AppenData = "Abscess"
    elif case == "Right medial iliac lymph node":
        AppenData = "ETC..."
    elif case == "Open wound at skull (HBC)":
        AppenData = "Wound"
    elif case == "Pleural Effusion":
        AppenData = "Pleural effusion"
    elif case == "Wound (skin laceration)":
        AppenData = "Wound"
    elif case == "Epidermal colleate กิน AMC +Pred จาก clinic Not improve":
        AppenData = "ETC..."
    elif case == "chylothorax":
        AppenData = "ETC..."
    elif case == "Abscess from RT FL":
        AppenData = "Abscess"
    elif case == "Wound @ Rt shoulder":
        AppenData = "Wound"
    elif case == "Wound @ Lt lumbar":
        AppenData = "Wound"
    elif case == "Skin lesion : nodule":
        AppenData = "ETC..."
    elif case == "Lt ear (otitis externa)":
        AppenData = "Ear exudate"
    elif case == "Fluid from retroperitoneal space":
        AppenData = "ETC..."
    elif case == "Wound @ lt neck":
        AppenData = "Wound"
    elif case == "Opened bone fracture":
        AppenData = "ETC..."
    elif case == "Abscess":
        AppenData = "Abscess"
    elif case == "Ub mucosa":
        AppenData = "Ub mucosa"
    elif case == "Nasal pus":
        AppenData = "Pleural effusion"
    elif case == "Ca nasal discharged":
        AppenData = "Pleural effusion"
    elif case == "Pus from pin protusion":
        AppenData = "ETC..."
    elif case == "Pus from abscess":
        AppenData = "Abscess"
    elif case == "Wound @ Lt elbow":
        AppenData = "Wound"
    elif case == "Papulocrustous lesion":
        AppenData = "ETC..."
    elif case == "Chronic open wound":
        AppenData = "Wound"
    elif case == "Pustule not improve after Convenia":
        AppenData = "Abscess"
    elif case == "Surgical site":
        AppenData = "Surgical Site"
    elif case == "Pustule (deep pyoderma)":
        AppenData = "pustule"
    elif case == "Wound exudate":
        AppenData = "Wound"
    elif case == "pus":
        AppenData = "pustule"
    elif case == "Broncho alveolar larvage ในหลอดเพาะเชื้อและในหลอด eppendorf sterile":
        AppenData = "ETC..."
    elif case == "Abdominal cavity":
        AppenData = "Abdominal effusion"
    elif case == "paronychia":
        AppenData = "ETC..."
    elif case == "Bite wound abscess":
        AppenData = "Bite wound"
    elif case == "Infected wound":
        AppenData = "Wound"
    elif case == "Abdo effusion":
        AppenData = "Abdominal effusion"
    elif case == "Rt. tarsal wound":
        AppenData = "Wound"
    elif case == "Exudate from deep pyoderma":
        AppenData = "ETC..."
    elif case == "Open hernia (abdominal cavity)":
        AppenData = "ETC..."
    elif case == "Exudate from mass at dorsal neck":
        AppenData = "ETC..."
    elif case == "Pericardial fluid":
        AppenData = "ETC..."
    elif case == "Abscess wound":
        AppenData = "Wound"
    elif case == "Wound @ right axilla area":
        AppenData = "Wound"
    elif case == "Rt nasal disc":
        AppenData = "Pleural effusion"
    elif case == "Rt. thoracic wall (wound abscess)":
        AppenData = "Wound"
    elif case == "Mass at Lt.thorax":
        AppenData = "ETC..."
    elif case == "Swab แผลที่ขาซ้าย":
        AppenData = "Wound"
    elif case == "Abscess/Exudate":
        AppenData = "Abscess"
    elif case == "หนองจาก cyst ข้างลำตัว":
        AppenData = "Abscess"
    elif case == "Exudate from wound; DDx: Bacterial folliculitis":
        AppenData = "Wound"
    elif case == "Nasal discharge (posterior ventral meatus)":
        AppenData = "Pleural effusion"
    elif case == "Abscess with sinus":
        AppenData = "Abscess"
    elif case == "Wound @ lt pinna":
        AppenData = "Wound"
    elif case == "Pus from wound":
        AppenData = "Wound"
    elif case == "Lt. ear exudate (otitis media)":
        AppenData = "Ear exudate"
    elif case == "Skin (acetate tape : Rod)":
        AppenData = "ETC..."
    elif case == "Opened wound near dermoid cyst":
        AppenData = "Wound"
    elif case == "Bed sore wounds at hip":
        AppenData = "Wound"
    elif case == "ตุ่มหนองที่ผิวหนังหลังคอ":
        AppenData = "Abscess"
    elif case == "fluid":
        AppenData = "Unknow"
    elif case == "Pulmonary mass":
        AppenData = "ETC..."
    elif case == "Right kidney":
        AppenData = "ETC..."
    elif case == "Abdomen (GI perforate)":
        AppenData = "Abdominal effusion"
    elif case == "Exudate from abscess":
        AppenData = "Abscess"
    elif case == "ก้อนที่ผิวหนังด้านข้างลำตัวฝั่งขวา":
        AppenData = "ETC..."
    elif case == "Pleural effusion":
        AppenData = "Pleural effusion"
    elif case == "Orthopedic operation":
        AppenData = "ETC..."
    elif case == "น้ำดี":
        AppenData = "ETC..."
    elif case == "Rt stifle abscess":
        AppenData = "Abscess"
    elif case == "swab":
        AppenData = "ETC..."
    elif case == "pyoderma":
        AppenData = "ETC..."
    elif case == "Wound exudate แผลกดทับ":
        AppenData = "Wound"
    elif case == "Left TECA":
        AppenData = "ETC..."
    elif case == "Cystic calculi":
        AppenData = "ETC..."
    elif case == "Exudate from marsupial prostatic abscess":
        AppenData = "Abscess"
    elif case == "Mass dorsal back":
        AppenData = "ETC..."
    elif case == "Wound Lt 1st digit":
        AppenData = "Wound"
    elif case == "Open wound @ ventral abdomen":
        AppenData = "Wound"
    elif case == "โพรงจมูก และแผล":
        AppenData = "Wound"
    elif case == "แผลที่ไหล่ขวา":
        AppenData = "Wound"
    elif case == "แผลที่ขา":
        AppenData = "Wound"
    elif case == "Bone cyst":
        AppenData = "ETC..."
    elif case == "Open wound (Dog bite) at thorax":
        AppenData = "Bite wound"
    elif case == "Abscess/cyst at right scapula":
        AppenData = "Abscess"
    elif case == "Wd (abscess) left cheek":
        AppenData = "Abscess"
    elif case == "Pus from skin (on cefa + griseofulvin from clinic)":
        AppenData = "ETC..."
    elif case == "Pus from liver mass":
        AppenData = "ETC..."
    elif case == "Nasal swab (both)":
        AppenData = "Pleural effusion"
    elif case == "Chronic bite wound abscess":
        AppenData = "Bite wound"
    elif case == "Purulent exudate from abscess (Rt elbow)":
        AppenData = "Abscess"
    elif case == "แผลทะลุช่องท้อง":
        AppenData = "Wound"
    elif case == "Dog bite wound at neck":
        AppenData = "Bite wound"
    elif case == "Left ureter":
        AppenData = "ETC..."
    elif case == "UB mucosa, urolith":
        AppenData = "Ub mucosa"
    elif case == "Calculi (เอาจากนิ่วในกระเพาะปัสสาวะ)":
        AppenData = "ETC..."
    elif case == "Wound @ perineum area":
        AppenData = "Wound"
    elif case == "Wound @ lumbar":
        AppenData = "Wound"
    elif case == "Tracheobronchial lavage":
        AppenData = "ETC..."
    elif case == "Ear wax (both)":
        AppenData = "Ear exudate"
    elif case == "Fluid stifle jt.":
        AppenData = "ETC..."
    elif case == "Infected wound from rupture mass":
        AppenData = "ETC..."
    elif case == "pododermatitis":
        AppenData = "ETC..."
    elif case == "Pus at gingiva":
        AppenData = "ETC..."
    elif case == "Chronic wound (orthopedic device removed)":
        AppenData = "Wound"
    elif case == "Fistula from dermoid cyst":
        AppenData = "ETC..."
    elif case == "Wound @ left FL":
        AppenData = "Wound"
    elif case == "Exudate from chronic wound":
        AppenData = "Wound"
    elif case == "Opened hernia (intestine)":
        AppenData = "ETC..."
    elif case == "Bite wound at left shoulder":
        AppenData = "Bite wound"
    elif case == "Abdomen (bite wound)":
        AppenData = "Bite wound"
    elif case == "Wound @ right hip mass":
        AppenData = "Wound"
    elif case == "Dog bite wound (around cervical area)":
        AppenData = "Bite wound"
    elif case == "Superficial Sprading Pyoderma":
        AppenData = "ETC..."
    elif case == "Pus from papule":
        AppenData = "ETC..."
    elif case == "Urine (both hindlimb paralysis ต้องบีบ UB)":
        AppenData = "Urine"
    elif case == "Unk":
        AppenData = "Unknow"
    elif case == "Crust from Skin":
        AppenData = "ETC..."
    elif case == "BAL":
        AppenData = "Unknow"
    elif case == "Tail":
        AppenData = "Unknow"
    elif case == "bile":
        AppenData = "Bite wound"
    elif case == "Fistula tract":
        AppenData = "ETC..."
    elif case == "Chronic bite wound (recur)":
        AppenData = "ETC..."
    elif case == "Nasal cavity (Rhinoscopy)":
        AppenData = "ETC..."
    elif case == "Screw site (open wound)":
        AppenData = "Wound"
    elif case == "Dead bone in nasal cavity":
        AppenData = "ETC..."
    elif case == "Fistular tract (bite wound)":
        AppenData = "Bite wound"
    elif case == "Open wound @ OD":
        AppenData = "Wound"
    elif case == "Opened wound//Plate fixation 1 month":
        AppenData = "Wound"
    elif case == "Lt.ear cerumen":
        AppenData = "Ear exudate"
    elif case == "Pus from renal pelvis (left)":
        AppenData = "pustule"
    elif case == "Lt.ear cerumen DDx.: Otitis externa":
        AppenData = "Ear exudate"
    elif case == "Wound at back":
        AppenData = "Wound"
    elif case == "Wound @ right FL":
        AppenData = "Wound"
    elif case == "Right hl mass":
        AppenData = "ETC..."
    elif case == "Surgical wound (Cross pin at left distal femur)":
        AppenData = "Surgical Site"
    elif case == "LHL opened fx":
        AppenData = "ETC..."
    elif case == "Exudate wound":
        AppenData = "Wound"
    elif case == "Nasal cavity rhinoscopy":
        AppenData = "Pleural effusion"
    elif case == "Abscess Lt FL":
        AppenData = "Abscess"
    elif case == "Surgical wound":
        AppenData = "Surgical Site"
    elif case == "Bite wound at neck":
        AppenData = "Bite wound"
    elif case == "Abdominal cavity (Bite wound)":
        AppenData = "Bite wound"
    elif case == "Pustule from skin":
        AppenData = "pustule"
    elif case == "Exudate from Rt carpal joint":
        AppenData = "ETC..."
    elif case == "Abscess หลัง":
        AppenData = "Abscess"
    elif case == "Left ear wax":
        AppenData = "Ear exudate"
    elif case == "Surgical site infection":
        AppenData = "Surgical Site"
    elif case == "Wound @ หน้าเท้า of Lt HL":
        AppenData = "Wound"
    elif case == "Abscess @ neck":
        AppenData = "Abscess"
    elif case == "Nasal mass":
        AppenData = "ETC..."
    elif case == "Opened wound (HBC)":
        AppenData = "Wound"
    elif case == "Abdominal cavity (Uroabdomen)":
        AppenData = "Abdominal effusion"
    elif case == "Pustule (Deep pyoderma)/ pododermatitis":
        AppenData = "pustule"
    elif case == "Exudate  (wound)":
        AppenData = "Wound"
    elif case == "Purulent exudate from Rt chest drain":
        AppenData = "pustule"
    elif case == "Pleural fluid":
        AppenData = "Pleural effusion"
    elif case == "Pus from left kidney":
        AppenData = "ETC..."
    elif case == "Exudate from Lt metaphalanges wound":
        AppenData = "Wound"
    elif case == "Chronic wound at rt. scapular area":
        AppenData = "Wound"
    elif case == "Swab from bite wound":
        AppenData = "Bite wound"
    elif case == "หนองจากตุ่มหนองที่ผิวหนังใต้ท้อง":
        AppenData = "pustule"
    elif case == "Opened wound @ Rt.HL(รถชน) >open bone fx":
        AppenData = "Wound"
    elif case == "Aural exudate":
        AppenData = "ETC..."
    elif case == "UB mucosa (ประวัติ Cytic calculi)":
        AppenData = "Ub mucosa"
    elif case == "Abdominal swab":
        AppenData = "Abdominal effusion"
    elif case == "Purulent exudate pododermatitis /acral lick":
        AppenData = "pustule"
    elif case == "Abscess at back":
        AppenData = "Abscess"
    elif case == "Wound with purulent discharge":
        AppenData = "Wound"
    elif case == "Abscess at left inguinal":
        AppenData = "Abscess"
    elif case == "Salivary mucocele":
        AppenData = "ETC..."
    elif case == "Abscess (1st phalange Rt.HL)":
        AppenData = "Abscess"
    elif case == "Stump pyometra":
        AppenData = "ETC..."
    elif case == "Prostatic abscess":
        AppenData = "Abscess"
    elif case == "Skin exudate":
        AppenData = "ETC..."
    elif case == "Bite wound with open fracture":
        AppenData = "Bite wound"
    elif case == "น้ำในช่องท้อง":
        AppenData = "Abdominal effusion"
    elif case == "Exudate from open wound at Lt.FL":
        AppenData = "Wound"
    elif case == "Exudate from wound at tail":
        AppenData = "Wound"
    elif case == "Open wound":
        AppenData = "Wound"
    elif case == "Pus at skin":
        AppenData = "ETC..."
    elif case == "Chronic close fistula wound":
        AppenData = "Wound"
    elif case == "Mammary abscess":
        AppenData = "Abscess"
    elif case == "Skin/sc abscess at Lt.thorax":
        AppenData = "Abscess"
    elif case == "Deep pyoderma หาง":
        AppenData = "ETC..."
    elif case == "nan":
        AppenData = "Unknow"
    elif case == "Ear swab (Chronic wound otitis)":
        AppenData = "Ear exudate"
    elif case == "Exudate from abscess wound":
        AppenData = "Abscess"
    elif case == "Purulent ear wax (Rt.ear)":
        AppenData = "Ear exudate"
    elif case == "Swab from Lt ear canal":
        AppenData = "Ear exudate"
    elif case == "Swab from Rt ear canal":
        AppenData = "Ear exudate"
    elif case == "Nasal swab":
        AppenData = "ETC..."
    elif case == "Deep exudate":
        AppenData = "ETC..."
    elif case == "Deep Exudate":
        AppenData = "ETC..."
    elif case == "Bite wound at right forelimb":
        AppenData = "Bite wound"
    elif case == "แผลที่ rt tarsal jt.":
        AppenData = "Wound"
    elif case == "Contaminated wound":
        AppenData = "Wound"
    elif case == "Wound @ Rt HL":
        AppenData = "Wound"
    elif case == "Wound @ Rt femur":
        AppenData = "Wound"
    elif case == "Abscess bite wound":
        AppenData = "Bite wound"
    elif case == "Wound @ neck":
        AppenData = "Wound"
    elif case == "Swab หนองที่หู":
        AppenData = "Ear exudate"
    elif case == "Urine เคยได้รับ Amoxy-clav และ Marbofloxacin มาก่อนหน้านี้ ปัจจุบันให้Marbofloxacin อยู่":
        AppenData = "Urine"
    elif case == "skin":
        AppenData = "ETC..."
    elif case == "Fluid from mass (serosang+purulent)":
        AppenData = "pustule"
    elif case == "Exudate from the Rt ear":
        AppenData = "Ear exudate"
    elif case == "Abscess @ left lumbar (recurrent)":
        AppenData = "Abscess"
    elif case == "Sc abscess @ suture line":
        AppenData = "Abscess"
    elif case == "Lt ear exudate":
        AppenData = "Ear exudate"
    elif case == "Wound with purulent discharge / mass":
        AppenData = "Wound"
    elif case == "UB mucosa+urine+calculus":
        AppenData = "Ub mucosa"
    elif case == "Chronic open wound at Rt inguinal":
        AppenData = "Wound"
    elif case == "Fistula track @ ventral neck":
        AppenData = "ETC..."
    elif case == "Wound fistula tract at neck":
        AppenData = "Wound"
    elif case == "Wound with purulent discharge (chronic wound)":
        AppenData = "Wound"
    elif case == "Crust from skin; not improve after AMC":
        AppenData = "ETC..."
    elif case == "Open wound at lumbosacral area":
        AppenData = "Wound"
    elif case == "Nasal mucosa":
        AppenData = "Pleural effusion"
    elif case == "Abscess @ dorsal neck":
        AppenData = "Abscess"
    elif case == "Fluid from renal pelvis":
        AppenData = "ETC..."
    elif case == "Wound / Pregnancy patient":
        AppenData = "Wound"
    elif case == "Lt facial abscess":
        AppenData = "Abscess"
    elif case == "Wound":
        AppenData = "Wound"
    elif case == "Wound at lumbar":
        AppenData = "Wound"
    elif case == "Screw from pelvic":
        AppenData = "ETC..."
    elif case == "Abscess at left lumbar area":
        AppenData = "Abscess"
    elif case == "Abscess (Rt. forelimb)":
        AppenData = "Abscess"
    elif case == "Open hernia":
        AppenData = "ETC..."
    elif case == "Bited wound":
        AppenData = "Bite wound"
    elif case == "Swab from cheek":
        AppenData = "ETC..."
    elif case == "Uterine mucosa":
        AppenData = "Ub mucosa"
    return AppenData


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

@app.route('/GP', methods=['POST'])
def get_data():
    value =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    request_json = request.get_json()
    value[0] = request_json.get('id')
    temp = request_json.get('species')
    le = LabelEncoder()
    le.fit(['Dog', 'Cat', 'cat', 'Feline', 'C'])
    temp = le.transform([temp])
    value[1] = temp
    temp = request_json.get('submitted_sample')
    temp = SumitEncode(temp)
    le.fit(['Wound', 'ETC', 'Ub mucosa', 'pustule', 'ETC...', 'Abscess','Abdominal effusion', 'Ear exudate', 'Urine', 'Surgical Site','Pleural effusion', 'Bite wound', 'Unknow'])
    value[2] = le.transform([temp])
    temp = request_json.get('bact_species_1')
    le.fit(['Staphylococcus schleiferi', 'Staphylococcus pseudintermedius','Enterococcus faecalis', 'Staphylococcus lugdunensis','Lactococcus garvieae', 'Staphylococcus haemolyticus','Staphylococcus hominis ssp hominis','Enterococcus faecium (1.8x105 CFU/ml)','Staphylococcus aureus / Staphylococcus pseudintermedius (1.2x105 CFU/ml)','Staphylococcus pseudintermedius or S. aureus or S. haemolyticus','Streptococcus canis', 'Enterococcus faecium','Enterococcus gallinarum', 'Staphylococcus epidermidis','Streptococcus agalactiae','Staphylococcus pseudintermedius (1.0x103 CFU/ml)','Enterococcus faecium (3.0x103 CFU/ml)', 'Staphylococcus sciuri','Gemella haemolyticus/Gemella sanguinis','Micrococcus luteus/lylae','Staphylococcus pseudintermedius (9.0x103 CFU/ml)','Staphylococcus aureus', 'Streptococcus thoraltensis','Streptococcus pyogenes','Streptococcus dysgalactiae ssp dysgalactiae or Streptococcus sanguinis','Erysipelothrix rhusiopathiae','Staphylococcus caprae or Staphylococcus chromogenes','Streptococcus dysgalactiae ssp equisimilis','Staphylococcus pseudintermedius (2.0x103 CFU/ml)','Staphylococcus pseudintermedius (8.9x104 CFU/ml)','Staphylococcus pseudintermedius (1.2x105 CFU/ml)','Staphylococcus xylosus or Staphylococcus simulans or Staphylococcus chromogenes','Staphylococcus vitulinus or Staphylococcus capitis','Staphylococcus scuiri', 'Staphylococcus caprae','Staphylococcus chromogenes','Staphylococcus lugdunensis (1.0x103 CFU/ml)','Staphylococcus simulans', 'Staphylococcus saprophyticus','Staphylococcus cohnii ssp urealyticus (1.0x103 CFU/ml)','Staphylococcus pseudintermedius (9.4x106 CFU/ml)','Kocuria rosea / Kocuria varians / Kocuria rhizophila','Streptococcus sanguinis', 'Streptococcus infantarius ssp coli','Enterococcus faecalis (1.0x103 CFU/ml)','Unidentified gram positive bacteria (+catalase, -oxidase)','Staphylococcus warneri', 'Staphylococcus cohnii ssp urealyticus','Staphylococcus hominis ssp hominis (3.0x103 CFU/ml)','Kocuria rhizophila','Low discrimination among Staphylococcus aureus, Staphylococcus chromogenes, Staphylococcus pseudintermedius (2.7x105 CFU/ml)','Dermacoccus nishinomiyaensis / Kytococcus sedentarius (2.6x105 CFU/ml)','Streptococcus agalactiae, Streptococcus constellatus ssp constellatus, or Streptococcus dysgalactiae ssp equisimilis','Streptococcus gallolyticus ssp pasteurianus (เลือก Streptococcus agalactiae)','Staphylococcus capitis','Enterococcus faecium (1.4 x 107 cfu/mL)','Staphylococcus hominis ssp hominis / Staphylococcus warneri','Staphylococcus chromogenes (9.4x104 CFU/ml)','Streptococcus iniae', 'Streptococcus pseudoporcinus','Enterococcus faecium (2.9x106 CFU/ml)','Enterococcus gallinarum / Enterococcus faecium (1.0x103 CFU/ml)','Enterococcus faecalis (7.0x103 CFU/ml)','Staphylococcus chromogenes / Staphylococcus warneri','Staphylococcus caprae / Staphylococcus capitis / Staphylococcus warneri','Staphylococcus aureus (1.8x105 CFU/ml)','Enterococcus faecalis (5.0x105 CFU/ml)','Lactococcus garvieae (5.8x106 CFU/ml)','Staphylococcus warneri (1.8x107CFU/ml)','Staphylococcus warneri (2.0x103 CFU/ml)', 'Bacillus spp.','Staphylococcus aureus or Staphylococcus pseudintermedius','Staphylococcus capitis / Staphylococcus hominis ssp hominis / Staphylococcus warneri','Staphylococcus aureus, Staphylococcus chromogenes or Staphylococcus hyicus','Staphylococcus pseudintermedius (5.2x105 CFU/ml)','Staphylococcus pseudintermedius (3.6x104 CFU/ml)','Staphylococcus aureus (2.1x107 CFU/ml)','Enterococcus faecalis (1x103 CFU/ml)','Enterococcus faecium (7.7x104 CFU/ml)','Staphylococcus pseudintermedius (8.1x106 CFU/ml)','Streptococcus parasanguinis','Enterococcus faecium (1.1x107 CFU/ml)','Streptococcus pseudoporcinus (1.5x107 CFU/ml)','Unidentified Gram positive cocci, +Catalase, -Oxidase, -motility','Enterococcus faecium (9.0x103 CFU/ml)','Non or low reactive biopattern (Gram positive bacteria, Rod shape, Positive catalase, Negative oxidase) (2.6x104 CFU/ml)','Streptococcus agalactiae / Streptococcus dysgalactiae ssp equisimilis','Staphylococcus equorum','Staphylococcus pseudintermedius (8.7x104 CFU/ml)','Staphylococcus hyicus', 'Staphylococcus warneri (1.0x103 CFU/ml)','Streptococcus oralis / Streptococcus mitis','Staphylococcus simulans / Staphylococcus chromogenes','Streptococcus pneumoniae','Enterococcus casseliflavus / Enterococcus gallinarum','Staphylococcus hominis ssp hominis (8.0x104 CFU/ml)','Staphylococcus aureus (4.2x104 CFU/ml)','Staphylococcus epidermidis (2.0x103 CFU/ml)','Streptococcus mitis / Streptococcus oralis','Staphylococcus pseudintermedius (8.2x105 CFU/ml)','Staphylococcus auricularis','Staphylococcus pseudintermedius (2.5x105 CFU/ml)','Non or Low reactive biopattern (1.3x105 CFU/ml)','Staphylococcus hominis ssp hominis or Staphylococcus hominis ssp novobiosepticus','Streptococcus anginosus','Staphylococcus caprae / Staphylococcus chromogenes / Staphylococcus warneri','Kocuria virians (2.3x104 CFU/ml)','Staphylococcus caprae (2.3x104 CFU/ml)','Staphylococcus aureus / Staphylococcus schleiferi','Enterococcus faecalis (2.2x106 CFU/ml)','Enterococcus faecium (2.0x103 CFU/ml)', 'Enterococcus hirae','Staphylococcus pseudintermedius (7.0x105 CFU/ml)','Streptococcus pseudoporcinus / Streptococcus dysgalactiae ssp equisimilis','Granulicatella adiacens (เลือกยา Streptococcus agalactiae)','Enterococcus faecium (>105 CFU/ml)','Streptococcus canis (2.0x103 CFU/ml)','Enterococcus faecium (4.0x103 CFU/ml)','Enterococcus faecium (8.8x104 CFU/ml)','Streptococcus pseudoporcinus / Streptococcus pyogenes','Enterococcus faecium (4x103 CFU/ml)','Staphylococcus aureus/Staphylococcus pseudintermedius','Staphylococcus simulans /Staphylococcus chromogenes /Staphylococcus xylosus','Kocuria rhizophila (6.2x104 CFU/ml)','Staphylococcus warneri (>105 CFU/ml)','Staphylococcus capitis/ Staphylococcus caprae/ Staphylococcus warneri','Streptococcus pluranimalium','Staphylococcus simulans, Staphylococcus chromogenes or Staphylococcus xylosus','Enterococcus faecium (1.4x105 CFU/ml)','Enterococcus faecium (4.1x104 CFU/ml)','Enterococcus faecalis (>105 CFU/ml)', 'Enterococcus cecorum','Enterococcus faecalis (1.6x104 CFU/ml)','Globicatella sanguinis (>105 CFU/ml)', 'Staphylococcus lentus','Enterococcus durans / Enterococcus hirae','Low discrimination (6.3x106 CFU/ml)','Streptococcus agalactiae, Streptococcus anginosus, Streptococcus gordonii','Enterococcus durans (2.6x104 CFU/ml)','Staphylococcus caprae (1.0x103 CFU/ml)','Staphylococcus chromogenes/Staphylococcus pseudintermedius','Staphylococcus aureus (>105 CFU/ml)','Staphylococcus chromogenes / Staphylococcus lugdunensis / Staphylococcus warneri','Staphylococcus pseudintermedius (4.7x104 CFU/ml)','Staphylococcus chromogenes (1.7x106 CFU/ml)','Staphylococcus pseudintermedius (1.5x106 CFU/ml)','Staphylococcus simulans (2.8x104 CFU/mlX','Enterococcus faecium (1.2x106 CFU/ml)','Enterococcus faecium (1.2x105 CFU/ml)'])
    value[3] = le.transform([temp])
    temp = request_json.get('Cefoxitin')
    le = LabelEncoder()
    le.fit( ['-', 'nan', '+', '*+', 'S'])
    value[4] = le.transform([temp])
    temp = request_json.get('Benzyl penicillin')
    le.fit(['S', 'R', 'nan', 'R*', '*S', '*R','-'])
    value[5] = le.transform([temp])
    value[6] = le.transform([request_json.get('Amoxicillin/clavulanic acid')])
    value[7] = le.transform([request_json.get('Oxacillin')])
    value[8] = le.transform([request_json.get('Cephalothin')])
    value[9] = le.transform([request_json.get('Cefpodoxime')])
    value[10] =le.transform([request_json.get('Cefovecin')])
    value[11] =le.transform([request_json.get('Gentamicin')])
    value[12] =le.transform([request_json.get('Enrofloxacin')])
    le.fit(['-', 'nan', '+', '*+', 'S'])
    value[13] = le.transform([request_json.get('Inducible clindamycin')])
    le.fit(['S', 'R', 'nan', 'R*', '*S', '*R','-'])
    value[14] =le.transform([request_json.get('Erythromycin')])
    value[15] =le.transform([request_json.get('Clindamycin')])
    value[16] =le.transform([request_json.get('Vancomycin')])
    value[17] =le.transform([request_json.get('Tetracycline')])
    value[18] =le.transform([request_json.get('Nitrofurantoin')])
    value[19] =le.transform([request_json.get('Fusidic acid')])
    value[20] =le.transform([request_json.get('Mupirocin')])
    value[21] =le.transform([request_json.get('Chloramphenicol')])
    value[22] =le.transform([request_json.get('Rifampicin')])
    value[23] =le.transform([request_json.get('Sulfamethoxazole/trimethoprim')])
    le.fit(['-', 'nan', '+', '*+', 'S'])
    value[24] =le.transform([request_json.get('Ampicillin')])
    le.fit(['S', 'R', 'nan', 'R*', '*S', '*R', '-'])
    value[25] =le.transform([request_json.get('Cefotaxime')])
    value[26] =le.transform([request_json.get('Ceftriaxone')])
    value[27] =le.transform([request_json.get('Levofloxacin')])
    value[28] =le.transform([request_json.get('Linezolid')])
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


if __name__ == "__main__":
    app.run(debug=True)