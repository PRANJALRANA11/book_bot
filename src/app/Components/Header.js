import React from 'react'
import Image from "next/image";
export default function Header() {
  return (
    <div className='header_div'>
      <p className='header_heading'>Best Website builders in the US</p>
      <div className='header_line'></div>
      <div className='sub_header'>
      <Image className='icon_subheader1'
      src="/tick.png"
      width={18}
      height={18}
      alt="Picture of the search icon"
    />
        <p className='sub_header_para1'>
        Last Updated - February 22, 2020
        </p>

        <Image className='icon_subheader2' 
      src="/info.png"
      width={18}
      height={18}
      alt="Picture of the search icon"
    />
        <p className='sub_header_para2'>
        Advertising Disclosure
        </p>
        <p className='sub_header_para3'>
        Top Relevant
        </p>
        <Image className='icon_subheader3'
      src="/drop.png"
      width={18}
      height={18}
      alt="Picture of the search icon"
    />
      </div>
      <div className='header_line'></div>
      <div className='tools_div'>
        <p className='tools_para'>Tools</p>
        <p className='tools_para'>AWS Builder</p>
        <p className='tools_para'>Start Build</p>
        <p className='tools_para'>Build Supplies</p>
        <p className='tools_para'>Tooling</p>
        <p className='tools_para'>BlueHosting</p>
      </div>
      <div className='hosting_div'>
        <p className='hosting_para1'>Home</p>
        <Image className='hosting_icon'
      src="/vector.png"
      width={12}
      height={12}
      alt="Picture of the search icon"
    />
        <p className='hosting_para2'>Hosting for all</p>
        <Image className='hosting_icon'
      src="/vector.png"
      width={12}
      height={12}
      alt="Picture of the search icon"
    />
        <p className='hosting_para1'>Hosting</p>
        <Image className='hosting_icon'
      src="/vector.png"
      width={12}
      height={12}
      alt="Picture of the search icon"
    />
        <p className='hosting_para2'>Hosting6</p>
        <Image className='hosting_icon'
      src="/vector.png"
      width={12}
      height={12}
      alt="Picture of the search icon"
    />
        <p className='hosting_para2'>Hosting5</p>
      </div>
    </div>
  )
}
