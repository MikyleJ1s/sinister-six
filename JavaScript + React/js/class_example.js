console.log("Outside of the class")
class Customer{

    constructor(){
        console.log("Here is a Constructor")
    }
    // variables ...
    #customer_name = "John" // #customer_name makes it private
    _customer_number = "+27841035468" // _customer_number makes it protected
    customer_city = "Cape Town"

    get_customer_name() {
        return this.#customer_name
    }
    set_customer_name(value) {
        this.#customer_name = value
    }

    // this is a method ...
    display_details(){
        console.log(this.get_customer_name() + " lives in " + this.customer_city)
    }
}

// creating the object ...
let obj = new Customer()
obj.display_details()

obj.set_customer_name("Bob")
obj.customer_city = "New York"
obj.display_details()

const vehicles = [{
    "vehicle_color": "red", 
    "vehicle_type": "car", 
    "vehicle_capacity": 4, 
    "vehicle_registration": new Date('2017-02-23')
}, {
    "vehicle_color": "blue", 
    "vehicle_type": "bike", 
    "vehicle_capacity": 2, 
    "vehicle_registration": new Date('2020-10-06')
}, {
    "vehicle_color": "yellow", 
    "vehicle_type": "bus", 
    "vehicle_capacity": 20, 
    "vehicle_registration": new Date('2022-05-18')
}]
console.log(vehicles)

vehicles.push({
    "vehicle_color": "green", 
    "vehicle_type": "van", 
    "vehicle_capacity": 3, 
    "vehicle_registration": new Date('2002-01-03')
})

console.log(vehicles)

let blue_car = vehicles.find(vehicle => vehicle.vehicle_color === "blue")
console.log(blue_car)

let car_blue = vehicles.filter(vehicle => vehicle.vehicle_color === "blue")
console.log(car_blue)

let vehicleCapacity = vehicles.map(vehicle => {
    if (vehicle.vehicle_capacity <= 2){
        return "small"
    }
    if (vehicle.vehicle_capacity <= 5){
        return "medium"
    }
    return "large"
})

console.log(vehicleCapacity)


let vehiclesCapactityWithVehicleType = vehicles.map(vehicle =>{
    let capacityDetails = {
        "capacity" : vehicle.vehicle_capacity,
        "type" : vehicle.vehicle_type,
        "size" : "large" };
    if(vehicle.vehicle_capacity <=3){
        capacityDetails.size = "Small";}
    if(vehicle.vehicle_capacity <=5){
        capacityDetails.size = "Medium";
    }
    capacityDetails.size = "Large";
    return capacityDetails;});
console.log(vehiclesCapactityWithVehicleType);

class Student{
    constructor(student_name,student_age,student_mark){
        console.log("Student class Constructor.....");
        this.student_name = student_name;
        this.student_age = student_age;
        this.student_mark = student_mark;
    }
    displayStudentDetails(){
        console.log(this.student_name +"\t"+this.student_age+"\t"+this.student_mark);
    }}
    
let studentData = new Array();
studentData.push(new Student("Johny",23,8));
studentData.push(new Student("Jin",22,9));
studentData.push(new Student("Romi",22,8.5));
studentData.push(new Student("Rime",21,7));

console.log(studentData);
let studentTopper = studentData.find(student => student.student_mark === 9); // filter works too
console.log(studentTopper);

let student_results = studentData.map(student => {
    if (student.student_mark >= 9){
        return "A"
    }
    if ((student.student_mark < 9) && (student.student_mark >= 8)){
        return "B"
    }
    return "C"
})

console.log(student_results)