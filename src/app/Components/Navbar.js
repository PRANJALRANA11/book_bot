import React from 'react'
import Image from "next/image";
export default function Navbar() {
  return (
    <div className='Navbar_div'>
        <div className='Nav_search_div'>
        <Image className='Navbar_search_icon'
      src="/IMAGE.png"
      width={18}
      height={18}
      alt="Picture of the search icon"
    />
        <input className='Navbar_search'/>
        </div>
        <div className='Nav_items'>
            <a href='/' className='Nav_item_ancor'>Categories</a>
            <a href='/' className='Nav_item_ancor'>Website Builders</a>
            <a href='/' className='Nav_item_ancor'>Today's Deals</a>
        </div>
    </div>
  )
}
