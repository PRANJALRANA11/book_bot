import React from 'react'
import Image from "next/image";
export default function RelatedProducts() {
  return (
    <div>
      <h1 className='related_h1'>Related deals you might like for</h1>
      <div className=' Related_products_div'>
        <div className='Related_products_1'>
        <Image style={{marginLeft: '40px'}}
      src="/download 1.png"
      width={191}
      height={173}
      alt="Picture of the search icon"
    />
            <div style={{display:"flex",marginTop:"3rem",marginLeft:"2rem"}}>
                <div style={{marginRight:"2rem",color:"#074786",backgroundColor:"#F2F4F7",width:"4rem",height:"1rem"}}>20% off</div>
                <div style={{marginRight:"2rem",color:"#074786",backgroundColor:"#F2F4F7"}}>Limited Time</div>
            </div>
            <h3 style={{color:"#626E79",marginLeft:"5rem",marginTop:"2rem"}}>Webbuilder 1</h3>
            <h4 style={{color:"#626E79",fontWeight:"400"}}>Computer  Modern clasic with wix support</h4>
            <div style={{display:'flex'}}>
                <h2 style={{color:"#5C6874",marginRight:"1rem"}}>$39.96</h2>
                <p style={{marginTop:"1rem",color:"#9FA9B3",marginRight:"1rem"}}>$49.96</p>
                <p style={{color:"#EF4C5D"}}>(20% Off)</p>
            </div>
            <button>View Deal</button>
        </div>
        <div className='Related_products_1'>
        <Image style={{marginLeft: '40px'}}
      src="/download 1.png"
      width={191}
      height={173}
      alt="Picture of the search icon"
    />
            <div style={{display:"flex",marginTop:"3rem",marginLeft:"2rem"}}>
                <div style={{marginRight:"2rem",color:"#074786",backgroundColor:"#F2F4F7",width:"4rem",height:"1rem"}}>20% off</div>
                <div style={{marginRight:"2rem",color:"#074786",backgroundColor:"#F2F4F7"}}>Limited Time</div>
            </div>
            <h3 style={{color:"#626E79",marginLeft:"5rem",marginTop:"2rem"}}>Webbuilder 1</h3>
            <h4 style={{color:"#626E79",fontWeight:"400"}}>Computer  Modern clasic with wix support</h4>
            <div style={{display:'flex'}}>
                <h2 style={{color:"#5C6874",marginRight:"1rem"}}>$39.96</h2>
                <p style={{marginTop:"1rem",color:"#9FA9B3",marginRight:"1rem"}}>$49.96</p>
                <p style={{color:"#EF4C5D"}}>(20% Off)</p>
            </div>
            <button>View Deal</button>
        </div>
        <div className='Related_products_1'>
        <Image style={{marginLeft: '40px'}}
      src="/download 1.png"
      width={191}
      height={173}
      alt="Picture of the search icon"
    />
            <div style={{display:"flex",marginTop:"3rem",marginLeft:"2rem"}}>
                <div style={{marginRight:"2rem",color:"#074786",backgroundColor:"#F2F4F7",width:"4rem",height:"1rem"}}>20% off</div>
                <div style={{marginRight:"2rem",color:"#074786",backgroundColor:"#F2F4F7"}}>Limited Time</div>
            </div>
            <h3 style={{color:"#626E79",marginLeft:"5rem",marginTop:"2rem"}}>Webbuilder 1</h3>
            <h4 style={{color:"#626E79",fontWeight:"400"}}>Computer  Modern clasic with wix support</h4>
            <div style={{display:'flex'}}>
                <h2 style={{color:"#5C6874",marginRight:"1rem"}}>$39.96</h2>
                <p style={{marginTop:"1rem",color:"#9FA9B3",marginRight:"1rem"}}>$49.96</p>
                <p style={{color:"#EF4C5D"}}>(20% Off)</p>
            </div>
            <button>View Deal</button>
        </div>
        <div></div>
        <div></div>
      </div>
    </div>
  )
}
