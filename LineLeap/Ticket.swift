//
//  Ticket.swift
//  LineLeap
//
//  Created by Jason Brill on 1/7/17.
//  Copyright © 2017 LineLeap. All rights reserved.
//

import Foundation

class Ticket:NSObject {
    var price:String
    var bar:Bar
    var tid:String
    
    init(priceIn:String, barIn:Bar, tidIn:String){
        price = priceIn
        bar = barIn
        tid = tidIn
    }
}
