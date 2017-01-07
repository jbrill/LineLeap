//
//  UserController.swift
//  LineLeap
//
//  Created by Jason Brill on 1/6/17.
//  Copyright © 2017 LineLeap. All rights reserved.
//

import UIKit

class UserController {
        
    static var sharedInstance:UserController = UserController()
        
    var currUser:User?
        
    func register(email:String, password:String, firstname:String, lastname: String, userType: String, myCompletion: (String?) -> Void){
    }
        
        
    func login(email:String, password:String, onCompletion: (String?) -> Void){
          onCompletion("SUCCESS")
    }
        
    func obtainLocations(onCompletion: (String?) -> Void){
            
    }
        
        
    func logout(onCompletion: (String?) -> Void){
        
    }
    /*
    // Only override draw() if you perform custom drawing.
    // An empty implementation adversely affects performance during animation.
    override func draw(_ rect: CGRect) {
        // Drawing code
    }
    */

}
