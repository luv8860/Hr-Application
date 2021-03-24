import 'dart:ui';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
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
            // {
            //     'dept': department,
            //     'region': region,
            //     'education': education,
            //     'gender': gender,
            //     'recruitment_channel': recruitment,
            //     'kpi': kpi == 'yes' ? 1 : 0,
            //     'award': award == 'yes' ? 1 : 0,
            //     'age': age,
            //     'no_of_trainings': trainings,
            //     'length_of_service': service,
            //     'avg': avg,
            //     'previous_year_rating': rate
            //   }
            {
              "dept": "Sales & Marketing",
              "region": "region_19",
              "education": "Bachelor's",
              "gender": "male",
              "recruitment_channel": "sourcing",
              "no_of_trainings": 1,
              "age": 34,
              "previous_year_rating": 3,
              "length_of_service": 7,
              "kpi": 0,
              "awards": 0,
              "avg": 50
            }));
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
    return urll == null
        ? Center(
            child: Container(
                height: 200, width: 200, child: CircularProgressIndicator()))
        : Dialog(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(Constants.padding),
            ),
            elevation: 0,
            backgroundColor: Colors.transparent,
            child: contentBox(context),
          );
  }

  contentBox(context) {
    Stack(
      children: <Widget>[
        Container(
          padding: EdgeInsets.only(
              left: Constants.padding,
              top: Constants.avatarRadius + Constants.padding,
              right: Constants.padding,
              bottom: Constants.padding),
          margin: EdgeInsets.only(top: Constants.avatarRadius),
          decoration: BoxDecoration(
              shape: BoxShape.rectangle,
              color: Colors.white,
              borderRadius: BorderRadius.circular(Constants.padding),
              boxShadow: [
                BoxShadow(
                    color: Colors.black, offset: Offset(0, 10), blurRadius: 10),
              ]),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              Text(
                "Result",
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.w600),
              ),
              SizedBox(
                height: 15,
              ),
              Text(
                urll,
                style: TextStyle(fontSize: 14),
                textAlign: TextAlign.center,
              ),
              SizedBox(
                height: 22,
              ),
              Align(
                alignment: Alignment.bottomRight,
                child: FlatButton(
                    onPressed: () {
                      Navigator.of(context).pop();
                    },
                    child: Text(
                      "OK",
                      style: TextStyle(fontSize: 18),
                    )),
              ),
            ],
          ),
        ),
        Positioned(
          left: Constants.padding,
          right: Constants.padding,
          child: CircleAvatar(
            backgroundColor: Colors.transparent,
            radius: Constants.avatarRadius,
            child: ClipRRect(
                borderRadius:
                    BorderRadius.all(Radius.circular(Constants.avatarRadius)),
                child: Icon(Icons.info, size: 75, color: Colors.black54)),
          ),
        ),
      ],
    );
  }
}
