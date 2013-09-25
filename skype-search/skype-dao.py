import sqlite3
import logging

DATABASE = '/Users/wcampbell/Library/Application Support/Skype/willcampbell_ha/main.db'

unique_participants_sql = 'SELECT DISTINCT(participants) FROM Chats'
messages_by_author_sql = 'SELECT from_dispname, body_xml FROM Messages where dialog_partner = ?'

def most_common(t):
    word_counter = {}
    for word in t:
        if word and word != "willcampbell_ha":
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    return popular_words

class BaseDao(object):

    def __init__(self, db):
        logging.info('Opening a sqlite db connection')
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        
    def get_all_messages(self, *authors):
        '''
        Return a list of messages by authors
        '''
        self.c.execute(messages_by_author_sql, authors)
        return self.c.fetchall()
        
    def get_unique_participants(self):
        self.c.execute(unique_participants_sql)
        return self.c.fetchall() 
        
b = BaseDao(DATABASE)
#print b.get_all_messages("stacy.vanderworth")

p = []
for participants in b.get_unique_participants():
    participant_list = participants[0]
    if participant_list:
        p += participant_list.split()
    
print most_common(p)[:3]