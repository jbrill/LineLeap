//
//  NearbyMeetingCell.swift
//  LineLeap
//
//  Created by Jason Brill on 1/6/17.
//  Copyright © 2017 LineLeap. All rights reserved.
//

import UIKit

class NearbyMeetingCell: UITableViewCell {
    @IBOutlet weak var price: UILabel!

    @IBOutlet weak var barPicture: UIImageView!
    @IBOutlet weak var city: UILabel!
    @IBOutlet weak var barTitle: UILabel!
    @IBOutlet weak var distance: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
        
        let str = NSAttributedString(string: "$30", attributes: [
            NSForegroundColorAttributeName : UIColor.c1(),
            NSStrokeColorAttributeName : UIColor.black,
            NSStrokeWidthAttributeName : -1,
            NSFontAttributeName : UIFont.systemFont(ofSize: 60.0)
            ])
        
        barTitle.attributedText = str
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }
    
    @IBAction func BarClicked(_ sender: Any) {
        
    }
}
