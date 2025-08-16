import medSyncIcon from "../assets/images/landing-page/medsync-icon.svg"
import arrowRight from "../assets/images/landing-page/arrow-right.svg"
import medSyncLogo from "../assets/images/landing-page/medsync-logo.svg"
import {Link} from "react-router-dom"

const LandingPage = () => {
  return (
    <>
      <div className="landing-page">
        <div className="landing-page__logo">
          <img
            className="logo"
            src={medSyncLogo}
            alt="MedBrand Logo"
          />
        </div>

        <div className="landing-page__icon">
          <img
            className="landing-page__icon--img"
            src={medSyncIcon}
            alt="Med"
          />
        </div>

  <p className="landing-page__text">Sog‘lig‘ingiz bizning ustuvor vazifamiz.</p>
  <Link to="/see_a_doctor" className="arrow-button button">Shifokorga uchrashuv
          <span className="arrow">
            <img src={arrowRight} alt="Arrow Right"/>
          </span>
        </Link>

  <Link to="/get_tested" className="button-second button">Tahlil topshirish</Link>

  <p className="landing-page__bottom">
        Shifokor va diagnostikani darhol <b>Telegram</b> orqali bron qiling
  </p>
      </div>
    </>
  )
}

export default LandingPage
