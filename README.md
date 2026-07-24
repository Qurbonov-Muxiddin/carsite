# Django Mini Exam (CBV) — Car Site

## O'rnatish (Uzbek)

1. Virtual muhit yarating va faollashtiring:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS / Linux
   ```

2. Kutubxonalarni o'rnating:
   ```
   pip install -r requirements.txt
   ```

3. Migratsiyalarni bajaring:
   ```
   python manage.py migrate
   ```

4. Admin uchun superuser yarating (ixtiyoriy, Brand qo'shish uchun kerak bo'lishi mumkin):
   ```
   python manage.py createsuperuser
   ```

5. Serverni ishga tushiring:
   ```
   python manage.py runserver
   ```

6. Brauzerda oching: http://127.0.0.1:8000/

## Topshiriq talablari va ular qayerda bajarilgan

| № | Talab | Qayerda |
|---|---|---|
| 1 | Ro'yxatdan o'tish / Login / Logout | `cars/views.py` — RegisterView, UserLoginView, UserLogoutView |
| 2 | Brand va Cars modellari, ForeignKey | `cars/models.py` |
| 3 | To'liq CRUD, barchasi CBV | `cars/views.py` — CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView |
| 4 | ModelForm (Create/Update) | `cars/forms.py` — CarForm |
| 5 | Detail sahifa | `cars/templates/cars/car_detail.html` |
| 6 | Search (GET parametri) | `CarListView.get_queryset()` — `?q=...` |
| 7 | base.html + extends/block | `cars/templates/cars/base.html` va barcha boshqa templates |
| 8 | simple_tag | `cars/templatetags/cars_extras.py` — site_name, current_year, total_cars_count |
| 9 | Navbar barcha sahifalarda | `base.html` ichidagi `<nav>` |
| 10 | Login qilmagan foydalanuvchi Create/Update/Delete ga kira olmaydi | `LoginRequiredMixin` — CarCreateView, CarUpdateView, CarDeleteView |

## Admin panel

`/admin/` orqali Brand va Car obyektlarini qo'shishingiz mumkin (avval superuser yarating).

Eslatma: Loyihada rasm (ImageField) ishlatilgani uchun `Pillow` kutubxonasi kerak — u `requirements.txt` da bor.
