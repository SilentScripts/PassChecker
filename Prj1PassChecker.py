import getpass
import string
import random
import pygal


#Method used to check with the other main methods, if the password entered is strong or not
def passValidation(anonymous):
    
    #To check the length of the users password
    pwLength = passWdLength(anonymous)
    
    #To check if the user's password has Captial letters
    pwUpLow = passUpLow(anonymous)
    
    #To check if there are numbers in the user's password
    pwNumb = passNumb(anonymous)
    
    #To check if the password has at least one special character
    pwSpecials = passSpecials(anonymous)
    
    #To check if whitespaces are found
    pwSpaces = passSpaceCheck(anonymous)
    
    #To check if input is a commonly used password
    pwCommon = commonPasswords(anonymous)
    
    #Result to check whether or not the password is strong
    if pwLength and pwUpLow and pwNumb and pwSpecials and pwSpaces and pwCommon:
        print("\n\n[System]: You have a very strong password, good job!")  
    else:
        print("\n\n[System]: Not good, this password isn't strong enough.")


#Method used to give information on how to create a strong password
def passInstructions():
    print("What makes a STRONG password:")
    print("- A strong password is at least 14 characters long, this program checks if its 14-24 characters long")
    print("- The password must include both uppercase and lowercase")
    print("- Numeric characters are also needed in your passwords")
    print("- Special characters, often forgotten but very important for making your password more secure")
    print("- There are no whitespaces in a password, it will not work on any site.")
    print("- Avoid using very simple or common passwords eg. (names, dictionnary words, etc.)\n\n")


#Method used to verify the length of passwords
def passWdLength(anonymous):
    wdLength = len(anonymous)
    if wdLength < 14:
        print(listOfErrors("[EC]_MIN_LENGTH"))
        return False
    elif wdLength > 24:
        print(listOfErrors("[EC]_MAX_LENGTH"))
        return False
    return True


#Method used to check if both upper and lower case are found in the password
def passUpLow(anonymous):
    upperExists = False
    lowerExists = False
    
    for char in anonymous:
        if char.isupper():
            upperExists = True
        if char.islower():
            lowerExists = True

    if not upperExists:
        print(listOfErrors("[EC]_MISSING_UPPERCASE"))
    if not lowerExists:
        print(listOfErrors("[EC]_MISSING_LOWERCASE"))
    
    if not upperExists or not lowerExists:
        return False
    else:
        return True


#Method used to check if numbers are found in the password
def passNumb(anonymous):
    digitExists = False
    
    for char in anonymous:
        if char.isdigit():
            digitExists = True
    
    if not digitExists:
        print(listOfErrors("[EC]_MISSING_NUMBER_VAL"))
        return False
    else:
        return True


#Method used to check if special characters are found in the password
def passSpecials(anonymous):
    special = string.punctuation
    
    for char in anonymous:
        if char in special:
            return True
    
    print(listOfErrors("[EC]_MISSING_SPECIAL_CHAR"))
    return False


#Method used to check if whitespaces are found in the password
def passSpaceCheck(anonymous):
    if " " in anonymous:
       print(listOfErrors("[EC]_WHITE_SPACE"))
       return False
    else:
       return True 


#Method used to check if the password is a commonly used
def commonPasswords(anonymous):
    try:
        with open("/Applications/Programming/PythonProgrammin/Project1_PasswordChecker/common_passwords.txt") as x:
            lines = x.readlines()
            for line in lines:
                if line.rstrip() == anonymous:
                    print(listOfErrors("[EC]_COMMON_PASSWORD"))
                    return False
    except FileNotFoundError:
        print("Error: Common passwords file not found.")
    return True


#List of errors (reasons why it is not a good password)
def listOfErrors(code):
    # Define error codes and their corresponding messages for program validation
    errors = {
        "[EC]_MIN_LENGTH": "[EC]_MIN_LENGTH: The input does not meet the minimum required length criteria defined by the program.",
        "[EC]_MAX_LENGTH": "[EC]_MAX_LENGTH: The input exceeds the maximum allowed limit as per the program's specifications.",
        "[EC]_MISSING_UPPERCASE": "[EC]_MISSING_UPPERCASE: The input is missing uppercase that is mandatory.",
        "[EC]_MISSING_LOWERCASE": "[EC]_MISSING_LOWERCASE: The input is missing lowercase that is mandatory.",
        "[EC]_MISSING_NUMBER_VAL": "[EC]_MISSING_NUMBER_VAL: The input fails to meet the required character type(s), such as numeric characters as needed by the program.",
        "[EC]_MISSING_SPECIAL_CHAR": "[EC]_MISSING_SPECIAL_CHAR: The input is missing at least one special character that is mandatory.",
        "[EC]_WHITE_SPACE": "[EC]_WHITE_SPACE: Whitespaces are not allowed in passwords.",
        "[EC]_COMMON_PASSWORD": "[EC]_COMMON_PASSWORD: This password is too simple/common therefore, it is not safe for account protection."
    }

    # To check if the provided code exists in the errors dictionary and return the corresponding message
    return errors.get(code, "Invalid error code provided.")  # Default message if the error code is not found


#Main menu of of the program
def passMenu():
    valide = False
    optionPicked = input(
        "\n\n\nSystem: "
        "\n     Option 1: [Password Health Check] (Simple checker that tells you why your password isn't strong if it is weak.)"
        "\n     Option 2: [Password suggestion] (I will propose a strong password you can use.)"
        "\n     Option 3: [Brute-force time calculator] (I will calculate an average time it would take for your password to be comprimised.)"
        "\n     Option 4: [Complexity and Score analyzer] (I will show how complexe your password is and rate it /10 for how strong it is)"
        "\n     Option 5: [End the program]"
        "\n\nOption chosen: "
    ).strip()
    
    while not valide and optionPicked != "5":
        if optionPicked.isdigit():
            if optionPicked == "1":
                password = getpass.getpass("\n\n[System] Enter a password and we'll check if it is strong or not:\n")
                while len(password) > 24:
                    password = getpass.getpass("Try again (Maximum 24 characters): ")
                passValidation(password)
                valide = True
                
            elif optionPicked == "2":
                passSuggestion()
                valide = True
                
            elif optionPicked == "3":
                anonymous = getpass.getpass("\n\n[System] Enter a password and we'll give a rundown how strong the password is:\n").strip()
                while len(anonymous) > 24:
                    anonymous = getpass.getpass("Try again (Maximum 24 characters): ")
                BForceCalc(anonymous)
                valide = True
                
            elif optionPicked == "4":
                anonymous = getpass.getpass("\n\n[System] Enter a password and we'll give a detailed analysis:\n").strip()
                while len(anonymous) > 24:
                    anonymous = getpass.getpass("Try again (Maximum 24 characters): ")
                complexityDataScore(anonymous)
                valide = True
                
            elif optionPicked == "5":
                valide = True
                
            else:
                optionPicked = input("\nPlease pick one of the options listed in the menu.\n\nOption chosen: ")
        else:
            optionPicked = input("\n[System] That wasn't a number. Try again.\n\nOption chosen: ")
            
    return str(optionPicked)


#Method used to create a strong password for user to use
def passSuggestion():
    newPasswordGenerated = ""
    special = string.punctuation
    passRndLength = random.randint(14,24)
    
    newPasswordGenerated += random.choice(special)
    newPasswordGenerated += str(random.randint(0, 9))
    newPasswordGenerated += random.choice(string.ascii_uppercase)
    newPasswordGenerated += random.choice(string.ascii_lowercase)
    
    while len(newPasswordGenerated) < passRndLength:
        characterChosen = random.choice(["special", "number", "upper", "lower"])
        if characterChosen == "special":
            newPasswordGenerated += random.choice(special)
            
        elif characterChosen == "number":
            newPasswordGenerated += str(random.randint(0, 9))
            
        elif characterChosen == "upper":
            newPasswordGenerated += random.choice(string.ascii_uppercase)
            
        elif characterChosen == "lower":
            newPasswordGenerated += random.choice(string.ascii_lowercase)

    
    passGenCharList = list(newPasswordGenerated)
    random.shuffle(passGenCharList)
    result = ''.join(passGenCharList)
    newPasswordGenerated = result
    
    if len(newPasswordGenerated) == passRndLength:
        print("\nHere is your new password: " + newPasswordGenerated + "\n")


#Mini function used to get the parameters for the BruteForce and Complexity functions
def passData(anonymous):
    special = string.punctuation
    lowCaseAlphaRange = len(string.ascii_lowercase)
    UppCaseAlphaRange = len(string.ascii_uppercase)
    numberRange = len(string.digits)
    SpeCharRange = len(special)
    spaceDepth = 0
    
    lowerExist = False
    upperExist = False
    digitsExist = False
    punctExist = False
    
    dataDictionary = {
        "lowChar": 0,
        "upChar": 0,
        "numbChar": 0,
        "punChar": 0
    }
    
    for char in anonymous:
        if char.islower():
            lowerExist = True
            dataDictionary["lowChar"] += 1
            
        if char.isupper():
            upperExist = True
            dataDictionary["upChar"] += 1
            
        if char.isdigit():
            digitsExist = True
            dataDictionary["numbChar"] += 1
            
        if char in special:
            punctExist = True
            dataDictionary["punChar"] += 1
    
    if lowerExist:
        spaceDepth += lowCaseAlphaRange
    if upperExist:
        spaceDepth += UppCaseAlphaRange
    if digitsExist:
        spaceDepth += numberRange
    if punctExist:
        spaceDepth += SpeCharRange
        
    
    return dataDictionary, spaceDepth


#Gives a more in-depth analysis on the password to be used
def BForceCalc(anonymous):
    _, spaceDepth = passData(anonymous)
        
    total_hashes = spaceDepth ** len(anonymous)
    
    hashDict = {
        "hashcat_Est_Time": total_hashes/30000000000,
        "hydra_Est_Time": total_hashes/100,
        "patator_Est_Time": total_hashes/500
    }
    
    est_results = {}

    for tool, value in hashDict.items():
        if value < 1:
            est_results[tool] = "almost instantly"
        elif value < 60:
            est_results[tool] = str(int(value)) + " seconds"
        elif value < 3600:
            est_results[tool] = str(int(value / 60)) + " minutes"
        elif value < 86400:
            est_results[tool] = str(int(value / 3600)) + " hours"
        elif value < 31536000:
            est_results[tool] = str(int(value / 86400)) + " days"
        else:
            est_results[tool] = str(int(value / 31536000)) + " years"
    
        
    hashCatResult = est_results["hashcat_Est_Time"]
    hashHydraResult = est_results["hydra_Est_Time"]
    hashPatResult = est_results["patator_Est_Time"]
    
    expcd_results = {
        "hashcat_Est_Time": hashDict["hashcat_Est_Time"]/2,
        "hydra_Est_Time": hashDict["hydra_Est_Time"]/2,
        "patator_Est_Time": hashDict["patator_Est_Time"]/2
    }
    
    
    for tool, value in expcd_results.items():
        if value < 1:
            expcd_results[tool] = "almost instantly"
        elif value < 60:
            expcd_results[tool] = str(int(value)) + " seconds"
        elif value < 3600:
            expcd_results[tool] = str(int(value / 60)) + " minutes"
        elif value < 86400:
            expcd_results[tool] = str(int(value / 3600)) + " hours"
        elif value < 31536000:
            expcd_results[tool] = str(int(value / 86400)) + " days"
        else:
            expcd_results[tool] = str(int(value / 31536000)) + " years"
    
    
    hashcat_Expected_Result = expcd_results["hashcat_Est_Time"]
    hydra_Expected_Result = expcd_results["hydra_Est_Time"]
    patator_Expected_Result = expcd_results["patator_Est_Time"]
    
    
    print("\n     -- SUMMARY ANALYSIS --      \n"
          "\nPassword length: " + str(len(anonymous)) + 
          "\nSpace Depth: " + str(spaceDepth) +
          "\nTotal guesses: " + str(total_hashes) +
          
          "\n\nEstimated time (not definitive but plausible): " + 
          "\n- Hashcat (GPU, SHA1 @ 30B H/s): " + hashCatResult +
          "\n- Hydra (SSH @ 100 H/s): " + hashHydraResult +
          "\n- Patator (HTTP @ 500 H/s): " + hashPatResult +
          
          "\n\nExpected time (average case):" +
          "\n- Hashcat: " + hashcat_Expected_Result +
          "\n- THC-Hydra: " + hydra_Expected_Result +
          "\n- Patator: " + patator_Expected_Result)
        

#Gives the user an analysis of how complexe their password is then rates it 1-10 for its strength level
def complexityDataScore(anonymous):
    status = commonPasswords(anonymous)
    advice = ""
    
    if status == True:
        status_result = "✅ Not a common password"
    else:
        status_result = "❌ Is a common password"
    
    dataDict, spaceDepth = passData(anonymous)
    
    resultScore = 0
    
    if dataDict["lowChar"] > 0:
        resultScore += 1
    if dataDict["upChar"] > 0:
        resultScore += 1
    if dataDict["numbChar"] > 0:
        resultScore += 1
    if dataDict["punChar"] > 0:
        resultScore += 1
        
    if len(anonymous) >= 14 and len(anonymous) <= 19:
        resultScore += 1
    elif len(anonymous) >= 20 and len(anonymous) <= 24:
        resultScore += 2
        
    if spaceDepth >= 60:
        resultScore += 2
    elif spaceDepth >= 30 and spaceDepth < 60:
        resultScore += 1
    else:
        resultScore += 0
        
    if status == True:
        resultScore += 2
        
    
    if resultScore >= 0 and resultScore <= 3:
        resultDesc = "WEAK"
    elif resultScore >= 4 and resultScore <= 7:
        resultDesc = "MODERATE"
    else:
        resultDesc = "STRONG"
    
    
    print("\n------------------------------------------------" +
          "\n\nPassword Complexity & Strength Evaluation" +
          "\n\n------------------------------------------------" +
          "\n\n     Password length: " + str(len(anonymous)) +
          "\n     Character set size: " + str(spaceDepth) +
          "\n\n     Character type breakdown:" +
          "\n       - Lowercase letters: " + str(dataDict["lowChar"]) +
          "\n       - Uppercase letters: " + str(dataDict["upChar"]) +
          "\n       - Numbers: " + str(dataDict["numbChar"]) +
          "\n       - Special characters: " + str(dataDict["punChar"]) +
          "\n\n     Status: " + status_result +
          "\n\n     Strength score: "+ str(resultScore) +"/10 (" + resultDesc + ")" +
          "\n\n------------------------------------------------")
    
    
    complexityVisDict = {
        "length": len(anonymous),
        "depth": spaceDepth,
        "lower": dataDict["lowChar"],
        "upper": dataDict["upChar"],
        "numb": dataDict["numbChar"],
        "special": dataDict["punChar"],
        "result": resultScore
    }
    
    
    complexityVisDict = visualCalc(complexityVisDict)
    
    visual_Chart = pygal.SolidGauge(inner_radius=0.50)
    
    visual_Chart.add("Password Length:", [{'value': complexityVisDict["length"], 'max_value': 100}])
    visual_Chart.add("Character set size:", [{'value': complexityVisDict["depth"], 'max_value': 100}])
    visual_Chart.add("Lowercase letters:", [{'value': complexityVisDict["lower"], 'max_value': 100}])
    visual_Chart.add("Uppercase letters:", [{'value': complexityVisDict["upper"], 'max_value': 100}])
    visual_Chart.add("Numbers:", [{'value': complexityVisDict["numb"], 'max_value': 100}])
    visual_Chart.add("Special characters:", [{'value': complexityVisDict["special"], 'max_value': 100}])
    visual_Chart.add("Strength score:", [{'value': complexityVisDict["result"], 'max_value': 100}])

    
    visual_Chart.render_to_file('visual_Chart.svg')


#Pygal visual adaptation of Complexity data score
def visualCalc(complexDict):
    score = {
        "length": 0,
        "depth": 0,
        "lower": 0,
        "upper": 0,
        "numb": 0,
        "special": 0,
        "result": 0
    }
    
    for key, rawValue in complexDict.items():
        if key == "length":
            score["length"] = int((rawValue / 24) * 100)
        
        elif key == "depth":
            score["depth"] = int(min((rawValue * 100) / 60, 100))
            
        elif key == "lower":
            score["lower"] = int(min((rawValue * 100)/ complexDict["length"], 100))
        
        elif key == "upper":
            score["upper"] = int(min((rawValue * 100)/ complexDict["length"], 100))
        
        elif key == "numb":
            score["numb"] = int(min((rawValue * 100)/ complexDict["length"], 100))
        
        elif key == "special":
            score["special"] = int(min((rawValue * 100)/ complexDict["length"], 100))
            
        else:
            score["result"] = rawValue * 10

    return score


print("\n\n -- Welcome to PassChecker.io -- \n\n")

passInstructions()

password = getpass.getpass("[System] Enter a password and we'll check if it is strong or not:\n")

passValidation(password)

option = passMenu()
while option != "5":
    option = passMenu()

