from io import BytesIO

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Spacer, Table

from company.models import Company


def download_pdf(request):
    pdf = generate_pdf()
    response = HttpResponse(pdf.read(), content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=company.pdf"
    pdf.close()
    return response


def send_mail_pdf(request, email):
    pdf = generate_pdf()

    email_message = EmailMessage(
        "Report of all company's",
        "All company's",
        settings.EMAIL_HOST_USER,
        [email],
        attachments=[("company.pdf", pdf.read(), "application/pdf")],
    )
    email_message.send()
    pdf.close()

    return HttpResponse("Email sent with PDF")


def generate_pdf():
    data = Company.objects.all()
    elements = []

    for company in data:
        elements.append(Spacer(1, 22))
        elements.append(generate_company_table([company]))
        elements.append(Spacer(1, 22))
        elements.append(generate_product_table(company.products.all()))

    pdf_buffer = BytesIO()

    doc = SimpleDocTemplate(pdf_buffer, rightMargin=25, leftMargin=25, topMargin=42, bottomMargin=18)

    doc.build(elements)
    pdf_buffer.seek(0)
    return pdf_buffer


def generate_company_table(companies):
    headers = ["Name", "Address", "NIT", "Phone"]
    table_data = [headers] + [[company.name, company.direction, company.nit, company.phone] for company in companies]
    return Table(table_data, colWidths=100, rowHeights=15)


def try_get_price(product, code):
    try:
        return product.prices.get(code=code).price
    except ObjectDoesNotExist:
        return "N/A"


def generate_product_table(products):
    all_data = [["Name", "Code", "Price in USD", "Price in EUR", "Price in COP"]]
    for product in products:
        all_data.append(
            [
                product.name,
                product.code,
                try_get_price(product, 1),
                try_get_price(product, 2),
                try_get_price(product, 3),
            ]
        )
    return Table(
        all_data,
        colWidths=100,
        rowHeights=20,
    )
