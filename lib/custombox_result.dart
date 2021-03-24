import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:hr_application/custombox.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Constants {
  Constants._();
  static const double padding = 20;
  static const double avatarRadius = 45;
}

class CustomDialogBox2 extends StatefulWidget {
  final String department;
  final String region;
  final String education;
  final String gender;
  final String recruitment;
  final String kpi;
  final String award;
  final String age;
  final String trainings;
  final String service;
  final String avg;
  final String rate;
  const CustomDialogBox2(
      {Key key,
      this.department,
      this.region,
      this.education,
      this.gender,
      this.recruitment,
      this.kpi,
      this.award,
      this.age,
      this.trainings,
      this.service,
      this.avg,
      this.rate})
      : super(key: key);

  @override
  _CustomDialogBox2State createState() => _CustomDialogBox2State(
      department,
      region,
      education,
      gender,
      recruitment,
      kpi,
      award,
      age,
      trainings,
      service,
      avg,
      rate);
}

class _CustomDialogBox2State extends State<CustomDialogBox2> {
  final String department;
  final String region;
  final String education;
  final String gender;
  final String recruitment;
  final String kpi;
  final String award;
  final String age;
  final String trainings;
  final String service;
  final String avg;
  final String rate;
  _CustomDialogBox2State(
      this.department,
      this.region,
      this.education,
      this.gender,
      this.recruitment,
      this.kpi,
      this.award,
      this.age,
      this.trainings,
      this.service,
      this.avg,
      this.rate);
  String url = "https://hr-application-flutter.herokuapp.com/";
  var urll;
  void getname() async {
    var send = await http.post(url,
        headers: {'Content-Type': 'application/json'},
        body: json.encode(
            {
                "dept": department.toString(),
                "region": region.toString(),
                "education": education.toString(),
                "gender": gender.toString(),
                "recruitment_channel": recruitment.toString(),
                "kpi": kpi == 'yes' ? 1 : 0,
                "awards": award == 'yes' ? 1 : 0,
                "age": age.toString(),
                "no_of_trainings": trainings.toString(),
                "length_of_service": service.toString(),
                "avg": avg.toString(),
                "previous_year_rating": rate.toString()
              }
            // {
            //   "dept": "Sales & Marketing",
            //   "region": "region_19",
            //   "education": "Bachelor's",
            //   "gender": "male",
            //   "recruitment_channel": "sourcing",
            //   "no_of_trainings": 1,
            //   "age": 34,
            //   "previous_year_rating": 3,
            //   "length_of_service": 7,
            //   "kpi": 0,
            //   "awards": 0,
            //   "avg": 50
            // }
            ));
    final decode = json.decode(send.body);
    setState(() {
      print(decode.toString() + 'main');
      urll = decode['result'];
      print(urll);
    });
  }

  @override
  void initState() {
    super.initState();
    getname();
  }

  @override
  Widget build(BuildContext context) {
    if (urll == null) {
      return Center(
          child: Container(
              height: 200, width: 200, child: CircularProgressIndicator()));
    } else {
      return CustomDialogBox(
          title: "Result",
          descriptions: urll == "yes"
              ? "Yes this candidate is eligible"
              : "Sorry This candidate is not eligible",
          text: "OK");
    }
  }
}
