__author__ = 'linglin'
"""
Generate the hint id for problem_skill.json and hint image references for hints.json,
according to skill_problem.json as where is
the start & end of hint-img-index of one problem.
"""

from os.path import expanduser
from collections import OrderedDict
import json
import re
import codecs




class HintUtil(object):

    def setSettings(self, grade_id=2, section_id="1.1", numbersofHintsperProblem=[3]):
        home = expanduser("~")

        th_str = "th"
        if grade_id == 3 : th_str = "rd"
        elif grade_id == 2 : th_str = "nd"
        elif grade_id == 1 : th_str = "st"

        self.hints_name1 = home + '/Documents/skill_hints.json'
        self.hints_name = home + "/mathjoy/app/static/src/data/math/" + str(grade_id) + th_str + "/" + section_id + "/hints.json"

        self.problem_name1 = home + "/Documents/skill_problem.json"
        self.problem_name = home + "/mathjoy/app/static/src/data/math/" + str(grade_id) + th_str + "/" + section_id + "/skill_problem.json"

        self.problem_out = home + "/Documents/skill_problem_out.json"
        self.hints_out = home + '/Documents/skill_hints_out.json'

        self.hints_infile1 = home + "/Documents/skill_content.txt"
        self.hints_infile = home + "/Downloads/Grade " + str(grade_id) + "-Skill " + section_id + ".txt"

        self.hintNumPattern=numbersofHintsperProblem
        #self.hintNumPattern=[]
        #for all problems that have the same number of hints
        #self.hintNumPattern.append(numberofHintsperProblem)
        #for all problems that have 4, 5, 4, 5 ,... hints
        #self.hintNumPattern = [4,4,4,4,4,4,5,4,4,4,4]
        #self.hintNumPattern = [3,5,5,6,6,6,6,6,6,6,6]
        #special hint number
        #self.hintNumPattern = [2,2,2,2,3,2,2,2,3,2] -- g4 chp8.6
        #self.hintNumPattern = [6,2,2,2,3,2,2,2,3,2]
        #self.hintNumPattern = [3,3,3,4,3,4,3,3,3,4]

        self.grade_id = grade_id
        self.hintimgs = []
        self.loadGradeHintImg(self.grade_id)


        self.problem_data=[]
        self.hints_data=[]


    def readHintContent(self):
        with open(self.hints_infile, 'r') as hf:
            hint_contents = hf.readlines()
        self.hint_array = []
        hint_token = " Hint:"
        #hintreg = re.compile("[0-9]+[a-z]{2} Hint:")
        idx = 0
        while idx < len(hint_contents):
            hint_line = str(hint_contents[idx]).rstrip('\n')
            #print "current_line --- ", hint_line
            one_problem_hint = []
            hints_dict = {}
            while hint_token in hint_line:
                idx += 1
                one_hint = []
                hint_idx = int(hint_line[0:1])

                one_hint.append(str(hint_contents[idx]).rstrip('\n'))
                #one_hint.append(hint_contents[idx])
                one_problem_hint.insert(hint_idx-1, one_hint)
                hints_dict[hint_idx] = one_hint

                print "add hint --- ", hint_contents[idx]

                next_line = str(hint_contents[idx+1]).rstrip('\n')
                while hint_token not in next_line and next_line.strip() != "":
                    idx += 1
                    one_hint.append(str(hint_contents[idx]).rstrip('\n'))
                    #one_hint.append(hint_contents[idx])
                    if idx + 1 < len(hint_contents):
                        next_line = str(hint_contents[idx+1]).rstrip('\n')
                    else:
                        break
                idx += 1
                hint_line = str(hint_contents[idx]).rstrip('\n')

            '''
            for one_hint in one_problem_hint:
                self.hint_array.append(one_hint)
            '''
            hints_dict = OrderedDict(sorted(hints_dict.items()))
            debug_count = 0
            for hintidx, one_hint in hints_dict.iteritems():
                self.hint_array.append(one_hint)
                debug_count += 1
            if debug_count > 0:
                print " !!!!!!!!!!!!!!!!!! debug count for hint: ", debug_count


            idx += 1
        for indx, cur_hint in enumerate(self.hint_array):
            print indx, cur_hint

    def updateHintContent(self):
        if len(self.hint_array) == len(self.hints_data):
            for idx, one_hint in enumerate(self.hint_array):
                hint_content = " ".join(one_hint)
                print idx, " || ", hint_content
                self.hints_data[idx]["description"] = hint_content

    def updateHintContentWithHintItem(self):
        if len(self.hint_array) <= len(self.hints_data):
            print "start updating Hint Content !!!!!!!!!"
            for idx, one_hint in enumerate(self.hint_array):
                hint_content = " ".join(one_hint)
                print idx, " || ", hint_content
                #self.hints_data[idx]["description"] = hint_content

                self.hints_data[idx]["hintItem"][0]["value"] = hint_content
                """
                pcount = (idx / 8 + 1) - 1
                hintcount = (1+idx) % 8
                if hintcount == 0:
                    hintcount = 8
                """
                """
                # 4.2/math-g4-c4-s4-2-p1-h1-img1.png
                if hintcount != 2 and hintcount != 4 and hintcount != 6:
                    img_url = "4.4/math-g4-c4-s4-4-p" + str(pcount) + "-h" + str(hintcount) + "-img1.png"
                else:
                    img_url = ""
                print " ---  imgurl --- ", img_url
                self.hints_data[idx]["hintItem"][1]["value"] = img_url
                """





    def loadGradeHintImg(self,gradeid):
        if gradeid == 3:
            self.hintimgs.append("../../../theme/sea/hint-img-fish-left.png")
            self.hintimgs.append("../../../theme/sea/hint-img-dolphin-left.png")
            self.hintimgs.append("../../../theme/sea/hint-img-whale-left.png")
            self.hintimgs.append("../../../theme/sea/hint-img-crab-left.png")
            self.hintimgs.append("../../../theme/sea/hint-img-seahorse-left.png")
            self.hintimgs.append("../../../theme/sea/hint-img-octopus-left.png")
            return
        if gradeid == 2:
            self.hintimgs.append("../../theme/safari/hint-img-elephant-left.png")
            self.hintimgs.append("../../theme/safari/hint-img-giraffe-left.png")
            self.hintimgs.append("../../theme/safari/hint-img-hippopotamus-left.png")
            self.hintimgs.append("../../theme/safari/hint-img-zebra-left.png")
            self.hintimgs.append("../../theme/safari/hint-img-tiger-left.png")
            self.hintimgs.append("../../theme/safari/hint-img-lion-left.png")
            return
        if gradeid == 4:
            self.hintimgs.append("../../../theme/farm/hint-img-cat.png")
            self.hintimgs.append("../../../theme/farm/hint-img-cow.png")
            self.hintimgs.append("../../../theme/farm/hint-img-dog.png")
            self.hintimgs.append("../../../theme/farm/hint-img-duck.png")
            self.hintimgs.append("../../../theme/farm/hint-img-horse.png")
            self.hintimgs.append("../../../theme/farm/hint-img-pig.png")
            self.hintimgs.append("../../../theme/farm/hint-img-rabbit.png")
            self.hintimgs.append("../../../theme/farm/hint-img-rooster.png")
            self.hintimgs.append("../../../theme/farm/hint-img-sheep.png")
            return
        if gradeid == 5:
            self.hintimgs.append("../../../theme/g5/hint-g5-img1.png")
            self.hintimgs.append("../../../theme/g5/hint-g5-img2.png")
            self.hintimgs.append("../../../theme/g5/hint-g5-img3.png")
            self.hintimgs.append("../../../theme/g5/hint-g5-img4.png")
            self.hintimgs.append("../../../theme/g5/hint-g5-img5.png")
            self.hintimgs.append("../../../theme/g5/hint-g5-img6.png")
            self.hintimgs.append("../../../theme/g5/hint-g5-img7.png")
            self.hintimgs.append("../../../theme/g5/hint-g5-img8.png")
            return


    def getHintsData(self):
        hints_str = ""
        with open(self.hints_name, 'r') as hf:
            hints_str = hf.read()
        hints_data = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(hints_str)
        print hints_data
        self.hints_data = hints_data
        return hints_data

    def getProblemData(self):
        problem_str = ""
        with open(self.problem_name, 'r') as pf:
            problem_str = pf.read()
        problem_data = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(problem_str)
        #print problem_data
        self.problem_data=problem_data
        return problem_data

    def updateProblemId(self):
        pid=0
        for problem in self.problem_data:
            pid +=1
            problem["problem_id"] = pid

    def updateHintId(self):
        hid=0
        for hint in self.hints_data:
            hid +=1
            hint["hint_id"] = hid

    def updateExerciseImageId(self):
        EIid=0
        rePrefix = re.compile("[0-9]+.[0-9]+\/math-g[0-9]+-c[0-9]+-s[0-9]+-[0-9]+-p")
        reSuffix = re.compile("-img[0-9]+.png")
        for problem in self.problem_data:
            if problem["assisted_exercise"]==False:
                EIid +=1
                if "images" in problem:
                    for img in problem["images"]:
                        if "image_name" not in img or "image_url" not in img:
                            continue
                        img_str=img["image_name"]
                        mpre = rePrefix.search(img_str)
                        msuf = reSuffix.search(img_str)
                        if mpre and msuf:
                            print mpre.group()
                            print msuf.group()
                            img["image_name"] = mpre.group() + str(EIid) + msuf.group()
                            img["image_url"] = mpre.group() + str(EIid) + msuf.group()
                            print img["image_url"]
                if problem["template_type"] == "rowtype":
                    for row in problem["problemItems"]:
                        for part in row:
                            if "type" in part and part["type"] == "image":
                                img_str = part["value"]
                                mpre = rePrefix.search(img_str)
                                msuf = reSuffix.search(img_str)
                                if mpre and msuf:
                                    print mpre.group()
                                    print msuf.group()
                                    part["value"] = mpre.group() + str(EIid) + msuf.group()
                                    print part["value"]

                else:
                    for problemItem in problem["problemItems"]:
                        if "img" in problemItem:
                            img_str= problemItem["img"]
                            mpre = rePrefix.search(img_str)
                            msuf = reSuffix.search(img_str)
                            if mpre and msuf:
                                print mpre.group()
                                print msuf.group()
                                problemItem["img"] = mpre.group() + str(EIid) + msuf.group()
                                print problemItem["img"]
                        if "options" in problemItem:
                            for optionItem in problemItem["options"]:
                                if "img" in optionItem:
                                    img_str = optionItem["img"]
                                    mpre = rePrefix.search(img_str)
                                    msuf = reSuffix.search(img_str)
                                    if mpre and msuf:
                                        print mpre.group()
                                        print msuf.group()
                                        optionItem["img"] = mpre.group() + str(EIid) + msuf.group()
                                        print optionItem["img"]


    def updateProblemHint(self):
        hintid=0
        for problem in self.problem_data:
            problem_id = int(problem["problem_id"])
            print problem_id
            hintNumPatternIndex = (problem_id-1) % len(self.hintNumPattern)
            print hintNumPatternIndex
            hintNum = self.hintNumPattern[hintNumPatternIndex]
            hintIds=[]
            for i in range(hintNum):
                hintid += 1
                hintIds.append(hintid)
            print hintIds
            problem["hintIds"]=hintIds
            print problem["hintIds"]



    def updateHintIcon(self):
        for problem in self.problem_data:
        # print problem
            hintIds = problem["hintIds"]
            print hintIds
            hintImgIndex = 0
            for hintId in hintIds:
                hintIndex = int(hintId) - 1
                print self.hints_data[hintIndex]
                self.hints_data[hintIndex]["hinticon"] = self.hintimgs[hintImgIndex % len(self.hintimgs)]
                print self.hints_data[hintIndex]
                hintImgIndex += 1


    def writeProblemOut(self):
        problem_out_str = json.dumps(self.problem_data, indent=2, separators=(',', ': '))
        print problem_out_str
        with open(self.problem_out, 'w+') as of:
            of.write(problem_out_str)


    def writeHintsOut(self):
        hints_out_str = json.dumps(self.hints_data, indent=2, separators=(',', ': '))
        print hints_out_str
        with open(self.hints_out, 'w+') as of:
            of.write(hints_out_str)


    @staticmethod
    def process_updateHintAndInProblem():
        hut = HintUtil()
        hut.setSettings()

        hut.getProblemData()
        hut.updateProblemId()
        hut.updateProblemHint()
        hut.writeProblemOut()

        hut.getHintsData()
        hut.updateHintId()
        hut.updateHintIcon()
        hut.writeHintsOut()


    @staticmethod
    def process_updateHintId():
        hut = HintUtil()
        hut.setSettings(5,"6.14")
        hut.getHintsData()
        hut.updateHintId()
        hut.writeHintsOut()


    @staticmethod
    def process_updateProblem():
        hut = HintUtil()
        hut.setSettings(6,"1.1",[5])

        hut.getProblemData()
        hut.updateProblemId()
        hut.updateExerciseImageId()
        hut.updateProblemHint()
        hut.writeProblemOut()

    @staticmethod
    def process_updateHint():
        hut = HintUtil()
        hut.setSettings(5,"6.10")
        hut.getProblemData()

        hut.getHintsData()
        hut.updateHintId()
        hut.updateHintIcon()
        hut.writeHintsOut()

    @staticmethod
    def process_updateHintAndContent():
        hut = HintUtil()
        hut.setSettings(5, "6.13")
        hut.getProblemData()
        hut.getHintsData()
        hut.updateHintId()
        hut.updateHintIcon()
        hut.readHintContent()
        #hut.updateHintContent()
        hut.updateHintContentWithHintItem()
        hut.writeHintsOut()




if __name__ == '__main__':

    HintUtil.process_updateProblem()
    #HintUtil.copyProblemOutToIn()
    #HintUtil.process_updateHintAndContent()


    #HintUtil.process_updateHint()
    #HintUtil.process_updateHintId()

    #hutil = HintUtil()
    #hutil.setSettings(5, "4.1")
    #hutil.readHintContent()

