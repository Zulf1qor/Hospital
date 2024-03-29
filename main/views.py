from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


class Get_Employee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class Get_Room(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class Get_Address(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class Get_Cashflow(ListAPIView):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer


class Get_Patient(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class Get_Testimonal_patient(ListAPIView):
    queryset = Testimonal_patient.objects.all()
    serializer_class = Testimonal_patientSerializer


class Get_Department(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class Get_Operation(ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class Get_Attendance(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class Get_Cassa(ListAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer

@api_view(["GET"])
def employee_by_full_name(request):
    full_name = request.GET.get('full_name')
    employee = Employee.objects.filter(full_name__icontains=full_name)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_specialty(request):
    specialty = request.GET.get('specialty')
    employee = Employee.objects.filter(specialty__icontains=specialty)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    employee = Employee.objects.filter(spphone_number__icontains=phone_number)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_address(request):
    address = request.GET.get('address')
    employee = Employee.objects.filter(address__icontains=address)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_room(request):
    room = request.GET.get('room')
    employee = Employee.objects.filter(room__icontains=room)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_salary(request):
    salary = request.GET.get('salary')
    employee = Employee.objects.filter(salary__icontains=salary)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_started_work(request):
    started_work = request.GET.get('started_work')
    employee = Employee.objects.filter(started_work__icontains=started_work)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_age(request):
    age = request.GET.get('age')
    employee = Employee.objects.filter(age__icontains=age)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_extra_phone_number(request):
    extra_phone_number = request.GET.get('extra_phone_number')
    employee = Employee.objects.filter(extra_phone_number__icontains=extra_phone_number)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def patient_by_full_name(request):
    full_name = request.GET.get('full_name')
    patient = Patient.objects.filter(full_name__icontains=full_name)
    ser = PatientSerializer(patient, many=True)
    return Response(ser.data)


@api_view(["GET"])
def patient_by_age(request):
    age = request.GET.get('age')
    patient = Patient.objects.filter(age__icontains=age)
    ser = PatientSerializer(patient, many=True)
    return Response(ser.data)


@api_view(["GET"])
def patient_by_room(request):
    room = request.GET.get('room')
    patient = Patient.objects.filter(room__icontains=room)
    ser = PatientSerializer(patient, many=True)
    return Response(ser.data)


@api_view(["GET"])
def patient_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    patient = Patient.objects.filter(phone_number__icontains=phone_number)
    ser = PatientSerializer(patient, many=True)
    return Response(ser.data)


@api_view(["GET"])
def patient_by_doctor(request):
    doctor = request.GET.get('doctor')
    patient = Patient.objects.filter(doctor__icontains=doctor)
    ser = PatientSerializer(patient, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_name(request):
    name = request.GET.get('name')
    room = Room.objects.filter(name__icontains=name)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_deparment(request):
    deparment = request.GET.get('deparment')
    room = Room.objects.filter(deparment__icontains=deparment)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_number(request):
    number = request.GET.get('number')
    room = Room.objects.filter(number__icontains=number)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_equipment(request):
    equipment = request.GET.get('equipment')
    room = Room.objects.filter(equipment__icontains=equipment)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def cashflow_by_patient(request):
    patient = request.GET.get('patient')
    cashflow = Cashflow.objects.filter(patient__icontains=patient)
    ser = CashflowSerializer(cashflow, many=True)
    return Response(ser.data)


@api_view(["GET"])
def cashflow_by_timestamp(request):
    timestamp = request.GET.get('timestamp')
    cashflow = Cashflow.objects.filter(timestamp__icontains=timestamp)
    ser = CashflowSerializer(cashflow, many=True)
    return Response(ser.data)


@api_view(["GET"])
def cashflow_by_payment_type(request):
    payment_type = request.GET.get('payment_type')
    cashflow = Cashflow.objects.filter(payment_type__icontains=payment_type)
    ser = CashflowSerializer(cashflow, many=True)
    return Response(ser.data)


@api_view(["GET"])
def testimonal_patient_by_payment_type(request):
    payment_type = request.GET.get('payment_type')
    testimonal_patient = Testimonal_patient.objects.filter(payment_type__icontains=payment_type)
    ser = Testimonal_patientSerializer(testimonal_patient, many=True)
    return Response(ser.data)

@api_view(["GET"])
def equipment_filter_by_name(request):
    name = request.GET.get('name')
    equipment = Equipment.objects.filter(name__icontains=name)
    ser = EquipmentSerializer(equipment, many=True)
    return Response(ser.data)


@api_view(["GET"])
def department_filter_by_name(request):
    name = request.GET.get('name')
    department = Department.objects.filter(name__icontains=name)
    ser = DepartmentSerializer(department, many=True)
    return Response(ser.data)


@api_view(["GET"])
def attendance_filter_by_employee(request):
    employee = request.GET.get('employee')
    attendance = Attendance.objects.filter(employee=employee)
    ser = EmployeeSerializer(attendance, many=True)
    return Response(ser.data)


@api_view(["GET"])
def attendance_filter_by_date(request):
    date = request.GET.get('date')
    attendance = Attendance.objects.filter(date=date)
    ser = AttendanceSerializer(attendance, many=True)
    return Response(ser.data)


@api_view(["GET"])
def cashflow_filter_by_timestap(request):
    timestap = request.GET.get('timestap')
    cashflow = Cashflow.objects.filter(timestap=timestap)
    ser = CashflowSerializer(cashflow, many=True)
    return Response(ser.data)


@api_view(["GET"])
def cashflow_filter_by_amount(request):
    amount = request.GET.get('amount')
    amount = float(amount_str.replace(',','.'))
    cashflow = Cashflow.objects.filter(amount=amount)
    ser = CashflowSerializer(cashflow, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_by_doctor(request):
    doctor = request.GET.get('doctor')
    operation = Operation.objects.filter(doctor=doctor)
    ser = OperationSerializers(operation, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_operation_by_date_time(reuqest):
    date_time = reuqest.GET.get('date_time')
    operation = Operation.objects.filter(date_time=date_time)
    ser = OperationSerializers(operation, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_operation_by_time(request):
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')
    if start_time and end_time:
        filtered_operation = Operation.objects.filter(start_time__gte=start_time, end_time__lte=end_time)
        for operation in filtered_operation:
            print(operation)
        ser = OperationSerializers(filtered_operation, many=True)
        return Response(ser.data)
    else:
        return Response({"error": "Both start_time and end_time are required."}, status=400)


@api_view(['GET'])
def filter_operation_by_patient(request):
    patient = request.GET.get('patient')
    operation = Operation.objects.filter(patient=patient)
    ser = OperationSerializers(operation, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_operation_by_room(request):
    room = request.GET.get('room')
    operation = Operation.objects.filter(room=room)
    ser = OperationSerializers(operation, many=True)
    return Response(ser.data)