
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'catering.settings')

django.setup()


from orders.models import buyurtma, Sotuv
from pasuda_qoshish.models import Toifalash



for i in Toifalash.objects.all():
    print(i.id)


for i in buyurtma.buyurtmalar.all():
    if isinstance(i, buyurtma):
        print(i.id, i.maxsulot.nomi)
        i.delete()


{
    "buyurtmalar": [
        {
            'nomi': 'Sarvar',
            'puli': 1200,
            'sotuv_id': 1,
            "toifa_id": 1
        },
        {
            'nomi': 'Sarvar',
            'puli': 1200,
            'sotuv_id': 1,
            "toifa_id": 1
        },
        {
            'nomi': 'Sarvar',
            'puli': 1200,
            'sotuv_id': 1,
            "toifa_id": 1
        },
        {
            'nomi': 'Sarvar',
            'puli': 1200,
            'sotuv_id': 1,
            "toifa_id": 1
        },
        {
            'nomi': 'Sarvar',
            'puli': 1200,
            'sotuv_id': 1,
            "toifa_id": 1
        },
    ]
}


