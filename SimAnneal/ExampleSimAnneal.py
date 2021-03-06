#Example 1: To solve a transposition cipher using the SimAnneal library

#It tends to be the later transpositions that use this method. Use other program - transposition AUTO Row if it's read off by row
#This program will automatically run through all possible keys up to length ten, using the read off by columns method This is the method employed by Practical and by default by dcode.fr.

#Import required modules
import copy
import math
import collections
from statistics import QuadgramSetup, GetLikelihood
from utilities import InputText
import itertools
import simAnneal

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Setup quadgram fitness scores
QuadgramSetup()

#temp on same order of magnitude as cost. AND critically cost increases with worseness
def scaledQuadgram(text):
    return 5000*(1-(GetLikelihood(text))/(35000))

scaledQuadgram("AAGYBWWADBLKNKTAAONHIWTGRNPETEESSTDLNEYEOIEETUNADTAWOSNAIRNRUTHAOFTPSYEEUAAHTSUECOWICTDDASYREEITTTELHDSOISVKHNILTTEYTORWAEEDASAYBEREIMEOXGENSATGTNLORTPERRREIAINIHEANAIEHATOACUESMDUCLOGTLNSLAAENONWATDTELHBSSEDKAISOVTDEMONMRYTNGDNUFIVIREESLHEUECEIEISAYRIALDROAITODIMNTIOITSRHDPCEYTAGTHAAIETREIEOEFDEECLWETHSIEOETLIINUCTVEEMRWYEILWNEBOIFHUAOWRTGSHNONGEGECPLLHWANHDCNHNSCTENITECAWMBWRMPNRWRHCEIAAAOHOLTHEAOSNNSDSYEGBSHTHAREFPRNTOEEGCTHTEKAYCGWDLGGDATOWATULTVBNLWOPEOODCEEYIOGTLWNIOTUOGWTNLSOVNANNMLYIOJFATEARIRPATTOGOHMNIIENTVBTSTTIATRRSECITNAFLITROIMOCEIRTDHAATESAAITEARFIAOSEODNAPOTTIRRETGYIDEOMIWTTOOETRAAVHETOHNEEPSCMANMCAEOSEGTYNOMSSIGTLIHTFEISKIGSEMNBOENAIEHUITARAMORIAIIEHHIIALONCDHNFLOAOFOTYHRNOBTARLFTHNEHLNWRLFENOTAOAONUETOOEUTYTIDEEPTNWUHTDREHUBNESSTTBEHNONRHTDREIAOEHRAFIAWHHBPIEHYCTKHEWHNPSKUTIMLNVHIHTICARONVAEDLRFIEOSONNOWOCOTESRTTINIIBNHNSCIIOYATAEOTORURHATAHSDEEBMAIHIEEECUWDMCTLGDKATHRFIIINEULGNAITOEWRLEEAEIRMRUNEOIVIETEYDEUAEEHEDOWOORTEIETOGMRWFNUTSLDTISLWIDTNCINEORUIREEROARIOWRKIESRYEERPHOUTNYTOEPWHIEAYUERSMRHTATVGCHEFNSHIONMIEAHDEAEGVWLHLMSGSHWEOSPPALFNLHSTUWFTATNDHEEEHESWKHSTREIELAWRDEIOBESIHOYININILABAILERGEATIALNTLTRTEIFEITRIGNWODSVSOTACESEWIAYTHLTSEEYEIRENSHIETLEITTRWTRTAEHEIIEWIRTUUIHLLRDYHHDHGDPHLNTHROLIVIEVSDYLOTMOYDHPLIAYEVHAWSWEAONLAEHEETTHACDHIFHBLAHCCLEMSGWSPFENNPIWTNSHFOLLNHDSETNTICFRIOTIUIHCIFRAUTNIVUODHHSMFBHARCEADHNANTAIALELTASTNVAREHETGATANHEVNEHINNNETRCDOGUVRSTSRETCWRSNAMSDSSNWIENNNDNMHTEITLTDFTKHIYIETOTTAIIYAGTADDOAYTATUATNTNTTDPFDTSHTWDEDLIOARANHIHUNNOOGIORANDRUIRSATFSDULUEGSTAYUINUEELRTLRTEMAHERHTLOIEYEATOOTYCOAEIBEHOTETEMSHATOSNINNESEEGRENNIRITNTCYYIOTISYECELASAOHRHNRELEFTEPWAYOEOYARIAUSEALGIULOEUHTBRASTNTASLHTKNTSSBHSGALOAPNNRIAADLKAHIOYGNIMLTRAOYIUWNYYAULHUEOOTASKSNAOFSACEMPILTCOHALETAWPRRTOAOHMIUOAETOMIUDANEHHETITODLLEYTDASWFTTNRACTTTATAOOTLTEDAGHEIMOTOCOLLTNREOTRCYDKGEYSIGAWEOSNAKHMLITINSTENEGSEHINCOMETDSMTLACMAAERTMVLPIDDENIHFIEOEHSBENSROSOANIWTDLNLEBHBLITROOHEISSOLIITLNCFTSEWROHYNYEUNSVNNSAUUEAMRYNIEAIIOOITIITIDTOFVPEWNCYAWTNFROIERSNMTAEINOONTSWGLNEOAGHOERHAONAOEULEEIOTWORTSOTIITORHBTIROFALTERDDHTSNLTMATTRTNEANAAKEHTNESUOYETEIUECLTTTOILVEWRRLENLETAUCEKOSHXSRRBNLLDEDMORCGTAWOEMDNTAEEAUYKSSAOCORATAATKANHFSDAIEARWCEPAVTSNENANDEUEWPTDOTOTTHOUTOHSCSWITIAWYIOHEHTOHIENTTRCMIGEEE")
scaledQuadgram("HARRYIFYOUAREREADINGTHISTHENYOUAREPROBABLYALSOWONDERINGWHEREIAMIAMSORRYTODISAPPEARBUTIHAVEALOTTOTHINKABOUTANDNEEDTOWORKTHINGSOUTONMYOWNIAMONTHETRAINTOMASSOURIENOWANDHOPINGTHATIWILLFINDTHEANSWERSINEEDTHERETHOUGHIHAVEALREADYBEGUNTOPUTTHEPIECESTOGETHERTHESTORYSTARTEDATMICHAELFARADAYSLIGHTHOUSEATTRINITYWHARFANDTHATSHOULDHAVEBEENABIGCLUEESPECIALLYWITHTHEREFERENCETOTHEFACILITYINFLORENCESLETTERTOHIMWETAKEITSOMUCHFORGRANTEDNOWTHATWEMISSEDTHEIMPORTANCEOFTHATPLACEITWASWHENILOOKEDINTOSOUTERPOINTTHATIREALISEDWHYITMIGHTBERELEVANTANDNOWASITRAVELTHROUGHTHEFOOTHILLSOFTHEHIMALAYAITISALLCOMINGINTOFOCUSTHEATTACHEDREPORTWASDISCOVEREDBYONEOFTHEELVESINTHELAMPATSOUTERPOINTANDWASCLEARLYLEFTTHEREFORMETOFINDIAMSTILLNOTSUREWHATTHECONSPIRACYSETOUTTODOBUTINOWKNOWTHESIGNIFICANCEOFTRINITYWHARFANDSOUTERANDICANTAKEAGOODGUESSATWHYTHEYWEREINTERESTEDINGEORGEEVERESTSHOUSEINTHEMOUNTAINSIDONTKNOWWHYITHINKTHEREMIGHTSTILLBESOMETHINGTOFINDTHEREBUTSINCETHECONSPIRACYISCLEARLYSTILLACTIVEIHAVETOKNOWWHATTHEYAREDOINGANDTHISISTHEONLYLEADIHAVETHECONNECTIONBETWEENTHEEARLYCONSPIRATORSISALSOMUCHCLEARERTOMENOWTHEYALLHADANINTERESTINMATHEMATICSANDTHENATURALSCIENCESADALOVELACEWASAKEYMEMBEROFBABBAGESTEAMWITHHEREARLYEXPERIMENTSWITHPROGRAMMINGMARYEVERESTBOOLEWASANEXPERTINLOGICHIGHLYEDUCATEDANDWELLVERSEDININDIANMATHEMATICALTHOUGHTATFIRSTFLORENCENIGHTINGALEDOESNTLOOKLIKEAGREATFITWITHTHEGROUPSHEISCELEBRATEDMOREFORMODERNISINGNURSINGBUTHERINNOVATIONSWEREBASEDONSERIOUSDATAANALYSISUSINGEVERYTHINGSHEKNEWABOUTSTATISTICSANDTHATWASALOTCAROLINEHERSCHELWASANOTHERREMARKABLEWOMANTHEFIRSTTOBEPAIDASALARYASASCIENTISTBUTITHINKHERROLEWASSOMETHINGMORESHEHADHUGEINFLUENCEINSOCIETYANDALSOHELDAPOSITIONINGOVERNMENTLIKECHARLIEANDTRINITYSHEWASTECHNICALLYGIFTEDANDWELLPLACEDTOTAKEFULLADVANTAGEOFTHOSEGIFTSINEEDTOKNOWWHATTHEYARETRYINGTODOWHYANDHOWTRINITYWARNEDMENOTTOTELLYOUABOUTHERLETTERBUTTHATWASNEVERAPOSSIBILITYEVENIFIDIDNTLETYOUKNOWWHATWASGOINGONIAMPRETTYSURETHATYOUWOULDHAVEFOUNDOUTANDIWOULDMUCHRATHERTELLYOUMYSELFTHEONLYREASONIDIDNTCOMETOYOUSTRAIGHTAWAYISTHATISTILLDONTKNOWWHATISGOINGONANDIDIDNTWANTTOPUTYOUINTHEDIFFICULTPOSITIONOFHAVINGTODECIDEWHETHERTOTRUSTMEORNOTHOPEFULLYTHISVISITWILLPROVIDETHEEVIDENCEWENEEDTOUNRAVELTHECONSPIRACYANDTOCLEARMYNAMEIWILLWRITETOYOUAGAINWITHNEWSFROMTHEPARKJODIE")

#Simulated Annealing parameters
TEMP_INIT = 10000
COOLING_RATE = 0.03

#Get text and strip punctuation and spaces
text = InputText()


#Before any padding applied
originalText = text



def decrypt(cipherText,key,alphKey):
    """Decrypt transposition cipherText with key"""

    #Efficiency boost: produce reverse key map from value to index in key.
    reverseMap = {a : i for i,a in enumerate(key)}
    #print(reverseMap)

    chars = [] #stores the characters read off in the correct order to produce the transposition rectangle.
    rows = int(len(cipherText)/len(key))  #Compute number of rows in the matrix

    #Rotate text into matrix as required
    for i in range(len(key)):
        chars.append(cipherText[i*rows:(i+1)*rows])

    #Will store resulting columns in correct order
    columns = [[] for i in range(len(chars))]
   # print(columns)

    #Perform the reordering
    for i,char in enumerate(alphKey):
     #   print(char)
        columns[reverseMap[char]] = chars[i]
        key = key[:reverseMap[char]] + " " + key[reverseMap[char] + 1:]

    #Read off:
    # H E L L O
    # G O O D F
    # R I E N D
    finalReadout = ""
    #print(columns)
    for i in range(len(columns[0])):
        for col in columns:
            finalReadout += col[i]

    
    return finalReadout

for keyLength in range(9,15):

    #Pad if required
    if len(originalText) % keyLength != 0:
        paddedText = originalText + (((((len(originalText) // keyLength) + 1) * keyLength) - len(originalText)) * ".")
    else:
        paddedText = originalText

    score = -100000
    bestText = ""
    for i in range(1):
        bestResult = simAnneal.simAnneal(TEMP_INIT,ALPHABET[:keyLength],lambda key : float(scaledQuadgram(decrypt(paddedText,key,ALPHABET[:keyLength]))),COOLING_RATE)
        if GetLikelihood(decrypt(paddedText,bestResult,ALPHABET[:keyLength])) > score:
            score = GetLikelihood(decrypt(paddedText,bestResult,ALPHABET[:keyLength]))
            bestText = bestResult

    print(decrypt(paddedText,bestResult,ALPHABET[:keyLength]))
    print("With key length "+ str(keyLength) +" the best key is " +  str(bestResult))
    print("Score: " + str(GetLikelihood(decrypt(paddedText,bestResult,ALPHABET[:keyLength]))))
    print("\n")
