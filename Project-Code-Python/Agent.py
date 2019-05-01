# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image
from PIL import ImageChops as chops
from PIL import ImageFilter
import numpy as np
import math
from io import BytesIO


class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        #print("\n" + problem.name+"\n")

        answer = 0


        imageArray_A = self.getImages(problem, 'A')
        imageArray_B = self.getImages(problem, 'B')
        imageArray_C = self.getImages(problem, 'C')




        image_A = Image.open(problem.figures['A'].visualFilename).convert("L")
        image_B = Image.open(problem.figures['B'].visualFilename).convert("L")
        image_C = Image.open(problem.figures['C'].visualFilename).convert("L")



        # check if figures are the same
        if problem.problemType == "2x2":
            print(problem.name)

            if self.equalImages(imageArray_A, imageArray_B) and self.equalImages(imageArray_A, imageArray_C) == True:
                #print('figures are equal')
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        if self.equalImages(imageArray_C,self.getImages(problem, solutions)) == True:
                            answer = solutions
                            print('answer....',answer)

            elif self.reflectionLeftRight(image_A,image_B) < 1.0 and self.find_difference(image_A , image_B) > 1.0:
                print('A is left right reflection of B')
                diffArray=[]
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diff = self.reflectionLeftRight(image_C, Image.open(problem.figures[solutions].visualFilename).convert("L"))
                        diffArray.append(diff)
                #print('diffArray.....',diffArray)
                answer = diffArray.index(min(diffArray)) + 1
                print('answer.....',answer)

            elif self.reflectionUpDown(image_A,image_C) < 1.0:
                print('A is upside down reflection of C')
                diffArray=[]
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diff = self.reflectionUpDown(image_B, Image.open(problem.figures[solutions].visualFilename).convert("L"))
                        diffArray.append(diff)
                #print('diffArray.....',diffArray)
                answer = diffArray.index(min(diffArray)) + 1
                print('answer.....',answer)

            elif self.reflectionLeftRight(image_A, image_C) < 1.0:
                print('A is reflection of C')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diff = self.reflectionLeftRight(image_B,
                                               Image.open(problem.figures[solutions].visualFilename).convert("L"))
                        diffArray.append(diff)
                # print('diffArray.....',diffArray)
                answer = diffArray.index(min(diffArray)) + 1
                print('answer.....', answer)

            elif self.fill_figure_check(image_A, image_B) < 15 and self.fill_figure_check(image_A, image_B) > 12:
                print('B is a fill of A')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diff = self.fill_figure_check(image_C, Image.open(problem.figures[solutions].visualFilename).convert("L"))
                        diffArray.append(diff)
                #print('diffArray.....', diffArray)
                answer = diffArray.index(max(diffArray)) + 1
                print('answer.....', answer)

            elif self.dissapearing_object_check(image_A, image_C) == True:
                print('object dissappeared')
                AC_diff = self.find_difference(image_A, image_C)
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diff = self.find_difference(image_B, Image.open(problem.figures[solutions].visualFilename).convert("L"))
                        diffArray.append(diff)
                #print('diffArray.....', diffArray)
                answer = min(enumerate(diffArray), key=lambda x: abs(x[1]-AC_diff))
                answer = answer[0]+1
                print('answer.....', answer)

            elif self.dissapearing_object_check(image_A, image_B) == True:
                print('object dissappeared')
                AB_diff = self.find_difference(image_A, image_B)
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diff = self.find_difference(image_C, Image.open(problem.figures[solutions].visualFilename).convert("L"))
                        diffArray.append(diff)
                #print('diffArray.....', diffArray)
                answer = min(enumerate(diffArray), key=lambda x: abs(x[1]-AB_diff))
                answer = answer[0]+1
                print('answer.....', answer)

            else:
                answer =  -1

        if problem.problemType == "3x3":
        #if problem.problemType == "3x3" and problem.name == "Basic Problem D-06":
            print(problem.name)

            image_A = Image.open(problem.figures['A'].visualFilename).convert("L")
            image_B = Image.open(problem.figures['B'].visualFilename).convert("L")
            image_C = Image.open(problem.figures['C'].visualFilename).convert("L")
            image_D = Image.open(problem.figures['D'].visualFilename).convert("L")
            image_E = Image.open(problem.figures['E'].visualFilename).convert("L")
            image_F = Image.open(problem.figures['F'].visualFilename).convert("L")
            image_G = Image.open(problem.figures['G'].visualFilename).convert("L")
            image_H = Image.open(problem.figures['H'].visualFilename).convert("L")



            # print('AE diff..', self.find_difference(image_A, image_E))
            # print('CD diff..', self.find_difference(image_C, image_D))
            # print('FG diff..', self.find_difference(image_F, image_G))

            #print('# black pixels', self.count_black_pixels(image_H)- self.count_black_pixels(image_F))
            #print('# black pixels', self.count_black_pixels(image_F)- self.count_black_pixels(image_A))

            # union_AB = self.get_union(image_D, image_H)
            # union_BC = self.get_intersection(image_D, image_F)
            # union_DC = self.get_image_difference(image_D, image_C)

            #print('mse: ', self.rmsdiff(union_AB,image_B))

            #AB_XOR = chops.logical_or(image_A_1,image_E_1)

            #AB_XOR_G = chops.logical_and(AB_XOR,image_A_1)

            #AB_XOR.show()
            #AB_XOR_G.show()

            #print('diff..', self.find_difference(union_AE,image_A))
            #print('diff..', self.find_difference(union_BF,image_B))
            #print('diff..', self.find_difference(union_DC, image_C))
            #print(' diff..', chops.difference(image_A,image_B).getbbox())
            # print('AE diff..', self.find_difference(image_A, union_AE))
            # print('CD diff..', self.find_difference(image_C, image_D))
            #union_AB.show()
            #union_BC.show()

            #B_pixel_count = self.count_black_pixels(image_D)
            #c_pixel_count  = self.count_black_pixels(image_G)

            #print('pixel count', B_pixel_count , c_pixel_count)
            #print('main pixel count', self.count_black_pixels(image_D))

            #print("rolling solver..", self.rolling_solver(image_A, image_B,image_C, image_G, image_H, problem))
            #print("solve_by_pixel_diff..", self.solve_by_pixel_diff(problem, image_A,image_B ,image_C ,image_D,image_E,image_G))
            #print('diagnol  :', self.diagonal_sover( problem, image_A, image_B,  image_D,image_E,image_F,image_H))


            answer_array = []

            # if self.find_difference(image_B, self.get_union(image_B,image_F)) < 1.0 and self.find_difference(image_D, self.get_union(image_D, image_H)) < 1.0:
            #     print('BF union = B')
            #     diffArray = []
            #     for solutions in sorted(problem.figures):
            #         if solutions.isnumeric():
            #             E_to_answer_diff = self.find_difference(image_E, self.get_union(image_E,Image.open(problem.figures[solutions].visualFilename).convert("L")))
            #             diffArray.append(E_to_answer_diff)
            #     print('diffArray: ', diffArray)


            # if self .find_difference(chops.logical_and(image_A_1,image_D_1),chops.logical_and(image_A_1,image_B_1)) < 1.0:
            #     print('AB logical and = AD logical and')
            #     diffArray = []
            #     for solutions in sorted(problem.figures):
            #         if solutions.isnumeric():
            #             answer_diff = self.find_difference(chops.logical_and(Image.open(problem.figures[solutions].visualFilename).convert("1"),image_F_1),chops.logical_and(Image.open(problem.figures[solutions].visualFilename).convert("1"),image_H_1))
            #             diffArray.append(answer_diff)
            #     print('diffArray:', diffArray)


            if self.find_difference(image_C, self.get_intersection(image_A, image_B)) < 1.0:
                print('AB intersection = C')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        answer_diff = self.find_difference(Image.open(problem.figures[solutions].visualFilename).convert("L"), self.get_intersection(image_G, image_H))
                        diffArray.append(answer_diff)
                answer = diffArray.index(min(diffArray)) + 1
                answer_array.append(answer)
                #answer = max(set(answer_array), key=answer_array.count)
                print('answer....', answer)
                #print('diffArray:', diffArray)

            elif self.find_difference(image_G, self.get_intersection(image_A, image_D)) < 1.0:
                print('AD intersection = G')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        answer_diff = self.find_difference(Image.open(problem.figures[solutions].visualFilename).convert("L"), self.get_intersection(image_C, image_F))
                        diffArray.append(answer_diff)
                answer = diffArray.index(min(diffArray)) + 1
                answer_array.append(answer)
                #answer = max(set(answer_array), key=answer_array.count)
                print('answer....', answer)
                #print('diffArray:', diffArray)







            elif self.find_difference(self.get_union(image_A, image_F), image_H)< 1.0:
                print('A and F union = H')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        #diff = self.find_difference(self.get_union(image_B, Image.open(problem.figures[solutions].visualFilename).convert("L")),image_D)
                        diff = self.rmsdiff(image_D, self.get_union(image_B, Image.open(problem.figures[solutions].visualFilename).convert("L")))
                        diffArray.append(diff)
                answer = diffArray.index(min(diffArray)) + 1
                print('diffarray :', diffArray)
                print('answer....', answer)



            elif self.find_difference(image_A, self.get_image_difference(image_B, image_C)) < 1.0:
                print('BC difference = A')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        G_answer_diff = self.find_difference(image_G, self.get_image_difference(image_H, Image.open(problem.figures[solutions].visualFilename).convert("L")))
                        diffArray.append(G_answer_diff)

                answer = diffArray.index(min(diffArray)) + 1
                answer_array.append(answer)
                #answer = max(set(answer_array), key=answer_array.count)
                print('answer....', answer)
                #print('diffArray:', diffArray)




            elif self.find_difference(image_A, self.get_union(image_B,image_C)) < 1.0 and self.find_difference(image_D, self.get_union(image_E,image_F)) < 1.0:
                print('B union C  = A')

                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        G_answer_diff = self.find_difference(image_G, self.get_union(image_H,Image.open(problem.figures[solutions].visualFilename).convert("L")))
                        diffArray.append(G_answer_diff)
                        if self.find_difference(image_G, self.get_union(image_H,Image.open(problem.figures[solutions].visualFilename).convert("L"))) < 1.0:
                            answer = solutions
                answer_array.append(answer)
                #answer = max(set(answer_array), key=answer_array.count)
                print('answer....', answer)
                #print('diffArray:', diffArray)

            elif self.find_difference(image_B, self.get_union(image_A,image_C)) < 1.0 and self.find_difference(image_E, self.get_union(image_D,image_F)) < 1.0:
                print('A + C = B')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        H_answer_diff = self.find_difference(image_H, self.get_union(image_G, Image.open(problem.figures[solutions].visualFilename).convert("L")))
                        diffArray.append(H_answer_diff)
                        if self.find_difference(image_H, self.get_union(image_G,Image.open(problem.figures[solutions].visualFilename).convert("L"))) < 1.0:
                            answer = solutions
                answer_array.append(answer)
                #answer = max(set(answer_array), key=answer_array.count)
                print('answer....', answer)
                #print('diffArray:', diffArray)



            elif self.count_black_pixels(image_B) + self.count_black_pixels(image_C) == self.count_black_pixels(image_A):
                print('BC pixel count is similar to A')
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        if self.count_black_pixels(image_H) + self.count_black_pixels(Image.open(problem.figures[solutions].visualFilename).convert("L")) == self.count_black_pixels(image_G):
                            answer = solutions
                answer_array.append(answer)
                answer = max(set(answer_array), key = answer_array.count)
                print('answer....', answer)


            elif self.find_difference(image_A, image_B) < 1.0 and self.find_difference(image_B, image_C) < 1.0:
                print('images are similar')
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        if self.find_difference(image_G,Image.open(problem.figures[solutions].visualFilename).convert("L")) < 1.0:
                            answer = solutions
                            answer_array.append(answer)
                            print('answer....',answer)

            elif self.find_difference(image_A,image_G) < 1.0:
                print('images are similar')
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        if self.find_difference(image_C,Image.open(problem.figures[solutions].visualFilename).convert("L")) < 1.0:
                            answer = solutions
                            answer_array.append(answer)
                            print('answer....', answer)

            elif self.find_difference(image_A, image_E) < 1.0 and self.find_difference(image_C, image_D) < 1.0:
                print('AE, BF and CD are similar')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diffArray.append(self.find_difference(image_E, Image.open(problem.figures[solutions].visualFilename).convert("L")))
                        answer = diffArray.index(min(diffArray)) + 1
                        answer_array.append(answer)
                print('answer....', answer)

                #print('diffArray....', min(diffArray))

            elif self.find_difference(self.get_image_difference(image_D, image_F),self.get_image_difference(image_A, image_C)) < 1.0:
                print('subtracted images are similar')
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        if self.find_difference(self.get_image_difference(image_D, image_F), self.get_image_difference(image_G, Image.open(problem.figures[solutions].visualFilename).convert("L"))) < 1.0:
                            answer = solutions
                            answer_array.append(answer)
                            print('answer....', answer)

            elif self.find_difference(self.get_image_difference(image_A, image_G),self.get_image_difference(image_B, image_H)) < 1.0:
                print('subtracted images are similar')
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        if self.find_difference(self.get_image_difference(image_B, image_H), self.get_image_difference(image_C, Image.open(problem.figures[solutions].visualFilename).convert("L"))) < 1.0:
                            answer = solutions
                            answer_array.append(answer)
                            print('answer....', answer)



            # if self.find_difference(self.get_union(image_A, image_E),image_A) < 1.0 and self.find_difference(self.get_union(image_B, image_F),image_B) < 1.0 :
            #     print('image union')
            #     union_AE = self.get_union(image_A, image_E)
            #     AE_diff = self.find_difference(image_A, union_AE)
            #     #print('AE diff..', AE_diff)
            #     diffArray = []
            #     for solutions in sorted(problem.figures):
            #         if solutions.isnumeric():
            #             diff = self.find_difference(image_E, self.get_union(image_E, Image.open(problem.figures[solutions].visualFilename).convert("L")))
            #             diffArray.append(diff)
            #             #print(diff)
            #     #print('diffArray: ', diffArray)
            #     answer = min(enumerate(diffArray), key=lambda x: abs(x[1] - AE_diff))
            #     answer = answer[0] + 1
            #     print('answer....', answer)


            elif self.find_difference(self.get_union(image_A, image_B), image_C) < 1.0 and self.find_difference(self.get_union(image_D, image_E), image_F) < 1.0:
                print('overlaying images')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diff = self.find_difference(self.get_union(image_G, image_H),Image.open(problem.figures[solutions].visualFilename).convert("L"))
                        diffArray.append(diff)
                answer = diffArray.index(min(diffArray)) + 1
                answer_array.append(answer)
                #print('diffArray:', diffArray)
                print('answer....', answer)

            elif self.find_difference(self.get_union(image_B, image_F), image_B) < 1.0 and self.find_difference(self.get_union(image_A, image_E), image_A) < 1.0:
                print('B union F = B')
                diffArray = []
                AE_diff = self.find_difference(self.get_union(image_A, image_E), image_A)
                union_AE = self.get_union(image_A, image_E)
                #print('diff : ', self.rmsdiff(union_AE, image_A))
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        mse = self.rmsdiff(image_E, self.get_union(image_E, Image.open(problem.figures[solutions].visualFilename).convert("L")))
                        #answer_diff = self.find_difference(self.get_union(image_E, Image.open(problem.figures[solutions].visualFilename).convert("L")), image_E)
                        diffArray.append(mse)
                answer = min(enumerate(diffArray), key=lambda x: abs(x[1] - self.rmsdiff(union_AE, image_A)))
                answer = answer[0] + 1
                #print('diffArray : ', diffArray)
                print('answer....', answer)


            elif self.find_difference(self.get_union(image_A, image_F), image_A) < 1.0 and self.find_difference(self.get_union(image_C, image_E), image_C) < 1.0:
                print('A and F union = A')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diff = self.find_difference(
                            self.get_union(image_D, Image.open(problem.figures[solutions].visualFilename).convert("L")),
                            image_D)
                        diffArray.append(diff)
                answer = diffArray.index(min(diffArray)) + 1
                # print('diffarray :', diffArray)
                print('answer....', answer)


            elif self.diagonal_sover( problem, image_A, image_B,  image_D,image_E,image_F,image_H) != -1:
                answer = self.diagonal_sover( problem, image_A, image_B,  image_D,image_E,image_F,image_H)
                print('answer diagonal....', answer)






            # if self.reflectionLeftRight(image_A, image_C) < 1.0 and self.reflectionLeftRight(image_D, image_F) < 1.0 :
            #     print('here $$$$')
            #     diffArray = []
            #     for solutions in sorted(problem.figures):
            #         if solutions.isnumeric():
            #             diff = self.reflectionLeftRight(image_G,Image.open(problem.figures[solutions].visualFilename).convert("L"))
            #             diffArray.append(diff)
            #     answer = diffArray.index(min(diffArray)) + 1
            #     print('answer.....', answer)
            #
            elif self.increasing_objects(problem,'A','B','C') and self.increasing_objects(problem,'A','D','G'):
                print('here<<<<<<')
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        if self.increasing_objects(problem, 'G', 'H', solutions):
                            answer = solutions
                            answer_array.append(answer)
                print('answer:', answer)

            elif self.increasing_objects(problem,'A','F','H'):
                print('A < F < H')
                BD_pixel_diff = self.count_black_pixels(image_D)- self.count_black_pixels(image_B)
                #print('BD_diff: ', BD_pixel_diff)
                solution_arr = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        pixel_diff = self.count_black_pixels(image_B)- self.count_black_pixels(Image.open(problem.figures[solutions].visualFilename).convert("L"))
                        solution_arr.append(pixel_diff)
                answer = min(enumerate(solution_arr), key=lambda x: abs(x[1] - BD_pixel_diff))
                answer = answer[0] + 1
                print('answer:', answer)
                #print('diffArray :', solution_arr)



            # elif self.decreasing_objects(problem,'A','B','C') and self.decreasing_objects(problem, 'D','E','F'):
            #     print('here----------')
            #     for solutions in sorted(problem.figures):
            #         if solutions.isnumeric():
            #             if self.increasing_objects(problem, 'G', 'H', solutions):
            #                 answer = solutions
            #     print('answer...:', answer)

            # elif self.increasing_objects(problem,'C','E','G'):
            #     print('here----------')
            #     for solutions in sorted(problem.figures):
            #         if solutions.isnumeric():
            #             if self.increasing_objects(problem, 'A', 'E', solutions):
            #                 answer = solutions
            #     print('answer:', answer)



            # elif self.decreasing_objects(problem,'A','D','G') and self.increasing_objects(problem,'A','B','C'):
            #     print('here****')
            #     diffArray = []
            #     GH_diff = self.find_difference(image_G,image_H)
            #     for solutions in sorted(problem.figures):
            #         if solutions.isnumeric():
            #             diff = self.find_difference(image_H,Image.open(problem.figures[solutions].visualFilename).convert("L"))
            #             diffArray.append(diff)
            #     answer = min(enumerate(diffArray), key=lambda x: abs(x[1] - GH_diff))
            #     answer = answer[0] + 1
            #     print('answer:', answer)
            #
            # elif  round(self.find_difference(image_C, image_F),2) == round(self.find_difference(image_G, image_H),2):
            #     print('here::::::::')
            #     AD_diff = round(self.find_difference(image_A, image_D),3)
            #     diffArray = []
            #     for solutions in sorted(problem.figures):
            #         if solutions.isnumeric():
            #             diff = round(self.find_difference(image_H, Image.open(problem.figures[solutions].visualFilename).convert('L')),3)
            #             #print('ans_diff...',round(self.find_difference(image_G, image_H),3),'==', round(self.find_difference(image_H, Image.open(problem.figures[solutions].visualFilename).convert('L')),3))
            #             diffArray.append(diff)
            #     answer = min(enumerate(diffArray), key=lambda x: abs(x[1] - AD_diff))
            #     answer = answer[0] + 1
            #     print('answer:', answer)



            # elif abs(self.compare_diff(image_A, image_B,image_C)) < abs(self.compare_diff(image_D, image_E,image_F)):
            #     print('here~~~~~~~')
            #     diffArray = []
            #     DFE_diff = abs(self.compare_diff(image_D, image_E,image_F))
            #     for solutions in sorted(problem.figures):
            #         if solutions.isnumeric():
            #             diff = abs(self.compare_diff(image_G, image_H, Image.open(problem.figures[solutions].visualFilename).convert('L')))
            #             diffArray.append(diff)
            #     answer = min(enumerate(diffArray), key=lambda x: abs(x[1] - DFE_diff))
            #     answer = answer[0] + 1
            #     print('answer:', answer)



            elif 2.02 > self.union_solver(image_A,image_B,image_C) > 1.99:
                print("image union...")
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        if 2.0 > self.union_solver(image_G,image_H,Image.open(problem.figures[solutions].visualFilename).convert('L')) > 1.99:
                            answer = solutions
                            answer_array.append(answer)
                print('answer..',answer)






            elif self.increasing_objects(problem,'C','D','H'):
                print('C < D < H')
                BF_pixel_diff = self.count_black_pixels(image_F) - self.count_black_pixels(image_B)
                solution_arr = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        pixel_diff = self.count_black_pixels(image_B) - self.count_black_pixels(Image.open(problem.figures[solutions].visualFilename).convert("L"))
                        solution_arr.append(pixel_diff)
                answer = min(enumerate(solution_arr), key=lambda x: abs(x[1] - BD_pixel_diff))
                answer = answer[0] + 1
                print('answer:', answer)
                print('diffArray :', solution_arr)

            elif self.find_difference(self.get_union(image_C, image_D), image_H) < 1.0:
                print('C and D union = H')
                diffArray = []
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diff = self.find_difference(self.get_union(image_B, Image.open(problem.figures[solutions].visualFilename).convert("L")),image_D)
                        diffArray.append(diff)
                answer = diffArray.index(min(diffArray)) + 1
                print('diffarray :', diffArray)
                print('answer....', answer)

            # elif self.find_difference(self.get_union(image_A, image_F), image_A) < 1.0 and self.find_difference(
            #         self.get_union(image_C, image_E), image_C) < 1.0:
            #     print('A and F union = A')
            #     diffArray = []
            #     for solutions in sorted(problem.figures):
            #         if solutions.isnumeric():
            #             diff = self.find_difference(
            #                 self.get_union(image_D, Image.open(problem.figures[solutions].visualFilename).convert("L")),
            #                 image_D)
            #             diffArray.append(diff)
            #     answer = diffArray.index(min(diffArray)) + 1
            #     # print('diffarray :', diffArray)
            #     print('answer....', answer)







            else:
                answer = -1



        return int(answer)

    def getImages(self, problem, imagename):
        figure = problem.figures[imagename]
        # print('figure name...',figure.visualFilename)
        figureImage = Image.open(figure.visualFilename).convert("L")

        figureImage = figureImage.filter(ImageFilter.SMOOTH_MORE)
        nparray = np.array(figureImage)
        return nparray


##check for equal images
    def equalImages(self, image1, image2):
        if np.array_equal(image1,image2):
            #print('true')
            return True
        else:
            return False



    def reflectionLeftRight(self, image1,image2):
        rotate_B = image2.transpose(Image.FLIP_LEFT_RIGHT)
        diff = self.find_difference(image1, rotate_B)
        return diff

    def reflectionUpDown(self, image1,image2):
        rotate_B = image2.transpose(Image.FLIP_TOP_BOTTOM)
        diff = self.find_difference(image1, rotate_B)
        return diff

    def fill_figure_check(self, image1, image2):
        diff = self.find_difference(image1, image2)
        return diff

    def dissapearing_object_check(self, image1, image2):
        diff = self.find_difference(image1, image2)
        if diff != 0.0:
            return True

    def dissapearing_object_check_AB(self, image1, image2):
        diff = self.find_difference(image1, image2)
        if diff > 0.0 and diff < 1:
            return True




    def find_difference(self,first_image, second_image):
        # Reference: http://rosettacode.org/wiki/Percentage_difference_between_images#Python

        pairs = zip(first_image.getdata(), second_image.getdata())
        if len(first_image.getbands()) == 1:
            # for gray-scale jpegs
            dif = sum(abs(p1 - p2) for p1, p2 in pairs)
        else:
            dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

        n_components = first_image.size[0] * first_image.size[1] * 3

        return (dif / 255.0 * 100) / n_components


##------------- 3x3 methods-------------

    #check if images are the same
    def checkSimilarity_3x3(self, image1, image2):
        diff_1_2 = self.find_difference(image1,image2)
        #print('diff----', diff_1_2)
        return diff_1_2

    def compare_diff(self,image1,image2,image3):
        diff_1_2 = abs(self.find_difference(image1,image2))
        diff_3_4 = abs(self.find_difference(image2,image3))
        #print('diff_1_2...' , diff_1_2)
        #print('diff_3_4...' , diff_3_4)
        #print('diff_3_4 - diff_1_2...', round(diff_3_4 - diff_1_2,1))
        return abs(diff_3_4 - diff_1_2)

    def check_increased_objects(self,image1,image2,image3):
        diff_1_2 = self.find_difference(image1, image2)
        diff_3_4 = self.find_difference(image1, image3)
        diff_ratio = diff_3_4 / diff_1_2
        #print('diff_ratio....',round(diff_ratio,2))
        return round(diff_ratio,3)

    def get_pixel_ratio(self,image1, image2):
        sum1 = np.sum(image1)
        sum2 = np.sum(image2)
        return float(sum1) / sum2

    def getImageDarkPixelRatio(self,problem,image_name):
        imageArray = self.getImages(problem, image_name)
        white_pixels = np.count_nonzero(imageArray)
        return (imageArray.size - white_pixels)/imageArray.size



    def increasing_objects(self,problem,image1,image2,image3):
        pixel_ratio1 = self.getImageDarkPixelRatio(problem, image1)
        pixel_ratio2 = self.getImageDarkPixelRatio(problem, image2)
        pixel_ratio3 = self.getImageDarkPixelRatio(problem, image3)
        return pixel_ratio3 > pixel_ratio2 > pixel_ratio1

    def decreasing_objects(self,problem,image1,image2,image3):
        pixel_ratio1 = self.getImageDarkPixelRatio(problem, image1)
        pixel_ratio2 = self.getImageDarkPixelRatio(problem, image2)
        pixel_ratio3 = self.getImageDarkPixelRatio(problem, image3)
        return pixel_ratio3 < pixel_ratio2 < pixel_ratio1

    def get_pixel_difference(self,image1, image2):
        pixels1 = (image1.shape[0] * image1.shape[1]) - int(np.sum(image1))
        pixels2 = (image2.shape[0] * image2.shape[1]) - int(np.sum(image2))
        return abs(pixels1 - pixels2)


    def get_black_pixel_count(self, problem, image_name):
        imageArray = self.getImages(problem, image_name)
        white_pixels = np.count_nonzero(imageArray)
        return (imageArray.size - white_pixels)

    def decreasing_pixel_diff(self, image1, image2):
        pixels1 = (image1.shape[0] * image1.shape[1]) - int(np.sum(image1))
        pixels2 = (image2.shape[0] * image2.shape[1]) - int(np.sum(image2))
        return pixels1 > pixels2

    def get_bounding_box(self, image):
        # convert to grayscale and invert
        image_inv = chops.invert(image)
        return image_inv.getbbox()

    def get_image_difference(self,first_image, second_image):
        return chops.invert(chops.difference(first_image, second_image))

    def get_intersection(self,first_image, second_image):
        return chops.lighter(first_image, second_image)

    def get_union(self,first_image, second_image):
        return chops.darker(first_image, second_image)



    def union_solver(self,image_A, image_B, image_C):
        union_AC = self.get_union(image_A, image_C)
        # print(union_AC.size)
        union_AC_arr = np.array(union_AC)

        union_AC_arr_white = np.count_nonzero(union_AC_arr)
        union_AC_black_pixels = union_AC_arr.size - union_AC_arr_white

        # print('union black pixels: ', union_AC_black_pixels)

        B_arr = np.array(image_B)
        B_white = np.count_nonzero(B_arr)
        B_black_pixels = B_arr.size - B_white
        # print('B black pixels: ', B_black_pixels)

        #print('ratio', union_AC_black_pixels / B_black_pixels)
        return union_AC_black_pixels / B_black_pixels



    def count_nonblack_pil(self,img):
        #https://codereview.stackexchange.com/questions/55902/fastest-way-to-count-non-zero-pixels-using-python-and-pillow
        bbox = img.getbbox()
        if not bbox: return 0
        return sum(img.crop(bbox)
                   .point(lambda x: 255 if x else 0)
                   .convert("L")
                   .point(bool)
                   .getdata())

    def count_black_pixels(self, img):
        w, h = np.size(img)
        w_pixels = self.count_nonblack_pil(img)
        b_pixels = w * h - w_pixels
        return  b_pixels



    def mse(self,imageA, imageB):
        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])

        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err

    def rmsdiff(self,im1, im2):
        "Calculate the root-mean-square difference between two images"
        diff = chops.difference(im1, im2)
        h = diff.histogram()
        sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares / float(im1.size[0] * im1.size[1]))
        return rms



    def diagonal_sover(self, problem, image_a, image_b,  image_d,image_e,image_f,image_h):
        try:
            plus = self.get_intersection(image_f, image_h)
            circle = self.get_image_difference(plus, image_f)
            four_dots = self.get_image_difference(image_a, plus)
            square = self.get_image_difference(circle, image_b)
            heart = self.get_image_difference(four_dots, image_e)

            diff_1 = self.find_difference(self.get_union(plus, four_dots), image_a)
            diff_2 = self.find_difference(self.get_union(heart, four_dots), image_e)
            sol_image = self.get_union(square, four_dots)

            diff_score_array = []
            if diff_1 < 2 and diff_2 < 2:
                #print('here..')
                for solutions in sorted(problem.figures):
                    if solutions.isnumeric():
                        diff_score = self.find_difference(sol_image, Image.open(problem.figures[solutions].visualFilename).convert('L'))
                        #print('diff_score :', diff_score)
                        diff_score_array.append(diff_score)

                if min(diff_score_array) < 5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1
            else:
                return -1

        except BaseException:
            pass




















