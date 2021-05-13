import spacy
import PyPDF2
import os

nlp = spacy.load('en_core_web_sm')

def readPdfFile(filename, folder_name):
    
    data_path = str(os.getcwd()) + "\\" + folder_name

    file = open(data_path + "\\" + filename, mode="rb")

    pdf_reader = PyPDF2.PdfFileReader(file)
    num_pages = pdf_reader.numPages

    text = []
    for pages in range(0, num_pages):
        current_page = pdf_reader.getPage(pages)
        text.append(current_page.extractText().replace("\n","").lower())

    # # remove \n from list
    # text = [t.replace("\n", "").lower() for t in text]

    # store content of 1-last page in a seperate list
    rest_pages = []
    for t in text[1:]:
        rest_pages.append(t[115:])

    # store 0th page content separately
    first_page = [text[0][850:]]

    # storing the 0th and 1-last page content after cleaning in text
    text = first_page + rest_pages
    
    # creating a single string containing full text
    full_text = "".join(text)

    print(full_text)

    return full_text


# customer sentence segmenter for creating spacy document object
def setCustomBoundaries(doc):
    # traversing through tokens in document object
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i + 1].is_sent_start = True
        if token.text == ".":
            doc[token.i + 1].is_sent_start = False
    return doc


# # create spacy document object from pdf text
# def getSpacyDocument(pdf_text, nlp):
#     main_doc = nlp(pdf_text)  # create spacy document object

#     return main_doc

# # adding setCusotmeBoundaries to the pipeline
# nlp.add_pipe(setCustomBoundaries, before='parser')

# def createKeywordsVectors(keyword, nlp):
#     doc = nlp(keyword)  # convert to document object

#     return doc.vector


# # method to find cosine similarity
# def cosineSimilarity(vect1, vect2):
#     # return cosine distance
#     return 1 - spatial.distance.cosine(vect1, vect2)


# # method to find similar words
# def getSimilarWords(keyword, nlp):
#     similarity_list = []

#     keyword_vector = createKeywordsVectors(keyword, nlp)

#     for tokens in nlp.vocab:
#         if (tokens.has_vector):
#             if (tokens.is_lower):
#                 if (tokens.is_alpha):
#                     similarity_list.append((tokens, cosineSimilarity(keyword_vector, tokens.vector)))

#     similarity_list = sorted(similarity_list, key=lambda item: -item[1])
#     similarity_list = similarity_list[:30]

#     top_similar_words = [item[0].text for item in similarity_list]

#     top_similar_words = top_similar_words[:3]
#     top_similar_words.append(keyword)

#     for token in nlp(keyword):
#         top_similar_words.insert(0, token.lemma_)

#     for words in top_similar_words:
#         if words.endswith("s"):
#             top_similar_words.append(words[0:len(words)-1])

#     top_similar_words = list(set(top_similar_words))

#     top_similar_words = [words for words in top_similar_words if enchant_dict.check(words) == True]

#     return ", ".join(top_similar_words)

  
# keywords = ['label', 'package']
# similar_keywords = getSimilarWords(keywords, nlp)

if __name__ == "__main__":
    readPdfFile('pdf.pdf', 'testpdf')