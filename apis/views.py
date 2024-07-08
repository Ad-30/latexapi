from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
import os
from .templatefun import template_one
import json
from pylatex import Document, NoEscape 
import urllib.request
from .templatefun import *
from PIL import Image
from uuid import uuid4
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from apis.authentication import AccessKeyAuthentication
from django.conf import settings
@method_decorator(csrf_exempt, name='dispatch')
@authentication_classes([AccessKeyAuthentication])
# @permission_classes([IsAuthenticated])
class LaTeXToPDFView(APIView):
    def post(self, request, format=None):
        try:
            image_name = None
            applicant_data = json.loads(request.POST.get('applicantData', '{}'))
            # print(request.POST.get('imageURL'))
            if not applicant_data:
                return Response({'error': 'Json data required'}, status=400)

            if 'selectedTemplate' not in applicant_data:
                return Response({'error': 'Selected template not provided'}, status=400)

            if applicant_data["selectedTemplate"] in [3, 5]:
                image_url = request.POST.get('imageURL')
                if not image_url:
                    return Response({'error': 'Image URL required for selected template 3'}, status=400)
                try:
                    image_name = image_url.split('/')[-1].replace('%', '')
                    image_path = os.path.join(settings.BASE_DIR, 'apis', 'pdfs', image_name)
                    try:
                        urllib.request.urlretrieve(image_url, image_path)
                    except:
                        urllib.request.urlretrieve('https://resushape.s3.eu-north-1.amazonaws.com/user.png', image_path)
                    image = Image.open(image_path)
                    target_width = 100
                    original_width, original_height = image.size
                    target_height = int((target_width / original_width) * original_height)
                    resized_image = image.resize((target_width, target_height))
                    resized_image.save(image_path)
                    image.close()
                except urllib.error.URLError as e:
                    return Response({'error': 'Failed to retrieve image from URL'}, status=400)
                except OSError as e:
                    return Response({'error': 'Error processing image file'}, status=400)
                except Exception as e:
                    return Response({'error': f'Unexpected error with image processing: {str(e)}'}, status=500)

            def generate_pdf():
                try:
                    doc = Document(geometry_options={'tmargin': '0.8in', 'bmargin': '0.8in', 'lmargin': '0.8in', 'rmargin': '0.8in'})
                    if applicant_data["selectedTemplate"] == 1:
                        doc_head, doc_body = template_one(applicant_data, image_name)
                    elif applicant_data["selectedTemplate"] == 2:
                        doc_head, doc_body = template_two(applicant_data, image_name)
                    elif applicant_data["selectedTemplate"] == 3:
                        doc_head, doc_body = template_three(applicant_data, image_name)
                    elif applicant_data["selectedTemplate"] == 4:
                        doc_head, doc_body = template_four(applicant_data, image_name)
                    elif applicant_data["selectedTemplate"] == 5:
                        doc_head, doc_body = template_five(applicant_data, image_name)
                    else:
                        return Response({'error': 'Selected Template Does Not Exist'}, status=400)
                    doc.preamble.append(NoEscape(doc_head))
                    doc.append(NoEscape(doc_body))
                    pdf_name = f"resume_{uuid4()}"
                    pdf_path = os.path.join(settings.BASE_DIR, 'apis', 'pdfs', pdf_name)
                    doc.generate_pdf(pdf_path, clean_tex=True)
                    return pdf_name
                except Exception as e:
                    return Response({'error': f'Error generating PDF: {str(e)}'}, status=500)

            pdf_ex = ".pdf"
            pdf_name_or_response = generate_pdf()

            if isinstance(pdf_name_or_response, Response):
                return pdf_name_or_response
            else:
                try:
                    file = os.path.join(settings.BASE_DIR, 'apis', 'pdfs', pdf_name_or_response + pdf_ex)
                    response = FileResponse(open(file, 'rb'), as_attachment=True, filename="resume.pdf")
                    if applicant_data["selectedTemplate"] in [3, 5]:
                        image_path = os.path.join(settings.BASE_DIR, 'apis', 'pdfs', image_name)
                        os.remove(image_path)
                    os.remove(file)
                    return response
                except FileNotFoundError as e:
                    return Response({'error': 'PDF file not found'}, status=500)
                except Exception as e:
                    return Response({'error': f'Error returning PDF file: {str(e)}'}, status=500)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            return Response({'error': f'Unexpected server error: {str(e)}'}, status=500)
        
            
        