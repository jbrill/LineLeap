//
//  User.swift
//  LineLeap
//
//  Created by Jason Brill on 1/6/17.
//  Copyright © 2017 LineLeap. All rights reserved.
//

import UIKit

class User: NSObject {
    var name:String
    var email:String
    var uid:String
    var photo:UIImage
    var bars:[Bar] = []
    var tickets:[Ticket] = []
    
    init(nameIn:String, emailIn:String, uidIn:String, photoIn:UIImage){
        name = nameIn
        email = emailIn
        uid = uidIn
        photo = photoIn
    }
}
