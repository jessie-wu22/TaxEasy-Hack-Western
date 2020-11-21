import os
import azure
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential

################## API KEYS ####################
endpoint = "https://taxes.cognitiveservices.azure.com/"
key = "c811898d898b4b73b63e501d6c4b5782"

# Initializing FormRecognizer
form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))
form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))

def train():
    ##################### TRAINING A MODEL TO RECOGNIZE TAX FORMS ###################
    #t4 trainingDataUrl = "https://hacktax.blob.core.windows.net/taxforms?sp=racwdl&st=2020-11-21T16:42:53Z&se=2020-11-23T16:42:00Z&sv=2019-12-12&sr=c&sig=lWWgoAcKdbIwiyG2Lm6Wez1%2BFlWmCklQjbnxcni4occ%3D"
    #t4a_trainingDataUrl = "https://hacktax.blob.core.windows.net/taxfoura?sp=racwdl&st=2020-11-21T13:47:03Z&se=2020-11-23T13:47:00Z&sv=2019-12-12&sr=c&sig=Gfo8MZoVAYBis9LY28%2FznJqPmYFYqbeM7qqUqcDA694%3D"
    #t4_oastrainingDataUrl = "https://hacktax.blob.core.windows.net/taxoas?sp=racwdl&st=2020-11-21T14:27:07Z&se=2020-11-23T14:27:00Z&sv=2019-12-12&sr=c&sig=5aLgR3QqZ1%2Fump7WZ7Rlom%2BtUvKlfEbtcswKQAtOhGk%3D"
    #t4_ptrainingDataUrl = "https://hacktax.blob.core.windows.net/taxp?sp=racwdl&st=2020-11-21T14:53:36Z&se=2020-11-23T14:53:00Z&sv=2019-12-12&sr=c&sig=k03YDp6QkYUZfKeIKyIBGq8GiDeNVyaTysJ4BPeazqo%3D"
    #t1032trainingDataUrl = "https://hacktax.blob.core.windows.net/tonezerotwo?sp=racwdl&st=2020-11-21T18:50:07Z&se=2020-11-22T18:50:07Z&sv=2019-12-12&sr=c&sig=%2B91D2WpxoNTqwB70iAwGd0wxguEDW%2Ftrfdj4FJIXwiE%3D"
    trainingDataUrl = "https://hacktax.blob.core.windows.net/tfoure?sp=racwdl&st=2020-11-21T19:21:34Z&se=2020-11-22T19:21:34Z&sv=2019-12-12&sr=c&sig=C%2BsKHHZ9PRhMisC4Ai27bGuMIPyQyyZLa66zA7b%2F5%2FE%3D"
    poller = form_training_client.begin_training(trainingDataUrl, use_training_labels=True)
    model = poller.result()

    print("Model ID: {}".format(model.model_id))
    print("Status: {}".format(model.status))
    print("Training started on: {}".format(model.training_started_on))
    print("Training completed on: {}".format(model.training_completed_on))

    print("\nRecognized fields:")
    for submodel in model.submodels:
        print(
            "The submodel with form type '{}' has recognized the following fields: {}".format(
                submodel.form_type,
                ", ".join(
                    [
                        field.label if field.label else name
                        for name, field in submodel.fields.items()
                    ]
                ),
            )
        )

    # Training result information
    for doc in model.training_documents:
        print("Document name: {}".format(doc.name))
        print("Document status: {}".format(doc.status))
        print("Document page count: {}".format(doc.page_count))
        print("Document errors: {}".format(doc.errors))

def predict(formType: str,file: str) -> dict:
    # CHOOSING WHICH OCR MODEL TO USE
    if(formType == "t4"):
        model_id = "622af8ca-b4b1-4b21-9a1d-43660e99e26f"
    # t4a model
    elif(formType == "t4a"):
        model_id = "e767d07a-0893-4942-86dd-00e1d95985ec"
    # t4a OAS model
    elif(formType == "t4aoas"):
        model_id = "85ddc545-fa1d-4db2-9702-e23ea1c3071f"
    # t4a p model
    elif(formType == "t4ap"):
        model_id = "0e55897c-f345-45f1-8e71-d8482879bc17"
    # t1032 model
    elif(formType == "t1032"):
        model_id = "e90c5cf8-c853-4533-8d7a-44c04d88d776"
    else:
        model_id = "77dad902-b83d-4380-8cbd-f66d02e08939"

    with open(file, "rb") as f:
        poller = form_recognizer_client.begin_recognize_custom_forms(
            model_id=model_id, form=f
        )

    result = poller.result()

    # dictionary to store all the results
    myDict = {}

    for recognized_form in result:
        for name, field in recognized_form.fields.items():
            myDict[name] = field.value_data.text

    return myDict

