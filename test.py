from deepface import DeepFace
import os

path = input(' enter path:  ')
images = os.listdir(path)

attributes = ['race']

output_file = open('output.txt', 'a')

for img in images:
    dct = DeepFace.analyze(f"{path}/{img}", attributes)
    asian = dct['race']['asian']
    indian = dct['race']['indian']
    latino = dct['race']['latino hispanic']
    black = dct['race']['black']
    white = dct['race']['white']
    middle_eastern = dct['race']['middle eastern']
    dominant_race = dct['dominant_race']

    output_file.write(img)
    output_file.write(', ')
    output_file.write('asian, ')
    output_file.write(str(asian))
    output_file.write(', ')
    output_file.write('indian, ')
    output_file.write(str(indian))
    output_file.write(', ')
    output_file.write('black, ')
    output_file.write(str(black))
    output_file.write(', ')
    output_file.write('white, ')
    output_file.write(str(white))
    output_file.write(', ')
    output_file.write('middle eastern, ')
    output_file.write(str(middle_eastern))
    output_file.write(', ')
    output_file.write('dominant race, ')
    output_file.write(str(dominant_race))
    output_file.write(', ')
    output_file.write('\n')

    print('hello')


output_file.close()
