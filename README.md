# TaxEasy (Hack Western)

## Inspiration
Our team’s mission is to build a tool that alleviates stress on Canadians during the hefty tax season.

With Canadians spending over 7 hours to complete their tax returns and over $5 billion dollars to cover personal income compliance costs, we decided to come up with a solution to help Canadians save time and money. We created TaxEasy as a web application that uses machine learning to generate a tax return file based on your tax slips! With TaxEasy, Canadians don’t need to understand the complications involved with taxes to file their tax returns. All they need to do is upload their tax slips and TaxEasy will do the rest.

While filing taxes only occurs once a month, it is a gruelling task that takes up time and money. We built TaxEasy in hopes of making Canadians’ lives easier so that they can use their saved time to explore their interests and spend time with their loved ones.

## What it does
TaxEasy is a web application that simplifies the process of completing a tax return as it generates a tax return file for Canadians by taking the information given on tax slips. Using optical character recognition (OCR), TaxEasy recognizes specific categories in the uploaded tax slips and fills out the tax return form accordingly. For instance, when scanning the T4 form, TaxEasy looks for the “Employment Income” box and inserts the given value into the tax return form’s section for Employment Income. This is all done with a simple click of a button. Users only need to upload their tax slips for this process to occur.

## How we built it
We used Microsoft Azure’s Optical Character Recognition (OCR) API for our machine learning implementation. This API was used to train 6 models to recognize the distinct categories present in the following tax slips: T4, T4A, T4A(OAS), T4AP, T1032, and T4E. During the training process, we used supervised learning by creating a labelled training set. We assigned labels based on the information needed on a tax return form. For instance, a tax return form requires an individual’s Employment Income on their T4. Thus, we trained our model to identify where that is on a T4 based on our labels. Moreover, we used Pandas, a Python library, to store the tax return data into a csv-file which was then used to fill in a blank tax return form. For our front-end we used HTML, CSS, Bootstrap, and Python Flask to ensure responsiveness and the smooth integration between our front-end and back-end.
