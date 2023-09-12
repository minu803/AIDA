
import config

def get_age_guidance():
    if config.age == 2:
        config.age_guidances = '''
        A child who is 2 years old:
        Knows some spatial concepts, such as "in" or "on"
        Knows pronouns, such as "you," "me" or "her"
        Knows descriptive words, such as "big" or "happy"
        Uses 3-word sentences
        Speech is becoming more accurate, but may still leave off ending sounds. Strangers may not be able to understand much of what is said.
        Answers simple questions
        Begins to use more pronouns, such as "you" or "I"
        Uses question inflection to ask for something, such as "my ball?"
        Begins to use plurals, such as "shoes" or "socks" and regular past tense verbs, such as "jumped"

        From 2.5 to 3 years old: the mean length utterance the child can produce is about 2.91 - 3.23
        '''
    if config.age == 3:
        config.age_guidances = '''
        A child who is 3 years old:
        Groups objects, such as foods or clothes
        Identifies colors
        Uses most speech sounds, but may distort some of the more difficult sounds, such as l, r, s, sh, ch, y, v, z, th. These sounds may not be fully mastered until age 7 or 8.
        Uses consonants in the beginning, middle, and ends of words. Some of the more difficult consonants may be distorted, but attempts to say them
        Strangers are able to understand much of what is said
        Able to describe the use of objects, such as "fork" or "car"
        Has fun with language; enjoys poems and recognizes language absurdities, such as, "Is that an elephant on your head?"
        Expresses ideas and feelings rather than just talking about the world around him or her
        Uses verbs that end in "ing," such as "walking" or "talking"
        Answers simple questions, such as "What do you do when you are hungry?"
        Repeats sentences.
        
        From 3 to 4 years old: mean length utterance is about 3.43 - 4.09.
        '''
    if config.age == 4:
        config.age_guidances = '''
        A child who is 4 years old:
        Understands spatial concepts, such as "behind" or "next to"
        Understands complex questions
        Speech is understandable, but makes mistakes pronouncing long, difficult, or complex words, such as "hippopotamus"
        Uses some irregular past tense verbs, such as "ran" or "fell"
        Describes how to do things, such as painting a picture
        Lists items that belong in a category, such as animals or vehicles
        Answers "why" questions
        
        From 4 to 5 years old: mean length utterance is about 4.1 - 4.75.
        '''
    if config.age == 5:
        config.age_guidances = '''
        A child who is 5 years:
        Understands time sequences (for example, what happened first, second, or third)
        Carries out a series of 3 directions
        Understands rhyming
        Engages in conversation
        Sentences can be 8 or more words in length
        Uses compound and complex sentences
        Describes objects
        Uses imagination to create stories
        
        From 5 to 6 years old: mean length utterance is about 4.38 - 4.96.
        '''

'''
Kids often learn words about things they can touch, see, or do during their preschool years. 
These words have 'concrete' meanings. But kids also start learning 'relational' words when they're about two years old.
These are words that tell us how things relate to each other. For example, some words show us how things happen, 
like 'could', 'will', 'both', 'after', 'instead', 'inside', 'whose', 'all', 'enough', 'where', 'what', 
and different ways to say 'to be'. Other words show relationships, like 'aunt' and 'niece', 'boss' and 'worker', 
verbs like 'balance' and 'put', and words that show differences like 'big' and 'small', 'good' and 'bad', 
and 'quickly' and 'slowly'. Preschool kids don't usually learn many words that are symbols for other words, 
like 'add', 'plan', 'science', 'history', 'divide'. Instead, they learn words that represent real things they 
can see and do.
'''
