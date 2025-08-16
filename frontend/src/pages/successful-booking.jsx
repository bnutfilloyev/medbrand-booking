import logo from "../assets/images/landing-page/medsync-logo.svg"
import {useCloudStorage} from "@vkruglikov/react-telegram-web-app"
import {useEffect} from "react"

function RegistrationConfirmation() {
  window.Telegram.WebApp.disableClosingConfirmation()
  const storage = useCloudStorage()

  useEffect(() => {
    storage.removeItem("selectedDoctor")
    storage.removeItem("selectedDiagnostic")
    storage.removeItem("selectedLocation")
    storage.removeItem("selectedTimeSlot")
  }, [])

  return (
    <div className="registration-confirmation">
      <img
        className="logo"
        src={logo}
  alt="MedBrand logo"
      />
  <p className="registration-confirmation__title">Muvaffaqiyatli</p>
      <p className="registration-confirmation__text">
                Uchrashuvingizni MedBrand orqali muvaffaqiyatli bron qildingiz.
        <br/><br/>
                Endi yopishingiz yoki yana bir uchrashuv bron qilishingiz mumkin!
      </p>
      <div
        className="button arrow-button"
        onClick={() => {
          window.Telegram.WebApp.close()
        }}
  >Yopish
      </div>
  <a href="/" className="button button-second">Yana bir uchrashuv bron qilish</a>
    </div>
  )
}

export default RegistrationConfirmation
