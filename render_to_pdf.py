# HTML File

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Mushak - 6.4</title>
    <style media="all">
        body {
            font-weight: 100;
            font-size: 9.3px;
        }

        .hrItem {
            border: none;
            height: 1px;
            /* Set the hr color */
            color: #333; /* old IE */
            background-color: #fff; /* Modern Browsers */
        }

        {# Table Header and Footer Fixed #}
        table {
            width: 100%
        }

        thead tr,
        tfoot tr {
            position: absolute;
            left: 0;
            right: 15px;
            /* to not cover the scrollbar*/
            background: red
        }

        thead th,
        tfoot td {
            display: inline-block;
        }

        thead tr {
            top: 0
        }

        tfoot tr {
            top: 500px /* same value has max-height from div */
        }

    </style>
</head>
<body>
<header>
    <table>
        <tr style="border: none;">
            <td style="width: 20%;border: none;">
                <img width="100px" height="100px" src="http://127.0.0.1:8000/folder/media/government_image.png">
            </td>
            <td style="text-align: center; width: 60%;border: none;">
                <p>Test
                <p>
                <p>Test</p>
                <p>Test
                <p>
                <p>Test</p>
            </td>
            <td style="width: 20%;text-align: center;">
                Test
            </td>
        </tr>
    </table>
</header>

<script type="text/css">

</script>
</body>
</html>

# views.py 

def get(self, request, *args, **kwargs):
    tempate = get_template('demo/render_to_pdf.html')
    context = {
        'order_id': 12345,
        'img_url': 'http://127.0.0.1:8000/folder/media/government_image.png',
        'amount': 39.99,
        'registered_person': 'Hasan Mahmud',
        'registered_person_bin_no': '1234567895789',
        'registered_person_address': 'Khilgaon, Dhaka, Bangladesh',
        'bill_no': 1233434,
        'diclist': {
            'id': [1, 2, 3],
        },
        'range': range(1, 5)
    }

    pdf = render_to_pdf('demo/render_to_pdf.html', context)

    return HttpResponse(pdf, content_type='application/pdf')


# utils.py

from io import BytesIO, StringIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

# URL

path('render_to_pdf', render_to_pdf.as_view(), name="render_to_pdf"),