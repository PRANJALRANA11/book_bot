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
      </div>
      <div style={{display:"flex"}}>
            <h1 style={{marginLeft:"13rem",fontWeight:"500", color:"#5C6874", marginTop:"9rem",marginRight:"25rem"}}>Sign up and get exclusive special deals</h1>
            <input style={{height:"52px",width:"348px" , marginTop:"9rem",borderRadius:"10px 0px 0px 10px",borderColor:"#9FA9B3"}}/>
            <button style={{backgroundColor:"#1B88F4",width:"97px",height:"57px", marginTop:"9rem",border:"none",borderRadius:"0px 10px 10px 0px"}}>Sign Up</button>
        </div>
    </div>
  )
}
