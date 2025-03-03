package None;

import java.util.List;
import lombok.*;






/**
  Data class for representations of the resource in other media types than text/html which is the default for landing_page_url.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RepresentationVariant  {

  private String url;
  private String mediaType;
  private String encodingFormat;
  private Integer size;

}
