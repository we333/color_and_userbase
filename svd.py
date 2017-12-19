#coding=utf-8
import sys
from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data

likes={
    # "A":{"music","x-men","programming","hindi","english","himesh","lil wayne","rap","travelling","coding"},
    # "B":{"travelling","pop","hanging out","friends","facebook","tv","skating","religion","english","chocolate"},
    # "C":{"programming","pop","rap","gardens","flowers","birthday","tv","summer","youtube","eminem"},
    # "D":{"skating","opera","sony","apple","iphone","music","winter","mango shake","heart","microsoft"},
    # "E":{"music","pics","guitar","glamour","paris","fun","lip sticks","cute guys","rap","winter"},
    # "F":{"office","women","dress","casuals","action movies","fun","public speaking","microsoft","developer"},
    # "G":{"heart","beach","summer","laptops","youtube","movies","hindi","english","cute guys","love"},
    # "H":{"women","beach","laptops","movies","himesh","world","earth","rap","fun","eminem"},
    # "I":{"pilgrimage","programming","house","world","books","country music","bob","tom hanks","beauty","tigers"},
    # "J":{"rap","smart girls","music","wrestling","brock lesnar","country music","public speaking","women","coding","iphone"},
    # "K":{"skating","mountaineering","racing","athletics","sports","adidas","nike","women","apple","pop"},
    # "L":{"heart","sunidhi","hindi","love","love songs","cooking","adidas","beach","travelling","flowers"},
    # "M":{"travelling","comedy","tv","facebook","youtube","cooking","horror","movies","dublin","animals"},
    # "N":{"women","games","xbox","x-men","assassin's creed","pop","rap","opera","need for speed","jeans"},
    # "O":{"heart","mountaineering","sky diving","sony","apple","pop","perfumes","luxury","eminem","lil wayne"},
    # "P":{"cute guys","xbox","shower","beach","summer","english","french","country music","office","birds"}

    "A":{"clothes","hat","shoes"},
    "B":{"shoes","clothes","trousers"},
    "C":{"trousers","shoes","clothes","shock",},
    "D":{"shoes"},
}

def color_user(input_file, output_file, data_file):

    data = Data()

    # VALUE = 1.0
    # for username in likes:
    #     for user_likes in likes[username]:
    #         data.add_tuple((VALUE, username, user_likes)) # Tuple format is: <value, row, column>

    #读取所有user的履历，制作成SVD可执行的matrix
    f_r = open(data_file, 'r')
    for line in f_r:
        info = line.split(',')
        data.add_tuple((1.0, info[0], info[1]))

    svd = SVD()
    svd.set_data(data)
    k = 5 # Usually, in a real dataset, you should set a higher number, e.g. 100
    svd.compute(k=k, min_values=3, pre_normalize=None, mean_center=False, post_normalize=True)

    #从question里读取需要被推荐的userid
    fr = open(input_file, 'r')
    for line in fr:
        userid = line
        output_userid = svd.similar(userid)[1][0] #与目标user最接近的一个user

    #print(output_userid)
    #保存最接近的userid
    fw = open(output_file, 'w')
    fw.write(str(output_userid))

'''
[1]:question.csv 读取需要被推荐的用户的id
[2]:answer.csv 保存最接近的user的id
[3]:data.csv 网站所有用户的履历
'''

color_user(sys.argv[1], sys.argv[2], sys.argv[3])


