//
//  Bar.swift
//  LineLeap
//
//  Created by Jason Brill on 1/7/17.
//  Copyright © 2017 LineLeap. All rights reserved.
//

import UIKit

class Bar: NSObject {
    var name:String
    var email:String
    var barid:String
    var photo:UIImage
    
    init(nameIn:String, emailIn:String, baridIn:String, photoIn:UIImage){
        name = nameIn
        email = emailIn
        barid = baridIn
        photo = photoIn
    }
    
}
